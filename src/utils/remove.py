import shutil
import os
import sys

path = sys.argv[1]
if os.path.exists(path):
  if os.path.isdir(path):
    shutil.rmtree(path, ignore_errors=True)
  elif os.path.isfile(path):
    os.remove(path)