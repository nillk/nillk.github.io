---
title: Java generics <Object> 와 <? extends Object>의 차이
categories:
  - programming
  - java
tags:
  - java
  - generics
---

분명히 알았는데, 다시 되짚어 보려니 뭔가 모호해서 generics를 정리해보기로 했다. 글로 하나씩 정리해보는 거랑 그냥 알고 있다고 생각하는 거랑 생각보다 큰 차이라는 걸 요즘들어 느낀다. 오늘은  `<Object>` 와 `<? extends Object>` 의 명확한 차이.

이 둘은 얼핏 보기엔 같아 보이지만 조금 다르다. 저 키워드를 기반으로 찾으면 또 나오는 비슷한 질문이 [`<?>` 와 `<? extends Object>`의 차이](https://stackoverflow.com/questions/8055389/whats-the-difference-between-and-extends-object-in-java-generics)인데 이 두 경우는 같으며 `extends Object`는 몇 케이스를 제외하고는 `extends Object`가 redundant하다고 하다고 한다.

### `List<Object>` 와 `List<? extends Object>` 는?
`List<Object>`는 이 list가 가지고 있는 객체들이 Object라는 것을 얘기하는 거지만, `List<? extends Object>`는 이 list가 가지고 있는 객체들이 Object의 subclass임을 말한다. 다시 말해, `List<? extends Object>`는 `List<String>`, `List<Number>`, `List<SomeClass>` 등의 list를 받을 수 있다는 것. 그래서 `List<Number>`는 `List<? extends Object>`의 서브타입일 수 있지만, `List<Object>`의 서브타입일 수는 없다. `Number`는 `Object`의 subclass지만 `List<Number>`는 `List<Object>`의 subclass가 아니지!

그래서 
```java
public void listTest(List<Object> list) {
  list.add("Hello, generics!");
}
```
는 되지만,
```java
public void listTest(List<? extends Object> list) {
  list.add("Hello, generics!");
}
```
이건 컴파일 에러가 난다. 잘 생각해보면 답이 나온다.
`List<? extends Object>` 라는 건 Object의 서브 클래스를 가지고 있는 리스트이다. 컴파일러는 이 리스트가 가지고 있는 게 Object일지, Number일지, String인지 그 외 다른 Class일지 모른다. 따라서 저기서 그냥 String을 넣어버리면 에러가 난다! 넘어 온 list가 Number를 가지고 있는 List이면 어떡해!