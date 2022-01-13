#!/usr/bin/env python
import pandas as pd
import numpy as np
import sympy as sp
import string
import math
from collections import OrderedDict
from importlib.machinery import SourceFileLoader

char_stats = SourceFileLoader('char_stats', './char_stats.py').load_module()

def extract_data(all_data):
    di = {}
    for let in string.ascii_uppercase:
        di[let] = char_stats.Char_stats()

    error_count = 0
    for idx, val in enumerate(all_data):
        if not isinstance(val, str) and math.isnan(val):
            #print(f"blank cell found at index {idx}")
            continue
        try:
            letter = val[0]
            di[letter].set_count(di[letter].get_count()+1)
            num = int(val[1:])
            if sp.isprime(num):
                di[letter].add_prime(num)
        except ValueError:
            print(f"value error found at index {idx}: {val}")
            error_count+=1
        except KeyError:
            print(f"key error found at index {idx}: {val}")
            error_count+=1
    return di, error_count

def rank_by_function(di, function):
    if function=="count":
        ordered = sorted(di.items(), key=lambda x: x[1].get_count(), reverse=True)
        vals = [item[1].get_count() for item in ordered]
    elif function=="prime_count":
        ordered = sorted(di.items(), key=lambda x: x[1].get_prime_count(), reverse=True)
        vals = [item[1].get_prime_count() for item in ordered]
    elif function=="avg_prime":
        ordered = sorted(di.items(), key=lambda x: x[1].get_avg_prime() if not math.isnan(x[1].get_avg_prime()) else 0, reverse=True)
        vals = [item[1].get_avg_prime() for item in ordered]
    elif function=="prime_percentage":
        ordered = sorted(di.items(), key=lambda x: x[1].get_prime_percentage(), reverse=True)
        vals = [round(item[1].get_prime_percentage(), 4) for item in ordered]
    keys = [item[0] for item in ordered]
    return dict(zip(keys,vals))

def print_counts(di):
    for key in di.keys():
        print(f"""key: {key}, count: {di[key].get_count()}, prime_count: {di[key].get_prime_count()}, avg prime: {di[key].get_avg_prime()}, prime percentage: {di[key].get_prime_percentage()}""")

def main():
    df = pd.read_csv("../data/SearchForPrimes.csv", header=None)
    all_data = df.to_numpy().flatten()
    di, error_count = extract_data(all_data)
    #print_counts(di)
    print("\nFor each character, how many times does it occur in the file?")
    print(rank_by_function(di, "count"))
    print("\nFor each character, how many times is it paired with a prime number?")
    print(rank_by_function(di, "prime_count"))
    print("\nWhat character has the highest average of prime numbers?")
    od = rank_by_function(di, "avg_prime")
    print(list(od.items())[0])
    print("\nRank the characters based on their prime number percentage")
    print(rank_by_function(di, "prime_percentage"))
    print(f"\nFinal error count: {error_count}")

if __name__ == "__main__":
    main()
