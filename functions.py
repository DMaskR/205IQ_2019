#! /usr/bin/env python

import math

def f_de_x(mu, sigma, x):

    res = (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-math.pow((x - mu), 2)/(2 * math.pow((sigma), 2)))

    return (res)

def morceau_de_fonction(mu, sigma, x):

    res = math.exp(-math.pow((x - mu), 2)/(2 * math.pow((sigma), 2)))

    return (res)

def iteration_trapeze(a, b, mu, sigma):

    res = (b - a) * ((morceau_de_fonction(mu, sigma, a) + morceau_de_fonction(mu, sigma, b)) / 2)

    return (res)

def p(mu, sigma, maxval):

    res = 0

    for i in range(0, maxval):
        res += iteration_trapeze(i, (i + 1), mu, sigma)
    
    res = (1 / (sigma * math.sqrt(2 * math.pi))) * res

    return (res)

def yiss(mu, sigma, a, b):

    res = 0

    for i in range(a, b):
        res += iteration_trapeze(i, (i + 1), mu, sigma)
    
    res = (1 / (sigma * math.sqrt(2 * math.pi))) * res

    return (res)