import os
import json

class DocumentLoader:
    def __init__(self, relative_path):
        # 현재 스크립트 파일의 디렉토리를 기준으로 상대 경로를 계산
        self.base_dir = os.path.dirname(__file__)
        self.file_path = os.path.join(self.base_dir, relative_path)
        self.documents = []

    def load_documents(self):
        """JSONL 파일에서 문서를 로드합니다."""
        with open(self.file_path, 'r', encoding='utf-8') as file:
            for line in file:
                document = json.loads(line.strip())
                # 'assertion' 키가 있는지 확인하고, 해당 값만 documents 리스트에 추가
                if 'assertion' in document:
                    self.documents.append(document['assertion'])

    def get_documents(self):
        """로드된 문서 리스트를 반환합니다."""
        return self.documents

# 사용 예시: 현재 스크립트 위치와 상대적으로 파일 경로를 지정
if __name__ == "__main__":
    # 상대 경로 예시: 'data/candle_dataset_v1.jsonl'
    loader = DocumentLoader('data/candle_dataset_v1.jsonl')
    loader.load_documents()
    documents = loader.get_documents()
    print(documents)