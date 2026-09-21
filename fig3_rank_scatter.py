#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fig3_rank_scatter.py —— 感知维数论文 图3 双面板秩-秩散点（复现件）

2026-09-21 数值核对终稿：图与预注册 v0.2 锁定数据逐项核对通过（14 点全部吻合），
本脚本由核对工作补录落盘（原生成脚本会话内嵌未存档，教训同 mantel_v0.1 整理——
图件必须脚本化存档）。重跑: python3 fig3_rank_scatter.py [--out 路径]

数据源（全部预注册 v0.2 锁定，跑前于结果先）：
  X = OR 功能基因数 intact（NMT 2014, Genome Res 24:1485-96, Fig 1A 图像精读）
  Y(左)  = 嗅球神经元数 ×10^6（Ribeiro 2014 FNA 8:23 Table 1；人=Oliveira-Pinto
           2014 男女均值 5.2M；象=Neves 2014 908.37M）
  Y(右)  = 全脑神经元数 ×10^6（Herculano-Houzel 系 isotropic fractionator，
           预注册 v0.1 主表+v0.2 L23 扩容：豚鼠 239.62M/绒猴 635.80M）
  ρ 值 = Spearman + exact permutation（预注册 v0.1/v0.2 锁定判据）
         OB n=6: +0.486（图注 +0.49）；全脑 n=8: -0.143（图注 -0.14）
"""
import argparse
import math

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# (物种, OR intact, OB 神经元 M, 全脑神经元 M)  —— 预注册 v0.2 锁定值
# OB 主集 n=6 = 主集锁定（绒猴 OB 有值但属 S2 敏感性口径，不入主面板——
# 预注册 v0.2 L22 主集六种；误入则 n=7 ρ=+0.536=S2 而非主分析 +0.486）
OB_MAIN = {"human", "macaque", "mouse", "rat", "guinea pig", "elephant"}
DATA = [
    ("human",      386,   5.20, 86100.00),
    ("macaque",    309,   8.47,  6376.16),
    ("mouse",     1130,   3.89,    70.89),
    ("rat",       1207,  11.10,   200.13),
    ("guinea pig", 796,   6.06,   239.62),
    ("elephant",  1948, 908.37, 257040.00),
    ("dog",        811,   None,  2252.69),
    ("marmoset",   366,   2.11,   635.80),
]


def rank(xs):
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    r = [0.0] * len(xs)
    for pos, i in enumerate(order):
        r[i] = pos + 1.0
    return r


def spearman(a, b):
    ra, rb = rank(a), rank(b)
    n = len(a)
    ma, mb = sum(ra) / n, sum(rb) / n
    num = sum((x - ma) * (y - mb) for x, y in zip(ra, rb))
    den = math.sqrt(sum((x - ma) ** 2 for x in ra) * sum((y - mb) ** 2 for y in rb))
    return num / den


def panel(ax, rows, y_idx, title, label_y):
    xs = [math.log10(r[1]) for r in rows]
    ys = [math.log10(r[y_idx]) for r in rows]
    ax.scatter(xs, ys, s=90, color="#2e4057", zorder=3)
    for r, x, y in zip(rows, xs, ys):
        ax.annotate(r[0], (x, y), textcoords="offset points", xytext=(8, 4), fontsize=11)
    rho = spearman([r[1] for r in rows], [r[y_idx] for r in rows])
    ax.set_title(f"{title}\nρ = {rho:+.2f} (exact-permutation reference)", fontsize=13)
    ax.set_xlabel(r"$\log_{10}$ functional OR genes (NMT 2014)", fontsize=12)
    ax.set_ylabel(label_y, fontsize=12)
    print(f"  {title}: n={len(rows)} rho={rho:+.4f}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="fig3_rank_scatter.png")
    args = ap.parse_args()

    ob_rows = [r for r in DATA if r[2] is not None and r[0] in OB_MAIN]
    wb_rows = [r for r in DATA if r[3] is not None]
    print("复现 fig3（数值层，预注册 v0.2 锁定数据）：")
    fig, axes = plt.subplots(1, 2, figsize=(14.5, 5.6))
    panel(axes[0], ob_rows, 2,
          "row-specific: olfactory bulb (n=6)", r"$\log_{10}$ neurons")
    panel(axes[1], wb_rows, 3,
          "total: whole brain (n=8)", r"$\log_{10}$ neurons")
    fig.suptitle(
        "Budget line: whole-brain refuted / row-specific positive "
        "— budgets must be allocated by row", fontsize=15)
    fig.tight_layout(rect=(0, 0, 1, 0.93))
    fig.savefig(args.out, dpi=150)
    print(f"  已输出 {args.out}")
    # 期望锚点（预注册 v0.2 首跑）：OB +0.486 / 全脑 -0.143
    assert abs(spearman([r[1] for r in ob_rows], [r[2] for r in ob_rows]) - 0.486) < 0.005
    assert abs(spearman([r[1] for r in wb_rows], [r[3] for r in wb_rows]) - (-0.143)) < 0.005
    print("  ρ 锚点校验通过（+0.486/-0.143）——与预注册首跑一致")


if __name__ == "__main__":
    main()
