#---------------------------------------------------------------------------
# Supporting scripts for making a general psf/pdb file

# Import modules

import os
import sys
import numpy
import re
import shutil
import glob

# Define headers for psf files

def psfgen_headers(fin,topname,outname):
    fin.write(';# headers and inputs \n')
    fin.write('package require psfgen \n')
    fin.write('%s\t %s\n' %('topology',topname))
    fin.write('%s\t %s\n' %('set outputname', outname))
              
    
def monomer_ratios(opt):

    if opt == 'A' || opt == 'a':

        # G:S = 0.78, H = 2 (A); pCA:FA = 6:32

        gsrat = 0.27
        
        optflag = 1
    
    elif opt == 'B' || opt == 'b':

        # H:G:S = 27:41:32 (B); pCA:FA = 1
        gmonrat = 0.27

        optflag = 1

    else:

        optflag = -1

    return optflag




def psfgen_postprocess(fin,basic_pdb):
    
    # outname is already there. no need again

    fin.write(';# Writing output \n')
    fin.write('regenerate angles dihedrals \n')
    fin.write('coordpdb %s\t%\n' %(basic_pdb,';# dimer pdb for 
    reference'))
    fin.write('guesscoord ;# guesses rest of the coordinates \n')
    fin.write('writepdb $outputname.pdb \n')
    fin.write('writepsf $outputnmae.psf \n')
    fin.write(';# exit')


def gencpy(dum_maindir,dum_destdir,fylname):

    srcfyl = dum_maindir + '/' + fylname

    if not os.path.exists(srcfyl):
        print('ERROR: ', srcfyl, 'not found')
        return

    desfyl = dum_destdir + '/' + fylname
    shutil.copy2(srcfyl,desfyl)
