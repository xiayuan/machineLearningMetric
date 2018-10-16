#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn import cross_validation,metrics
import numpy as np


def read_file(pred_file, label_file):
    """
    数据读取
    """
    pf = open(pred_file, 'r')
    lf = open(label_file, 'r')
    
    pf_list = []
    lf_list = []
    
    for pi in pf:
        pf_list.append(float(pi.rstrip('\n')))
    
    for li in lf:
        lf_list.append(int(li.rstrip('\n')))

    pf_np = np.array(pf_list)
    lf_np = np.array(lf_list)

    return pf_np, lf_np


def get_auc(y_pred, y_true):
    """
    传统的auc计算，基于sklearn
    """
    test_auc = metrics.roc_auc_score(y_true, y_pred)
    print test_auc 


def auc2(y_pred, y_true):
    """
    auc的物理意义在于: 随机正样本比随机负样本得分高的概率，随机选取一个正例和一个负例，分类器给正例的打分大于分类器给负例的打分的概率。
    基于这种只管的思路可以更快速的技术auc
    注: auc计算只关注概率的rank排序, 而不在乎概率的值, 利用概率值对结果进行排序后, 概率值的修改, 不影响最终auc结果
    注: 缺陷是不能存在相同概率的情况
    """
    sortList = sorted([(y_pred[i], y_true[i]) for i in range(len(y_pred))], key=lambda x: -x[0])
    score = 0.0
    true_count = sum(y_true)
    false_count = len(y_true) - true_count
    total_false = false_count

    for i in sortList:
        if i[1] == 1:
            score += 1.0 / true_count * false_count / total_false
        else:
            false_count -= 1

    print score

def calculateNegUnderPos(y_pred, y_true):
    """
    auc的物理意义在于: 将M+N个样本按照概率由大到小排序后，对于任意的一个正样本，计算比它概率小的负样本的个数，然后求和，除以M*N，即为AUC。
    基于这种只管的思路可以更快速的技术auc
    注: auc计算只关注概率的rank排序, 而不在乎概率的值, 利用概率值对结果进行排序后, 概率值的修改, 不影响最终auc结果
    注: 缺陷是不能存在相同概率的情况
    """
    sortList = sorted([(y_pred[i], y_true[i]) for i in range(len(y_pred))], key=lambda x: x[0])
    score = 0.0
    true_count = sum(y_true)
    false_count = len(y_true) - true_count
    total_false = false_count
    
    for index, i in enumerate(sortList):
        if i[1] == 1:
            for j in range(index):
                if sortList[j][1] == 0:
                    score += 1.0

    print score / (true_count * false_count)

if __name__=="__main__":
    y_pred, y_true = read_file("first_pred.txt","first_gt.txt")
    get_auc(y_pred, y_true)
    auc2(y_pred, y_true)
    calculateNegUnderPos(y_pred, y_true)

