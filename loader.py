import os
import json
from collections import defaultdict, Counter


class DocumentLoader:
    def __init__(self, relative_path):
        self.base_dir = os.path.dirname(__file__)
        self.file_path = os.path.join(self.base_dir, relative_path)
        self.documents = []

    def load_documents(self):
        target_domains = {'states of usa',
                          'countries', 'continents', 'regions'}
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

    def print_unique_facets_and_domains(self):
        unique_facets = set()
        unique_domains = set()
        with open(self.file_path, 'r', encoding='utf-8') as file:
            for line in file:
                document = json.loads(line.strip())
                if 'facet' in document:
                    facet = document['facet']
                    if isinstance(facet, list):
                        unique_facets.update(facet)
                    elif isinstance(facet, str):
                        unique_facets.add(facet)
                if 'domain' in document:
                    domain = document['domain']
                    if isinstance(domain, list):
                        unique_domains.update(domain)
                    elif isinstance(domain, str):
                        unique_domains.add(domain)
        print("Unique Facets:")
        for facet in unique_facets:
            print(f"- {facet}")
        print("\nUnique Domains:")
        for domain in unique_domains:
            print(f"- {domain}")

    def save_subjects_of_countries_to_file(self, output_path):
        subjects_counter = Counter()
        facets_by_subject = defaultdict(Counter)
        output_content = ""

        with open(self.file_path, 'r', encoding='utf-8') as file:
            for line in file:
                document = json.loads(line.strip())
                if 'domain' in document and document['domain'] == 'countries':
                    if 'subject' in document and 'facet' in document:
                        subject = document['subject']
                        facets = document['facet']
                        subjects_counter[subject] += 1
                        if isinstance(facets, list):
                            for facet in facets:
                                facets_by_subject[subject][facet] += 1
                        elif isinstance(facets, str):
                            facets_by_subject[subject][facets] += 1

        output_content += "Subjects and their frequencies in 'countries' domain (sorted by frequency):\n"
        for subject, count in subjects_counter.most_common():
            output_content += f"\n{subject}: {count} occurrences\n"
            output_content += "Facet frequencies:\n"
            for facet, facet_count in facets_by_subject[subject].items():
                output_content += f"  - {facet}: {facet_count}\n"

        # Save to file
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(output_content)
        print(f"Output has been saved to {output_path}")


# 사용 예시
if __name__ == "__main__":
    loader = DocumentLoader('data/candle_dataset_v1.jsonl')
    loader.load_documents()
    # 저장할 파일의 경로를 지정해주세요. 예: 'documents.txt'
    output_file_path = 'data/documents.txt'
    output_file_path2 = 'data/countries.txt'
    loader.save_documents_to_file(output_file_path)
    print(f"Documents have been saved to {output_file_path}")
    loader.print_unique_facets_and_domains()
    loader.save_subjects_of_countries_to_file(output_file_path2)
