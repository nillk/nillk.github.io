---
title: Scalatest - fixtures에 System-Rules 사용하기
categories:
  - programming
  - scala
tags:
  - programming
  - scala
  - scalatest
  - test
  - system rules
date: 2017-07-18 00:51:22
---

## JUnit Rules - System-Rules

요즘 Scala test code를 열심히 작성하는 중이다. 당연히 [ScalaTest](http://www.scalatest.org) 사이트를 뻔질나게 드나드는 중인데, 본래 Scala와도 그다지 친하지 않았는데 ScalaTest는 당연히 낯선 친구라서 어려워 하고 있다. 오늘 회사에서 누군가가 남겨놓고 떠난 코드에 얄팍하게나마 테스트 코드를 작성하던 중에 코드 내에 `System.getenv`를 호출하는 부분이 있다는 걸 알았고, 테스트만을 위해 로컬에 환경변수를 설정하기엔 몹시 애매한 상황이어서 아니 이걸 어떻게 하지??? 하다가 [JUnit rules](https://github.com/junit-team/junit4/wiki/Rule)형태의 [System-Rules](http://stefanbirkner.github.io/system-rules/)라는 library가 있다는 걸 알게 되었다. 들어가보면 알겠지만 `java.lang.System`을 사용하는 테스트 코드를 지원하는 JUnit rules라고 보면 될 것 같다. 여러가지 System관련 rule이 있는데 환경변수를 이용할 수 있는 rule 사용법은 다음과 같다.

```java
public void EnvironmentVariablesTest {
  @Rules
  public final EnvironmentVariables environmentVariables = new EnvironmentVariables();

  @Test
  public void setEnvironmentVariable() {
    environmentVariables.set("name", "value");
    assertEquals("value", System.getenv("name"));
  }
}
```

그래서 이걸 사용하려고 했는데... 그냥 Java였거나 [JUnitSuite](http://www.scalatest.org/getting_started_with_junit_4_in_scala) 를 쓰고 있었으면 간단하게 `@Rule` annotation과 함께 행복한 테스트 코드 작성을 시작할 수 있었는데 하필 나는 FunSuite를 쓰고 있었고, 이걸 바꾸기는 싫었기 때문에 Scala 2주차 초짜는 이걸 과연 ScalaTest에 우겨넣을 수 있는 것인가 멘붕에 빠졌다. 이럴땐 역시 공식 홈페이지지. 이것 저것 뒤지다 *[Sharing fixtures](http://scalatest.org/user_guide/sharing_fixtures)* 라고 소개되어 있는 방법으로 넣으면 되겠다 싶었고, 운 좋게 딱 저 방법으로 누가 올려준 [샘플 코드](http://stackoverflow.com/a/32160901)도 찾았다!

## ScalaTest - fixtures
fixture는 간단하게 말해 test code에서 **test를 위해 필요한 *file* 이나 *socket, database, connection* 등의 객체 덩어리 혹은 설정들** 이라고 보면 될 것 같다. 여러 테스트 코드에서 같은 fixture를 사용한다고 하더라도 같은 코드를 굳이 또 쓸 필요는 없겠지? 그래서 ScalaTest에선 크게 3가지 정도의 코드 중복을 막기 위한 방법을 추천한다.
* Refactor using Scala
> test들이 서로 다른 fixture들을 필요로 할 때
* Override `withFixture`
> 대부분 혹은 모든 test들이 같은 fixture를 필요로 할 때
* Mix in a *before-and-after* trait
> fixture코드가 실패하면 test가 fail되는 게 아니라 suite 자체가 중단되어야 할 때

그리고 각각에 대한 세부 적용 방법이 또 있다.
### Refactor using Scala
#### [get-fixture methods](http://www.scalatest.org/user_guide/sharing_fixtures#getFixtureMethods)
여러 테스트에 동일한 불변의 fixture object를 생성해야 하고, 사용 후에 정리하거나 할 필요가 없을 때 하나 혹은 그 이상의 get-fixture methods를 쓰는 게 가장 간단한 접근 방법
#### [fixture-context objects](http://www.scalatest.org/user_guide/sharing_fixtures#fixtureContextObjects)
fixture method와 field를 trait(혹은 class)에 둠으로써, 각각의 테스트에서 새로 생성된 fixture를 사용할 수 있고, 여러 개를 섞어서 사용할 수도 있다. get-fixture methods와 다르게 여러 테스트에서 서로 다른 fixture object가 필요할 때 사용하며, 같은 점은 사용 후에 정리할 필요가 없다는 점
#### [loan-fixture methods](http://www.scalatest.org/user_guide/sharing_fixtures#loanFixtureMethods)
별개의 테스트가 서로 다른 fixture들을 필요로 하고, *테스트가 끝난 후에는 정리가 필요할 때* 사용할 수 있다. 테스트 코드가 외부의 부작용 다시 말해, 파일을 생성하거나 데이터 베이스를 생성하거나 하는 짓을 할 때, 사용하면 좋다.

### Override 'withFixture'
#### [withFixture(NoArgTest)](http://www.scalatest.org/user_guide/sharing_fixtures#withFixtureNoArgTest)
거의 대부분 혹은 모든 테스트 코드가 같은 fixture를 필요로 할 때 추천한다. 테스트 코드의 시작 혹은 끝에서 뭔가 다른 작업(원문에는 side-effect라고 작성되어 있었지만 다른 작업이라는 말이 적절한 것 같음)을 수행해야 하고, fixture object를 테스트 코드에 넘길 필요가 없을 때 이 방법을 사용할 수 있다.  ScalaTest `Suite` trait의 `runTest` 구현은 no-arg test function을 `withFixture(NoArgTest)`에 넘긴다. 그리고 이 메소드 안에서는 간단하게 테스트 코드를 실행한다. 그러므로, 이 메소드를 *Override* 하면 test코드 앞에서 setup을 수행할 수 있고, 테스트 코드가 끝나면 clean할 수 있다.

#### [withFixture(OneArgTest)](http://www.scalatest.org/user_guide/sharing_fixtures#withFixtureOneArgTest)
withFixture(NoArgTest)와 비슷하지만, test 에서 fixture 를 사용해야 할 때 사용하면 될 것 같다.

### Mix in a *before-and-after* trait
#### [BeforeAndAfter](http://www.scalatest.org/user_guide/sharing_fixtures#beforeAndAfter)
이 전까지 나왔던 기법은 다 각각의 테스트 *도중에* 필요한 작업을 수행한다. 그리고 그런 작업을 수행하면서 에러가 나면 *테스트 실패* 로 기록된다. 하지만 이런 setup과 cleanup작업 도중에 에러가 발생하면 전체 suite를 취소하고 더 이상 테스트 코드를 수행하고 싶지 않을 때 이 방법을 사용한다. 각 테스트 시작/끝 말고 테스트 전과 후에 같은 작업을 수행하고 싶을 때.

#### [BeforAndAfterEach](http://www.scalatest.org/user_guide/sharing_fixtures#composingFixtures)
테스트의 시작과 끝보다는 테스트 전/후에 같은 작업을 하는 trait을 쌓고 싶을 때 사용한다.

## 결론
대략의 내용은 이렇고 나 같은 경우에는 테스트용 환경 변수가 필요한 상황이었기 때문에, `withFixture(NoArgTest)` 방법을 사용했다. 상세 내용은 홈페이지 링크를 보면 나오지만, `withFixture(NoArgTest)` 메소드는 Scalatest Suite에 정의되어있는 lifecyle 중 하나이며, `withFixture` 메소드는 *테스트 함수를 실행해야만 한다.* 따라서 이 메소드를 Override하고 테스트 함수 전/후에 원하는 동작을 구현하면 된다.

그래서 나는 테스트용 trait을 하나 만들어 그 안에 `withFixture` 메소드를 Override하고, 테스트 코드 실행 전에 환경 변수를 세팅해주는 로직을 추가했다. 그리고 이 환경변수가 필요한 테스트 클래스마다 아까 만든 trait을 사용하도록 하였다.


