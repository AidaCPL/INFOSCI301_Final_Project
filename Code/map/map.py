import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import os


import pandas as pd
import plotly.express as px

# Load the dataset
main_url = "https://raw.githubusercontent.com/AidaCPL/INFOSCI301_Final_Project/main/Data/Main.csv"
df_main = pd.read_csv(main_url)

# Define country mappings (ISO-3 and full country names)
country_mapping = {
    'us': ('USA', 'United States'),
    'mx': ('MEX', 'Mexico'),
    'za': ('ZAF', 'South Africa'),
    'eg': ('EGY', 'Egypt'),
    'in': ('IND', 'India'),
    'pn': ('PNG', 'Papua New Guinea'),
    'ru': ('RUS', 'Russia'),
    'sa': ('SAU', 'Saudi Arabia'),
    'ng': ('NGA', 'Nigeria'),
    'cn': ('CHN', 'China'),
    'es': ('ESP', 'Spain'),
    'uk': ('GBR', 'United Kingdom'),
    'it': ('ITA', 'Italy'),
    'ar': ('ARG', 'Argentina'),
    'br': ('BRA', 'Brazil'),
    'au': ('AUS', 'Australia')
}

# Add ISO-3 codes and full country names
df_main['ISO3'] = df_main['Country'].map(lambda x: country_mapping[x][0])
df_main['Country_Full'] = df_main['Country'].map(lambda x: country_mapping[x][1])

# Calculate the individual attention scores
df_main['Attention_Score'] = df_main['pass_Attention2']

# Calculate the credibility score for each country
credibility_scores = (
    df_main.groupby(['ISO3', 'Country_Full'])['Attention_Score']
    .mean()
    .reset_index()
)
credibility_scores.rename(columns={'Attention_Score': 'Credibility_Score'}, inplace=True)

# Your existing code for pyecharts
from pyecharts.charts import Map
from pyecharts import options as opts

# Prepare data for pyecharts
data = [list(z) for z in zip(credibility_scores['Country_Full'], credibility_scores['Credibility_Score'])]

# Create the world map
world_map = (
    Map()
    .add(
        series_name="",
        data_pair=data,
        maptype="world",
        is_map_symbol_show=False
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Credibility Score by Country",
            pos_left="center",
            title_textstyle_opts=opts.TextStyleOpts(font_size=18),
        ),
        legend_opts=opts.LegendOpts(is_show=False),
        visualmap_opts=opts.VisualMapOpts(
            min_=0.4,
            max_=0.8,
            is_piecewise=True
        )
    )
    .set_series_opts(
        label_opts=opts.LabelOpts(is_show=False)
    )
)

# Save the map as an HTML file
html_file = "credibility_score_map.html"
world_map.render(html_file)

# Now set up Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout of the Dash app
app.layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Credibility Score by Country"), width={'size': 6, 'offset': 3})
        ]),
        dbc.Row([
            dbc.Col(html.Iframe(src=html_file, width="100%", height="800px"), width=12)
        ])
    ])
])

# Run the Dash app
if __name__ == "__main__":
    app.run_server(debug=True)