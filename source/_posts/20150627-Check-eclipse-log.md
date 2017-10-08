---
title: Eclipse plugin 개발시 Cmd에서 log 확인
categories:
  - environment
  - eclipse
tags:
  - environment
  - eclipse
  - tip
date: 2015-06-27 21:47:27
---

Eclipse Plugin을 개발하다보면, 개발환경에서 띄운 Eclipse가 아니라 사용자의 환경에서 Plugin이 설치된 상태의 이클립스를 띄워봐야 하는 경우가 있다 ㅜ ㅜ
개발 환경에서 띄우면 개발용 Eclipse console 창에서 target platform eclipse 의 log를 확인할 수 있는데, 그냥 사용자 Eclipse를 띄울 때는 log를 어떻게 확인할까?

1. cmd 창 띄운다.
2. Log 를 확인해야 하는 eclipse 폴더로 이동한다.
3. 아래 명령어를 친다.
```shell
eclipsec -consoleLog
```

이러면 개발할 때와 마찬가지로 eclipse에서 출력하는 log를 cmd 창에서 확인할 수 있다

