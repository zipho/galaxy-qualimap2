#!/usr/bin/env python
from __future__ import print_function
import argparse
from subprocess import check_call, CalledProcessError
import shlex
import sys
import logging

log = logging.getLogger(__name__)


def qualimap_multi_bamqc(input_file, out_dir, jv_mem_size):
    #multi-bamqc -r -d ./bamlistinput.txt -outdir ./Kaust_kxdr/variants/qualimap -outformat PDF --java-mem-size=16G
    cmdline_str = "qualimap multi-bamqc -r -d {} -outdir {} -outformat PDF --java-mem-size={}".format(input_file,
                                                                                                      out_dir,
                                                                                                      jv_mem_size)
    cmdline = new_split(cmdline_str)
    try:
        check_call(cmdline)
    except CalledProcessError:
        print("Error running the qualimap multi bamqc", file=sys.stderr)


def new_split(value):
    lex = shlex.shlex(value)
    lex.quotes = '"'
    lex.whitespace_split = True
    lex.commenters = ''
    return list(lex)


def main():
    parser = argparse.ArgumentParser(description="Generate Bam Quality Statistics")
    parser.add_argument('--input_file')
    parser.add_argument('--out_dir', default="/tmp/bamstats")
    parser.add_argument('--java_mem_size', default="8G")

    args = parser.parse_args()

    qualimap_multi_bamqc(args.input_file, args.out_dir, args.java_mem_size)


if __name__ == "__main__": main()