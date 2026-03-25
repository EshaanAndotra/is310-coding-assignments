# Fandom Wiki Scraping Assignment

## Chosen Wiki
For this assignment, I chose the Dune Wiki because of the new Dune movie coming out. I am interested in the world of Dune and its large groups of interesting characters such as the Bene Gesserit.

## What I Scraped
I scraped data from the Dune Wiki's Characters page. Specifically, I collected character names and links to their individual wiki pages.

## Why This Data Matters
This kind of data could be useful for researchers interested in fan communities or digital humanities. A character list can help show which characters are emphasized in crowd sourced knowledge bases (in this case the fandom) and how fictional worlds are organized online. It could also be used as a starting point for studying character networks, popularity, or representation across different versions of a story.

## Tools Used
I used:
- `cloudscraper` to request the webpage
- `BeautifulSoup` to parse the HTML
- Python's built in `csv` module to save the scraped data

## Robots.txt / Website Policy
Before scraping, I checked the website's robots.txt file to review whether scraping was allowed and what restrictions might apply.

Robots.txt link:
`https://dune.fandom.com/robots.txt`
The file allows access to standard wiki pages under /wiki/, which includes the category page used in this project. It disallows access to special system pages (e.g., /wiki/Special:, /wiki/User:), which were not accessed during scraping.

The script only makes a single request to a public page and does not overload the server.

## Output
The scraped data is stored in:
- `dune_characters.csv`