# !/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
from sklearn import svm
from sklearn.model_selection import GridSearchCV    # 0.17 grid_search
import matplotlib.pyplot as plt


if __name__ == "__main__":
    N = 50
    # 随机种子
    np.random.seed(0)
    # 随机来点数据  sin函数的
    x = np.sort(np.random.uniform(0, 6, N), axis=0)
    y = 2*np.sin(x) + 0.1*np.random.randn(N)
    x = x.reshape(-1, 1)
    print('x =\n', x)
    print('y =\n', y)

    model = svm.SVR(kernel='rbf')
    c_can = np.logspace(-2, 2, 10)
    gamma_can = np.logspace(-2, 2, 10)
    # 自动寻最优参数GridSearchCV
    svr = GridSearchCV(model, param_grid={'C': c_can, 'gamma': gamma_can}, cv=5)
    svr.fit(x, y)
    print('验证参数：\n', svr.best_params_)
    #  初始化测试数据
    x_test = np.linspace(x.min(), x.max(), 100).reshape(-1, 1)
    # 预测
    y_hat = svr.predict(x_test)
    # 可视化
    sp = svr.best_estimator_.support_
    plt.figure(facecolor='w')
    plt.scatter(x[sp], y[sp], s=120, c='r', marker='*', label='Support Vectors', zorder=3)
    plt.plot(x_test, y_hat, 'r-', linewidth=2, label='RBF Kernel')
    plt.plot(x, y, 'go', markersize=5)
    plt.legend(loc='upper right')
    plt.title('SVR', fontsize=16)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()
