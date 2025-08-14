import json
import re
from PIL import Image
from typing import Dict, List, Any
import os

def convert_message_format(conversation: Dict) -> Dict:
    """
    Convert a single conversation from the original format to the desired format.
    
    Args:
        conversation: Dictionary containing the original message format
        
    Returns:
        Dictionary in the converted format
    """
    converted_messages = []
    
    for message in conversation["messages"]:
        role = message["role"]
        content = message["content"]
        
        if role == "user":
            # Check if content contains an image tag
            img_match = re.search(r'<img>(.*?)</img>', content)
            
            if img_match:
                # Extract image path and text content
                img_path = f"/kaggle/input/cddm-dataset/dataset{img_match.group(1)}"
                text_content = re.sub(r'<img>.*?</img>', '', content).strip()
                
                # Remove "Picture 1: " or similar prefixes if they exist
                text_content = re.sub(r'^Picture \d+:\s*', '', text_content)
                
                # Create the new content structure
                new_content = []
                
                # Add text content if it exists
                if text_content:
                    new_content.append({
                        'type': 'text',
                        'text': text_content
                    })
                
                # Add image content
                try:
                    # Load the image using PIL
                    if os.path.exists(img_path):
                        img = Image.open(img_path)
                        new_content.append({
                            'type': 'image',
                            'image': img
                        })
                    else:
                        print(f"Warning: Image file not found: {img_path}")
                        # Create a placeholder - you might want to skip these or handle differently
                        new_content.append({
                            'type': 'image',
                            'image': f"<Missing: {img_path}>"
                        })
                except Exception as e:
                    print(f"Error loading image {img_path}: {e}")
                    new_content.append({
                        'type': 'image',
                        'image': f"<Error loading: {img_path}>"
                    })
                
                converted_messages.append({
                    'role': role,
                    'content': new_content
                })
            else:
                # No image, just text content
                converted_messages.append({
                    'role': role,
                    'content': [{'type': 'text', 'text': content}]
                })
        else:
            # Assistant messages are just text
            converted_messages.append({
                'role': role,
                'content': [{'type': 'text', 'text': content}]
            })
    
    return {'messages': converted_messages}

def convert_jsonl_file(input_file: str, output_file: str = None) -> List[Dict]:
    """
    Convert a JSONL file from original format to desired format.
    
    Args:
        input_file: Path to input JSONL file
        output_file: Path to output file (optional)
        
    Returns:
        List of converted conversations
    """
    converted_dataset = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f):
            line = line.strip()
            if line:
                try:
                    conversation = json.loads(line)
                    converted_conv = convert_message_format(conversation)
                    converted_dataset.append(converted_conv)
                except json.JSONDecodeError as e:
                    print(f"Error parsing line {line_num + 1}: {e}")
                except Exception as e:
                    print(f"Error processing line {line_num + 1}: {e}")
    
    # Save to output file if specified
    if output_file:
        if output_file.endswith('.jsonl'):
            # Save as JSONL
            with open(output_file, 'w', encoding='utf-8') as f:
                for conv in converted_dataset:
                    json.dump(conv, f, ensure_ascii=False, default=str)
                    f.write('\n')
        else:
            # Save as JSON
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(converted_dataset, f, ensure_ascii=False, indent=2, default=str)
    
    return converted_dataset

# Example usage
def main():
    # Convert your JSONL file
    input_file = "testdataset.jsonl"  # Replace with your actual file path
    output_file = "converted_dataset.jsonl"  # Output file path
    
    # Convert the file
    converted_dataset = convert_jsonl_file(input_file, output_file)
    
    # Print example of the first conversation
    if converted_dataset:
        print("Example of converted format:")
        print(f"converted_dataset[0] = {converted_dataset[0]}")
        print(f"\nTotal conversations converted: {len(converted_dataset)}")
        
        # Show structure of first message with image
        first_conv = converted_dataset[0]
        for msg in first_conv['messages']:
            if msg['role'] == 'user' and len(msg['content']) > 1:
                print(f"\nFirst user message with image:")
                print(f"Role: {msg['role']}")
                print(f"Content structure:")
                for i, content_item in enumerate(msg['content']):
                    if content_item['type'] == 'image':
                        print(f"  [{i}] type: {content_item['type']}, image: {type(content_item['image'])}")
                    else:
                        print(f"  [{i}] type: {content_item['type']}, text: '{content_item['text']}'")
                break

if __name__ == "__main__":
    
    # Convert test file
    converted_dataset = convert_jsonl_file("testdataset.jsonl", "test_output.jsonl")
    
    # Show result
    print("Sample conversion result:")
    if converted_dataset:
        print(f"converted_dataset[0] = {converted_dataset[0]}")