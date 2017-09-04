---
title: Programming for everybody (Python) - 3.조건문, 예외처리
date: 2015-08-31 01:13:16
categories:
  - programming
  - python
tags:
  - python
  - programming
  - coursera
  - programming for everybody
---

## 3.1 Conditional Statements
conditional steps의 statement는 실행될 수도 아닐 수도!
```
if question :
  statement
```
If the question(condition) is false then python will skip all the statement.

### Comparison Operator
* < : Less than
* <=  : Less than or Equal
* ==  : Equal to
* \>= : Greater than or Equal
* \>  : Greater than
* !=  : Not equal

Comparison operator look at variables but do not change the variables.

### Indentation
**Python에서 Indentation은 매우 중요함!**  
Indentation은 scope를 가리킴 (for나 if후에 꼭 하나씩 넣어줘)  
Indent를 감소시켜서 이전 레벨로 되돌리는 건 for나 if block이 끝났다는 얘기  
comment와 빈 줄은 무시됨(indentation에 아무런 영향을 미치지 않음)  
**tab과 space를 섞어 쓰지마!** 잘못하면 indentation error를 받을 수 있다.

## 3.2 Examples of Confitional Statements
### Two way decisions
우리는 어떤 논리 표현식이 true/false이냐에 따라 다른 일을 하고 싶을 때가 있지! 그건 마치 우리가 여행을 떠났을 때 어떤 길을 택해야 하는 것 같은거지. 우리는 하나를 선택해야 하지 둘 다는 안 돼. if and else

### Multi-way
if elif else!
뭐, else를 굳이 쓰지 않아도 돼! 그리고 elif가 엄청 많을 수도 있지! logic에 따라서

## 3.3 Try and Except
조금 다른 Conditional 문을 보자!  
이건 사실 내가 만드는 로직이 아니야. 이건 뭔가 *프로그램을 망쳐버릴 수 있는 애를 처리* 하는거지. 우리는 이런 위험한 부분을 `try/except` 구문으로 감싸면 돼. 만약 `try`에 있는 코드가 성공적으로 동작하면 `except`는 건너뛰게 될거고, `try`에 있는 코드가 실패하면 `except`구문으로 건너뛰게 될거야.

예를 들어 나는 숫자를 입력받아야 하는데 사용자가 문자를 입력했어. 아마 프로그램은 거기서 그냥 Traceback을 출력해버리고 죽어버리겠지. 하지만 난 그러고싶지 않은걸!  
우리는 그런 위험한 구문이 어디인지 알아. 그리고 우리는 그 순간에 프로그램이 죽는 게 아니라 다른 대안이 실행되었으면 좋겠어! 일종의 보험 같은 것.

```
astr = 'Hello Bob'
try :
  istr = int(astr)
except :
  istr = -1
```

But, try블록 안에 쓸데 없는 코드까지는 넣지 마. 분명하게 해. 뭘 처리하고 싶은지.


---
### Homework
* [3.1](3.1.py)
* [3.3](3.3.py)
