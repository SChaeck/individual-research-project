import os
import json


class CaptionLoader:
    def __init__(self, relative_path):
        self.file_path = os.path.join(os.getcwd(), relative_path)
        self.captions = []

    def load_captions(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for annotation in data['annotations']:
                self.captions.append(annotation['caption'])

    def save_captions_to_file(self, output_path):
        with open(output_path, 'w', encoding='utf-8') as file:
            for caption in self.captions:
                file.write(caption + '\n')


# 사용 예시
if __name__ == "__main__":
    loader = CaptionLoader('data/captions_train2017.json')
    loader.load_captions()
    output_file_path = 'data/caption.txt'
    loader.save_captions_to_file(output_file_path)
    print(f"Captions have been saved to {output_file_path}")
