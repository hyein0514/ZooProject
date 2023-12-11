import heapq

def dijkstra(graph, start):
    distance = {node: float('infinity') for node in graph}
    distance[start] = 0
    previous = {node: None for node in graph}

    # 우선순위 큐를 사용하여 최소 거리 노드 선택
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # 현재 노드까지의 거리가 이미 갱신된 경우 무시
        if current_distance > distance[current_node]:
            continue

        # 현재 노드의 인접 노드를 순회하며 최단 거리 갱신
        for neighbor, weight in graph[current_node].items():
            distance_to_neighbor = current_distance + weight

            # 더 짧은 경로를 발견한 경우 갱신
            if distance_to_neighbor < distance[neighbor]:
                distance[neighbor] = distance_to_neighbor
                previous[neighbor] = current_node
                heapq.heappush(priority_queue, (distance_to_neighbor, neighbor))

    return distance, previous

# 인접 리스트
graph = {
    '입구': {'제2 아프리카관': 55},
    '제2 아프리카관': {'입구': 55, '대동물관': 24, '낙타사': 45},
    '대동물관': {'제2 아프리카관': 24, '낙타사': 22, '해양관': 35, '남미관': 77},
    '낙타사': {'제2 아프리카관': 45, '대동물관': 22, '해양관': 21, '맹수사': 26},
    '해양관': {'낙타사': 21, '대동물관': 35, '맹수사': 25, '곰사': 21, '사슴사': 13},
    '맹수사': {'낙타사': 26, '해양관': 25, '곰사': 21},
    '곰사': {'맹수사': 21, '해양관': 21, '남미관': 33},
    '사슴사': {'해양관': 13, '남미관': 31},
    '남미관': {'곰사': 33, '사슴사': 31, '대동물관': 77}
}


# 시작 노드 지정
start_node = input("시작 노드를 입력하세요: ").strip()
distances, previous = dijkstra(graph, start_node)

# 결과 출력
print(f"시작 노드: {start_node}")
print("-" * 30)
for destination, dist in distances.items():
    print(f"최소 거리 ({start_node}에서 {destination}): {dist}")

    # 최소 경로 출력
    path = []
    current = destination
    while current:
        path.append(current)
        current = previous[current]
    path.reverse()
    print(f"최소 경로: {' -> '.join(path)}")
    print("-" * 30)