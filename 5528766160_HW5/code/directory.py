# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         directory
# Description:  create a new folder
# Author:       Kuan-Hui Lin
# Date:         2020/5/12
# -------------------------------------------------------------------------------

import os
def create_directory(path):
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)