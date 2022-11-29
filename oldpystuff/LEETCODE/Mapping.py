class Mapping:
    def minDistance(word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        if n * m == 0:
            return n + m
        
        D = [ [0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            D[i][0] = i
        for j in range(m + 1):
            D[0][j] = j
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = D[i - 1][j] + 1
                down = D[i][j - 1] + 1
                left_down = D[i - 1][j - 1] 
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                D[i][j] = min(left, down, left_down)
        
        return D[n][m]
    def walking(t : int) -> float:
        return t * 1.2

pos1 = "673406674928664597"
pos2 = "673406674928664597"

dis = Mapping.minDistance(pos1,pos2)
t = Mapping.walking(dis)

print(f"從 {pos1} 到 {pos2} 需要 {t} 小時")