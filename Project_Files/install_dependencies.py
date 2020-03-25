# python3 install_dependencies.py

import argparse
import os

parser = argparse.ArgumentParser(description="git clone repos in source folder")

f = open("dependencies_list", "r")
urls=[]
libs=[]
for x in f:
    # tp prevent 'https:' we use split (": ")
    (lib,link) = x.split(": ")
    lib = lib.strip()
    link = link.strip()
    urls.append(link)
    libs.append(lib)
f.close()

f = open("upstream", "r")
upstreams=[]
for x in f:
    (lib,link) = x.split(": ")
    link = link.strip()
    upstreams.append(link)
f.close()

os.mkdir("sources")

for i in range (0,len(urls)):
    upstream = upstreams[i]
    print("Cloning  " + libs[i] + " ...")
    command = "git clone " + urls[i] + " sources/" + libs[i]
    os.system(command)
    os.chdir('sources/' + libs[i])
    add_remote = "git remote add upstream " + upstream
    os.system(add_remote)
    os.chdir("../")
    os.chdir("../")

