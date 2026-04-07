import json
import requests
from pathlib import Path
from rich import print as rprint
 
EUROPEANA_API_KEY = Path(__file__).parent / "api_key.txt"
EUROPEANA_API_KEY = EUROPEANA_API_KEY.read_text().strip()
 
swapi_url = "https://swapi.dev/api/films/4/"
swapi_response = requests.get(swapi_url)
film = swapi_response.json()
 
rprint("\n[bold yellow]Star Wars Film from SWAPI:[/bold yellow]")
rprint(film)
 

 
search_query = film["title"]
 
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
    "query": search_query,
    "items": items
}
 

output_path = Path(__file__).parent / "swapi_europeana_data.json"
output_path.write_text(json.dumps(output, indent=2))
 
print(f"\nData saved to {output_path}")
