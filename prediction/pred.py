#!/usr/bin/env python
# coding: utf-8

# In[51]:


import pandas as pd
import numpy as np
import joblib
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("yield_dataset.csv")

# Drop unnecessary columns
df = df.drop(columns=["Farm_ID", "Location", "Confidence_Interval"])

# Define features and target
X = df.drop(columns=["Predicted_Yield"])
y = df["Predicted_Yield"]

# Identify only numerical features
numerical_features = X.select_dtypes(include=["float64", "int64"]).columns.tolist()

# Compute correlation with the target
corr_matrix = df[numerical_features + ["Predicted_Yield"]].corr()
top_features = (
    corr_matrix["Predicted_Yield"]
    .abs()
    .sort_values(ascending=False)
    .index[1:6]
    .tolist()
)

# Keep only the top 5 numerical features
X = X[top_features]

print(f"Selected Top 5 Numerical Features: {top_features}")

# Preprocessing pipeline (only for numerical features)
preprocessor = ColumnTransformer([
    ("num", StandardScaler(), top_features)
])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit the Preprocessor First
preprocessor.fit(X_train)

# Transform the data
X_train_transformed = preprocessor.transform(X_train)
X_test_transformed = preprocessor.transform(X_test)

# Convert transformed data back to DataFrame
X_train_transformed = pd.DataFrame(X_train_transformed, columns=top_features)
X_test_transformed = pd.DataFrame(X_test_transformed, columns=top_features)

# Define the model
regressor = RandomForestRegressor(n_estimators=300, max_depth=10, random_state=42)

# Train the model on transformed data
regressor.fit(X_train_transformed, y_train)

# Predictions
y_pred = regressor.predict(X_test_transformed)

# Model evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.4f}")
print(f"R-Squared Score: {r2:.4f}")

with open('yield4_prediction_model.pkl', 'wb') as model_file:
    pickle.dump(regressor, model_file)
print("Model saved successfully!")

# Save the fitted preprocessor
joblib.dump(preprocessor, "scaler4.pkl")
print("Fitted Scaler saved successfully!")


# In[52]:


import joblib

scaler = joblib.load("scaler4.pkl")
print(type(scaler))  

model = joblib.load("yield4_prediction_model.pkl")
print(type(model))  


# In[53]:


import numpy as np
import pandas as pd
import joblib

# Load the trained model and scaler
model = joblib.load("yield4_prediction_model.pkl")
scaler = joblib.load("scaler4.pkl")  # ColumnTransformer with only numerical scaling

# Define new input data (Ensure values match expected range)
new_data = pd.DataFrame([[
    4.5,   # Historical_Yield
    120,   # Rainfall (mm)
    80,    # Humidity (%)
    6.5,   # Soil_pH
    3.2    # Organic_Content (%)
]], columns=["Historical_Yield", "Rainfall", "Humidity", "Soil_pH", "Organic_Content"])

# Apply the same scaling transformation
processed_data = scaler.transform(new_data)

# Make a prediction
prediction = model.predict(processed_data)

print("Predicted Yield:", prediction[0])


# In[59]:


import numpy as np
import pandas as pd
import joblib

# Load the trained model and scaler
model = joblib.load("yield4_prediction_model.pkl")
scaler = joblib.load("scaler4.pkl")  # ColumnTransformer with only numerical scaling

# Define new input data (Ensure values match expected range)
new_data = pd.DataFrame([[
    4.5,   # Historical_Yield
    120,   # Rainfall (mm)
    80,    # Humidity (%)
    6.5,   # Soil_pH
    3.2    # Organic_Content (%)
]], columns=["Historical_Yield", "Rainfall", "Humidity", "Soil_pH", "Organic_Content"])

# Apply the same scaling transformation
processed_data = scaler.transform(new_data)

# Make a prediction
prediction = model.predict(processed_data)

print("Predicted Yield:", prediction[0])

