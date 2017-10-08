---
title: Ubuntu에서 ssl certificate verify failed 에러시 설정 (인증서 등록)
categories:
  - environment
tags:
  - environment
date: 2016-07-15 01:05:02
---

```shell
pip3 install django
    Collecting django
Could not find a version that satisfies the requirement django (from versions: )
No matching distribution found for django
```

회사에서 Ubuntu 16.04에 pip를 이용해 Django를 설치하려고 했는데 자꾸 위와 같은 에러 메시지가 나오고 설치가 되지 않았다. 열심히 구글링 했더니 저 메시지는 *인터넷에 접근을 못 하는 상태*라는 글을 발견해서 또 열심히 이것저것 다른 명령어를 쳐보면서 구글링. 인터넷도 당연히 되고, 프록시도 다 세팅되어 있는데 대체 왜일까... 하다가. 조금 다른 명령어를 쳤더니 *Ssl certificate_verify_failed* 라는 에러 메시지를 볼 수 있었다. 그리고 결국 해결책을 찾아냈다. 일단 우리 회사에서 인터넷에 접속하려면

1. Proxy setting
2. 회사에서 발급한 인증서를 루트 인증기관에 등록

해야 하는데 보통 윈도우에서 개발할 때는 1. Proxy setting만 좀 신경써주면 됐었다. 일단 패키지 관리자를 안 쓰니까... 회사에서 처음으로 Ubuntu에 pip로 뭘 설치하려고 하니까 이런 문제를 발견한 것 같다. 2번이 문제의 원인이었다.

그래서 발견한 해결책

1. /usr/share/ca-certificates 위치에 인증서를 위한 폴더를 하나 만듦
```
sudo mkdir /usr/share/ca-certificates/extra
```
2. 회사에서 발급한 인증서를 1에서 만든 폴더로 옮김
```
sudo cp foo.crt /usr/share/ca-certificates/extra/foo.crt
```
3. 우분투가 해당 인증서 파일의 경로를(/usr/share/ca-certificates를 기준으로 상대경로) /etc/ca-certificates.conf에 추가하게 만듦
```
sudo dpkg-reconfigure ca-certificates
```
그러니 되었다 T_T!!!!! 할렐루야

해결 방법 원글 링크
http://askubuntu.com/questions/73287/how-do-i-install-a-root-certificate
