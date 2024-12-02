import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go
import pandas as pd

# Load your data
main_data =  pd.read_csv('https://raw.githubusercontent.com/AidaCPL/INFOSCI301_Final_Project/refs/heads/main/Data/Main.csv')


# Check column names
print(main_data.columns)

# Ensure no missing values
main_data = main_data.dropna(subset=['CRT', 'Edu'])

# Social media mapping
social_media_options = {
    "Facebook": "fb",
    "Twitter": "tw",
    "Snapchat": "sn",
    "Instagram": "ig",
    "Whatsapp": "wh",
    "TikTok": "ti",
    "Other": "ot",
    "No Social Media": "no"
}

# Initialize Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.Label("Social Media:"),
    dcc.Dropdown(
        id="social-media-dropdown",
        options=[{"label": name, "value": code} for name, code in social_media_options.items()],
        value="fb",
        clearable=False
    ),
    dcc.Graph(id="crt-education-plot")
])

@app.callback(
    Output("crt-education-plot", "figure"),
    Input("social-media-dropdown", "value")
)
def update_plot(social_media_column):
    try:
        # Debugging: Print selected column
        print(f"Selected Social Media Column: {social_media_column}")

        # Aggregate data for mean and confidence intervals
        aggregated_data = main_data.groupby(['Edu', social_media_column]).agg(
            mean_CRT=('CRT', 'mean'),
            lower_CI=('CRT', lambda x: x.mean() - 1.96 * x.std() / (len(x) ** 0.5)),
            upper_CI=('CRT', lambda x: x.mean() + 1.96 * x.std() / (len(x) ** 0.5))
        ).reset_index()

        print(aggregated_data.head())  # Debugging: Check aggregated data

        # Create the plot
        fig = go.Figure()

        for group in aggregated_data[social_media_column].unique():
            group_data = aggregated_data[aggregated_data[social_media_column] == group]
            fig.add_trace(go.Scatter(
                x=group_data['Edu'],
                y=group_data['mean_CRT'],
                mode='lines+markers',
                name=f"Use: {group}",
                line_shape='spline'
            ))
            # Add confidence intervals as shaded areas
            fig.add_trace(go.Scatter(
                x=group_data['Edu'].tolist() + group_data['Edu'][::-1].tolist(),
                y=group_data['upper_CI'].tolist() + group_data['lower_CI'][::-1].tolist(),
                fill='toself',
                name=f"CI: {group}",
                showlegend=False,
                opacity=0.2
            ))

        # Update layout
        fig.update_layout(
            title=f"CRT vs Education Level by {social_media_column.capitalize()} Use",
            xaxis_title="Education Level",
            yaxis_title="CRT (Cognitive Reflection Task)",
            legend_title=f"{social_media_column.capitalize()} Use"
        )

        return fig

    except Exception as e:
        print(f"Error: {e}")
        return go.Figure()  # Return an empty figure if there's an error

if __name__ == "__main__":
    app.run_server(debug=True)