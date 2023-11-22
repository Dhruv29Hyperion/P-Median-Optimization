import numpy as np


def tietz_and_bart(D, H, p):
    
    V = np.arange(D.shape[0])

    R = H @ D
    print(f"{R=}")
    V1 = np.copy(V[:p])

    while True:
        # select a initial vertex subset V1 of length p
        print(f"{V1=}\n")
        print(f"{V=}\n")
        P1JS = []
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

            print(f"{jvertex=}")
            print(f"{P1J=}")
            print("\n")
            P1JS.append(P1J)

        print(f"{P1JS=}")
        r1 = 0
        for j in np.arange(len(V1)):
            for i in P1JS[j]:
                jvertex = V1[j]
                r1 += R[i, jvertex]
        print(f"{r1=}")
        print("\n")

        REM_VBs = list(set(V) - set(V1))
        print(f"{REM_VBs=}")
        VB = REM_VBs[0]
        # for VB in REM_VBs:
        print(f"{VB=}")

        DELTA_BJS = []

        for jvertexidx in np.arange(len(V1)):
            V1copy = V1.copy()
            jvertex = V1copy[jvertexidx]
            print(f"{jvertex=}")
            V1copy[jvertexidx] = VB

            print(f"{V1copy=}")
            SUBR = R[:, V1copy]
            print(f"{SUBR=}\n")
            
            DELTA_BJ = 0
            i = 0
            for ithrow in SUBR:
                print(f"{ithrow=}")
                ithrowmin = np.min(ithrow)
                print(f"{ithrowmin=}")
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
                elif rij <= rib <= ris:
                    SOME_DELTA_IBJ = rij - rib
                elif rij <= ris <= rib:
                    SOME_DELTA_IBJ = rij - ris
                print(f"{i=} {ris=} {rij=} {rib=} {SOME_DELTA_IBJ=}\n")
                DELTA_BJ += SOME_DELTA_IBJ
                i += 1
            print(f"{DELTA_BJ=}\n")
            DELTA_BJS.append(DELTA_BJ)
        DELTA_BK = np.min(DELTA_BJS)
        print(f"{DELTA_BJS=} {DELTA_BK=}")
        if DELTA_BK < 0:
            # we found the VK meeting required conditions
            V1[np.argmin(DELTA_BJS)] = VB

        print(f"{V1=}")

        print("== NEXT MASTER ITERATION ==")
        



if __name__ == "__main__":

    np.random.seed(10)

    D = np.array(
        [
            [0, 5, 1, 6],
            [5, 0, 2, 3],
            [1, 2, 0, 2],
            [6, 3, 2, 0],
        ],
    )  # 3 x 3 so 3 nodes
    H = np.array(
        [
            [10000, 0, 0, 0],
            [0, 4, 0, 0],
            [0, 0, 3, 0],
            [0, 0, 0, 1],
        ],
    )

    tietz_and_bart(D, H, p=2)

    pass
