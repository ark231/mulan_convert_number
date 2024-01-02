#!/usr/bin/env python3
import sys

import argparse

CONS = "KGSZTDNHMRPB"

def num_to_int(num:str)->int:
    return int(num)

def mulan_to_int(mulan:str)->int:
    result = 0
    num_digree = len(mulan) / 3
    assert num_digree % 1 == 0
    for i in range(0, len(mulan), 3):
        result += CONS.index(mulan[i].upper()) * (12 ** (num_digree - i / 3 - 1))
    result = int(result)
    return result

def mudig_to_int(mudig:str)->int:
    pass

def int_to_num(val:int)->str:
    return str(val)

def int_to_mulan(val:int)->str:
    result = ""
    if val == 0:
        return "ket"
    sign = val / abs(val)
    tmp_value = abs(val)
    while tmp_value != 0:
        remainder = tmp_value % 12
        result = CONS[remainder] + "et" if sign>0 else "ap" + result
        tmp_value //= 12
    result = result[0].lower() + result[1:]
    return result

def int_to_mudig(val:int)->str:
    if val==0:
        return "K"
    result=""
    sign=val/abs(val)
    tmp_value = abs(val)
    while tmp_value != 0:
        remainder = tmp_value % 12
        result = CONS[remainder] + ("" if sign>0 else chr(0x0305))+ result
        tmp_value //= 12
    return result

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("-f","--from",type=str,choices=["number","mulan","mulan-digits","mudig"],required=True)
    parser.add_argument("-t","--to",type=str,choices=["number","mulan","mulan-digits","mudig"],required=True)
    parser.add_argument("-p","--precision",type=int,help="maximum number of digits in fraction part of mulan/mudig")
    parser.add_argument("value",type=str)
    args=parser.parse_args()
    value=0
    match getattr(args,"from"):
        case "number":
            value=num_to_int(args.value)
        case "mulan":
            value=mulan_to_int(args.value)
        case "mulan-digits"|"mudig":
            value=mudig_to_int(args.value)
    result=""
    match args.to:
        case "number":
            result=int_to_num(value)
        case "mulan":
            result=int_to_mulan(value)
        case "mulan-digits"|"mudig":
            result=int_to_mudig(value)
    print(result)



if __name__ == "__main__":
    main()
