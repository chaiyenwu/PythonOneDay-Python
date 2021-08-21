#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: justinwu
"""
x=2**3+5*2-5/5+5%2
y=1<<2
print(x)
print(y)
b=3 #(11)
c=3 #(11)
d=b&c #(11&11)
print(d) #(11)
e=b^c #(11^11)
print(e) #(0)
f=b|c #(11|11)
print(f) #(11)
g=1<5 #True
print(g)
h=1>5 #False
print(h)

I=g and h
print(I)

P = g or h
print(P)