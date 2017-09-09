---
title: Mac에 Java 설치
categories:
  - environment
tags:
  - environment
  - java
  - mac
date: 2015-06-20 00:00:57
---

### Java download
[Java download link](http://www.oracle.com/technetwork/java/javase/downloads/index.html)

일단 위 사이트에 가서 Java를 다운 받는다. 기본적으로 SE, EE, ME 버전이 있는데 각각 *Standard Edition, Enterprise Edition, Micro Edition*의 약자다. 그냥 공부를 하기 위한 거라면 SE를 받아 설치하면 된다.

### JAVA_HOME setting
다운 받아서 Next를 열심히 누르다보면 이미 설치는 끝나 있을테고 마무리로 환경변수 설정만 해주면 된다. 터미널에서 아래와 같은 명령어 입력.

```shell
vi ~/.bash_profile
```

vi 에디터가 열릴텐데, 아래 문장을 추가한다.

```shell
export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_45.jdk/Contents/Home
```

중간에 있는 **1.8.0_45는 설치된 버전 정보이므로 본인이 설치한 버전으로 수정하여 입력**해야 한다. 설치 과정에서 그냥 Next버튼만 눌렀다면, 저 기본 경로에서(/Library/Java/JavaVirtualMachines/)설치된 버전이 무엇인지 확인할 수 있다.  
수정한 후 내용은 다음과 같다. (PC설정별로 다를 수 있다.)

![](path_setting.png)

### Check installation
JAVA_HOME 설정 후, 터미널에서 아래 명령어를 이용해 본인이 설치한 java의 버전이 나오는지 확인한다.

```shell
$ java -version
java version "1.8.0_45"
Java(TM) SE Runtime Environment (build 1.8.0_45-b14)
Java HotSpot(TM) 64-Bit Server VM (build 25.45-b02, mixed mode)
```
