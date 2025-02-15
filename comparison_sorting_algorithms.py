# -*- coding: utf-8 -*-
"""Comparison_Sorting_algorithms.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1T6dnnwMEeP8l1tbxLwJtb68Ji_IYtCV3
"""

#Merge Sort
def mergeSort(arr):
  if (len(arr) > 1):
    mid_array = len(arr)//2
    left_array = arr[:mid_array]
    right_array = arr[mid_array:]
    mergeSort(left_array)
    mergeSort(right_array)
    i=j=k=0
    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            arr[k] = left_array[i]
            i = i+1
        else:
            arr[k] = right_array[j]
            j = j+1
        k = k+1
    while i < len(left_array):
        arr[k] = left_array[i]
        i = i+1
        k = k+1
    while j < len(right_array):
        arr[k] = right_array[j]
        j= j+1
        k= k+1

#Insertion Sort
def insertionSort(arr):
  for i in range(1, len(arr)):
    k = arr[i]
    j = i - 1
    while (j >= 0 and k > arr[j]):
      arr[j+1] = arr[j]
      j = j-1
    arr[j+1] = k

#Heap Sort
def heapSort(arr):
    h=[]
    for item in arr:
        heapq.heappush(h, item)
    for i in range(len(arr)):
        arr[i] = heapq.heappop(h)

#Heapify
#def heapify(array, n, i):
#  largest = i
#  left_arr = 2 * i + 1
#  right_arr = 2 * i + 2
#  if ((left_arr < n) and (array[i] < array[left_arr])):
#    largest = left_arr
#  if ((right_arr < n) and (array[largest] < array[right_arr])):
#    largest = right_arr
#  if (largest != i):
#    array[i],array[largest] = array[largest],array[i]
#    heapify(array, n, largest)

#Quick Sort
def quickSort(arr, low, high):
    if low < high:
        p = partition(arr,low,high)
        quickSort(arr, low, p-1)
        quickSort(arr, p+1, high)

#Partition
def partition(arr,low,high):
    piv = arr[low]
    i = low - 1
    for j in range(low,high):
        if arr[j]<piv:
            i= i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

#Modified Quick Sort with Median of three and Insertion sort for small subarrays
def modifiedQuickSort(arr,low,high, threshold =10):
    if high - low +1  <= threshold:
        insertion_sort_subarray(arr,low,high)
    elif low < high:
        p = medianThree(arr,low,high)
        modifiedQuickSort(arr,low,p-1,threshold)
        modifiedQuickSort(arr,p+1,high,threshold)

#Insertion Sort Subarrar
def insertion_sort_subarray(arr, low, high):
    for i in range(low + 1, high + 1):
        k = arr[i]
        j = i - 1
        while j >= low and arr[j] > k:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = k

def medianThree(arr,low,high):
    mid = (low + high) // 2
    if arr[low] > arr[mid]:
      arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    # arr[mid] is now the median; swap it with arr[high] to use it as pivot.
    arr[mid], arr[high] = arr[high], arr[mid]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

import matplotlib.pyplot as plt
import time
import random
import numpy as np
import sys
import heapq

sys.setrecursionlimit(10**6)

def run_experiments_sizes():
    # Define input sizes (n values)
    input_sizes = [1000, 2000, 3000, 4000, 5000, 10000, 20000, 40000, 50000, 60000, 80000, 90000, 100000]
    num_runs = 3  # Number of repetitions for averaging

    # Define the algorithms in a dictionary
    algorithms = {
        "Insertion Sort": insertionSort,
        "Merge Sort": mergeSort,
        "Heapsort": heapSort,
        "In-place Quicksort": lambda arr: quickSort(arr, 0, len(arr)-1),
        "Modified Quicksort": lambda arr: modifiedQuickSort(arr, 0, len(arr)-1, threshold=10)
    }

    # Scenarios: "Sorted", "Reversed"
    scenarios = ["Sorted", "Reversed"]
    # Create a nested dictionary to hold timing results per scenario
    results = { scenario: { alg: [] for alg in algorithms } for scenario in scenarios }

    for n in input_sizes:
        # Generate arrays for each scenario
        sorted_array = list(range(n))
        reversed_array = list(range(n, 0, -1))
        arrays = {
            "Sorted": sorted_array,
            "Reversed": reversed_array
        }

        print(f"Input Size: {n}")
        for scenario in scenarios:
            print(f"  Scenario: {scenario}")
            for name, sort_func in algorithms.items():
                total_time = 0.0
                for _ in range(num_runs):
                    arr_copy = arrays[scenario].copy()
                    start_time = time.perf_counter()
                    sort_func(arr_copy)
                    total_time += time.perf_counter() - start_time
                avg_time = total_time / num_runs
                results[scenario][name].append(avg_time)
                print(f"    {name}: {avg_time:.6f} sec")

    # Plotting results in two subplots (one for each scenario).
    plt.figure(figsize=(14, 12))
    for idx, scenario in enumerate(scenarios, 1):
        plt.subplot(2, 1, idx)
        for name in algorithms:
            plt.plot(input_sizes, results[scenario][name], marker='o', label=name)
        plt.xlabel("Input Size (n)")
        plt.ylabel("Avg Execution Time (sec)")
        plt.title(f"Performance ({scenario} Array)")
        plt.legend()
        plt.grid(True)
    plt.tight_layout()
    plt.show()

run_experiments_sizes()











