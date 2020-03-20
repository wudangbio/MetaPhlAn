import setuptools
from setuptools.command.install import install
from io import open
import sys, shutil, os, zipfile, tarfile, subprocess, tempfile, re, time
from urllib.request import urlretrieve

from metaphlan import download_unpack_zip

install_requires = ['numpy', 'h5py', 'biom-format', 'biopython', 'pandas', 'scipy', 'requests', 'dendropy', 'pysam']
setup_requires = ['numpy', 'cython']

if sys.version_info[0] < 3:
    sys.stdout.write('MetaPhlAn requires Python 3 or higher. Please update you Python installation')

class Install(install):
    def run(self):  
        install.run(self)
        print('Installing cmseq')

        current_install_folder=None
        for item in os.listdir(self.install_lib):
            full_path_item=os.path.join(self.install_lib, item)
            if os.path.isdir(full_path_item):
                if "metaphlan" == item:
                    current_install_folder=full_path_item
                    break
        
        cmseq_repo = "https://github.com/SegataLab/cmseq/archive/master.zip"
        cmseq_path = os.path.join(current_install_folder, "utils")
        download_unpack_zip(cmseq_repo, "cmseq.zip", cmseq_path, "cmseq")
        if(os.path.exists(os.path.join(cmseq_path,'cmseq-master'))):
            shutil.move(os.path.join(cmseq_path,'cmseq-master'), os.path.join(cmseq_path,'cmseq'))
        else:
            print("WARNING: Unable to install cmseq")


setuptools.setup(
    name='MetaPhlAn',
    version='3.0',
    author='Francesco Beghini',
    author_email='francesco.beghini@unitn.it',
    url='http://github.com/biobakery/MetaPhlAn/',
    license='LICENSE.txt',
    packages=setuptools.find_packages(),
    package_data = { 'MetaPhlAn' : [
        'metaphlan/utils/*'
    ]},
    cmdclass={
        'biocondainstall': Install
    },
    entry_points={
        'console_scripts': [
            'metaphlan = metaphlan.metaphlan:main',
            'strainphlan = metaphlan.strainphlan:main',

            'add_metadata_tree.py = metaphlan.utils.add_metadata_tree:main',
            'extract_markers.py = metaphlan.utils.extract_markers:main',
            'merge_metaphlan_tables.py  = metaphlan.utils.merge_metaphlan_tables:main',
            'plot_tree_graphlan.py = metaphlan.utils.plot_tree_graphlan:main',
            'read_fastx.py = metaphlan.utils.read_fastx:main',
            'sample2markers.py = metaphlan.utils.sample2markers:main',
            'strain_transmission.py = metaphlan.utils.strain_transmission:main',
        ]
    },
    description='MetaPhlAn is a computational tool for profiling the composition of microbial communities (Bacteria, Archaea and Eukaryotes) from metagenomic shotgun sequencing data (i.e. not 16S) with species-level. With the newly added StrainPhlAn module, it is now possible to perform accurate strain-level microbial profiling.',
    long_description=open('README.md').read(),
    install_requires=install_requires,
    setup_requires = setup_requires
)