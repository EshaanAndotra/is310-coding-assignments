from rich.console import Console
from rich.table import Table
from pathlib import Path

current_directory = Path.cwd()

console = Console()
console.print(f"[dim]Current directory:[/dim] {current_directory}\n")

console.print("[bold cyan]Here is some initial data:[/bold cyan]")

table = Table(title="Star Wars Shows", header_style="bold blue")
table.add_column("Released", style="cyan", no_wrap=True)
table.add_column("Title", style="magenta")
table.add_column("Episodes", justify="right", style="green")
table.add_row("Nov 12, 2019", "The Mandalorian", "24")
table.add_row("May 4, 2021", "The Bad Batch", "47")
table.add_row("Sep 21, 2022", "Andor", "12")
table.add_row("Aug 23, 2023", "Ahsoka", "8")
console.print(table)
console.print("\n[bold cyan]Now enter your own favorite shows:[/bold cyan]\n")
shows = []
while True:
    while True:
        title = input("Enter the show title: ")
        release = input("Enter the release date: ")
        episodes = input("Enter the number of episodes: ")
        console.print("\n[bold yellow]You entered:[/bold yellow]")
        preview = Table(title=f"Shows Preview", header_style="bold blue")
        preview.add_column("Released", style="cyan")
        preview.add_column("Title", style="magenta")
        preview.add_column("Episodes", justify="right", style="green")
        preview.add_row(release, title, episodes)
        console.print(preview)
        confirm = input("Is this correct? (yes/no): ").strip().lower()
        if confirm == "yes":
            shows.append((release, title, episodes))
            console.print("[green]Entry saved.[/green]\n")
            break
        else:
            console.print("[red]Please re-enter the data.[/red]\n")
    another = input("Add another show? (yes/no): ").strip().lower()
    if another != "yes":
        break
file_path = Path("shows_data.csv")
with open(file_path, "w") as edit_file:
    edit_file.write("Released, Title, Episodes\n")
    for show in shows:
        edit_file.write(f"{show[0]}, {show[1]}, {show[2]}\n")

console.print(f"\n[bold green]Data saved successfully![/bold green]")
console.print(f"[bold]File location:[/bold] {file_path.resolve()}")