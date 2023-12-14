import numpy as np
from itertools import combinations
from datetime import  datetime


def tietz_and_bart(D, H, p):
    V = np.arange(D.shape[0])

    R = H @ D
    # select a initial vertex subset V1 of length p
    V1 = np.copy(V[:p])  # NOTE: we assume that V1 is the first p vertices

    print(f"{R=}")
    print(f"{V1=}\n")

    PREV_COST = 0
    COST = 0

    cycle_count = 0
    while True:
        VERTEX_SEEN_AS_SOURCE = set(V1)
        P1JS = []

        # P1J calculation, which is correct for this setup.
        for jvertex in V1:
            # for every v_{j} \belongs V1
            P1J = []
            for ivertex in V:
                # append it if ALL distances from i to j are smaller than from i to k.
                dist_from_ivertex_to_jvertex = R[ivertex, jvertex]
                for kvertex in V1:
                    dist_from_ivertex_to_kvertex = R[ivertex, kvertex]
                    if dist_from_ivertex_to_jvertex > dist_from_ivertex_to_kvertex:
                        break
                else:
                    P1J.append(ivertex)
                # do not append because we got breaked

            P1JS.append(P1J)
        print(f"{P1JS=}")

        # scenario's cost
        # COST = 0
        # for j in np.arange(len(V1)):
        #     for i in P1JS[j]:
        #         jvertex = V1[j]
        #         COST += R[i, jvertex]
        # print(f"{COST=}\n")

        # REM_VB cannot be in any previous Vx.
        REM_VBs = list(set(V) - VERTEX_SEEN_AS_SOURCE)

        print(f"{REM_VBs=}")

        NEXT_VB_IDX = 0
        while NEXT_VB_IDX < len(REM_VBs):
            VB = REM_VBs[NEXT_VB_IDX]

            # for VB in REM_VBs:
            print(f"{VB=}")

            DELTA_BJS = []

            for jvertexidx in np.arange(len(V1)):
                V1copy = V1.copy()
                jvertex = V1copy[jvertexidx]
                print(f"{jvertex=}")

                # TRYING VB as jvertex replacement (hypothesis)
                V1copy[jvertexidx] = VB
                VERTEX_SEEN_AS_SOURCE.add(VB)

                print(f"{V1copy=}")
                SUBR = R[:, V1copy]
                # print(f"{SUBR=}\n")

                DELTA_BJ = 0
                i = 0
                for ithrow in SUBR:
                    # print(f"{ithrow=}")
                    ithrowmin = np.min(ithrow)
                    # print(f"{ithrowmin=}")
                    rij = R[i, jvertex]

                    # if rij != ithrowmin_BEFORE:
                    #     continue

                    # if rij == ithrowmin:
                    #     pass

                    ris = np.sort(ithrow)[1]
                    rib = R[i, VB]

                    # case 1
                    if rib <= rij:
                        SOME_DELTA_IBJ = rij - rib
                    elif rij <= rib and rib <= ris:
                        SOME_DELTA_IBJ = rij - rib
                    elif rij <= ris and ris <= rib:
                        SOME_DELTA_IBJ = rij - ris
                    # print(f"{i=} {ris=} {rij=} {rib=} {SOME_DELTA_IBJ=}\n")
                    DELTA_BJ += SOME_DELTA_IBJ
                    i += 1
                print(f"{DELTA_BJ=}\n")
                DELTA_BJS.append(DELTA_BJ)

            DELTA_BK = np.min(DELTA_BJS)
            print(f"{DELTA_BJS=} {DELTA_BK=}")

            if DELTA_BK < 0:
                # we found the VK meeting required conditions
                print(
                    f"Found {VB} better than {V1[np.argmin(DELTA_BJS)]} in setup {V1} with improvement {DELTA_BK}. Hence updating V1."
                )
                V1[np.argmin(DELTA_BJS)] = VB

            NEXT_VB_IDX += 1

        print(f"{VERTEX_SEEN_AS_SOURCE=}")

        print(f"{V1=}")

        COST = 0
        for j in np.arange(len(V1)):
            for i in P1JS[j]:
                jvertex = V1[j]
                COST += R[i, jvertex]

        if COST == PREV_COST:
            break
        else:
            PREV_COST = COST

        cycle_count += 1
        print("== NEXT CYCLE ==")

    return V1, COST, cycle_count


if __name__ == "__main__":
    np.random.seed(10)

    D = np.array(
        [
            [0, 1, 2, 2, 40, 20],
            [1, 0, 1, 2, 8, 18],
            [2, 1, 0, 1, 9, 19],
            [2, 2, 1, 0, 9.5, 20.5],
            [40, 8, 9, 9.5, 0, 60],
            [20, 18, 19, 20.5, 60, 0],
        ],
    )  # 3 x 3 so 3 nodes

    # # random 12x12 symmetric matrix
    # D = np.random.randint(0, 100, size=(50, 50))
    # D = (D + D.T) / 2
    # np.fill_diagonal(D, 0)
    # print(D)

    H = np.array(
        [
            [1, 0, 0, 0, 0, 0],
            [0, 3, 0, 0, 0, 0],
            [0, 0, 2, 0, 0, 0],
            [0, 0, 0, 5, 0, 0],
            [0, 0, 0, 0, 4, 0],
            [0, 0, 0, 0, 0, 6],
        ],
    )

    # H = np.eye(50)


    print("== INPUTS ==")
    print(D)
    print(H)
    print("Calculating for p = 3")

    print("== TEITZ AND BART (VERTEX SUB.) SOLVER ==")

    st = datetime.now()
    print(tietz_and_bart(D, H, p=3))
    print(f"Time taken: {(datetime.now() - st).microseconds} mis ")
