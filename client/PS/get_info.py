import os

parent_dir_name = (os.path.dirname(os.path.realpath(__file__)) + '\\')
proc = os.system('{}PsExec.exe -i -s -r aa powershell.exe {}get_soft.ps1'.format(parent_dir_name, parent_dir_name))
