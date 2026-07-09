def solution(mats, park):
    mats = sorted(mats, reverse = True)
    M, N = len(park), len(park[0])

    for l in mats:
        startIdxSet = set((i,j) for i in range(M-l+1) for j in range(N-l+1))
        for a, b in startIdxSet:
            ret = set()
            for i in range(a,a+l):
                for j in range(b,b+l):
                    ret.add(park[i][j])
            if ret == {'-1'}:
                return l
    return -1