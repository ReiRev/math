from __future__ import annotations
import matplotlib.pyplot as plt
import numpy as np


def plot_cp(func, lim: list[double]):  # 複素平面上に描く
    # FigureとAxesを描画
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.grid()

    ax.set_xlim(lim)
    ax.set_ylim(lim)

    # 実軸
    plt.quiver(lim[0], 0, lim[1]-lim[0], 0, angles='xy', scale_units='xy',
               width=0.005, headwidth=10, headlength=10, headaxislength=5, scale=1)
    plt.text(1.05*lim[1], 0.02*lim[0], 'Re')
    # 虚軸
    plt.quiver(0, lim[0], 0, lim[1]-lim[0], angles='xy', scale_units='xy',
               width=0.005, headwidth=10, headlength=10, headaxislength=5, scale=1)
    plt.text(0.03*lim[0], 1.05*lim[1], 'Im')
    # 原点
    plt.text(0.1*lim[0], 0.1*lim[0], '$O$')

    # 余分な目盛りを削除
    xt = list(ax.get_xticks())
    for i in [0, np.floor(lim[0]), np.ceil(lim[1])]:
        xt.remove(i)
    ax.set_xticks(xt)
    ax.set_yticks(xt)

    # 虚軸の目盛りを"n j"に変更
    imlabel = []
    for ticks in ax.get_yticks():
        imlabel.append(str(ticks)+" j")
    ax.set_yticklabels(imlabel)

    # 軸を中央に移動
    ax.spines['bottom'].set_position('center')
    ax.spines['left'].set_position('center')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    plt.plot(np.real(func), np.imag(func))

    # 出力
    plt.show()
