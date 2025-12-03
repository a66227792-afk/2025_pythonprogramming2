def merge_files(file1_path, file2_path, output_file_path):
    # 파일 1 읽기
    with open(file1_path, 'r',  encoding='utf-8') as file1:
        file1_content = file1.read()

    # 파일 2 읽기
    with open(file2_path, 'r',  encoding='utf-8') as file2:
        file2_content = file2.read()

    # 파일 1과 파일 2의 내용 합치기
    merged_content = file1_content + '\n' + file2_content

    # 출력 파일에 합친 내용 쓰기
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(merged_content)

# 파일 경로 지정
file1_path = 'file1.txt'
file2_path = 'file2.txt'
output_file_path = 'output.txt'

# 파일 합치기 함수 호출
merge_files(file1_path, file2_path, output_file_path)