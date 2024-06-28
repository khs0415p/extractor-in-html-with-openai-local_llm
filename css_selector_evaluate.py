# Gpt4o css 셀렉터 평가
# - 원래 답이랑 비교할 필요 없음
# - 목록, 본문 path들이 섞여있기 때문

# - gpt-4o의 출력을 직접 확인해보거나 bs4를 이용해서 실제 텍스트와 일치하는지 확인하는 방법 적용


# html_data의 current_url을 이용하여, 모델이 생성한 path로 css_selector로 찔러보고
# html_data의 title, date, content의 내용과 일치하는지 판단하기.

import json
import pickle
import requests
import random
import tqdm

from collections import defaultdict
from bs4 import BeautifulSoup as bs
from agent import Agent
from utils import extract_json
random.seed(42)

with open('make_data/data/html_data.pk', 'rb') as f:
    html_data = pickle.load(f)

with open('make_data/data/css_data.pk', 'rb') as f:
    css_data = pickle.load(f)

output_file = open('css_selector_test.txt', 'w', encoding='utf-8')

random_indices = random.sample(range(len(html_data)), 10)
agent = Agent('gpt', 'css', 'prompt') # or function_call
for idx in tqdm.tqdm(random_indices):
    url = html_data[idx]['current_url']
    html = requests.get(url)
    soup = bs(html.text, 'html.parser')

    answer = agent.run(html_data[idx]['model_input'])
    answer = extract_json(answer)

    if isinstance(answer, dict):
        predict = defaultdict(str)
        actual = {"title" : html_data[idx]['ground_truth']['title'], "date": html_data[idx]['ground_truth']['date'], "content": '\n'.join([item['data'] for item in html_data[idx]['ground_truth']['content'] if item['type'] == 'txt'])}
        for key in ['title', 'date', 'content']:
            if isinstance(answer[key], list):
                for item in answer[key]:
                    if isinstance(item, list):
                        for ele in item:
                            css_selector = ele['path']
                            output = soup.select(css_selector)
                            for tag in output:
                                predict[key] += tag.text.strip()
                    else:
                        css_selector = item['path']
                        output = soup.select(css_selector)
                        for tag in output:
                            predict[key] += tag.text.strip()
            else:
                css_selector = answer[key]['path']
                output = soup.select(css_selector)
                for tag in output:
                    predict[key] += tag.text.strip()
        
        output_file.write(f"=============================== {idx}\n")
        output_file.write("[PREDICT]\n")
        output_file.write(json.dumps(predict, indent=4) + '\n')
        output_file.write("[ACTUAL]\n")
        output_file.write(json.dumps(actual, indent=4) + '\n')

output_file.close()