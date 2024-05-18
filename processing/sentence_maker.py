import os
import json

# 현재 파일의 디렉토리 경로를 가져옴
current_directory = os.path.dirname(__file__)

# data 폴더의 경로 설정
data_directory = os.path.join(current_directory, '../data')

# 파일 경로 설정
file_paths = {
    'food': os.path.join(data_directory, 'food.txt'),
    'drink': os.path.join(data_directory, 'drink.txt'),
    'clothing': os.path.join(data_directory, 'clothes.txt')
}

# 파일 읽기 함수
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

# 문장 처리 함수
def process_sentences(sentences, keyword):
    processed = []
    count = 0
    for sentence in sentences:
        if count >= 200:
            break
        if keyword in sentence:
            processed.append(sentence.strip().replace(keyword, '{national_keyword}'))
            count += 1
    return processed

# 결과를 저장할 딕셔너리
results = {}

# 각 파일에 대해 처리
for category, path in file_paths.items():
    sentences = read_file(path)
    processed_sentences = process_sentences(sentences, category)
    results[category] = processed_sentences

# 결과를 JSON 파일로 저장
output_path = os.path.join(data_directory, 'sentences.json')
with open(output_path, 'w', encoding='utf-8') as json_file:
    json.dump(results, json_file, ensure_ascii=False, indent=4)

print(f'Sentences have been processed and saved to {output_path}')
