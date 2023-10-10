#########################################
# wrapper for rule: basecall
#########################################
import os
import sys
import math
import subprocess
import re
from snakemake.shell import shell

shell.executable("/bin/bash")
#TODO logging
config_version_map = {
        'dna':'10.4.1_e8.2',
        'rna':'9.4.1'
}
flowcell_suffix_map = {
        'None':'',
        'prom':'_prom',
        'mk1c':'_mk1c'
}
config_version = config_version_map[snakemake.params.data_type]
command = "./"+str(snakemake.params.guppy_version)+\
        "/bin/guppy_basecaller"+\
        " --input_path all_reads/"+ str(snakemake.wildcards.reads_folder)+\
        " --save_path basecalling_output/"+str(snakemake.wildcards.reads_folder)+\
        " --config " + str(snakemake.params.guppy_version) + "/data/" + str(snakemake.params.data_type)+\
        "_r" + config_version + "_" + str(snakemake.params.bps) + "bps_" + str(snakemake.params.quality)+\ 
        flowcell_suffix_map[snakemake.params.flowcell] +".cfg"

shell(command)

