# Staying Power in Top Novels and NYT Bestsellers

An exploratory data analysis comparing the Goodreads Top 500 Novels with the NYT Bestseller list (1931–2020), looking at which books have staying power by which measure.

## Datasets

- **Top 500 Novels** - Goodreads top-ranked novels with metadata (genre, publication year, author info, ratings). Source: [Responsible Datasets in Context](https://github.com/melaniewalsh/responsible-datasets-in-context).
- **NYT Bestsellers** - Weekly bestseller rankings from 1931 to 2020. Source: [Post45 Data Collective](https://github.com/ecds/post45-datasets).

Both pull directly from GitHub in the notebook, no manual download needed.

## Question

The two lists are different ways of saying "this book mattered." Goodreads top novels are books readers rated highly long after publication. NYT bestsellers are books that sold well in a given week. The notebook explores which books have staying power by which measure — and how much overlap there really is.

## Sections

1. Setup and loading
2. Cleaning (lowercase title/author for matching, fix Goodreads numeric columns)
3. When were the top novels published
4. How long bestsellers stay on the NYT list
5. Do long-running bestsellers also make the top novels list
6. Author-level comparison: Goodreads ratings split by NYT appearance
7. Genre patterns in the top novels
8. Gaps and biases

## Requirements

```
pandas
altair
```

## How to run

Open StayingPowerInTopNovelsAndBestsellers.ipynb in Jupyter and run all cells. The datasets are pulled from public GitHub URLs.
