import requests

def get_coordinates(api_key, place_name):
    # Google Places API 엔드포인트
    endpoint = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"

    # API 호출에 필요한 파라미터 설정
    params = {
        "input": place_name,
        "inputtype": "textquery",
        "fields": "geometry/location",
        "key": api_key
    }

    try:
        # API 호출
        response = requests.get(endpoint, params=params)
        response.raise_for_status()  # 오류 발생 시 예외 처리

        # JSON 형식으로 응답을 파싱
        result = response.json()

        # 결과에서 좌표 추출
        coordinates = result['candidates'][0]['geometry']['location']
        return coordinates

    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something went wrong", err)

# API 키와 장소 이름 설정
api_key = "AIzaSyCUzWM4L4iAj-krLKiEx3MkD-j0HrqlNrs"
place_name = "아키하바라"  # 원하는 장소의 이름으로 변경

# 좌표 얻기
coordinates = get_coordinates(api_key, place_name)

# 결과 출력
print(f"{place_name}의 좌표: {coordinates}")
