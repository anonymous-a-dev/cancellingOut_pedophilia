import pandas as pd
from load_keys import load_key_culmination_factors

def load_and_merge_data(data_sources, key_factors_file):
    """
    Load and merge multiple datasets from different sources.
    :param data_sources: Dictionary of {dataset_name: file_path} for different data sources.
    :param key_factors_file: Path to the JSON file containing key factors.
    :return: Merged DataFrame with location, pressure_score, and resilience_score columns.
    """
    data_frames = []

    # Load each dataset and append to list
    for name, file_path in data_sources.items():
        df = pd.read_csv(file_path)
        data_frames.append(df)

    # Merge datasets on the 'location' column
    merged_data = data_frames[0]
    for df in data_frames[1:]:
        merged_data = pd.merge(merged_data, df, on='location')

    # Load key culmination factors from the external JSON file
    key_factors = load_key_culmination_factors(key_factors_file)

    # Highlight raw data exploration factors in the data
    for factor in key_factors["raw_data_exploration"]:
        if factor["name"] in merged_data.columns:
            # Highlight factor by applying logic specific to the factor's importance
            merged_data[f'{factor["name"]}_highlighted'] = merged_data[factor["name"]].apply(
                lambda x: highlight_factor(x, factor["name"])
            )

    # Extract positional attributes (for example: social ties, geographic location)
    merged_data['positional_attribute'] = merged_data.apply(extract_positional_attribute, axis=1)

    # Calculate intensity-likelihood factor based on specific culmination factors
    merged_data['intensity_likelihood_factor'] = merged_data.apply(calculate_intensity_likelihood, axis=1)

    # Calculate cost to system vs. harm canceled out, applying risk/cost analysis
    merged_data['cost_vs_harm'] = merged_data.apply(calculate_cost_vs_harm, axis=1)

    return merged_data


def highlight_factor(value, factor_name):
    """
    Placeholder function to highlight key culmination factors.
    This function should highlight the key factors based on the value and factor name.
    :param value: The value to be evaluated.
    :param factor_name: The name of the factor to be highlighted.
    :return: Highlighted value or tag.
    """
    # Example logic for highlighting certain factors
    if isinstance(value, str) and "important" in value.lower():
        return f"HIGHLIGHTED: {value}"
    # Add more logic based on other factors
    return value


def extract_positional_attribute(row):
    """
    Extract positional attributes, like geographic ties, social connections, etc.
    :param row: The row of the DataFrame to extract from.
    :return: Calculated positional attribute.
    """
    # Example logic based on geographic and social attributes
    if 'latitude' in row and 'longitude' in row:
        return f"Lat:{row['latitude']}, Lon:{row['longitude']}"
    # Add more complex logic as needed (e.g., relationships, influence score)
    return "Unknown"


def calculate_intensity_likelihood(row):
    """
    Calculate the intensity-likelihood factor based on key culmination factors.
    :param row: The row of the DataFrame to evaluate.
    :return: Intensity-likelihood score.
    """
    # Example: Logic that factors in multiple attributes
    likelihood = 0
    # Adding weights based on key factors
    if 'pressure_score' in row:
        likelihood += row['pressure_score'] * 0.6
    if 'resilience_score' in row:
        likelihood -= row['resilience_score'] * 0.4
    return max(0, likelihood)


def calculate_cost_vs_harm(row):
    """
    Calculate the cost to system vs. harm canceled out by prevention.
    :param row: The row of the DataFrame to evaluate.
    :return: Cost vs. harm ratio.
    """
    # Example logic based on system resource use and potential harm averted
    harm_potential = row.get('harm_potential', 0)
    prevention_cost = row.get('prevention_cost', 1)  # Avoid division by zero
    return harm_potential / prevention_cost if prevention_cost > 0 else 0
