---
title: Homebrew 이용해 python3 설치
categories:
  - environment
tags:
  - environment
  - homebrew
  - python
  - mac
date: 2015-06-15 01:00:57
---

Homebrew가 설치되어 있다면 python3 설치는 블로그에 쓰기도 멋쩍을 만큼 쉽다.

설치 과정에서 알게 된 것

1. mac에는 git과 마찬가지로 기본적으로 python이 설치되어 있다. 
2. 하지만, 2.x 버전으로 구버전이고, 애플에서 수정한(?) 버전의 python이다.
3. 따라서 Mac OS 업데이트나 여러 상황으로 python 패키지가 망가질 수 있다. (그냥 간단한 명령어 연습을 하기엔 큰 무리가 없을 듯)

이런 사실을 바탕으로 나는 python3버전을 따로 설치하기로 했다.

```shell
brew install python3 --with-brewed-openssl
```

그럼 알아서 openssl도 최신 버전으로 찾고, Dependencies도 찾아서 설치하고, 설치하고, 설치해준다.
`--with-brewed-openssl` 옵션을 붙이면 openssl을 최신으로 설치해주는 것 같다.
마지막으로 pip3까지. (pip는 python package를 관리해주는 아이!)
