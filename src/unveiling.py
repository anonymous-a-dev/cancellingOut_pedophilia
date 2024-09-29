# --------------------------
# Step 4: Geographic Visualization of Hotspots (Leads)
# --------------------------
def visualize_hotspots(merged_data, risk_data=None):
    """
    Visualize geographic risk hotspots on a map. This shows regions rather than individuals.
    :param merged_data: DataFrame containing geographic data and scores.
    :param risk_data: Optional DataFrame for highlighting risk areas (high-risk hotspots or overlaps).
    """
    # Plot the world map
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    ax = world.plot(figsize=(10, 10), color='white', edgecolor='black')

    # Plot all areas
    gdf = gpd.GeoDataFrame(merged_data, geometry=gpd.points_from_xy(merged_data.longitude, merged_data.latitude))
    gdf.plot(ax=ax, color='blue', markersize=5, label='All Data')

    if risk_data is not None:
        # Plot high-risk hotspots or overlap areas
        gdf_risk = gpd.GeoDataFrame(risk_data, geometry=gpd.points_from_xy(risk_data.longitude, risk_data.latitude))
        gdf_risk.plot(ax=ax, color='red', markersize=10, label='High-Risk Areas')

    plt.title('Geographic Visualization of Risk Hotspots')
    plt.legend()
    plt.show()