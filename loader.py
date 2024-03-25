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
        # 관심 있는 domain 값들
        target_domains = {'states of usa', 'countries', 'continents', 'regions'}
        with open(self.file_path, 'r', encoding='utf-8') as file:
            for line in file:
                document = json.loads(line.strip())
                if 'domain' in document:
                    domain = document['domain']
                    # domain이 리스트인 경우와 문자열인 경우 모두 고려
                    if isinstance(domain, list):
                        if any(d in target_domains for d in domain):
                            if 'assertion' in document:
                                self.documents.append(document['assertion'])
                    elif isinstance(domain, str):
                        if domain in target_domains:
                            if 'assertion' in document:
                                self.documents.append(document['assertion'])

    def get_documents(self):
        """로드된 문서 리스트를 반환합니다."""
        return self.documents

    def get_documents_count(self):
        """로드된 문서의 총 개수를 반환합니다."""
        return len(self.documents)

# 사용 예시: 현재 스크립트 위치와 상대적으로 파일 경로를 지정
if __name__ == "__main__":
    loader = DocumentLoader('data/candle_dataset_v1.jsonl')
    loader.load_documents()
    documents = loader.get_documents()
    documents_count = loader.get_documents_count()
    print(f"추출된 assertion: {documents}")
    print(f"총 추출된 assertion 수: {documents_count}")
