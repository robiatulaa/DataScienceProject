# Jabodetabek House Price Analysis Dashboard

This repository contains data and R code for analyzing housing prices in the **Jabodetabek region** (Jakarta, Bogor, Depok, Tangerang, Bekasi).  
It includes a cleaned dataset, R workspace files, and a Shiny dashboard application.

## Project Files

- **jabodetabek_house_price_cleaned.csv**  
  A cleaned dataset of housing prices in Jabodetabek with property features and prices.

- **jabodetabek_house_price.r**  
  The R script that builds and launches the interactive **Shiny dashboard** for exploring housing prices.

- **.RData**  
  Saved R workspace containing datasets, models, and objects used during analysis.

- **.Rhistory**  
  Command history of R sessions, useful for reviewing the analysis workflow.

## Requirements

- R (≥ 4.0.0)  
- RStudio (recommended)  
- R packages:  
  - `shiny`  
  - `tidyverse` (or `dplyr`, `ggplot2`, `readr`)  
  - Other packages depending on the dashboard code (e.g., `shinydashboard`, `plotly`, `DT` if used)

Install packages with:
```r
install.packages(c("shiny", "tidyverse"))

