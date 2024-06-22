import requests

BASE_URL = "http://127.0.0.1:5000"

def test_parse_resume(file_path):
    with open(file_path, 'rb') as f:
        response = requests.post(f"{BASE_URL}/parse", files={'file': f})
        print(response.json())

def test_get_taxonomy():
    response = requests.get(f"{BASE_URL}/taxonomy")
    print(response.json())

if __name__ == "_main_":
    test_parse_resume('tests/sample_resumes/resume1.pdf')
    test_parse_resume('tests/sample_resumes/resume2.docx')
    test_parse_resume('tests/sample_resumes/resume3.txt')
    test_get_taxonomy()