# Additional Python Notes
# ------------------------

# Capitalization matters in Python. Python is case-sensitive: min and Min are different.
# Spelling matters in Python. You must match the spelling of functions and variables exactly.
# Indentation matters in Python. Indentation is used to define code blocks and must be consistent.

# Functions
# ---------
# Functions are used to group code together and make it more readable and reusable.
# We define custom functions that can be called later in the code.
# Functions are blocks of logic that can take inputs, perform work, and return outputs.

# Defining Functions
# ------------------
# Define a function using the def keyword, followed by the function name, parentheses, and a colon. 
# The function name should describe what the function does.
# In the parentheses, specify the inputs needed as arguments the function takes.

# For example:
#    The function filtered_data() takes no arguments.
#    The function between(min, max) takes two arguments, a minimum and maximum value.
#    Arguments can be positional or keyword arguments, labeled with a parameter name.

# The function body is indented (consistently!) after the colon. 
# Use the return keyword to return a value from a function.

# Calling Functions
# -----------------
# Call a function by using its name followed by parentheses and any required arguments.
    
# Decorators
# ----------
# Use the @ symbol to decorate a function with a decorator.
# Decorators a concise way of calling a function on a function.
# We don't typically write decorators, but we often use them.

import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from palmerpenguins import load_penguins
from shiny import App, ui, render, reactive
from shinywidgets import render_plotly, output_widget

penguins = load_penguins()

app_ui = ui.page_sidebar(
    # Sidebar
    ui.sidebar(
        ui.h2("Sidebar"),

        ui.input_selectize(
            "selected_attribute",
            "Select Attribute",
            ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
        ),

        ui.input_numeric("plotly_bin_count", "Number of Plotly Histogram Bins", 20),
        ui.p("This controls how many bins the Plotly histogram will display."),

        ui.input_slider("seaborn_bin_count", "Number of Seaborn Bins", 1, 100, 20),

        ui.input_checkbox_group(
            "selected_species_list",
            "Filter by Species",
            ["Adelie", "Gentoo", "Chinstrap"],
            selected=["Adelie", "Gentoo", "Chinstrap"],
            inline=True
        ),

        ui.hr(),

        ui.a("GitHub", href="https://github.com/Kiruthikaa2512/cintel-02-data", target="_blank")
    ),

    ui.markdown("**Instructions:** Use dropdowns to explore the data visually."),
    ui.download_button("download_data", "Download Filtered Data"),

    # Main Content
    ui.layout_columns(
        ui.output_data_frame("data_table"),
        ui.output_data_frame("data_grid")
    ),

    ui.layout_columns(
        output_widget("plotly_hist"),
        ui.output_plot("seaborn_hist")
    ),

    ui.card(
        ui.card_header("Plotly Scatterplot: Species"),
        output_widget("plotly_scatterplot"),
        full_screen=True
    ),

    title="Penguin Explorer – Dashboard by Kiruthikaa"
)

def server(input, output, session):

    @reactive.Calc
    def filtered_data():
        return penguins[penguins["species"].isin(input.selected_species_list())]

    @output
    @render.data_frame
    def data_table():
        return filtered_data()

    @output
    @render.data_frame
    def data_grid():
        return filtered_data()

    @output
    @render_plotly
    def plotly_hist():
        return px.histogram(
            data_frame=filtered_data(),
            x=input.selected_attribute(),
            nbins=input.plotly_bin_count(),
            title="Plotly Histogram"
        )

    @output
    @render.plot
    def seaborn_hist():
        fig, ax = plt.subplots()
        sns.histplot(
            data=filtered_data(),
            x=input.selected_attribute(),
            bins=input.seaborn_bin_count(),
            ax=ax
        )
        ax.set_title("Seaborn Histogram")
        ax.set_xlabel(input.selected_attribute())
        return fig

    @output
    @render_plotly
    def plotly_scatterplot():
        return px.scatter(
            filtered_data(),
            x="bill_length_mm",
            y="body_mass_g",
            color="species",
            title="Penguins Plot (Plotly Express)",
            labels={
                "bill_length_mm": "Bill Length (mm)",
                "body_mass_g": "Body Mass (g)",
            },
            size_max=8
        )

    @output
    @render.download(filename="filtered_penguins.csv")
    def download_data():
        yield filtered_data().to_csv(index=False)
        
    # --------------------------------------------------------
# Reactive calculations and effects
# --------------------------------------------------------

# Add a reactive calculation to filter the data
# By decorating the function with @reactive, we can use the function to filter the data
# The function will be called whenever an input functions used to generate that output changes.
# Any output that depends on the reactive function (e.g., filtered_data()) will be updated when the data changes.

@reactive.calc
def filtered_data():
    return penguins

app = App(app_ui, server)

