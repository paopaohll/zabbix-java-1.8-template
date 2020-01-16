#!/usr/bin/python
#_*_ coding:utf-8 _*_

import sys
import os
import json


def discover():
    d = {}
    d['data'] = []
    with os.popen('/usr/bin/jps -l | grep -v Jps') as pipe:
        for i in pipe:
            res = i.split(" ")
            if res[1].replace("\n","").endswith(".jar"):
                pid, name = res[0], res[1].replace("\n","")
                info = {}
                info['{#PID}'] = pid.replace("\n", "")
                info['{#JARNAME}'] = name.replace("\n", "")
                d['data'].append(info)
        print(json.dumps(d))


def threads_number(pid):
    cmd = 'ps -eLf | grep %s | grep -v grep | wc -l' % pid
    result = os.popen(cmd).read().replace("\n", "")
    print(result)


def cpu_usage(pid):
    cmd = "ps aux|grep '%s'|grep -v 'grep'|grep -v 'ProcessCPU.py'|awk '{sum+=$3}; END{print sum}'" % pid
    cpu_cmd = "cat /proc/cpuinfo| grep 'processor'| wc -l"
    cpu_use = os.popen(cmd).read().replace("\n", "")
    cpu_num = os.popen(cpu_cmd).read().replace("\n", "")
    res = float(cpu_use) / float(cpu_num)
    print('%0.2f' % res)


def mem_usage(pid):
    cmd = "ps aux|grep '%s'|grep -v 'grep'|grep -v 'Processmemory.py'|awk '{sum+=$6}; END{print sum}'" % pid
    mem_use = os.popen(cmd).read().replace("\n", "")
    # 将结果单位换算：kb-> Gb
    res = float(mem_use) / 1024.0**2
    print('%0.2f' % res)


def vm_class_static(pid, target):
    dict = {"Loaded": 1, "Bytes": 2, "Unloaded": 3, "Bytes": 4, "Time": 5}
    target = dict[target]
    cmd = "jstat -class %s | awk 'NR>1{print $%s}'" % (pid, target)
    res = os.popen(cmd).read().replace("\n", "")
    print(res)


def vm_compiler_static(pid, target):
    dict = {"Compiled": 1, "Failed": 2, "Invalid": 3, "Time": 4, "FailedType": 5, "FailedMethod": 6}
    target = dict[target]
    if target == 6:
        cmd = "jstat -compiler %s | awk 'NR>1{print $6,$7}'" % (pid)
        res = os.popen(cmd).read().replace("\n", "")
        print(res)
    else:
        cmd = "jstat -class %s | awk 'NR>1{print $%s}'" % (pid, target)
        res = os.popen(cmd).read().replace("\n", "")
        print(res)


def vm_gc_static(pid, target):
    dict = {"S0C": 1, "S1C": 2, "S0U": 3, "S1U": 4, "EC": 5, "EU": 6, "OC": 7, "OU": 8, 
            "MC": 9, "MU": 10, "CCSC": 11, "CCSU": 12, "YGC": 13, "YGCT": 14, "FGC": 15, 
            "FGCT": 16, "GCT": 17}
    target = dict[target]
    cmd = "jstat -gc %s | awk 'NR>1{print $%s}'" % (pid, target)
    res = os.popen(cmd).read().replace("\n", "")
    print(res)


def vm_gcutil_static(pid, target):
    dict = {"S0": 1, "S1": 2, "E": 3, "O": 4, "M": 5, "CCS": 6, "YGC": 7, "YGCT": 8, 
            "FGC":9, "FGCT": 10, "GCT": 11}
    target = dict[target]
    cmd = "jstat -gcutil %s | awk 'NR>1{print $%s}'" % (pid, target)
    res = os.popen(cmd).read().replace("\n", "")
    print(res)


def vm_gccapacity_static(pid, target):
    dict = {"NGCMN": 1, "NGCMX": 2, "NGC": 3, "S0C": 4, "S1C": 5, "EC": 6, "OGCMN": 7, 
            "OGCMX": 8, "OGC": 9, "OC": 10, "MCMN": 11, "MCMX": 12, "MC": 13, "CCSMN": 14, 
            "CCSMX": 15, "CCSC": 16, "YGC": 17, "FGC": 18}
    target = dict[target]
    cmd = "jstat -gccapacity %s | awk 'NR>1{print $%s}'" % (pid, target)
    res = os.popen(cmd).read().replace("\n", "")
    print(res)


def vm_gcnew_static(pid, target):
    dict = {"S0C": 1, "S1C": 2, "S0U": 3, "S1U": 4, "TT": 5, "MTT": 6, "DSS": 7, "EC": 8, 
            "EU": 9, "YGC": 10, "YGCT": 11}
    target = dict[target]
    cmd = "jstat -gcnew %s | awk 'NR>1{print $%s}'" % (pid, target)
    res = os.popen(cmd).read().replace("\n", "")
    print(res)


def vm_gcnewcapacity_static(pid, target):
    dict = {"NGCMN": 1, "NGCMX": 2, "NGC": 3, "S0CMX": 4, "S0C": 5, "S1CMX": 6, "S1C": 7, 
            "ECMX": 8, "EC": 9, "YGC": 10, "FGC": 11}
    target = dict[target]
    cmd = "jstat -gcnewcapacity %s | awk 'NR>1{print $%s}'" % (pid, target)
    res = os.popen(cmd).read().replace("\n", "")
    print(res)


def vm_gcold_static(pid, target):
    dict = {"MC": 1, "MU": 2, "CCSC": 3, "CCSU": 4, "OC": 5, "OU": 6, "YGC": 7, "FGC": 8, "FGCT": 9, "GCT": 10}
    target = dict[target]
    cmd = "jstat -gcold %s | awk 'NR>1{print $%s}'" % (pid, target)
    res = os.popen(cmd).read().replace("\n", "")
    print(res)


def vm_gcoldcapacity_static(pid, target):
    dict = {"OGCMN": 1, "OGCMX": 2, "OGC": 3, "OC": 4, "YGC": 5, "FGC": 6, "FGCT": 7, "GCT": 8}
    target = dict[target]
    cmd = "jstat -gcoldcapacity %s | awk 'NR>1{print $%s}'" % (pid, target)
    res = os.popen(cmd).read().replace("\n", "")
    print(res)


def vm_gcmetacapacity_static(pid, target):
    dict = {"MCMN": 1, "MCMX": 2, "MC": 3, "CCSMN": 4, "CCSMX": 5, "CCSC": 6, "YGC": 7, "FGC": 8, 
            "FGCT": 9, "GCT": 10}
    target = dict[target]
    cmd = "jstat -gcmetacapacity %s | awk 'NR>1{print $%s}'" % (pid, target)
    res = os.popen(cmd).read().replace("\n", "")
    print(res)


if __name__ == '__main__':
    num = len(sys.argv)
    if num > 3:
        item, target, pid = sys.argv[1], sys.argv[2], sys.argv[3]
        if item == "class":
            vm_class_static(pid, target)
        elif item == "compiler":
            vm_compiler_static(pid, target)
        elif item == "gc":
            vm_gc_static(pid, target)
        elif item == "gcutil":
            vm_gcutil_static(pid, target)
        elif item == "gccapacity":
            vm_gccapacity_static(pid, target)
        elif item == "gcnew":
            vm_gcnew_static(pid, target)
        elif item == "gcnewcapacity":
            vm_gcnewcapacity_static(pid, target)
        elif item == "gcold":
            vm_gcold_static(pid, target)
        elif item == "gcoldcapacity":
            vm_gcoldcapacity_static(pid, target)
        else:
            vm_gcmetacapacity_static(pid, target)
    elif num > 2:
        arg, pid = sys.argv[1], sys.argv[2]
        if arg == 'cpu':
            cpu_usage(pid)
        elif arg == 'mem':
            mem_usage(pid)
        else:
            threads_number(pid)
    else:
        discover()
