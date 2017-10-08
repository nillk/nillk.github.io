---
title: Upper bounded wildcards
categories:
  - programming
  - java
tags:
  - programming
  - java
  - translation
date: 2016-12-28 17:08:00
---

[Upper Bounded Wildcards](http://docs.oracle.com/javase/tutorial/java/generics/upperBounded.html)

변수에 대한 제한을 좀 느슨하게 하기 위해 upper bounded wildcard를 사용할 수 있다. 예를 들어, `List<Integer>`, `List<Double>`, 그리고 `List<Number>`를 다루는 메소드를 작성하고 싶다고 해보자; 이건 upper bounded wildcard를 이용해 작성할 수 있다.

upper-bounded wildcard를 선언하기 위해서는 wildcard character ('*?*')를 사용하고, 그 다음 *extends* keyword를, 마지막으로 *upper bound*가 뒤따른다. 주의할 것은 이 문맥에서 *extends*는 일반적인 느낌의 **“extends”**(class에서 사용되는)와 **“implements”**(interface에서 사용되는) 둘 다 의미하는 것으로 사용한다.

`Number`, `Number`의 subtype들 즉, `Integer`, `Double`, 그리고 `Float`의 list들에 대해 동작하는 메소드를 작성하기 위해서는 `List<? extends Number>`를 사용해야 한다. `List<Number>`는 오직 `Number` type만으로 된 list인 반면에 `List<? extends Number>`는 `Number` type이나 그 subclass들의 list이기 때문에 `List<Number>`가 `List<? extends Number>`보다 더 제한적이다.

아래의 process 메소드를 보자:
```java
public static void process(List<? extends Foo> list) { /* ... */ }
```
The upper bounded wildcard, `<? extends Foo>`는 `Foo`가 어떤 타입이든, `Foo`와 `Foo`의 subtype에 대응한다. process 메소드는 list의 원소들을 `Foo` type으로 간주하며 접근할 수 있다:
```java
public static void process(List<? extends Foo> list) {
  for (Foo elem : list) {
    // ...
  }
}
```
`foreach` 구문 안에서, `elem` 변수는 list안의 각 원소들을 순회한다. `elem`은 `Foo` class에 정의한 어떤 메소드라도 사용할 수 있다.

`sumOfList` 메소드는 list에 있는 숫자들의 합을 돌려준다:
```java
public static double sumOfList(List<? extends Number> list) {
  double s = 0.0;
  for (Number n : list) {
    s += n.doubleValue();
  }
  return s;
}
```
아래 코드는 `Integer` object들로 이루어진 list를 써서 `sum = 6.0`을 출력한다:
```java
List<Integer> li = Arrays.asList(1, 2, 3);
System.out.println("sum = " + sumOfList(li));
```
`Double`값들로 이루어진 list 역시 같은 `sumOfList` 메소드를 사용할 수 있다. 아래 코드는 `sum = 7.0`을 출력한다:
```java
List<Double> ld = Arrays.asList(1.2, 2.3, 3.5);
System.out.println("sum = " + sumOfList(ld));
```
