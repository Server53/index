# This module makes importing from src possible
# and changes cwd to project root, 
# as all scripts intended to run from project root

import os
import pathlib
import sys

scripts_dir = pathlib.Path(__file__).parent
outer_dir = scripts_dir.parent

os.chdir(outer_dir)
sys.path.append(str(outer_dir))
