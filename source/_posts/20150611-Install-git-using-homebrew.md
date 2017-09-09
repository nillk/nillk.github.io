---
title: Homebrew 이용해 git 설치
date: 2015-06-11 22:38:01
categories:
  - environment
tags:
  - environment
  - homebrew
  - git
  - mac
---

새로 맥북을 사서 git을 설치하기 전에 확인을 위해 터미널에서

```shell
git --version
```

을 입력해봤더니 놀랍게도 이미 git이 설치되어 있었다. 오오 역시 MAC이라고 하려던 찰나

```shell
git version 2.3.2 (Apple Git-55)
```

뒤에 Apple Git-55라는 매우 수상한 문자가 붙어있어 검색을 해보았더니, *Mac은 Apple 전용인 오래된 버전의 Git을 기본적으로 가지고 있다*고 한다. 오래된 버전이라는 것은 둘째치고 Apple전용이라는 말에 찝찝하여 Git을 새로 설치했다.

일단 Homebrew 명령어를 이용해 Git을 설치한다.

```shell
brew install git
```

![](brew-install-git.png)

설치된 Git 정보 확인

```shell
brew info git
```

그럼 아래 사진과 같이 git에 대한 정보가 쭉 나열되는데, 이 중 Dependencies에서 Optional의 pcre를 보면 (✗)표시가 되어 있다. 그렇다면 pcre도 설치를 해준다. (설치된 상태로 나오면 당연히! 따로 설치할 필요 없음)

![](brew-info-git.png)

```shell
brew install pcre
```

![](brew-install-pcre.png)

그리고 다시 `git --version`을 입력해보았더니 새로 git을 설치했는데도 전과 동일한 버전 정보가 나왔다. 이 경우 아래와 같은 명령어를 입력해준다. 직접 .bash_profile을 수정해도 된다.

```shell
echo "export PATH=/usr/local/bin:$PATH" >> ~/.bash_profile
```

위 명령어를 입력하고 .bash_profile 파일을 확인해보면 `export PATH=/usr/local/bin:$PATH` 문구가 추가되어 있는 것을 확인할 수 있다.

![](export-path.png)

그리고 **터미널을 새로 띄워서** `git --version`을 입력해보면 새로 설치된 git을 인식한 걸 확인할 수 있다.

![](git-version.png)
