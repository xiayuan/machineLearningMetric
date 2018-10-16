from sklearn.metrics import precision_recall_curve
import numpy as np
import math


def get_pr_curve(pred_file,label_file):

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
    precision,recall,thresholds = precision_recall_curve(lf_np,pf_np,pos_label=1)

    print len(precision)
    print len(recall)
    print len(thresholds)

    for i in xrange(len(precision)):
            f1 = 2*precision[i]*recall[i]/(precision[i]+recall[i])
        #if math.fabs(precision[i]-1)<0.00001 or math.fabs(recall[i]-1)<0.00001 or math.fabs(recall[i]-0.5)<0.01:
            if i < len(thresholds):
                print "precision=%f recall=%f thresholds=%f f1=%f"%(precision[i],recall[i],thresholds[i],f1)
            else:
                print "precision=%f recall=%f "%(precision[i],recall[i])

    pos_num=lf_list.count(1)
    print "pos_num=%d total_num=%d psitive_percent=%f"%(pos_num,len(lf_np),pos_num/1./len(lf_np))
    
    


if __name__=="__main__":
    
    get_pr_curve("first_pred.txt","first_gt.txt")



