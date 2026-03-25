from bs4 import BeautifulSoup
import cloudscraper
import csv
from pathlib import Path

BASE_URL = "https://dune.fandom.com"
URL = "https://dune.fandom.com/wiki/Category:Characters"
OUTPUT_FILE = "./web-scraping/dune_characters.csv"

scraper = cloudscraper.create_scraper()

def fetch_page(url):
    response = scraper.get(url, timeout=10)
    response.raise_for_status()
    return response

def parse_characters(response):
    soup = BeautifulSoup(response.text, "html.parser")
    characters = []
    seen = set()
    category_div = soup.find("div", class_="category-page__members")

    if not category_div:
        print("Could not find category section.")
        return characters

    links = category_div.find_all("a", class_="category-page__member-link")
    print(f"\nFound {len(links)} character link(s).")

    for link in links:
        name = link.get_text(strip=True)
        href = link.get("href")

        if not name or not href:
            continue

        # Convert relative URL to full URL
        full_url = BASE_URL + href

        if full_url in seen:
            continue
        seen.add(full_url)

        characters.append({
            "character_name": name,
            "character_url": full_url,
        })

    print(f"Total characters extracted: {len(characters)}\n")
    return characters

def save_to_csv(characters, filename):
    filepath = Path(filename).resolve()

    with filepath.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["character_name", "character_url"])
        for character in characters:
            writer.writerow([character["character_name"], character["character_url"]])

    print(f"Saved to: {filepath}")
    print(f"Total rows: {len(characters)}")

def preview_results(characters, n=10):
    print(f"Preview: First {n} entries")
    for character in characters[:n]:
        print(f"  {character['character_name']:<30}  {character['character_url']}")

def main():
    print("Dune — Character Category Scraper")

    try:
        response = fetch_page(URL)
        characters = parse_characters(response)
        preview_results(characters)
        save_to_csv(characters, OUTPUT_FILE)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()