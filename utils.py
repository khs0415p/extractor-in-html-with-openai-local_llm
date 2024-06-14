import re
import json
import pickle

def extract_json(text: str):
    text = re.sub('```json|```', "", text).strip()

    try:
        text = json.loads(text)
    except:
        pass

    return text

def load_data(task):
    if task == 'html':
        file_name = "html_data.pk"
    else:
        file_name = "css_data.pk"
    
    with open(f'make_data/data/{file_name}', 'rb') as f:
        data = pickle.load(f)
    
    return data