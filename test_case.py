#coding:utf-8

import os,time
#列出某个文件夹下的所有case,这里用的是python，
#所有py 文件运行一次后会生成一个pyc 的副本
caselist =os.listdir(u'D:\\MyWorkpace\\tuyoumi\\src\\test_case')
for a in caselist:
    s =a.split('.')[1]   #选取后缀名为py 的文件
    if s =='py':
        #此处执行dos 命令并将结果保存到log.txt
        #CMD直接调用DOS命令
        os.system('cmd.exe /k python test_case\\%s  >>log.txt 2>&1' %a)
        print "请输入 exit，并回车"

#以上脚本还有不足，必须要在编辑器输出窗口手动加入DOS的退出命令：exit，按enter之后才能执行下一个case
#该脚本虽然只是实现了脚本、执行、log分离，但是并没有很好的实现批量执行