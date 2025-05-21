---
marp: true
style: | 
    section {
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: flex-start;
        font-size: 2em;
    }
    section.title {
        justify-content: center;
        text-align: center;
        align-items: center;
    }
    section::after {
        content: attr(data-marpit-pagination) " / " attr(data-marpit-pagination-total);
        font-size: 1.2em;
    }
math: katex
---
<!-- _class: title -->
<!-- paginate: true -->
# 適応的分散アルゴリズム 第３章<br>分散システムの安定性

川染翔吾

---
<!-- _class: title -->
# 3.3 合意

---
# 一様合意問題

$B$：初期値の全集合
各プロセス $P_i$ は局所変数 $d_{P_i}$, $w_{P_i}$ を持つ
- $d_{P_i}$：初期値
- $w_{P_i}$：合意値

各プロセス $P_i$ は変数 $w_{P_i}$ にちょうど1回だけある値 ($\in B$) を代入する

**一様合意性**：すべてのプロセス $P_i$ は、合意値を持つならば、同じ値を合意値として持つ
**停止性**：すべての正常プロセス $P_i$ はいつかは合意値を決定する
**妥当性**：合意値は常にあるプロセスの初期値から選択される