#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: justinwu
"""

class MyClass2:
    #範例屬性參考
    i=12345
    def f(self):
        return 'hello world'
    
x=MyClass2()
print(x.i)
print(x.f())
x2=MyClass2()
print(x2.i)
print(x2.f())
