---
title: 재미있는 Python 기본 모듈
categories:
  - programming
  - python
tags:
  - programming
  - python
date: 2017-01-11 10:51:00
---

### this
내가 좋아하는 The Zen of Python 이 나옴 \*_*
```
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

### dis
Disassembler for Python bytecode

구문의 stack 이 쭉 나온다.
```python
>>> import dis
>>> dis.dis(lambda x, y, z: (x + y) * z)
1           0 LOAD_FAST                0 (x)
            3 LOAD_FAST                1 (y)
            6 BINARY_ADD          
            7 LOAD_FAST                2 (z)
           10 BINARY_MULTIPLY     
           11 RETURN_VALUE       
```

### ast
Abstract Syntax Trees

식의 구문트리를 보여줌!!!
```python
>>> import ast
>>> ast.dump(ast.parse("(1 + 2) * 3"))
'Module(body=[Expr(value=BinOp(left=BinOp(left=Num(n=1), op=Add(), right=Num(n=2)), op=Mult(), right=Num(n=3)))])'
```
