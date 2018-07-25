#!/usr/bin/env python
from __future__ import print_function
import argparse
from subprocess import check_call, CalledProcessError
import sys
import logging

log = logging.getLogger(__name__)


def qualimap_bamqc(bam_filename, genomecov_file, out_dir, jv_mem_size):
    qualimap_command = [
        "qualimap", "bamqc",
        "-bam " + bam_filename,
        "-oc " + genomecov_file,
        "-outdir " + out_dir,
        "--java-mem-size=" + jv_mem_size
    ]

    try:
        check_call(qualimap_command)
    except CalledProcessError:
        print("Error running the qualimap bamqc", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(
        description="Generate Bam Quality Statistics"
    )
    parser.add_argument('--input_file')
    parser.add_argument('--out_genome_file', default="genome_results.txt")
    parser.add_argument('--out_dir')
    parser.add_argument('--java_mem_size', default="8G")

    args = parser.parse_args()
    
    qualimap_bamqc(
        args.input_file,
        args.out_genome_file,
        args.out_dir,
        args.java_mem_size
    )


if __name__ == "__main__":
    main()
