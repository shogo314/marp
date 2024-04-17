---
marp: true
style: |
    section {
        justify-content: normal;
    }
    section.title {
        justify-content: center;
        text-align: center;
    }
    img[alt~="center"] {
        display: block;
        margin: 0 auto;
    }
math: mathjax
---
<!-- _class: title -->
# 競技プログラミングってなあに

阪大競技プログラミング部RAIBOU

---
# 自己紹介
- name: shogo314
- 工学部電子情報工学科4年
- RAIBOU部長
- AtCoder 青
- 言語: Python3 / C++

![bg right:40% 80%](img/icon.png)

---
# 競技プログラミングって？
- プログラミングコンテストに参加して他の競技者と競う
- AtCoderや他の大抵のコンテストは以下の形式
    1. 開始時刻になったら問題セット（各問題の問題文と入出力例）が公開される
    1. 参加者は問題を解くためのプログラムを作成し、ソースコードを提出する
    1. 提出したプログラムは即座にジャッジサーバーで実行され、要求された通りの出力をしていれば正解となり、点数が与えられる
    1. 終了時刻に多くの点数を得ている参加者が上位、同点の場合はその点数に達するまでの時間が短いほうが上位として順位付けされる

---
# AtCoder
- 国内最大規模のコンテストサイト（世界的にも 2~4 番目くらい）
- 毎週土曜（たまに日曜）の 21:00~22:40 に AtCoder Beginner Contest が開催されている
    - 毎週１万人近い人数が参加している
    - 最も難易度の低いコンテスト
    - 初心者向けの問題から20人程しか正解しない問題まで幅広く7問出題される
- レーティングシステムが採用されており、コンテストの結果によりレートが変動する

---
# 競プロはこんな人におすすめ
- プログラミングの練習がしたいけど、作りたいものがない人
- コードを書くのが好きな人
- 効率的なコードを書けるようになりたい人
- 数学が好きな人
- 論理的なアイデアを考えるのが好きな人
- 勉強したことを繰り返すのが好きな人
- 持ち前の頭脳で戦いたい人

---
# 効率的なコードって？
- 競技プログラミングでは時間計算量が大事
- 時間計算量は計算回数のこと
- 問題ごとに実行時間制限が決まっているのでそれを満たすようにプログラムを書く

---
# 問題例
- ある整数 $N$ が入力で与えられる
- それが素数だった場合は `True` を出力
- 素数でなければ `False` を出力する
- $1 \le N \lt 10^{14}$
- 実行時間制限: 2sec

入力例
```
5
```
出力例
```
True
```

---
# 解法1
- $1$ は素数ではない
- $1$ と自分自身以外の約数をもたない数は素数

```py diff
def isprime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


N = int(input())
print(isprime(N))
```

これだとだいたい $N$ くらいの計算量になる

---
# 解法1
- $N$ が $a$ で割り切れるとき、$\frac{N}{a}$ でも割り切れる

```py
def isprime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if i * i > N:
            break
        if n % i == 0:
            return False
    return True


N = int(input())
print(isprime(N))
```

これだとだいたい $\sqrt{N}$ くらいの計算量になる

---
# 解法2
- ライブラリを使ってもよい

```py
import sympy

N = int(input())
print(sympy.isprime(N))
```

---
# パズル
- $5$ 個のボールがあり、重さはすべて異なる
- 天秤にボールを $1$ つずつのせて重さを比べることができる
- $8$ 回以内の比較でボールを軽い順に並べる

![center](img/sort-1.svg) ![center](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgvsNCqznlQdJa-MJryzDx7rHIr-4X1_1CmzYagy9XU1RjZZeBCjw2_Hs7sMM2RwLxMEq0xGND3eWwB3kCgdnrsRDNZIaVbI8RgFXoi4QACh_nrDtoZaL4R6-hnapeWb3_xO_vr71RGq0g/s400/tenbin.png)

---
# どうやって始めるの？（無料）
- プログラミング言語の勉強をする
    - AtCoder Programming Guide for beginners (C++ / Python3)
    - ほどほどでよい（ネットにある無料のやつを適当にやれば十分。やりながら勉強すればよい）
- とりあえず AtCoder でアカウントを作り、過去問を解いてみる
    - id は一度しか変更できない、同時に複数のアカウントを持つことは規約違反であることに注意
- AtCoder Beginner Contest に出る
- アルゴリズムの勉強をする
    - Aizu Online Judge のコースを進める

---
# どうやって始めるの？（有料）
- 本を読む
    - [関連書籍 - AtCoderInfo](https://info.atcoder.jp/more/contents/official-book)
    - 競技プログラミングの鉄則 ~アルゴリズム力と思考力を高める77の技術~
    - アルゴリズム的思考力が身につく! プログラミングコンテストAtCoder入門
    - アルゴリズム実技検定　公式テキスト［エントリー～中級編］
    - JOI 公式テキスト Pythonで問題解決
- paizaラーニング（RAIBOUに入ると無料！）

---
# 【宣伝】RAINBOUに⼊部しませんか？
- OUCC との兼部ももちろん OK
- 主な活動
    - ABC 後の感想戦
    - ICPC（国際⼤学対抗プログラミングコンテスト）の参加
    - OUPC（⼤阪⼤学プログラミングコンテスト）の開催
    - 合宿など
- 部費は $0$ 円！

---
<!-- _class: title -->
# 演習

---
# ビーバーチャレンジ
- URL: https://bebras.eplang.jp/
- 情報科学の問題を、知識を必要としないパズルにしたもの
- イラストを多く含み、選択形式

![center](https://bebras.eplang.jp/swfu/d/bebras_cover.png)

---
# MojaCoder
簡単なやつ
https://mojacoder.app/users/kusirakusira/problems/25GBC_A
https://mojacoder.app/users/Soni/problems/shopping
https://mojacoder.app/users/powell/problems/fizz-buzz
https://mojacoder.app/users/kusirakusira/problems/25GBC_B

計算量を意識する必要がある
https://mojacoder.app/users/namako/problems/minminminminsum
https://mojacoder.app/users/take44444/problems/division-game
