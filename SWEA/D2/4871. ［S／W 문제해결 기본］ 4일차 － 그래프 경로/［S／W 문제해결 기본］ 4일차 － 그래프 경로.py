def dfs(graph, start, goal, visited):
    stack = [start]
    
    while stack:
        current_node = stack.pop()
        
        if current_node == goal:
            return 1
        
        # 이전에 방문한 노드이면 
        if visited[current_node]:
            continue
        
        # 현재 노드를 방문 처리
        visited[current_node] = True
        
        for neighbor in graph[current_node]:
            # 방문하지 않은 이웃 노드를 스택에 추가
            if not visited[neighbor]:
                stack.append(neighbor)
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