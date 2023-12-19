import requests

def get_coordinates(api_key, query):
    # 카카오 맵 API 엔드포인트
    endpoint = "https://dapi.kakao.com/v2/local/search/keyword.json"

    # API 헤더에 키 설정
    headers = {
        "Authorization": f"KakaoAK {api_key}"
    }

    # API 호출에 필요한 파라미터 설정
    params = {
        "query": query
    }

    try:
        # API 호출
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()  # 오류 발생 시 예외 처리

        # JSON 형식으로 응답을 파싱
        result = response.json()

        # 결과에서 좌표 추출
        coordinates = result['documents'][0]['x'], result['documents'][0]['y']
        return coordinates

    except requests.exceptions.HTTPError as errh:
        print ("HTTP Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("OOps: Something went wrong",err)

# API 키와 장소 이름 설정
api_key = "bf1646daa9707fff9410f516d2163cc0" # Rest API 용 카카오 무한 스크롤 지도 어플용 Key
place_name = "카카오판교오피스"  # 원하는 장소의 이름으로 변경

# 좌표 얻기
coordinates = get_coordinates(api_key, place_name)

# 결과 출력
print(f"{place_name}의 좌표: {coordinates}")
