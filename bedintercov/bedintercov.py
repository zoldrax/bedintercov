#!/usr/bin/env python3
import sys
# import os
import csv


# import getopt


def main():
    delta = 1
    ranges = dict()
    with sys.stdin as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        for row in csv_reader:
            if not (row[0] in ranges):
                ranges[row[0]] = []
            ranges[row[0]].append((int(row[1]), delta))
            ranges[row[0]].append((int(row[2]), -delta))
    for chrom in ranges:
        sortedrandes = sorted(ranges[chrom])
        isect = 0
        pcoord = sortedrandes[0][0]
        for i in sortedrandes:
            if i[0] != pcoord:
                print("\t".join([chrom, str(pcoord), str(i[0]), str(isect)]))
                pcoord = i[0]
            isect += i[1]


if __name__ == "__main__":
    main()
