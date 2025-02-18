from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import pickle
import joblib
import os
import pandas as pd
from django.http import HttpResponse
from django.conf import settings  


# Define paths for model and scaler
MODEL_PATH = os.path.join(settings.BASE_DIR, 'prediction', 'yield4_prediction_model.pkl')
SCALER_PATH = os.path.join(settings.BASE_DIR, 'prediction', 'scaler4.pkl')

# Load Model & Preprocessor
with open(MODEL_PATH, 'rb') as model_file:
    model = pickle.load(model_file)

scaler = joblib.load(SCALER_PATH)  # Preprocessing pipeline

# Extract the feature names used for training
feature_names = scaler.transformers_[0][2]

# Yield Prediction View
def predict_yield(request):
   
    predicted_yield = None

    if request.method == "POST":
        try:
            # Collect input values from form
            input_data = [
                float(request.POST.get("historical_yield")),
                float(request.POST.get("rainfall")),
                float(request.POST.get("humidity")),
                float(request.POST.get("soil_ph")),
                float(request.POST.get("organic_content"))
            ]

            # Convert input to DataFrame with correct column names
            input_df = pd.DataFrame([input_data], columns=feature_names)

            # Preprocess the input
            processed_data = scaler.transform(input_df)

            # Predict yield
            predicted_yield = model.predict(processed_data)[0]
            predicted_yield = round(float(predicted_yield), 2) 

            # return render(request, 'prediction_result1.html', {'predicted_yield': round(predicted_yield, 2)})

        except Exception as e:
            predicted_yield = f"Error: {str(e)}"
        #     return render(request, 'prediction_result1.html', {'predicted_yield': "Error in prediction!"})

    return render(request, "predict1.html", {"predicted_yield": predicted_yield})

#OTHER VIEWS

# Home Page
# def home(request):
#     return render(request, 'index.html')

# Login View
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')  # Redirect to home after login
#         else:
#             messages.error(request, "Invalid credentials")
#     return render(request, 'login.html')

# Signup View
# def signup_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         confirm_password = request.POST.get('confirm_password', '')
        
#         if password == confirm_password:
#             from django.contrib.auth.models import User
#             if User.objects.filter(username=username).exists():
#                 messages.error(request, "Username already taken")
#             else:
#                 user = User.objects.create_user(username=username, password=password)
#                 user.save()
#                 messages.success(request, "Signup successful. Please log in.")
#                 return redirect('login')
#         else:
#             messages.error(request, "Passwords do not match")
    
#     return render(request, 'signup.html')

# Logout View
# @login_required
# def logout_view(request):
#     logout(request)
#     return redirect('login')  # Redirect to login after logout

# Change Password View
# @login_required
# def change_password(request):
#     if request.method == "POST":
#         current_password = request.POST.get("current_password")
#         new_password = request.POST.get("new_password")
#         confirm_password = request.POST.get("confirm_password")

#         if not current_password or not new_password or not confirm_password:
#             messages.error(request, "All fields are required.")
#             return redirect("changepassword")

#         if new_password != confirm_password:
#             messages.error(request, "New passwords do not match.")
#             return redirect("changepassword")

#         user = request.user
#         if not user.check_password(current_password):
#             messages.error(request, "Current password is incorrect.")
#             return redirect("changepassword")

#         user.set_password(new_password)
#         user.save()
#         messages.success(request, "Password changed successfully! Please log in again.")
#         return redirect("login")  # Redirect to login after changing password

#     return render(request, "changepassword.html")


from .forms import SugarcaneYieldForm

def save_yield_data(request):
    if request.method == 'POST':
        form = SugarcaneYieldForm(request.POST)
        if form.is_valid():
            form.save()  # Saves data with timestamp
            return redirect('success')  # Redirect to a success page after saving
    else:
        form = SugarcaneYieldForm()
    
    return render(request, 'yield_form.html', {'form': form})

