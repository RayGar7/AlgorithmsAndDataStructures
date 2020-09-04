from copy import copy, deepcopy


def rotate(m):
    if len(m) == 0:
        return []
    else:
        N = len(m) - 1
        r = deepcopy(m)
        for i in range(0, N+1):
            for j in range(0, N+1):
                r[i][j] = m[N-j][i]
        print(r)


rotate([[1, 2], [3, 4]])
rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


def rotate_in_place(m):
    N = len(m)
    for layer in range(0, N/2):
        first = layer
        last = N - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = m[first][i]
            // top: = left
            m[first][i] = m[last-offset][first]
            // left: = bottom
            m[last-offset][first] = m[last][last-offset]
            // bottom: = right
            m[last][last-offset] = m[i][last]
            // right: = top
            m[i][last] = top
