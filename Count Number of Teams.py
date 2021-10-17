"""
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

    Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
    
    A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) 
        where (0 <= i < j < k < n).

Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).
"""
n = list(map(int, input().split(',')))
c = 0
for pi_i in range(1, len(n)-1):
    l_low, l_gr, r_low, r_gr = 0, 0, 0, 0
    pivot = n[pi_i]

    for v in n[: pi_i]:
        if v < pivot:
            l_low += 1
        else:
            l_gr += 1

    for v in n[pi_i+1:]:
        if v < pivot:
            r_low += 1
        else:
            r_gr += 1
    c += (l_low * r_gr) + (l_gr * r_low)

print(c)
