---
title: Frontend Framework
categories:
  - environment
  - development tools
tags:
  - environment
  - development tools
  - frontend
  - framework
date: 2016-01-12 19:34:02
---

뜬금없이 파견된 프로젝트에서 웹 개발 그것도 프론트엔드를 하게 되었다. 입사 이래로 처음이야... 그래서 내게는 생소한 프레임워크가 많아 조금 헛갈려서 정리를 했다. 아직도 조금 헛갈리기는 하지만 익숙해지겠지.

### webpack
module bundler

* webpack은 모듈 + dependencies를 가지고 static assets을 생성
* application code를 가지고 정적 자원들과 개발 서버 생성해줌
* 사용하지 않는 코드들 처리, hot module replacement 지원 (다른 빌드 툴에 비한 이점)
* webpack의 진짜 강점은 loader들(loader들을 이용해 babel을 통해 JSX -> Javascript 변환 가능)
  * babel-loader는 ES2015와 JSX변환을 모두 지원
* AMD, CommonJS등의 모듈 포맷 지원 (loader를 이용해) ES6도 지원
* Support package manager: Bower, npm
* Loaders for non-code: CSS, templates...
* On-demand loading
* Built-in development server

### babel
transform compiler

* 브라우저 별로 ES6에 대한 지원 여부 차이가 크므로 현재는 ES6로 작성하면 ES5로 트랜스파일해야 실제로 사용 가능
* ECMAScript 6 문법으로 작성된 파일을 변환-컴파일
* 원래 6to5라는 이름으로 ES6 -> ES5 도구로 시작했는데, 인기가 좋아서 ES7이나 다른 트랜스파일도 지원하는 포괄적인 도구가 되기 위해 Babel로 이름 변경

### gulp
node.js기반의 task runner

* streaming build system
* project를 development, production, testing등의 다른 목적 별로 빌드해줌
* 예를 들어 production(운영)으로 build하면 JavaScript를 minify하고, Sass파일을 컴파일하고, 코드에 오류가 없는지 체크하고 싶겠지. 이걸 그냥 gulp task를 작성해서 하자!

### mocha
simple, flexible, fun javascript test framework for node.js & the browser

* support TDD, BDD
* 엄밀히 말하면 Test framework라기보다는 Test framework를 담는 interface같은 형태를 띄고 있고 runner를 포함하고 있음
  * Assertion을 포함하고 있지 않음. 대신 어떤 Assertion library라도 가져다가 사용할 수 있음

### chai
DBB/TDD assertion library for node and the browser



