import numpy as np

def multiply_list(list,multi):
    result = []
    for term in list:
        result.append(term*multi)
    return result
def euclid_formula(m,n):
    return [abs(2*m*n), abs(m**2-n**2) ,abs(m**2+n**2)]

def find_primitives(lim):
    triples = []
    for m in range(0, lim):
        for n in range(0, lim):
            triple = euclid_formula(m, n)

            if (0 not in triple):
                p = sum(triple)

                if (triple not in triples):
                    if(p <= 1000):
                        triples.append(triple)
    return triples
def get_non_primitives(triple):
    multi = 1
    p = 0
    trips = []

    while p <=1000:

        result = multiply_list(triple,multi)
        p = sum(result)

        multi +=1

        trips.append(result)

    return trips
def all_triples(lim):
    primitives = find_primitives(lim)

    total = []

    for prim in primitives:
        total.append(prim)

    for triple in primitives:
        non_prim = get_non_primitives(triple)

        for non in non_prim:
            if(sum(non)<=1000):
                total.append(non)

    return (total)

def sum_of_triples(triples):
    perimeters = []
    for trip in triples:
        p = sum(trip)
        if(p <= 1000):
            perimeters.append(p)
    return perimeters


perimeters = sum_of_triples(all_triples(200))
perimeters.sort()

from itertools import groupby
groups = ([list(j) for i, j in groupby(perimeters)])
print(sorted(groups,key=len))

max_len = 0
max_group = []
for group in groups:
    if(len(group) > max_len):
        max_len = len(group)
        max_group = group

print(max_group[0])