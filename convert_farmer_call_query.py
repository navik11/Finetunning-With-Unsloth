import pandas as pd
import json

# Read CSV
df = pd.read_csv("farmer_call_query_dataset.csv")

converted_dataset = []

for _, row in df.iterrows():
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": row["questions"]}
            ]
        },
        {
            "role": "assistant",
            "content": [
                {"type": "text", "text": row["answers"]}
            ]
        }
    ]
    converted_dataset.append({"messages": messages})

# Show sample
print(json.dumps(converted_dataset[0], indent=2))
