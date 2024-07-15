from django.shortcuts import render
from .forms import OutfitForm
import os
import pickle
import pandas as pd

# Load your models and encoders
current_directory = os.path.dirname(__file__)
encoder_path = os.path.join(current_directory, 'onehot_encoder.pkl')
lencoder_path = os.path.join(current_directory, 'label_encoder_y.pkl')
model_path = os.path.join(current_directory, 'recommendation_model.pkl')

def recommend_outfit(user_input_features):
    with open(encoder_path, 'rb') as f:
        onehot_encoder = pickle.load(f)
        
    with open(lencoder_path, 'rb') as f:
        label_encoder_y = pickle.load(f)
        
    with open(model_path, 'rb') as f:
        clf = pickle.load(f)

    user_input_encoded = onehot_encoder.transform(pd.DataFrame([user_input_features]))
    predicted_outfit_type = clf.predict(user_input_encoded)[0]
    decoded_outfit_type = label_encoder_y.inverse_transform([predicted_outfit_type])[0]
    
    return decoded_outfit_type

from django.shortcuts import render
from .forms import OutfitForm

def outfit_recommendation_view(request):
    if request.method == 'POST':
        form = OutfitForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data
            # Assume you have a function to handle recommendations
            recommended_outfit = recommend_outfit(user_input)
            return render(request, 'recommendation/result.html', {'form': form, 'recommended_outfit': recommended_outfit})
    else:
        form = OutfitForm()

    return render(request, 'recommendation/form.html', {'form': form})
