#! /usr/bin/env python

import math

def function(mean, deviation, x):

    res = (1 / (deviation * math.sqrt(2 * math.pi))) * math.exp(-math.pow((x - mean), 2)/math.pow((2 * deviation), 2))

    return (res)