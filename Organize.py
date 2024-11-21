import os
import shutil


# MacOS의 기본 다운로드 폴더 경로
downloads_folder = os.path.expanduser('~/Downloads')

# 파일 형식별 디렉토리 매핑
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.heic'],
    'Documents': ['.pdf', '.docx', '.txt', '.pages', '.ppt', '.pptx'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Programs': ['.dmg', '.pkg', '.zip'],
    'Code': ['.py', '.js', '.html', '.css', '.java', '.c', '.cpp', '.ipynb'],
    'Data': ['.csv', '.json', '.xls', '.xlsx', '.sql']
}

# 파일 정리 함수
def organize_files():
    for filename in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, filename)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            for folder, extensions in file_types.items():
                if file_ext in extensions:
                    folder_path = os.path.join(downloads_folder, folder)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    shutil.move(file_path, os.path.join(folder_path, filename))
                    break

organize_files()