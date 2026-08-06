def dfs(graph, start, goal, visited):
    if start == goal:
        return 1
    
    visited[start] = True
    
    for neighbor in graph[start]:
        # 방문하지 않은 경우
        if not visited[neighbor]:
            if dfs(graph, neighbor, goal, visited):
                return 1

    return 0


T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    
    graph = [[] for _ in range(V + 1)]
    
    # 간선 정보 입력
    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)
    
    # S -> G의 경로가 존재하는지 확인
    S, G = map(int, input().split())
    
    visited = [False] * (V + 1)
    
    result = dfs(graph, S, G, visited)
    
    print(f'#{test_case} {result}')