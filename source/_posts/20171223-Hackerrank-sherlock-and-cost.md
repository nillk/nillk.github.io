---
title: '[Hackerrank] Sherlock and Cost'
date: 2017-12-23 17:02:08
categories:
  - programming
  - algorithm
tags:
  - algorithm
  - hackerrank
  - dynamic programming
mathjax: true
---


한동안 못 보다가 다시 틈 날 때마다 알고리즘 문제를 하나씩 보고 있다. 전에는 백준에 주로 갔었는데 요샌 귀찮아서 Hackerrank에서 하나씩. 그리고 이제부터 푸는 문제는 차차 정리해서 올리기로! 예전에 풀었던 문제들도 언젠가...

오늘은 [Sherlock and Cost](https://www.hackerrank.com/challenges/sherlock-and-cost/problem) 문제를 풀었고, Algorithms에 Dynamic Programming 카테고리에 있는 문제다.

전체 코드는 가장 아래에 있다. 내가 생각한 식은 대략 아래와 같다.
$$
\begin{cases}
  S[i][1선택] = max(S[i - 1][1선택], S[i - 1][B\_i선택] + (B[i - 1] - 1)) \newline
  S[i][B\_i선택] = max(S[i - 1][1선택] + (B[i] - 1), S[i - 1][B\_i선택] + abs(B[i - 1] - B[i]))\\
\end{cases}
$$

S 는 문제에서 말한 S의 정의에 따른 *$i$ 인덱스 까지의 합의 최대값을 보관하는 배열*이다. 문제에서는 $A\_i$가 1과 $B\_i$사이의 값이라고 했는데, 결국 $A\_i - A\_{i-1}$ 의 절대값을 최대로 하기 위해서는 두 값의 차이가 최대여야 하기 때문에 중간값은 무시하고 1이거나 $B_i$라고 가정한다.

식을 풀어서 말해보자면 $i$번째 인덱스에서 1을 선택했을 시 최대값은 *$i-1$번째에 1을 택했을 때의 최대값 + 0 (1 - 1이기 때문에)*과 *$i-1$번째에 $B\_{i-1}$를 선택했을 때의 최대값 + ($B\_{i-1}$ - 1)*중 큰 값이며, $i$번째 인덱스에서 $B\_i$를 택했을 시 최대값은  *$i-1$번째에 1을 택했을 때의 최대값 + $B\_i - 1$*과 *$i-1$번째에 $B_\{i-1}$를 택했을 때의 최대값 + 절대값($B\_i - B\_{i-1}$)*중 큰 값이다.

```java
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
  public static void main(String args[] ) throws Exception {
    Scanner scan = new Scanner(System.in);
    
    int T = scan.nextInt();
    while (T-- > 0) {
      int N = scan.nextInt();
      int[] B = new int[N];
      int[][] S = new int[N][2];

      B[0] = scan.nextInt();
      for (int i = 1; i < N; i++) {
        B[i] = scan.nextInt();
                  
        S[i][0] = Math.max(S[i - 1][0], S[i - 1][1] + (B[i - 1] - 1));
        S[i][1] = Math.max(S[i - 1][0] + (B[i] - 1), S[i - 1][1] + Math.abs(B[i] - B[i - 1]));
      }

      System.out.println(Math.max(S[N - 1][0], S[N - 1][1]));
    }

    scan.close();
  }
}
```