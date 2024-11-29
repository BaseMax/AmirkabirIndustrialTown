import json

FILE_INPUT = 'data.json'
FILE_OUTPUT = 'clean.json'


def clean_json():
    with open(FILE_INPUT, 'r', encoding='utf-8') as f:
        data = json.load(f)
        with open(FILE_OUTPUT, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    clean_json()
