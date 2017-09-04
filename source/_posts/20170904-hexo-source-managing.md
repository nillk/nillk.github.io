---
title: Hexo source 파일도 git으로 관리하기
date: 2017-09-04 16:58:45
categories:
  - environment
  - hexo
tags:
  - environment
  - hexo
  - git
---

### Hexo blog source(.md) 파일도 git으로 관리할 수 있을까?
[Hexo](https://hexo.io/)로 블로그 시작한 지 4일 째. 이것저것 해보고 Tistory 글도 하나씩 옮겨오다 보니 작성하는 포스트 원글 자체도 git으로 관리하고 싶어졌다. Hexo를 써보면 알겠지만, `hexo deploy` 하면 *public* 디렉토리에 생성된 정적 파일들(html)만 github으로 올려진다. 그래서 문득 포스트 원본은 내 컴퓨터에서 날리면 답이 없는건가? 싶은 생각이 든 것.

### Source용으로 새 repository 사용?
그래서 어제 아무 생각 없이 github에 source 용으로 새 repository를 하나 만들고 blog 전체 디렉토리를 push했을 때까지는 좋았는데..... 그 이후에 다시 `hexo deploy`해보니 갑자기 blog repository에 *public* 디렉토리가 아니라 blog 전체 디렉토리가 올라가면서 그때까지 올렸던 commit log도 사라지고 당연히 *index.html* 이고 뭐고 없으니까 블로그는 죽었고 난리가 난 것. 그래서 잠깐 검색해보니 나처럼 세팅하고 사용하고 계신 분이 있던데 왜 나만 이런 문제가 T_T

#### Hexo directory 구조
hexo 디렉토리 구조는 아래와 같다.
```
blog
├── _config.yml // hexo 관련 설정 파일
├── package.json
├── scaffolds   // hexo에서 새 글을 작성할 때 사용되는 기본 template들
├── public      // hexo generate 명령어로 생성되는 정적 파일 폴더
├── source      // blog source 파일 폴더
|   ├── _drafts // 초안 모음
|   └── _posts  // generate될 post 모음
└── themes
```

### Blog repository에 source branch를 사용
그래서 일단 원상 복귀를 시켜놓고 오늘 다시 검색을 해보니 [Can deploy git ways upload source files at the same time ?](https://github.com/hexojs/hexo/issues/1899) 이런 질문글이 있었고, 여기서 해답을 찾았다. 답변 중에 다른 branch를 만들어서 upload 하라는 글이 있었다. 그래서 반신반의하며 다시 blog 디렉토리에서 source branch를 생성 후, remote로 push 했더니 되었다. 하나의 repository에서 source와 public 파일들 모두를 관리하게 되었으니 더 잘 된 것 같다.

```
git init
git checkout -b source
git add .
git commit -m "Hexo blog sources initial commit"
git remote add origin https://github.com/[id]/[id].github.io
git push -u origin source
```

이상해서 hexo 랑 hexo-deployer-git 프로젝트 소스도 좀 살펴봤는데 뭐가 문제인지는 아직 모르겠다.





