from datetime import datetime
start_time = datetime.now()

password = "332640"

x = list(int(i) for i in password)

attempt = [0 for i in range(len(x))]


def brute(A, i):
    for a in range(10):
        A[i] = a
        for b in range(10):
            A[i+1] = b
            for c in range(10):
                A[i + 2] = c
                for d in range(10):
                    A[i + 3] = d
                    for e in range(10):
                        A[i + 4] = e
                        for f in range(10):
                            A[i + 5] = f
                            if A == x:
                                print("Есть совпадение - ", A)
                            else:
                                pass



def main(A, i):
    brute(A,i)
    print("--- %s seconds ---" % (datetime.now() - start_time))


main(attempt, 0)

