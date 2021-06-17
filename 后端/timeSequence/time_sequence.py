import itertools
import argparse

import matplotlib.pylab as plt
import numpy as np
import pandas as pd
from matplotlib.pylab import style
from statsmodels.tsa.arima_model import ARIMA

# 设置matplotlib的样式
style.use('ggplot')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def readFile(file, column):
    pf = pd.read_csv(file, index_col=0, parse_dates=[0])
    pf = pf[pf.columns[column]].resample('M').mean()
    # pf_diff = pf.diff()
    pf = pf.dropna()

    pf[np.isnan(pf)] = 0
    pf[np.isinf(pf)] = 0
    return pf


def get_train(ts):
    start = ts.index[0].__str__()[:10]
    end = ts.index[int(len(ts.index) * 0.75)].__str__()[:10]

    # stock_train = ts['1949':'1958']
    return ts[start:end], start, end, (ts.index[-1] + (
                ts.index[int(len(ts.index) * 0.75)] - ts.index[0]) * 0.2).__str__()[:10]


def get_best_pqd(ts_train):
    p_re = 0
    q_re = 0
    d_re = 0
    bic_re = float('inf')
    p_min = 0
    d_min = 0
    q_min = 0
    p_max = 3
    d_max = 3
    q_max = 3

    # results_bic = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

    threads = []
    for p, d, q in itertools.product(range(p_min, p_max + 1),
                                     range(d_min, d_max + 1),
                                     range(q_min, q_max + 1)):
        print(f"try,p:{p}, d:{d}, q:{q}......")
        if p == 0 and d == 0 and q == 0:
            # results_bic[p][d][q] = np.nan
            continue
        try:
            model = ARIMA(ts_train, order=(p, d, q), freq='M')
            results = model.fit(disp=False)
            if results.bic < bic_re:
                p_re = p
                d_re = d
                q_re = q
                bic_re = results.bic
            # results_bic[p][d][q] = results.bic
        except:
            # print(f"error {p} {d} {q}")
            continue
    # print(results_bic)
    print(f"bic:{bic_re} p:{p_re} d:{d_re} q:{q_re}")
    return p_re, d_re, q_re


def get_model(train, p, d, q):
    # print(train)
    # return
    model = ARIMA(train, order=(p, d, q), freq='M')
    return model.fit(disp=False)


def pred(model, ts_end, pred_date):
    pred = model.predict(ts_end, pred_date, dynamic=True, typ='levels')
    return pred


def show_pred(pf, pred, path, title):
    plt.figure(figsize=(6, 6))
    plt.xticks(rotation=45)
    plt.title(f"牛发情的预测结果")
    plt.plot(pred)
    plt.plot(pf)
    plt.legend(["原数据", "预测"])
    plt.savefig(path)
    # plt.show()


def argsParser():
    """参数获取
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-file",
        type=str,
        help="待分析数据"
    )
    parser.add_argument(
        "-column",
        type=int,
        help="选择数据集中的行号"
    )
    parser.add_argument(
        "-path",
        type=str,
        help="结果图片保存地址"
    )
    parser.add_argument(
        "-title",
        type=str,
        help="结果标题",
        default="ARIMA模型"
    )
    args = parser.parse_args()
    return args.file, args.column, args.path, args.title


if __name__ == '__main__':
    file, column, path, title = argsParser()
    if title != None and column != None and path != None and title != None:
        pf = readFile(file, column)
        ts, start, end, pred_date = get_train(pf)
        # print(ts)
        p, d, q = get_best_pqd(ts)
        model = get_model(ts, p, d, q)
        print(model.bic)
        pred = pred(model, end, pred_date)
        show_pred(pf, pred, path, title)
    else:
        print("缺少参数 python time_sequence.py -h 获取帮助")
