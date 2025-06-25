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
# SRSW レジスタから MRSW レジスタの構成

- SRSW の多値レジスタを用いて、MRSWの多値レジスタを構成する
