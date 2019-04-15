# -*-coding:utf8-*-
import os
import xlrd
import xlwt

def raceevent_train_data(inputfile,outputfile):
    if not os.path.exists(inputfile):
        return
    record={}
    linenum=0
    fi=open(inputfile)
    for line in fi:
        if linenum==0:
            linenum+=1
            continue
        item=line.strip().split(',')
        user_id,frace_id=item[0],item[1]
        if user_id not in record:
            record[user_id]=[]
        record[user_id].append(frace_id)
    fi.close
    fo=open(outputfile,'w+')
    for userid in record:
        fo.write(' '.join(record[userid])+'\n')
    fo.close()

if __name__=='__main__':
    raceevent_train_data('./based_data/583userFinfo_train.txt','./based_data/combineout_userf_train.txt')


