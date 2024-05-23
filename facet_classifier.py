import os

# 파일 경로 설정
caption_file = 'data/caption.txt'
food_file = 'data/food.txt'
drink_file = 'data/drink.txt'
clothes_file = 'data/clothes.txt'

# 파일 읽기
with open(caption_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 문장 수를 세기 위한 변수 초기화
food_count = 0
drink_count = 0
clothes_count = 0

# 각 카테고리에 맞는 문장 저장하기
with open(food_file, 'a', encoding='utf-8') as food_f, \
        open(drink_file, 'a', encoding='utf-8') as drink_f, \
        open(clothes_file, 'a', encoding='utf-8') as clothes_f:
    for line in lines:
        if 'food' in line:
            food_f.write(line)
            food_count += 1
        if 'beer' in line:
            drink_f.write(line)
            drink_count += 1
        if 'clothing' in line:
            clothes_f.write(line)
            clothes_count += 1

# 각 파일에 저장된 문장 수 출력
print(f'{os.path.basename(food_file)}: {food_count} 문장')
print(f'{os.path.basename(drink_file)}: {drink_count} 문장')
print(f'{os.path.basename(clothes_file)}: {clothes_count} 문장')
