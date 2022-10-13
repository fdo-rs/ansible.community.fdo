from os import listdir, rename
PATH = '/home/lukawernig/FDO/Xlab/ansible_collections/community/fdo/playbooks/roles/'

def add():
    if i != 'rename.py':
        for i in listdir():
            rename(PATH + i, PATH + 'community.fdo.' + i)

def rem():
    for i in listdir():
        rename(PATH + i, PATH + i.replace("community.fdo.", ""))

rem()
