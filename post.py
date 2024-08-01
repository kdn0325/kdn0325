import os

def update_readme():
    readme_path = 'README.md'
    image_url = 'https://raw.githubusercontent.com/kdn0325/terminal-for-github-profile-readme/1adccd811a108350e5dbe91c5e4911c04bd6f289/github_stats.svg'
    
    # 읽어온 README 파일 내용
    with open(readme_path, 'r') as file:
        content = file.readlines()
    
    # 이미지 URL 업데이트
    new_content = []
    for line in content:
        if '<img src="' in line:
            line = f'<img src="{image_url}" />\n'
        new_content.append(line)
    
    # 수정된 내용으로 README 파일 업데이트
    with open(readme_path, 'w') as file:
        file.writelines(new_content)

if __name__ == "__main__":
    update_readme()
