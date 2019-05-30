#!/bin/bash
mkdir -p consensus_markers
cwd=$(pwd -P)
export PATH=${cwd}/../strainphlan_src:${PATH}
python2 ../strainphlan_src/sample2markers.py --ifn_samples sams/*.sam.bz2 \
                                             --input_type sam \
                                             --output_dir consensus_markers \
                                             --nprocs 10 | tee consensus_markers/log.txt
