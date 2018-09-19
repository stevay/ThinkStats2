"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import sys
from operator import itemgetter

import first
import thinkstats2


def Mode(hist):
    """Returns the value with the highest frequency.

    hist: Hist object

    returns: value from Hist
    """
    highest_freq = 0
    mode_val = 0
    for val, freq in hist.Items():
        if freq > highest_freq:
            highest_freq = freq
            mode_val = val
    
    return mode_val


def AllModes(hist):
    """Returns value-freq pairs in decreasing order of frequency.

    hist: Hist object

    returns: iterator of value-freq pairs
    """
    new_list = []
    for val in hist:
        new_list.append([val,hist.Freq(val)])
        
    return new_list

def WeightDifference(firsts, others):
    
    import numpy as np
    
    print('Mean difference: ',firsts.totalwgt_lb.mean()-others.totalwgt_lb.mean())
    
    # calculate Cohen Effect Size
    firsts_var = firsts.totalwgt_lb.var()
    others_var = others.totalwgt_lb.var()
    firsts_len = len(firsts.totalwgt_lb)
    others_len = len(others.totalwgt_lb)
    firsts_mean = firsts.totalwgt_lb.mean()
    others_mean = others.totalwgt_lb.mean()
    
    pooled_var = (firsts_len*firsts_var + others_len*others_var) / (firsts_len+others_len)
    mean_diff = firsts_mean - others_mean
    d = mean_diff / np.sqrt(pooled_var)
    print('Cohen Effect Size: ', d)

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    live, firsts, others = first.MakeFrames()
    hist = thinkstats2.Hist(live.prglngth)

    # test Mode    
    mode = Mode(hist)
    print('Mode of preg length', mode)
    assert mode == 39, mode

    # test AllModes
    modes = AllModes(hist)
    assert modes[0][1] == 4693, modes[0][1]

    for value, freq in modes[:5]:
        print(value, freq)
    
    # check weight difference
    WeightDifference(firsts,others)

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
