---
marp: true
style: | 
    section {
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: flex-start;
        font-size: 1.8em;
    }
    section.title {
        justify-content: center;
        text-align: center;
        align-items: center;
    }
    .small {
        font-size: 1.0em;
    }
    section::after {
        content: attr(data-marpit-pagination) " / " attr(data-marpit-pagination-total);
        font-size: 1.0em;
    }
    :root {
        --fw: 1;
    }
    .flex{
        display: flex;
        gap: 1em;
    }
    .sa {
        justify-content: space-around;
    }
    .sb {
        justify-content: space-between;
    }
    .sa div,.sb div{
        margin: 0.1em;
    }
    .fw div{
        flex: var(--fw);
    }
    .center-cols {
        justify-content: center;
        width: 100%;
    }
math: katex
---
<!-- _class: title -->
<!-- paginate: true -->
# 適応的分散アルゴリズム 第６章<br>無待機システム

川染翔吾

---
<!-- _class: title -->
# 6.2 無待機性

---
# 無待機性

- 線形化可能性を満たす共有オブジェクトを実現するための簡単な方法は相互排除
    - 共有オブジェクトを占有するプロセスが停止したとき、分散システム全体が停止してしまう

- **無待機性**：他のプロセスの停止故障や動作速度にかかわらず、プロセス自信の作業を有限時間内に完了できる
    - $n$ プロセスからなるシステムで $n-1$ 個のプロセスが停止故障しても、残り $1$ 個のプロセスは正常に動作する

---
<!-- _class: title -->
# 6.3 共有オブジェクトを実現する無待機アルゴリズム

---
# 共有レジスタ
- **原子レジスタ**：複数のプロセスが並行して実行したときでも、その大域履歴が線形化可能性を保証するレジスタ

- 共有レジスタは、格納できる値の種類数、${Read}$ 命令を実行できるプロセス数、および ${Write}$ 命令を実行できるプロセス数の違いで分類される

---
# レジスタの種類
- 格納できる値が $0$ から $k-1$ までの $k$ 種類のとき $k$ 値レジスタ
    - 最も単純なものは $2$ 値レジスタ
    - $k$ が $3$ 以上なら多値レジスタ
- $r$ 個のプロセスが ${Read}$ 命令を実行可能で、$w$ 個のプロセスが ${Write}$ 命令を実行可能なとき $r$R$w$W レジスタという
    - 最も単純なものは $1$R$1$W レジスタ
    - 単一か複数かだけを表したいときは、SRSW レジスタ、MRSW レジスタ、SRMW レジスタ、MRMW レジスタ
- 最も単純なレジスタは SRSW の $2$ 値レジスタ

---
# 高機能なレジスタの実現
- SRSW の $2$ 値レジスタは原子レジスタとして動作するものとして進める

- 任意の $r,w,k$ に対して、$1$R$1$Wの $2$ 値レジスタを用いて $r$R$w$W の $k$ 値レジスタを構成する無待機アルゴリズムを段階的に考える

1. SRSW の $2$ 値レジスタを用いて、SRSWの多値レジスタを構成する無待機アルゴリズム
1. SRSW の多値レジスタを用いて、MRSWの多値レジスタを構成する無待機アルゴリズム
1. MRSWの多値レジスタを用いて、MRMWの多値レジスタを構成する無待機アルゴリズム

---
# $2$ 値レジスタから多値レジスタの構成
- SRSW の $2$ 値レジスタを用いて、SRSWの多値レジスタを構成する
- 線形化可能性は局所性が成り立つので、SRSW の $k$ 値レジスタを一つ構成することを考える

---
# SRSW-M
- $k$ 値レジスタ $R$ を実現する
- $k$ 個の $2$ 値レジスタ $R_0,R_1,\dots,R_{k-1}$ を使用する
- $R=i$ を $R_i=1,R_0=R_1=\dots=R_{i-1}=0$ として実現する
    - 値 $1$ を格納する $2$ 値レジスタの最小インデックスが $k$ 値レジスタ $R$ が格納している値
- $R$ は初期値としてある値 $v_0 (0\le v_0 \le k-1)$ を持ち、$R_{v_0} = 1, R_i = 0 (i \ne v_0)$ が成り立つ

---
# 単純な読出し方法で失敗する例
### 書込み
- $R_v$ に $1$ を書込み、$R_i (0\le i \le v-1)$ にインデックスの降順で $0$ を書き込む

### 読出し
- $R_0$ からインデックスの昇順に読み出し、最初に $1$ を読み出したレジスタのインデックスを $R$ から読み出した値とする

---
# 単純な読出し方法で失敗する例
<img src="img/lec6_2/11.svg" height="500"/>

---
# SRSW-M
<div class="flex fw center-cols">
<div class="small" style="--fw: 1;">

### 読出し動作

1. $i \gets 0$
1. `while` $R_i = 0$ `do`
    - $i \gets i+1$
1. ${value} \gets i$
1. `for` $j \gets i-1$ `downto` $0$ `do`
    - `if` $R_j=1$ `then` ${value} \gets j$
1. `return` $value$

</div>
<div class="small" style="--fw: 1;">

### 値 $v$ の書込み動作

1. $R_v \gets 1$
1. `for` $i \gets v-1$ `downto` $0$ `do`
    - $R_i \gets 0$
1. `return` $(OK)$

</div>
</div>

---
# SRSW-M
SRSW-M は $k$ 個の SRSW の $2$ 値レジスタを用いて、SRSW の $k$ 値レジスタを実現する無待機アルゴリズムである

### 証明
無待機性を示す
2 の `while` が終了する、つまりレジスタ $R_i$ から値 $1$ を読み出すことを示す

初期状態では $R_{v_0} = 1$ が成り立つ。
$2$ 値レジスタ $R_i$ に値 $0$ を書き込むとき、その前に $R_v (v>i)$ に値 $1$ を書き込んでいる。このことから $P_r$ がレジスタ $R_i$ を読み出すときにはあるレジスタ $R_j (j \le i)$ が値 $1$ を保持していることを示せる

---
# SRSW レジスタから MRSW レジスタの構成

- SRSW の多値レジスタを用いて、MRSWの多値レジスタを構成する
- レジスタ $R$ に対して ${READ}$ 命令を実行できる $n$ 個のプロセスを $P_r (1\le r\le n)$、<br>${READ}$ 命令を実行できる単一のプロセスを $Q_w$ と表す
- MRSW レジスタ $R$ を実現するために $n^2 + n$ 個の SRSW レジスタを使用
---
- ${Val}_r$：プロセス $Q_w$ が共有レジスタ $R$ に書き込んだ値を各プロセス $P_r$ に伝えるためのレジスタ
- ${Report}_{i,j}$：プロセス $P_i$ がレジスタ $R$ から読み出した値を他のプロセス $P_j$ に伝えるためのレジスタ
- ${Val}_r$ および ${Report}_{i,j}$ には、レジスタ $R$ に格納する値とプロセス $Q_w$ が $R$ にその値を書き込んだときの時刻印の組を格納する
- 全ての SRSW レジスタの初期値は、$R$ の初期値 $v_0$ と時刻印の初期値 $0$ の組 $(v_0, 0)$

---
# 単純な読出し方法で失敗する例
### 書込み
- ${Val}_i (0\le i \le n-1)$ にインデックスの昇順で書き込む

### $P_i$ による読出し
- ${Val}_i$ から読み出す

---
# 単純な読出し方法で失敗する例
<img src="img/lec6_2/21.svg" height="500"/>

---
# MRSW-M

<div class="flex fw center-cols">
<div class="small" style="--fw: 1;">

### $P_r$ の読出し動作

1. $(v[0],ts[0]) \gets {Val}_r$
1. `for` $i \gets 1$ `to` $n$ `do`
    - $(v[i],ts[i]) \gets {Report}_{i,r}$
1. $j = \mathrm{maxarg}_{0 \le i \le n} ts[i]$
1. `for` $i \gets 1$ `to` $n$ `do`
    - ${Report}_{r,i} \gets (v[j],ts[j])$
1. `return` $v[j]$

</div>
<div class="small" style="--fw: 1;">

### 値 $v$ の書込み動作

1. $ts \gets ts + 1$
1. `for` $i \gets 1$ `to` $n$ `do`
    - ${Val}_i \gets (v,ts)$
1. `return` $(OK)$

</div>
</div>

---
# MRSW レジスタから MRMW レジスタの構成

- MRSW の多値レジスタを用いて、MRMWの多値レジスタを構成する
- 構成する $n$R$m$W レジスタ $R$ に対して ${Read}$ 命令を実行できる $n$ 個のプロセスを $P_r$ とし、${Write}$ 命令を実行できる $m$ 個のプロセスを $Q_w$ とする
- $m$ 個の $(n+m)$R$1$W レジスタ $R_i (1 \le i \le m)$ を使用する
- 共有レジスタ $R_i$ に対しては、プロセス $Q_i$ が ${write}$ 命令を実行でき、各プロセス $P_r (1 \le r \le n)$ および $Q_w (1 \le w \le m)$ が ${read}$ 命令を実行できる
- レジスタ $R_i$ が格納される値は、レジスタ $R$ が格納するデータと、プロセス $Q_i$ が $R_i$ にそのデータを書き込んだときの時刻印
- 全ての MRSW レジスタ の初期値は、レジスタ $R$ の初期値 $v_0$ と時刻印の初期値 $0$ の組 $(v_0,0)$

---
# MRMW-M

<div class="flex fw center-cols">
<div class="small" style="--fw: 1;">

### $P_r$ による読出し動作

1. `for` $i \gets 1$ `to` $m$ `do`
    - $(v[i],ts[i]) \gets R_i$
1. $j \gets \mathrm{maxarg}_{1\le i \le m} ts[i]$
    - $ts[i]$ が同じ場合は最小の $i$
1. `return` $v[j]$

</div>
<div class="small" style="--fw: 1;">

### $Q_w$ による値 $v$ の書込み動作

1. `for` $i \gets 1$ `to` $m$ `do`
    - $ts[i] \gets {R_i}.{ts}$
1. $ts \gets \max\{ts[i] | 1\le i\le m\}+1$
1. $R_w \gets (v,ts)$
1. `return` $(OK)$

</div>
</div>
