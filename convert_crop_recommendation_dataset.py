import pandas as pd

df = pd.read_csv('Crop_recommendation.csv')
df.head()

import json

formatted_data = []
for _, row in df.iterrows():
    prompt = (
        f"N: {row['N']}, P: {row['P']}, K: {row['K']}, temperature: {row['temperature']:.2f}, "
        f"humidity: {row['humidity']:.2f}, pH: {row['ph']:.2f}, rainfall: {row['rainfall']:.2f}"
    )
    response = f"Recommended crop: {row['label']}"
    formatted_data.append({"prompt": prompt, "response": response})

print(formatted_data[:5])  # Display first 5 entries for verification

converted_dataset = []
for item in formatted_data:
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": item["prompt"]}
                # If you have image paths, add:
                # {"type": "image", "image": Image.open("/path/to/image.jpg")}
            ]
        },
        {
            "role": "assistant",
            "content": [
                {"type": "text", "text": item["response"]}
            ]
        }
    ]
    converted_dataset.append({"messages": messages})

# Example output
print(converted_dataset[0])