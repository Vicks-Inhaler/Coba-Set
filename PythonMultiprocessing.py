# *********************************
# Python multiprocessing
# *********************************
# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():

    print("CPU Count : ", cpu_count())

    # a = Process(target=counter, args=(500000000,))
    # b = Process(target=counter, args=(500000000,))
    #
    # a.start()
    # b.start()
    #
    # print("processing...")
    #
    # a.join()
    # b.join()
    #
    # print("Done!")
    # print("finished in:", time.perf_counter(), "seconds")

    A = Process(target=counter, args=(125000000,))
    B = Process(target=counter, args=(125000000,))
    C = Process(target=counter, args=(125000000,))
    D = Process(target=counter, args=(125000000,))
    E = Process(target=counter, args=(125000000,))
    F = Process(target=counter, args=(125000000,))
    G = Process(target=counter, args=(125000000,))
    H = Process(target=counter, args=(125000000,))

    A.start()
    B.start()
    C.start()
    D.start()
    E.start()
    F.start()
    G.start()
    H.start()

    print("Processing...")

    A.join()
    B.join()
    C.join()
    D.join()
    E.join()
    F.join()
    G.join()
    H.join()

    print("Done!")
    print("Finished in : ", time.perf_counter(), "seconds")


if __name__ == '__main__':
    main()

# *********************************