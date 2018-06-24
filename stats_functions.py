# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 01:00:31 2018

@author: Mfundo Bright Shabalala
"""

from __future__ import division

def mean(numbers):
    sigma = 0
    n = 0
    for number in numbers:
        sigma += number
        n += 1
    return float(sigma)/max(n, 1)


def variance(numbers):
    square_mean_dev = 0
    n = 0
    for number in numbers:
        square_mean_dev += (number - mean(numbers))**2
        n += 1
    return float(square_mean_dev)/max(n, 1)


def pop_standard_dev(numbers):
    return variance(numbers)**0.5


def sample_standard_dev(numbers):
    n=0
    for number in numbers:
        n += 1
    if n<2:
        print("Error: Not enough sample data")
    else:
        return (n/max(n-1,1)*variance(numbers))**0.5
