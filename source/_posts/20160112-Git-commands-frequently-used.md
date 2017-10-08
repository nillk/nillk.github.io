---
title: 자주 사용하게 되는 Git 명령어
categories:
  - environment
  - development tools
tags:
  - environment
  - development tools
  - git
date: 2016-01-12 01:22:02
---

그냥 내가 자주 사용하는 git 명령어를 좀 정리해보려 한다.

#### status

```
git status
```
현재 working directory 상황을 보여준다. index에 올라가 있는 파일 목록. index에 올라가있진 않지만 수정된 파일 목록. 그리고 추가/삭제 된 파일 목록 등.

#### diff

```
git diff
```

기본적으로는 현재 working directory의 수정된 상황(아직 index에 add하지 않은 수정 사항)을 보여준다. 빨간색은 삭제된 것이고, 초록색은 추가된 것. 새로 생성한 파일은 당연스럽게도 보여주지 않는다. 파일 전체가 수정된 사항이니까.

##### options
* --cached
git diff --cached 명령어를 사용하면 working directory와 index와의 차이가 아니라 index에 올라가있는 파일과 마지막 commit과의 차이를 보여준다.
* --word-diff
원래 뒤에 모드를 더 써야 하는데 그냥 이렇게만 쓰면 plain으로 들어간다. 변경 사항을 전체 라인으로 보여주는 게 아니라 단어 별로 [-removed-] 나 {+added+} 형태로 조금 상세하게 보여준다.
* --color-words
바로 위 옵션과 비슷하게 단어별로 수정 사항을 색으로 표현해서 보여준다. 차이는 [-removed-]나 {+added+}같은 표식이 없다. --word-diff=color 에 무슨 --word-diff-regex=를 더한거라고는 하는데...

#### add
```
git add
```
수정된 파일을 index에 추가할 때 쓴다. 보통 뒤에 `.` 붙여서 쓰는데 그러면 현재 수정된 파일을 몽땅 index로 추가한다.

##### options
* -- FileName
FileName 이라는 특정 파일을 추가
* -- 추가하고 싶은 파일/폴더명을 입력하는데 너무 길다! 혹은 이름이 비슷한 여러 파일을 넣고 싶다! \* 를 wildcard로 인식하기 때문에 \* 쓰면 그냥 문자로 인식해서 맞는거 다 넣어줌. checkout 시에도 마찬가지로 * 동작.

#### commit
```
git commit
```
index에 올라가 있는 파일들을 commit 한다.

##### options
* -m "commit message"
commit message까지 한꺼번에 입력 가능
* --amend
**아직 push 안 했을 때** 파일을 더 추가해야 한다거나 commit message를 수정해야 한다거나 할 때 이용한다. (파일을 추가하고자 한다면 미리 add하여 index에 올려놓고 이 명령어 사용)

#### log
```
git log
```
log를 쭉 보여줌

##### options
* -- fileName
해당 파일의 log를 쭉 보여준다.
* | grep "nillk"
그냥 파이프라인. commit message 안에 nillk를 포함하는 commit을 찾아서 보여준다.

log 를 트리 형태로 보여주는 alias (~/.gitconfig에 추가)
```
[alias]
    lg = log --graph --name-status --abbrev-commit --decorate --format=format:'%C(bold red)%h%C(reset) - %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset)%C(bold yellow)%d%C(reset)%n''%C(bold white)%s%C(reset) %C(dim white)- %an%C(reset)%n' --all
```

#### show
```
git show <hash>
```
해당 hash commit 내용을 보여준다.

##### options
* --color-words
여기도 diff때와 마찬가지로 color-words옵션이 동작한다.



...
막상 정리하려니 잘 생각이 안 나서 여기까지만
