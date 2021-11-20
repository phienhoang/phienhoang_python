import multiprocessing


def worker():
    LIST.append('item')


LIST = []


if __name__ == "__main__":
    processes = [
        multiprocessing.Process(target=worker)
        for _ in range(5)
    ]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print(LIST)

    """В Python процессы выполняются независимо и имеют собственное пространство памяти.
    все процессы могут использовать глобальные данные, но у них будет разная память для обработки, поэтому они не влияют друг на друга."""