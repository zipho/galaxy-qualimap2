#!/usr/bin/env python
from __future__ import print_function
import argparse
import os
from subprocess import check_call, CalledProcessError
import shutil
import sys


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
    parser.add_argument('--out_genome_file')
    parser.add_argument('--out_dir')
    parser.add_argument('--out_zip')
    parser.add_argument('--out_html')
    parser.add_argument('--out_results')
    parser.add_argument('--java_mem_size')

    args = parser.parse_args()
    print(args)

    qualimap_bamqc(
        args.input_file,
        args.out_genome_file,
        args.out_dir,
        args.java_mem_size
    )

    shutil.make_archive(
        'raw_data_qualimapReport',
        'zip',
        os.path.join(args.out_dir, 'raw_data_qualimapReport')
    )

    shutil.move("raw_data_qualimapReport.zip", args.out_zip)
    shutil.move(
        os.path.join(args.out_dir, "genome_results.txt"),
        args.out_results
    )
    shutil.move(
        os.path.join(args.out_dir, "qualimapReport.html"),
        args.out_html
    )

if __name__ == "__main__":
    main()
