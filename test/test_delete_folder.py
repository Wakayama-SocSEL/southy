import sys
from utils import delete_folder

delete_folder(f'{sys.path[-1]}/tmp')