# Penguin Explorer – PyShiny Dashboard

An interactive data visualization dashboard created entirely in the [ShinyLive Playground](https://shinylive.io/py/) for exploring the Palmer Penguins dataset. This project demonstrates dynamic filtering, statistical visualization, and data export—all powered by PyShiny.

## Project Overview

This dashboard enables users to:
- Filter penguins by species and island using multi-select inputs
- Visualize the distribution of selected attributes using:
  - Plotly histograms with box summaries
  - Seaborn histograms with KDE
  - Violin plots segmented by species
  - Scatterplots of bill length vs. body mass
- View and interact with filtered data tables
- Download the filtered dataset as a CSV file

## Technologies Used

- **[PyShiny](https://shiny.posit.co/py/)**: for web application structure and interactivity
- **Plotly**: for interactive, browser-based visualizations
- **Matplotlib & Seaborn**: for statistical plotting
- **Palmerpenguins**: for the dataset
- **Shiny Playground (ShinyLive)**: as the development environment—no local setup required

## How to Run the App

To run this project:

1. Visit [ShinyLive Playground](https://shinylive.io/py/)
2. Paste the contents of `app.py` into the editor
3. Click **▶ Run** at the top of the editor
4. Interact with the dashboard and use the sidebar filters

You can also [export your project](https://shinylive.io/py/export/) to download and commit the code directly to your GitHub repository.

## File Structure

- `app.py`: Complete PyShiny application
- `requirements.txt`: Python dependencies
- `README.md`: Project overview and instructions

## Dependencies

Specify these in `requirements.txt` for clarity:

```
shiny
shinywidgets
matplotlib
seaborn
plotly
palmerpenguins
```

## License & Attribution

This dashboard uses the [palmerpenguins dataset](https://github.com/allisonhorst/palmerpenguins), provided under CC0 by Dr. Allison Horst.

