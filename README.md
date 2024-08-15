# Formula 1 Data Analysis

#### -- Project Status: [ On-Hold ]

## Project Intro/Objective
This project contains a dashboard analysing data of Formula 1 races from 1950 and up.

<!--
### Collaborators
|Name     |  Github Page   |  Personal Website  |
|---------|-----------------|--------------------|
|Nicolas Chagnet | [NicolasChagnet](https://github.com/NicolasChagnet)| [nicolaschagnet.github.io](https://nicolaschagnet.github.io)  | -->

### Data sources

* [Kaggle dataset](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020)

### Methods Used
* Data Analysis
* Data Visualization
* Predictive Modeling

### Technologies
* Python
* SQL
* Plotly Dash
* Pandas

## Project Description
The goals of this project were to analyze some dataset with strong relational links using SQL and present the results as a clear and interactive dashboard, built in Plotly. The dashboard summarizes the top race winners and qualifiers for a given year selected by the user. Once a year is chosen, the dashboard can be used to summarize a driver's grid and result positions as well as the overall lineup for any circuit.

All this analysis makes use of a Kaggle dataset with the following schema ([source](http://ergast.com/images/ergast_db.png)):
![Schema SQL](figs/schema.png)


## Getting Started

1. Clone this repository.
2. Raw data is being kept [here](data/raw) within this repo in `.csv` files. An sqlite database is located [here](data/final).
3. A script to generate the sqlite database from the `.csv` files can be found in `scripts/`.

To run dashboard, use
```bash
python3 app.py
```


<!-- ## Featured Notebooks/Analysis/Deliverables
* [Notebook/Markdown/Slide Deck Title](#)
* [Notebook/Markdown/Slide DeckTitle](#)
* [Blog Post](#) -->
