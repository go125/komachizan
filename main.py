#!/usr/bin/env python
# coding: utf-8

csv_name="result.csv"
csv_long_name="result_long.csv"

import itertools
import csv
import logging

logging.basicConfig(level=logging.DEBUG)

seq = (0,1,2,3,4,5,6,7)

seq_list=list(itertools.permutations(seq))

def make_oplist(num):
    op_list=[]
    for i in range(0,8):
        rand_int=num%4
        if rand_int==0:
            op_list.append("+")
        if rand_int==1:
            op_list.append("-")
        if rand_int==2:
            op_list.append("*")
        if rand_int==3:
            op_list.append("/")
        num=num//4
    return op_list

def func(seqs,oplist,debug=False):
    
    tmp_list=["1","2","3","4","5","6","7","8","9"]
    #すでにカッコで囲まれた式のリスト
    
    tmp_last_list=[1,2,3,4,5,6,7,8,9]
    #リストの各項目の最小値のリスト
    
    for j in range (0,len(seqs)):
        
        last_num=seqs[j]+1
        #今回入れる演算子の直前の位置にある数字
        #6と7の間に+を入れる場合、last_num=6
        
        next_first_num=last_num+1
        #今回入れる演算子の直後の位置にある数字
        #6と7の間に+を入れる場合、next_first_num=7
        
        for k in range(0,len(tmp_last_list)):
            
            if tmp_last_list[k]==next_first_num:
                
                last_num_list_num=k-1
                #last_num_list_numはlast_numがtmp_list配列に存在する位置である
                #例えば、last_num=6でtmp_list=["0","(1+(2+3))","4","(5*6)","7","8","9"]のときlast_num_list_num=3
                #last_numはtmp_last_listに存在しないことが多い
                #例えば、今回の場合、tmp_last_list=[0,1,4,5,7,8,9]となり、last_numはtmp_last_listに存在しない
                #一方、next_first_num(この例の場合は7)は必ずtmp_last_listに存在する
                #よってnext_first_numをtmp_last_listから探し、その位置の1つ手前をlast_num_list_numとする
                
        if debug:
            print("tmp_list:"+str(tmp_list))
            print("tmp_last_list:"+str(tmp_last_list))
            print("last_num:"+str(last_num))
            print("next_first_num:"+str(next_first_num))
            print("put "+oplist[last_num-1] +" between " +str(last_num)+" and "+str(next_first_num))
            print("last_num_list_num:"+str(last_num_list_num))
            print("make next lists")
        
        
        
        #last_num_list_numより前のtmp_listの項目はそのまま保持
        
        new_tmp_list=[]
        new_tmp_last_list=[]
        for m in range(0,last_num_list_num):
            new_tmp_list.append(tmp_list[m])
            new_tmp_last_list.append(tmp_last_list[m])
            
        if debug:
            print(new_tmp_list)
            print(new_tmp_last_list)
        
        
        #配列中のlast_num_list_numと(last_num_list_num+1)に相当する要素を演算子を用いて結合

        new_content="("+tmp_list[last_num_list_num]+oplist[last_num-1]+tmp_list[last_num_list_num+1]+")"
        new_tmp_list.append(new_content)
        new_tmp_last_list.append(tmp_last_list[last_num_list_num])
        
        if debug:
            print(new_tmp_list)
            print(new_tmp_last_list)
        
        
        #配列中の(last_num_list_num+2)以降に相当する要素はそのまま保持

        for m in range(last_num_list_num+2,len(tmp_list)):
            new_tmp_list.append(tmp_list[m])
            new_tmp_last_list.append(tmp_last_list[m])   
            
        if debug:
            print(new_tmp_list)
            print(new_tmp_last_list)

        
        #tmp_list,tmp_last_listの更新
        
        tmp_list=new_tmp_list
        tmp_last_list=new_tmp_last_list
 

    return tmp_list[0]
                
good_result=[]

def main(csv_long_name,max_count=4**8,margin=0.00001):
    #本来max_countは4**8である
    global good_result, seq_list
    init_count=0
    count=init_count
    while count<=init_count+max_count:
        oplist=make_oplist(count)
        for i in range(0,len(seq_list)):
            if i%10000==0:
                strs="In " +str(count)+"/"+str(max_count)+" steps, "+str(i)+"/"+str(len(seq_list))+" has finished."
                logging.info("%s",strs)
            try:
                eval(func(seq_list[i],oplist))
            except SyntaxError:
                continue
            except ZeroDivisionError:
                continue
            res=eval(func(seq_list[i],oplist))
            error=res-100
            if abs(error)<margin:
                good_result.append(func(seq_list[i],oplist))
                with open(csv_long_name,'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([func(seq_list[i],oplist)])
                
        count+=1


main(csv_long_name)

good_result=set(good_result)
good_result=list(good_result)

def make_csv(csv_name):
    global good_result
    with open(csv_name,'a') as f:
        writer = csv.writer(f)
        writer.writerow(["function"])
        for i in range(len(good_result)):
            func=good_result[i]
            writer.writerow([func])
            
make_csv(csv_name)
