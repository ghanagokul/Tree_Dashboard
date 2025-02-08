import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objects as go

# Load dataset
file_path = "Data_Viz_Challenge_2025-UCB_Trees.csv"
df = pd.read_csv(file_path)

# Initialize Dash app
app = dash.Dash(__name__)
server = app.server  # Expose server for deployment

# Create map figure
map_fig = px.scatter_mapbox(
    df, lat="Latitude", lon="Longitude", color="Tree Type",
    hover_data=["Common Name", "Genus", "Species"],
    title="Tree Distribution by Tree Type",
    zoom=14, color_discrete_map={"DECIDUOUS": "green", "EVERGREEN": "blue"}
)
map_fig.update_layout(mapbox_style="open-street-map")

# Scatter Plot: Canopy Spread vs. Height
scatter_fig = px.scatter(df, x="Height", y="Canopy Spread", color="Genus", 
                         hover_data=["Common Name", "Species"],
                         title="Canopy Spread vs. Height")

# Bar Chart: Genus Count
genus_counts = df["Genus"].value_counts().reset_index()
genus_counts.columns = ["Genus", "Count"]
genus_bar_fig = px.bar(genus_counts, x="Genus", y="Count", 
                       title="Tree Count by Genus")

# 3D Scatter Plot: Canopy Spread, Latitude, and Height (Colored by Tree Type)
scatter_3d_fig = px.scatter_3d(df, x="Height", y="Canopy Spread", z="Latitude", 
                               color="Tree Type", 
                               hover_data=["Common Name", "Species"],
                               title="3D Scatter: Canopy Spread, Latitude, and Height by Tree Type")

# Callback to update region stats
@app.callback(
    Output("region-stats", "children"),
    Input("tree-map", "clickData")
)
def update_region_stats(clickData):
    if clickData is None:
        return "Click on a region to see highest & lowest genus/species counts."
    
    lat, lon = clickData["points"][0]["lat"], clickData["points"][0]["lon"]
    region_df = df[(df["Latitude"].round(2) == round(lat, 2)) & (df["Longitude"].round(2) == round(lon, 2))]
    
    if region_df.empty:
        return "No data available for this region."
    
    genus_counts = region_df["Genus"].value_counts()
    species_counts = region_df["Species"].value_counts()
    
    highest_genus = genus_counts.idxmax() if not genus_counts.empty else "N/A"
    lowest_genus = genus_counts.idxmin() if len(genus_counts) > 1 else "N/A"
    highest_species = species_counts.idxmax() if not species_counts.empty else "N/A"
    lowest_species = species_counts.idxmin() if len(species_counts) > 1 else "N/A"
    
    return f"Highest Genus: {highest_genus}, Lowest Genus: {lowest_genus}, Highest Species: {highest_species}, Lowest Species: {lowest_species}"

# Layout
app.layout = html.Div([
    html.H1("Interactive Tree Data Dashboard", style={'textAlign': 'center', 'color': '#4CAF50', 'padding': '10px'}),
    dcc.Graph(id="tree-map", figure=map_fig),
    html.Div(id="region-stats", style={'padding': '15px', 'backgroundColor': 'white', 'borderRadius': '8px', 'marginTop': '10px', 'boxShadow': '2px 2px 10px rgba(0,0,0,0.1)'}),
    html.Div([
        dcc.Graph(id="scatter-plot", figure=scatter_fig, style={'width': '48%', 'display': 'inline-block'}),
        dcc.Graph(id="genus-bar-chart", figure=genus_bar_fig, style={'width': '48%', 'display': 'inline-block'})
    ]),
    dcc.Graph(id="scatter-3d-plot", figure=scatter_3d_fig, style={'width': '100%', 'marginTop': '20px'})
])

# Run app
if __name__ == '__main__':
    app.run_server(debug=True)
