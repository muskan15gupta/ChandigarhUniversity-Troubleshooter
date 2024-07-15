import pandas as pd

# Load the datasets
user_history_df = pd.read_csv('user_purchase_history (2).csv')  # Replace with the actual file path
outfit_df = pd.read_csv('outfit_recommendation_dataset (2).csv')  # Replace with the actual file path

# Display the first few rows of the datasets to verify loading
print(user_history_df.head())
print(outfit_df.head())

from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# Define categorical columns
categorical_columns = ['Occasion', 'Material', 'Pattern', 'Neckline', 'Fit', 'Accessory', 'Brand']

# Initialize OneHotEncoder
onehot_encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)

# Apply one-hot encoding to the categorical columns in outfit_df
X = onehot_encoder.fit_transform(outfit_df[categorical_columns])
y = outfit_df['Outfit_Type']

# Apply LabelEncoder to the target variable
label_encoder_y = LabelEncoder()
y_encoded = label_encoder_y.fit_transform(y)

# Save encoders
import pickle

with open('onehot_encoder.pkl', 'wb') as f:
    pickle.dump(onehot_encoder, f)

with open('label_encoder_y.pkl', 'wb') as f:
    pickle.dump(label_encoder_y, f)
from sklearn.model_selection import train_test_split

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

from sklearn.ensemble import RandomForestClassifier

# Initialize and train the classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Save the trained model
with open('recommendation_model.pkl', 'wb') as f:
    pickle.dump(clf, f)

def recommend_outfit(user_input_features):
    # Load the encoders and model
    with open('onehot_encoder.pkl', 'rb') as f:
        onehot_encoder = pickle.load(f)
        
    with open('label_encoder_y.pkl', 'rb') as f:
        label_encoder_y = pickle.load(f)
        
    with open('recommendation_model.pkl', 'rb') as f:
        clf = pickle.load(f)

    # Transform user input features using the onehot_encoder
    user_input_encoded = onehot_encoder.transform(pd.DataFrame([user_input_features]))
    
    # Predict the outfit type
    predicted_outfit_type = clf.predict(user_input_encoded)[0]
    
    # Decode the predicted outfit type
    decoded_outfit_type = label_encoder_y.inverse_transform([predicted_outfit_type])[0]
    
    return decoded_outfit_type

# Example user input
user_input_features = {
    'Occasion': 'Casual',
    'Material': 'Cotton',
    'Pattern': 'Striped',
    'Neckline': 'V-neck',
    'Fit': 'Slim',
    'Accessory': 'Watch',
    'Brand': 'Nike'
}

recommended_outfit = recommend_outfit(user_input_features)
print("Recommended outfit type:", recommended_outfit)


