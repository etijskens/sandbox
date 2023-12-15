# -*- coding: utf-8 -*-

"""
Package sandbox
=======================================

Top-level package for sandbox.
"""

__version__ = "0.0.0"


def tim():
    """"""
                   # build cloop: 3.877232 s
    timings = { 'cloop'      : 2.151362
              , 'numba cloop': 0.082121
              , 'cloopv'     : 0.035
              , 'cloopv1'    : 0.024925
              , 'cloopv1b'   : 0.014616
              }
    for k,v in timings.items():
        if k == 'cloop':
            vref = v
            print(f"{k}: {v}s")
        else:
            print(f"{k}: {v}s x{vref/v} x{vprev/v}")
        vprev = v

if __name__ == "__main__":
    tim()