import json
import pandas as pd

def load_key_culmination_factors(file_path):
    """
    Load key culmination factors, raw data exploration, and shaping factors from an external JSON file.
    :param file_path: Path to the JSON file containing key factors.
    :return: Dictionary containing 'raw_data_exploration', 'key_culmination_factors', and 'shaping_factors'.
    """
    with open(file_path, 'r') as file:
        key_factors = json.load(file)

    # Ensure all expected sections are present
    if not all(k in key_factors for k in ["raw_data_exploration", "key_culmination_factors", "shaping_factors"]):
        raise ValueError("Missing one or more required sections: 'raw_data_exploration', 'key_culmination_factors', 'shaping_factors'")

    # Convert the loaded sections into DataFrames
    df_raw_data_exploration = pd.DataFrame(key_factors["raw_data_exploration"])
    df_key_culmination_factors = pd.DataFrame(key_factors["key_culmination_factors"])
    df_shaping_factors = pd.DataFrame(key_factors["shaping_factors"])

    # Save to CSV
    df_raw_data_exploration.to_csv('raw_data_exploration.csv', index=False)
    df_key_culmination_factors.to_csv('key_culmination_factors.csv', index=False)
    df_shaping_factors.to_csv('shaping_factors.csv', index=False)

    return key_factors
