import pandas as pd
from src.preprocess_pipeline import preprocess_text
from src.config import preprocessing_config

# Example dataset
data = pd.read_csv('data/sample_dataset.csv')  # Must have 'text' column

# Apply preprocessing to each row
data['cleaned_text'] = data['text'].apply(lambda x: preprocess_text(x, preprocessing_config))

# Save processed data
data.to_csv('data/processed_dataset.csv', index=False)
print('Preprocessing completed and saved.')