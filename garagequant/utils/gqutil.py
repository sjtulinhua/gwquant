# encoding: UTF-8

"""

private utils

"""
from threading import currentThread


def gq_hosting_thread_info(snippet):
    debug_trace('\n* ' + snippet + 'revent loop (__run_loop) in thread:')
    debug_trace('\t - ' + currentThread().name)
    debug_trace('\t - ' + str(currentThread().ident) + '\n')


def debug_trace(strings):
    print(strings)
    # pass