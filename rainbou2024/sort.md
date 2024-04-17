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
# ソートアルゴリズムについて

---
# 扱う問題
改題元: [B - Interactive Sorting](https://atcoder.jp/contests/practice/tasks/practice_2)

- $5$ 個のボールがあり、重さはすべて異なる
- 天秤にボールを $1$ つずつのせて重さを比べることができる
- $8$ 回以内の比較でボールを軽い順に並べる

![center](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgvsNCqznlQdJa-MJryzDx7rHIr-4X1_1CmzYagy9XU1RjZZeBCjw2_Hs7sMM2RwLxMEq0xGND3eWwB3kCgdnrsRDNZIaVbI8RgFXoi4QACh_nrDtoZaL4R6-hnapeWb3_xO_vr71RGq0g/s400/tenbin.png)

---
# 二分挿入ソート (Binary insertion sort)
- ソートされた列に次の要素を適切な位置に挿入していく
- 挿入する位置は**二分探索**する

---
# 二分挿入ソート (Binary insertion sort)
![center](img/insertion-sort-1.svg)

---
# 二分挿入ソート (Binary insertion sort)
![center](img/insertion-sort-2.svg)

---
# 二分挿入ソート (Binary insertion sort)
![center](img/insertion-sort-3.svg)

---
# 二分挿入ソート (Binary insertion sort)
![center](img/insertion-sort-4.svg)

---
# 二分挿入ソート (Binary insertion sort)
![center](img/insertion-sort-5.svg)

---
# 二分挿入ソート (Binary insertion sort)
![center](img/insertion-sort-6.svg)

---
# マージソート (Merge sort)
- ソートされた $2$ つの列を**マージ**していく

---
# マージソート (Merge sort)
![center](img/merge-sort-1.svg)

---
# マージソート (Merge sort)
![center](img/merge-sort-2.svg)

---
# マージソート (Merge sort)
![center](img/merge-sort-3.svg)

---
# マージソート (Merge sort)
![center](img/merge-sort-4.svg)

---
# マージソート (Merge sort)
![center](img/merge-sort-5.svg)

---
# マージソート (Merge sort)
![center](img/merge-sort-6.svg)

---
# マージソート (Merge sort)
![center](img/merge-sort-7.svg)

---
<!-- _class: title -->
# 実は $7$ 回でできる

---
# マージ挿入ソート (Merge-insertion sort)
- $2$ つずつのペアを作り比較する
- 大きい方のグループを作りソートする
- ソートした列に残りを挿入していく

---
# マージ挿入ソート (Merge-insertion sort)
![center](img/merge-insertion-sort-1.svg)

---
# マージ挿入ソート (Merge-insertion sort)
![center](img/merge-insertion-sort-2.svg)

---
# マージ挿入ソート (Merge-insertion sort)
![center](img/merge-insertion-sort-3.svg)

---
# マージ挿入ソート (Merge-insertion sort)
![center](img/merge-insertion-sort-4.svg)

---
# マージ挿入ソート (Merge-insertion sort)
![center](img/merge-insertion-sort-5.svg)

---
# マージ挿入ソート (Merge-insertion sort)
![center](img/merge-insertion-sort-6.svg)
