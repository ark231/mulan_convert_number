#!/usr/bin/env python3
import sys

import argparse

from fractions import Fraction

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


def num_to_fraction(num:str)->Fraction:
    return Fraction(f"0.{num}")

def mulan_to_fraction(mulan:str)->Fraction:
    pass

def mudig_to_fraction(mudig:str)->Fraction:
    pass

def fraction_to_num(val:Fraction,precision:int)->str:
    return str(abs(val))[2:]

def fraction_to_mulan(val:Fraction,precision:int)->str:
    pass

def fraction_to_mudig(val:Fraction,precision)->str:
    assert val!=0.0
    sign=val/abs(val)
    abs_val=abs(val)
    result=""
    num_digs=0
    while abs_val>0.0 and num_digs<precision:
        dig=abs_val//Fraction(1,12)
        result+=CONS[int(dig)]+(chr(0x0305)if sign<0 else "")+chr(0x0323)
        num_digs+=1
        abs_val-=dig*Fraction(1,12)
        abs_val*=12
    return result


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("-f","--from",type=str,choices=["number","mulan","mulan-digits","mudig"],required=True)
    parser.add_argument("-t","--to",type=str,choices=["number","mulan","mulan-digits","mudig"],required=True)
    parser.add_argument("-p","--precision",type=int,default=12,help="maximum number of digits in fraction part of mulan/mudig")
    parser.add_argument("value",type=str)
    args=parser.parse_args()
    value=0
    if "."in args.value:
        int_part=args.value.split(".")[0]
        frac_part=args.value.split(".")[1]
    else:
        int_part=args.value
        frac_part=None
    match getattr(args,"from"):
        case "number":
            value=num_to_int(int_part)
            value+=0 if frac_part is None else num_to_fraction(frac_part)
        case "mulan":
            value=mulan_to_int(int_part)
            value+=0 if frac_part is None else mulan_to_fraction(frac_part)
        case "mulan-digits"|"mudig":
            value=mudig_to_int(int_part)
            value+=0 if frac_part is None else mudig_to_fraction(frac_part)
    result=""
    if value==0.0:
        sign=1
    else:
        sign=int(value/abs(value))
    if isinstance(value,Fraction):
        frac_part=(abs(value)%1)
        int_part=int(abs(value)-frac_part)
        int_part*=sign
        frac_part*=sign
    else:
        int_part=abs(value)
        frac_part=None
        int_part*=sign
    match args.to:
        case "number":
            result=f"{int_to_num(int_part)}{''if frac_part is None else f'.{fraction_to_num(frac_part,args.precision)}'}"
        case "mulan":
            result=f"{int_to_mulan(int_part)}{''if frac_part is None else f'{fraction_to_mulan(frac_part,args.precision)}'}"
        case "mulan-digits"|"mudig":
            result=f"{int_to_mudig(int_part)}{''if frac_part is None else f'{fraction_to_mudig(frac_part,args.precision)}'}"
    print(result)



if __name__ == "__main__":
    main()
