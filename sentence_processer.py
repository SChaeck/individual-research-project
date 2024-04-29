# nation 리스트 준비
nation = ['korean', 'turkish', 'egyptian', 'thai', 'mexican', 'spanish']


def process_sentences(input_file, output_file, nation_list):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(output_file, 'w', encoding='utf-8') as file:
        for line in lines:
            if '{national}' in line:
                # {national}을 포함하는 문장에 대해 nation 리스트의 각 요소로 대체한 문장을 생성
                for nation in nation_list:
                    processed_line = line.replace('{national}', nation)
                    file.write(processed_line)
            else:
                # [national]을 포함하지 않는 문장은 그대로 저장
                file.write(line)


# 사용 예시
input_file_path = 'data/sentences.txt'
output_file_path = 'data/processed_data.txt'
process_sentences(input_file_path, output_file_path, nation)
print(f"'{input_file_path}'에서 문장을 읽어 각각 '{output_file_path}'에 저장했습니다.")
