#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: justinwu
"""

from collections import deque
queue = deque(['阿呆','Eric','John','Michael','小寶','小文'])
print(queue)
queue.append('Terry')
print(queue)
queue.append('Graham')
print(queue)
print(queue.popleft())
print(queue)
print(queue.popleft())
print(queue)

print(queue.popleft())
print(queue)

