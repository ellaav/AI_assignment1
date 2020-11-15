from random import randint
import sys

N = 35
D = 10
MAX_W = 20
MAX_P = 10


def write_vertices(f, n):
    for i in range(1, n + 1):
        if randint(0, 2) > 0:
            p = randint(1, MAX_P)
            f.write('#V' + str(i) + " P" + str(p) + ' ;\n')
        else:
            f.write('#V' + str(i) + ' ;\n')
    f.write('\n')


def write_edges(f, n):
    e_num = 1
    for j in range(1, n):
        for k in range(j + 1, n + 1):
            if randint(0, 2) > 0:
                w = randint(0, MAX_W)
                f.write('#E' + str(e_num) + ' ' + str(j) +
                        ' ' + str(k) + ' W' + str(w) + ' ;\n')
                e_num += 1


if __name__ == '__main__':

    if len(sys.argv) > 1:
        N = int(sys.argv[1])
        if len(sys.argv) > 2:
            D = float(sys.argv[2])
            if len(sys.argv) > 3:
                MAX_W = int(sys.argv[3])

    with open('random_graph.txt', 'w') as f:
        f.write('#N ' + str(N) + ' ;\n')
        f.write('#D ' + str(D) + ' ;\n')
        write_vertices(f, N)
        write_edges(f, N)
        f.close()
    print('file random_graph.txt generated successfully')
