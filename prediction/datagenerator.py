import pandas as pd
import numpy as np
import random

# Function to generate realistic sugarcane dataset
def generate_sugarcane_dataset(num_samples=2000):
    np.random.seed(42)
    random.seed(42)

    # Possible categorical values
    locations = ["Tamil Nadu", "Andhra Pradesh", "Maharashtra", "Karnataka", "Uttar Pradesh"]
    soil_textures = ["Sandy", "Loamy", "Clayey"]
    irrigation_methods = ["Drip", "Flood", "Sprinkler"]
    fertilization_types = ["NPK", "Organic", "Urea", "Compost"]
    seasonal_trends = ["Increase", "Decrease", "Stable"]

    # Generate data
    data = []
    for i in range(num_samples):
        farm_id = f"F{str(i+1).zfill(4)}"
        location = random.choice(locations)
        rainfall = np.clip(np.random.normal(120, 30), 50, 200)  # Rainfall in mm
        temperature = np.clip(np.random.normal(30, 3), 25, 40)  # Avg Temperature (°C)
        humidity = np.clip(np.random.normal(70, 10), 50, 90)  # %
        soil_ph = np.clip(np.random.normal(6.5, 0.5), 5.5, 7.5)
        organic_content = np.clip(np.random.normal(2.0, 0.5), 1.0, 3.5)
        soil_texture = random.choice(soil_textures)
        irrigation_method = random.choice(irrigation_methods)
        fertilization = random.choice(fertilization_types)
        seasonal_trend = random.choice(seasonal_trends)
        soil_moisture = np.clip(np.random.normal(30, 5), 10, 50)  # %
        solar_radiation = np.clip(np.random.normal(500, 50), 400, 600)  # W/m²
        ndvi = np.clip(np.random.normal(0.6, 0.1), 0.4, 0.9)  # Vegetation index
        pesticide_use = random.uniform(0, 5)  # Liters per acre

        # Generate historical yield based on soil and weather conditions
        historical_yield = 80 + 5 * (soil_ph - 6.5) + 2 * (organic_content - 2.0) + \
                           0.3 * (humidity - 70) + 0.2 * (rainfall - 120) + 3 * ndvi
        historical_yield = np.clip(historical_yield, 60, 100)

        # Predicted yield with slight seasonal trend influence
        yield_adjustment = 0.05 if seasonal_trend == "Increase" else -0.05 if seasonal_trend == "Decrease" else 0
        predicted_yield = historical_yield * (1 + yield_adjustment)
        predicted_yield = np.clip(predicted_yield, 60, 100)
        confidence_interval = (predicted_yield - 3, predicted_yield + 3)

        # Append row
        data.append([
            farm_id, location, rainfall, temperature, humidity, soil_ph, organic_content, soil_texture,
            irrigation_method, fertilization, seasonal_trend, soil_moisture, solar_radiation, ndvi,
            pesticide_use, historical_yield, predicted_yield, confidence_interval
        ])

    # Create DataFrame
    df = pd.DataFrame(data, columns=[
        "Farm_ID", "Location", "Rainfall", "Temperature", "Humidity", "Soil_pH", "Organic_Content", "Soil_Texture",
        "Irrigation_Method", "Fertilization", "Seasonal_Trend", "Soil_Moisture", "Solar_Radiation", "NDVI",
        "Pesticide_Use", "Historical_Yield", "Predicted_Yield", "Confidence_Interval"
    ])

    # Save to CSV
    df.to_csv("yield_dataset.csv", index=False)
    print("Dataset saved as 'sugarcane_yield_dataset.csv'")

# Generate improved dataset
generate_sugarcane_dataset()
