import sys
sys.path.append('../southy')
from utils import delete_folder

delete_folder(f'{sys.path[-1]}/tmp')