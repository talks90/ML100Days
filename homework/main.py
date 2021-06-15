if __name__ == '__main__':
    import numpy as np

    a = np.random.randint(10, size=6)

    print(a.tolist())
    print(list(a))

    b = np.random.randint(10, size=(3, 4))

    print(b.tolist())
    print(list(b))

    c = np.random.randint(10, size=(2, 3, 2))

    print(c.tolist())
    print(list(c))

    def tolist(iterable):
        return [list(iterable[x]) for x in range(iterable.ndim + 1)]


    # print(tolist(a))
    print(tolist(b))
    # print(tolist(c))
