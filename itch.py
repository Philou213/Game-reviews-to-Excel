import re
import pandas as pd
from bs4 import BeautifulSoup


def get_vote_count(post, class_name):
    """Extract a vote count from a post."""
    element = post.select_one(f".{class_name}")

    if not element:
        return 0

    match = re.search(
        r"[-+]?\d+",
        element.get_text(strip=True)
    )

    return abs(int(match.group())) if match else 0


def clean_itch_filename(filename):
    """Remove 'Comments -' and 'by ...' from an itch.io filename."""
    name = filename

    name = re.sub(
        r"^Comments\s*-\s*",
        "",
        name
    )

    name = re.sub(
        r"\s+by\s+.*$",
        "",
        name
    )

    return name.strip()


def process_itch(input_dir, output_dir):
    """
    Convert all itch.io HTML comment pages in input_dir
    to XLSX files in output_dir.
    """

    output_dir.mkdir(parents=True, exist_ok=True)

    html_files = [
        *input_dir.glob("*.htm"),
        *input_dir.glob("*.html")
    ]

    print(f"Found {len(html_files)} HTML files.")

    # Loop on all html files in the directory
    for html_file in html_files:
        print(f"Processing: {html_file.name}")

        # Read HTML
        with open(
            html_file,
            "r",
            encoding="utf-8"
        ) as file:
            soup = BeautifulSoup(
                file.read(),
                "html.parser"
            )

        # Find comments and replies
        posts = soup.select(
            ".community_post_widget"
        )

        print(f"  Found {len(posts)} posts.")

        comments = []

        # Loop on all comments for the game
        for post in posts:

            # Post ID
            post_id = post.get("id", "")

            if post_id.startswith("post-"):
                post_id = post_id.removeprefix("post-")

            # Author
            author_element = post.select_one(
                ".post_author a"
            )

            author = (
                author_element.get_text(strip=True)
                if author_element
                else ""
            )

            # Timestamp
            date_element = post.select_one(
                ".post_date"
            )

            timestamp = (
                date_element.get("title", "")
                if date_element
                else ""
            )

            # Comment
            body_element = post.select_one(
                ".post_body"
            )

            comment = (
                body_element.get_text(
                    " ",
                    strip=True
                )
                if body_element
                else ""
            )

            # Votes
            upvotes = get_vote_count(
                post,
                "upvotes"
            )

            downvotes = get_vote_count(
                post,
                "downvotes"
            )

            comments.append({
                "author_id": post_id,
                "author_name": author,
                "review": comment,
                "votes_up": upvotes,
                "votes_down": downvotes,
                "created_timestamp": timestamp
            })

        # Create DataFrame
        df = pd.DataFrame(comments)

        # Create output filename
        name = clean_itch_filename(
            html_file.stem
        )

        output_file = output_dir / f"{name}.xlsx"

        # Export
        df.to_excel(
            output_file,
            index=False,
            engine="openpyxl"
        )

        print(f"  Created: {output_file}")

    print("itch.io processing complete.")