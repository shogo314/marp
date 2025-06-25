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
# スライドタイトル

名前

---
<!-- _class: title -->
# 大見出し

---
# SS-TOKEN-RING
プロセス $P_i$ の局所状態を $s_i \in \{0,1,\dots,K-1\}$ とする ($K$ は $n$ 以上の任意の自然数)
<div class="flex fw center-cols">
<div class="small" style="--fw: 1;">

### プロセス $P_0$ 上
1. $s_{n-1}=s_0$ なら
    - $s_0 \gets (s_0+1) \mod K$
</div>
<div class="small" style="--fw: 1;">

### プロセス $P(\ne P_0)$ 上
1. $s_{i-1}\ne s_i$ なら
    - $s_i \gets s_{i-1}$
</div>
</div>