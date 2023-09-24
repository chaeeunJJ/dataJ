# dataJ
import requests
res = requests.get("http://google.com")
res.raise_for_status()

#접속 권환 확인
#print("응답코드 :", res.status_code) # 200: 정답, 403: 접근 권한 없음

#if res.status_code == requests.codes.ok:
#    print("정상입니다")
#else:
#    print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

print(len(res.text))

#웹페이지 파일로 가져와서 열기
with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)