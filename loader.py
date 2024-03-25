import os
import json


class DocumentLoader:
    def __init__(self, relative_path):
        self.base_dir = os.path.dirname(__file__)
        self.file_path = os.path.join(self.base_dir, relative_path)
        self.documents = []

    def load_documents(self):
        target_domains = {'states of usa', 'countries', 'continents', 'regions'}
        with open(self.file_path, 'r', encoding='utf-8') as file:
            for line in file:
                document = json.loads(line.strip())
                if 'domain' in document:
                    domain = document['domain']
                    if isinstance(domain, list) and any(d in target_domains for d in domain):
                        if 'assertion' in document:
                            self.documents.append(document['assertion'])
                    elif isinstance(domain, str) and domain in target_domains:
                        if 'assertion' in document:
                            self.documents.append(document['assertion'])

    def get_documents(self):
        return self.documents

    def get_documents_count(self):
        return len(self.documents)

    def save_documents_to_file(self, output_path):
        with open(output_path, 'w', encoding='utf-8') as file:
            for document in self.documents:
                file.write(document + '\n')


# 사용 예시
if __name__ == "__main__":
    loader = DocumentLoader('data/candle_dataset_v1.jsonl')
    loader.load_documents()
    # 저장할 파일의 경로를 지정해주세요. 예: 'documents.txt'
    output_file_path = 'data/documents.txt'
    loader.save_documents_to_file(output_file_path)
    print(f"Documents have been saved to {output_file_path}")
