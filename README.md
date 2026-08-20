# Game Reviews to Excel

**By Philippe St-Laurent-Recoura**

A Python tool for collecting and converting game reviews from **Steam** and **itch.io** into structured Excel files.

## Features

- Convert Steam review CSV files into Excel workbooks.
- Organize Steam reviews into separate sheets based on language.
- Extract itch.io comments and replies from saved HTML pages.
- Process multiple files at once.
- Export the results as `.xlsx` files.

## Requirements

- Python 3.10+
- pandas
- openpyxl
- BeautifulSoup4

Install the required packages with:

```bash
pip install -r requirements.txt
```

## Usage
Run the program :
```
	python main.py
```
	
The program will ask which platform you want to process:
```
	1 - Steam
	2 - Itch.io
```
	
It will then ask for the input and output directories.

## Steam

Steam reviews are collected using the Steam Review Explorer.

### 1. Download the reviews

Go to:

https://project.joshhills.dev/steam-review-explorer

Select the game and download its reviews as a CSV file.

### 2. Put the CSV files in a folder

For example:

```
SteamReviews/
├── game1.csv
├── game2.csv
└── game3.csv
```

### 3. Run the program

Select:

```
1 - Steam
```

Enter the input directory containing the CSV files and the directory where you want the Excel files to be created.

Each CSV file will be converted into an Excel workbook.

Steam reviews are separated into different worksheets based on their language field:

```
game1.xlsx
├── english
├── french
├── german
├── japanese
└── ...
```

## Itch.io

itch.io comments are collected from the game's comments page.

### 1. Open the game's comments page

Go to:

```
https://{user}.itch.io/{game}/comments
```

### 2. Save the page as HTM

In your browser, save the page as an HTML file.

### 3. Put the HTML files in a folder

You can put multiple games in the same folder:

```
ItchReviews/
├── Comments - Game1 by Developer.htm
├── Comments - Game2 by Developer.htm
└── Comments - Game3 by Developer.htm
├── Comments - Game1 by Developer_files (Folder)
├── Comments - Game2 by Developer_files (Folder)
└── Comments - Game3 by Developer_files (Folder)
```

### 4. Run the program

Select:

```
2 - itch.io
```

Enter the input directory containing the HTML files.

The program will extract:

- Author
- Comment
- Upvotes
- Downvotes
- Timestamp

Each HTML file is converted into its own Excel workbook:

```
Comments - Game1 by Developer.htm
        ↓
Game1.xlsx
```
## Use of the output files
The generated Excel files can then be used for further analysis, such as:

- Review classification
- Sentiment analysis
- Language analysis
- Topic modeling
- Qualitative analysis
- Comparing reviews between platforms

## Key Descriptions
### Steam
| Key | Description |
|---|---|
| `recommendation_id` | Unique identifier of the Steam recommendation/review. |
| `recommendation_url` | URL of the Steam recommendation. |
| `author_steam_id` | Steam ID of the user who wrote the review. |
| `author_num_games` | Number of games owned by the author. |
| `author_num_reviews` | Number of reviews written by the author. |
| `author_minutes_playtime_last_two_weeks` | Number of minutes the author played the game during the last two weeks. |
| `author_last_played_timestamp` | Timestamp of the author's most recent play session for the game. |
| `review` | Text content of the review. |
| `weighted_review_score` | Steam's weighted score for the review. |
| `created_timestamp` | Timestamp indicating when the review was originally created. |
| `updated_timestamp` | Timestamp indicating when the review was last updated. |
| `voted_up` | Whether the author recommended the game (`true`/`false`). |
| `language` | Language in which the review was written. |
| `author_minutes_playtime_at_review_time` | Number of minutes the author had played the game when the review was written. |
| `author_minutes_playtime_forever` | Total number of minutes the author has played the game. |
| `written_during_early_access` | Whether the review was written while the game was in Early Access. |
| `marked_as_received_for_free` | Whether Steam indicates that the author received the game for free. |
| `steam_purchase` | Indicates whether the author bought the game |
| `votes_up` | Number of users who found the review helpful/upvoted it. |
| `votes_funny` | Number of users who marked the review as funny. |
| `comment_count` | Number of comments/replies posted on the review. |

### Itch
| Key | Description |
|---|---|
| `author_id` | Unique identifier of the Itch author. |
| `author_name` | Name of the author. |
| `review` | Text content of the review. |
| `votes_up` | Number of users who upvoted the review |
| `votes_down` | Number of users who downvoted the review |
| `created_timestamp` | Timestamp indicating when the reviews was created |
