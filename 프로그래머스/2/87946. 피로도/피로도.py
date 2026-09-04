def solution(k, dungeons):
    n = len(dungeons)
    visited = [False] * n
    max_count = 0

    def dfs(current_k, count):
        nonlocal max_count
        max_count = max(max_count, count)
        
        for i in range(n):
            req, cost = dungeons[i]
            # 아직 방문하지 않았고 최소 필요 피로도를 만족하는 경우
            if not visited[i] and current_k >= req:
                visited[i] = True
                dfs(current_k - cost, count + 1)
                visited[i] = False  # 백트래킹

    dfs(k, 0)
    return max_count