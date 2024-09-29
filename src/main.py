# Import necessary libraries
import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from scipy.spatial import distance
from data_load import load_and_merge_data
from risk_calculation import calculate_risk
from system_cost_balancing import load_system_cost_factors, calculate_system_cost


# --------------------------
# Main Execution
# --------------------------
if __name__ == "__main__":
    if __name__ == "__main__":
        # Step 1: Load multiple datasets
        data_sources = {
            'pressure_data': 'pressure_data.csv',
            'resilience_data': 'resilience_data.csv',
            'causal_data': 'causal_factors.csv'
        }
    # Step 2: Normalize the data and calculate risk
    merged_data = calculate_risk(merged_data)
    # Step 2: Normalize the data
    merged_data = normalize_data(merged_data)
    
    # Step 3.0: Load key culmination factors
    key_factors = load_key_culmination_factors('key_factors.json')
    
    # Step 3.1: Calculate pressure arisal using key factors
    merged_data = calculate_pressure_arisal(merged_data, key_factors)

    # Step 3.2 to 3.6: Identify key areas
    high_pressure_areas = identify_pressures(merged_data, threshold=0.75)
    pressure_culmination = identify_pressure_culmination(high_pressure_areas, proximity_threshold=0.1)
    low_resilience_areas = identify_irresilience(merged_data, threshold=0.25)
    overlap_data = identify_pressure_resilience_overlap(high_pressure_areas, low_resilience_areas)
    risk_data = identify_growth_of_risk(overlap_data)
    
    # Step 4: Visualize the risk areas (hotspots)
    visualize_hotspots(merged_data, risk_data)