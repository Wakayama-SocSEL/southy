import sys
sys.path.append('../southy')
from utils import clone_project, delete_folder


clone_project('https://github.com/tomoya0318/tomoya0318.git')
delete_folder('../tmp')