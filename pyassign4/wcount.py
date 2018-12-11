#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Xuefeng Wang"
__pkuid__  = "1800011707"
__email__  = "wang-xuefeng@pku.edu.cn"
"""

import sys
from urllib.request import urlopen
import collections


def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    lines = lines.lower()
    for i in [',','.','!','?',':',';','/','—','"','(',')',"'s","'re","'ll","/r","/n","_","--"]:
        lines = lines.replace(i," ")
    words = lines.split()
    ct = collections.Counter(words)
    ans = ct.most_common(topn)
    for (a,b) in ans:
        print(a+'\t',b)
    pass

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    
    else:
        paras = sys.argv
        url = paras[1]
        try:
            book = urlopen(url)
            if len(paras) > 2:
                topn = int(paras[2])
        except Exception as err:
            print(err)
        else:
            lines = book.read().decode()
            book.close()
            try:
                wcount(lines, topn)
            except:
                wcount(lines)
