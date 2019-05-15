import numpy as np
import operator
import os

def load_race_vec(input_file):
    if not os.path.exists(input_file):
        return {}
    linenum=0
    race_vec={}
    fp=open(input_file)
    for line in fp:
        if linenum==0:
            linenum+=1
            continue
        race=line.strip().split()
        race_id = race[0]
        if len(race)<100:
            continue
        if race_id=='</s>':
            continue
        race_vec[race_id]=np.array([float(ele) for ele in race[1:]])
    fp.close()
    return race_vec

def cal_race_sim(race_vec,race_id,output_file):
    if race_id not in race_vec:
        return
    score={}
    fix_race_vec=race_vec[race_id]
    for tmp_race_id in race_vec:
        if tmp_race_id == race_id:
            continue
        tmp_race_vec=race_vec[tmp_race_id]
        # 分母部分
        denominator=np.linalg.norm(fix_race_vec)*np.linalg.norm(tmp_race_vec)
        if denominator==0:
            score[tmp_race_id]=0
        else:
            # 分子部分
            # np.dot(fix_race_vec,tmp_race_id)
            # round 函数四舍五入(对应的数，保留小数点后几位)
            score[tmp_race_id]=round(np.dot(fix_race_vec,tmp_race_vec)/denominator,3)

    fw = open(output_file, "w+")
    out_str = race_id + "\t"
    tmp_list = []
    topK = 10
    for zuhe in sorted(score.items(), key=operator.itemgetter(1), reverse=True)[:10]:
        tmp_list.append(zuhe[0] + '_' + str(zuhe[1]))
    out_str += ';'.join(tmp_list)
    fw.write(out_str + '\n')
    fw.close()


def run_process(input_file,output_file,race_id):
    race_vec=load_race_vec(input_file)
    cal_race_sim(race_vec,str(race_id),output_file)
    # item_vec


if __name__=='__main__':
    # race_vec=load_race_vec('./data/race_partake_vec_6.txt')
    # print(len(race_vec))
    # print(race_vec['583'])
    input_id=input('请输入查看的race_id: ')
    run_process('./data/race_partake_vec_6.txt','./race_test/{}_test.txt'.format(str(input_id)),str(input_id))
