"""

Imports

"""
import torch
from time import time
from argparse import ArgumentParser

"""

Constants

"""
ITERATIONS = 10000

"""

Functions

"""
# Returns calculation time
def get_time(device: str, dimension: int) -> float:
    x = torch.rand(dimension, dimension, device=torch.device(device))
    start = time()

    for _ in range(ITERATIONS):
        x += x

    end = time()
    return end - start
"""

Main Function

"""
# Read arguments
parser = ArgumentParser()
parser.add_argument("dimension", type=int)

# Compute time
args = parser.parse_args()
cpu_time = get_time("cpu", args.dimension)
gpu_time = get_time("cuda", args.dimension)

# Print time
print(f"CPU Time: {cpu_time}")
print("")
print(f"GPU Time: {gpu_time}")