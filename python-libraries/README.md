# CLI Show Data Entry Tool

This project is a small Python command line application that lets you enter information about TV shows directly from the terminal and save that data to a file.

The script uses the **Rich** library to make the terminal output look nicer and **pathlib.Path** to handle file paths when saving data.

## What the Script Does

When you run the script, it first displays a table with some example show data. This is just to demonstrate how the formatting looks in the terminal.

After that, the program will prompt you to enter your own show information. You will be asked for:

- The show title  
- The release date  
- The number of episodes  

Once you enter the information, the script shows you a preview of what you typed in a table. You’ll then be asked to confirm whether the data is correct.

- If you confirm the entry, it will be stored.
- If something is wrong, the script will ask you to enter the information again.

You can keep adding shows for as long as you want. When you’re done, all of the confirmed entries will be written to a file.

## Output File

The script saves the data to a file called:

`shows_data.csv`

Each line of the file contains:

`Release Date, Title, Episodes`

Example:

```
Nov 12 2019, The Mandalorian, 24
Sep 21 2022, Andor, 12
Apr 10 2011, Game of Thrones, 73
```

At the end, the script will also print the full file path so you can easily find where the file was saved.

## Requirements

You’ll need **Python 3** and the **Rich** library.

Install Rich with:

```bash
pip install rich
```

## How to Run the Script

From the terminal, run:

```bash
python cli_data_entry.py
```

Then just follow the prompts to enter show data.

## Technologies Used

- Python  
- Rich (for styled terminal output)  
- pathlib.Path (for file handling)

## Notes

The `shows_data.csv` file is created by the script each time you run it. Since it’s automatically generated, it can be ignored in `.gitignore` if you don’t want Git to track it.