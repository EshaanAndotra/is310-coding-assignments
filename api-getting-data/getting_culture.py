import json
import requests
from pathlib import Path
from rich import print as rprint
 
EUROPEANA_API_KEY = Path(__file__).parent / "api_key.txt"
EUROPEANA_API_KEY = EUROPEANA_API_KEY.read_text().strip()
 
BRAWL_API_KEY = Path(__file__).parent / "brawl_key.txt"
BRAWL_API_KEY = BRAWL_API_KEY.read_text().strip()
 
brawlers_url = "https://api.brawlstars.com/v1/brawlers"
brawlers_response = requests.get(brawlers_url, headers={"Authorization": f"Bearer {BRAWL_API_KEY}"})
brawlers_data = brawlers_response.json()
 
rprint("\n[bold yellow]Brawlers from Brawl Stars API:[/bold yellow]")
rprint(brawlers_data)
 
brawler = brawlers_data["items"][0]
search_query = brawler["name"]
 
europeana_url = "https://api.europeana.eu/record/v2/search.json"
params = {
    "wskey": EUROPEANA_API_KEY,
    "query": search_query,
    "rows": 5,
}
 
europeana_response = requests.get(europeana_url, params=params)
europeana_data = europeana_response.json()
 
rprint("\n[bold blue]Europeana Results:[/bold blue]")
rprint(europeana_data)
 
items = europeana_data.get("items", [])
 
for item in items:
    item.pop("apikey", None)
 
output = {
    "brawler": brawler,
    "query": search_query,
    "items": items
}
 
output_path = Path(__file__).parent / "brawlstars_europeana_data.json"
output_path.write_text(json.dumps(output, indent=2))
 
print(f"\nData saved to {output_path}")