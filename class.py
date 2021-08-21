#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: justinwu
"""
class MyClass:
    #範例屬性參考
    i=12345

    
print(MyClass.i)


class Complex:
    #實體建構
    def __init__(self,realpart,imagpart):
        self.r = realpart
        self.i = imagpart
        
x=Complex(3.0,-4.5)
print(x.r,x.i)


