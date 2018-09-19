"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz'):
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    #CleanFemResp(df)
    return df

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)

        
resp = ReadFemResp()
print(resp.pregnum.value_counts().sort_index())

caseid_chosen = int(input("enter case id: "))

preg = nsfg.ReadFemPreg()
preg_map = nsfg.MakePregMap(preg)
indices = preg_map[caseid_chosen]
print(preg.outcome[indices].values)

print(resp[resp.caseid==caseid_chosen].pregnum)