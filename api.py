import requests
import json
from datetime import datetime

OUTPUT_FILENAME = "test.json"

def get_jsonplaceholder_info():
    # 현재 분 + 1 → 1~60 사이 값 (61이 될 경우 처리)
    current_minute = datetime.now().minute
    TIME = (current_minute + 1) % 60 or 60  

    URL = f"https://jsonplaceholder.typicode.com/todos/{TIME}"
    response = requests.get(URL)

    if response.status_code != 200:
        print("API 요청 실패:", response.status_code)
        return None

    data = response.json()
    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False)

    print(f"{OUTPUT_FILENAME} 저장 완료.")

if __name__ == "__main__":
    get_jsonplaceholder_info()
