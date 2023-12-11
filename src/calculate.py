from math import radians, sin, cos, sqrt, atan2

def haversine(lat1, lon1, lat2, lon2):
    # 지구의 반지름 (단위: km)
    R = 6371.0

    # 위도 및 경도 값을 라디안으로 변환
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine 공식 계산
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # 거리 계산 (단위: km)
    distance = R * c

    return distance

# 입구-제1 아프리카관
lat1, lon1 =  37.42966, 127.01724
lat2, lon2 = 37.42645, 127.01836
distance_km = haversine(lat1, lon1, lat2, lon2)
print(f"입구-제1 아프리카관: {distance_km:.2f} km")

# 입구-제2 아프리카관
lat1, lon1 =  37.42966, 127.01724
lat2, lon2 = 37.42608,  127.02146
distance_km = haversine(lat1, lon1, lat2, lon2)
print(f"입구-제2 아프리카관: {distance_km:.2f} km")

# 제2 아프리카관-제3 아프리카관
lat1, lon1 =  37.42645, 127.01836
lat2, lon2 = 37.42818,  127.01649
distance_km = haversine(lat1, lon1, lat2, lon2)
print(f"제2 아프리카관-제3 아프리카관: {distance_km:.2f} km")

# 제2 아프리카관-낙타사
lat1, lon1 =  37.42645, 127.01836
lat2, lon2 = 37.42391,  127.02232
distance_km = haversine(lat1, lon1, lat2, lon2)
print(f"제2 아프리카관-낙타사: {distance_km:.2f} km")

# 제2 아프리카관-대동물관
lat1, lon1 =  37.42645, 127.01836
lat2, lon2 = 37.42486,  127.02019
distance_km = haversine(lat1, lon1, lat2, lon2)
print(f"제2 아프리카관-대동물관: {distance_km:.2f} km")

# 제1 아프리카관-대동물관
lat1, lon1 =  37.42608,  127.02146
lat2, lon2 = 37.42486,  127.02019
distance_km = haversine(lat1, lon1, lat2, lon2)
print(f"제1 아프리카관-대동물관: {distance_km:.2f} km")

# 제3 아프리카관-낙타사
lat1, lon1 = 37.42818,  127.01649
lat2, lon2 = 37.42391,  127.02232
distance_km = haversine(lat1, lon1, lat2, lon2)
print(f"제3 아프리카관-낙타사: {distance_km:.2f} km")

# 낙타사-대동물관
lat1, lon1 =  37.42391,  127.02232
lat2, lon2 = 37.42486,  127.02019
distance_km = haversine(lat1, lon1, lat2, lon2)
print(f"낙타사-대동물관: {distance_km:.2f} km")

# 낙타사-맹수사
lat1, lon1 =  37.42391,  127.02232
lat2, lon2 = 37.42254,  127.02465
distance_km = haversine(lat1, lon1, lat2, lon2)
print(f"낙타사-맹수사: {distance_km:.2f} km")

# 낙타사-해양관
lat1, lon1 =  37.42391,  127.02232
lat2, lon2 = 37.42207,  127.02191
distance_km = haversine(lat1, lon1, lat2, lon2)
print(f"낙타사-해양관: {distance_km:.2f} km")

# 대동물관-남미관
lat1, lon1 =  37.42486,  127.02019
lat2, lon2 = 37.41811,  127.02204
distance_km = haversine(lat1, lon1, lat2, lon2)
print(f"대동물관-남미관: {distance_km:.2f} km")

# 대동물관-해양관
lat1, lon1 =  37.42486,  127.02019
lat2, lon2 = 37.42207,  127.02191
distance_km = haversine(lat1, lon1, lat2, lon2)
print(f"대동물관-해양관: {distance_km:.2f} km")

# 해양관-맹수사
lat1, lon1 =  37.42207,  127.02191
lat2, lon2 = 37.42254,  127.02465
distance_km = haversine(lat1, lon1, lat2, lon2)
print(f"해양관-맹수사: {distance_km:.2f} km")

# 해양관-곰사
lat1, lon1 =  37.42207,  127.02191
lat2, lon2 = 37.42080,  127.02368
distance_km = haversine(lat1, lon1, lat2, lon2)
print(f"해양관-곰사: {distance_km:.2f} km")

# 해양관-사슴사
lat1, lon1 =  37.42207,  127.02191
lat2, lon2 = 37.42092,  127.02188
distance_km = haversine(lat1, lon1, lat2, lon2)
print(f"해양관-사슴사: {distance_km:.2f} km")

# 맹수사-곰사
lat1, lon1 =  37.42254,  127.02465
lat2, lon2 = 37.42080,  127.02368
distance_km = haversine(lat1, lon1, lat2, lon2)
print(f"맹수사-곰사: {distance_km:.2f} km")

# 곰사-남미관
lat1, lon1 =  37.42080,  127.02368
lat2, lon2 = 37.41811,  127.02204
distance_km = haversine(lat1, lon1, lat2, lon2)
print(f"곰사-남미관: {distance_km:.2f} km")

# 사슴사-남미관
lat1, lon1 =  37.42092,  127.02188
lat2, lon2 = 37.41811,  127.02204
distance_km = haversine(lat1, lon1, lat2, lon2)
print(f"사슴사-남미관: {distance_km:.2f} km")