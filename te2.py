import os

linenum=0
line_list=[]
fi=open('./based_data/combineout_userf_train.txt')
for line in fi:
    item=line.strip().split(' ')
    line_list.append(item)
    linenum+=1

newline_list=[]
for itemnum in range(linenum):
    if len(line_list[itemnum])>1:
        newline_list.append(line_list[itemnum])
    else:
        print('line_list中 index为'+str(line_list)+'的list长度小于2')
# print(len(newline_list))
