#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: JacobSamro
# @Date:   2015-04-26 23:09:28
# @Last Modified by:   JacobSamro
# @Last Modified time: 2015-04-26 23:09:31
from definitions import *

def mapText(data):
    txts = TXT();
    txts =  [txts for txts in dir(txts) 
              if not txts.startswith('__')]

    var1 = TXT();
    obj_found = False
    for txt in txts:
        #print(var1.__getitem__(txt))
        if(data in var1.__getitem__(txt)):
            obj_found = True
            print(txt)

    if(obj_found == False):
        print('repeat')

mapText('what is your name')