from sklearn.preprocessing import MinMaxScaler

def calculate_risk(merged_data):
    """
    Normalize pressure and resilience data, and calculate risk score.
    :param merged_data: DataFrame containing pressure and resilience columns.
    :return: DataFrame with normalized pressure, resilience, and risk scores.
    """
    scaler = MinMaxScaler()

    # Normalize pressure and resilience data
    merged_data[['pressure_score']] = scaler.fit_transform(merged_data[['pressure_score']])
    merged_data[['resilience_score']] = scaler.fit_transform(merged_data[['resilience_score']])

    # Calculate risk score (higher pressure, lower resilience = higher risk)
    merged_data['risk_score'] = merged_data['pressure_score'] * (1 - merged_data['resilience_score'])

    return merged_data