from subprocess import call
import os


def create_folders(project_name):
    os.makedirs(project_name, exist_ok=True)
    call(['cd', project_name])
