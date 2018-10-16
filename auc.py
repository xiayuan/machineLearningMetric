from sklearn import cross_validation,metrics
import numpy as np




def read_file(pred_file, label_file):
    pf=open(pred_file, 'r')
    lf=open(label_file, 'r')
    
    pf_list=[]
    lf_list=[]
    
    for pi in pf:
        pf_list.append(float(pi.rstrip('\n')))
    
    for li in lf:
        lf_list.append(int(li.rstrip('\n')))

    pf_np=np.array(pf_list)
    lf_np=np.array(lf_list)

    return pf_np, lf_np



def get_auc(y_pred, y_true):
    test_auc = metrics.roc_auc_score(y_true, y_pred)
    print test_auc 


def auc2(y_pred, y_true):
    a = sorted([(y_pred[i], y_true[i]) for i in range(len(y_pred))], key=lambda x: -x[0])
    s = 0.0
    true_count = sum(y_true)
    false_count = len(y_true) - true_count
    total_false = false_count

    for i in a:
        if i[1]:
            s += 1.0 / true_count * false_count / total_false
        else:
            false_count -= 1

    print s
    return s


if __name__=="__main__":
    y_pred, y_true = read_file("first_pred.txt","first_gt.txt")
    get_auc(y_pred, y_true)
    auc2(y_pred, y_true)

