# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 01:00:31 2018

@author: Mfundo Bright Shabalala
"""

from __future__ import division

def mean(numbers):
    """
    Returns the mean value of a list of values.
    The argument must be a list.
    """
    sigma = 0
    n = 0
    for number in numbers:
        sigma += number
        n += 1
    return float(sigma)/max(n, 1)


def variance(numbers):
    """
    Returns the variance of the list of values.
    The argument must be a list.
    """
    square_mean_dev = 0
    n = 0
    for number in numbers:
        square_mean_dev += (number - mean(numbers))**2
        n += 1
    return float(square_mean_dev)/max(n, 1)


def pop_standard_dev(numbers):
    """
    Returns the population standard deviation of the list of values.
    The argument must be a list.
    """
    return variance(numbers)**0.5


def sample_standard_dev(numbers):
    """
    Returns the sample standard deviation of the list of values.
    The argument must be a list.
    """
    n=0
    for number in numbers:
        n += 1
    if n<2:
        print("Error: Not enough sample data")
    else:
        return (float(n)/(n-1)*float(variance(numbers)))**0.5
