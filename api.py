import requests
import os
import json
from datetime import datetime, timedelta

# --- 설정 ---
# 저장될 디렉토리와 파일명을 지정합니다.
def get_jsonplaceholder_info():
    OUTPUT_DIR = "/tmp"
    OUTPUT_FILENAME = "test.json"
    OUTPUT_PATH = os.path.join(OUTPUT_DIR, OUTPUT_FILENAME)

    # 시간 
    current_minute = datetime.now().minute
    TIME = current_minute + 1
    #API URL
    URL = f"https://jsonplaceholder.typicode.com/todos/{TIME}"

    def get_jsonplaceholder_info():
        response = requests.get(URL)
        if response.status_code != 200:
            print("API 요청 실패:", response.status_code)
            return None

        data = response.json()
        with open(OUTPUT_PATH, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False)

if __name__ == "__main__":
    get_jsonplaceholder_info()