# python3 mt2_gitlab.py -repo marsat/CTparental -t z2SDNdQ2P3fD_XeFM_fp -f gitlab_mt2.output
# python3 mt2_gitlab.py -repo nsnam/ns-3-dev -t z2SDNdQ2P3fD_XeFM_fp -f gitlab_mt2_1.output

import argparse
from perceval.backends.core.gitlab import GitLab
import json

parser = argparse.ArgumentParser(description="perceval for gitlab")
parser.add_argument("-repo",help="enter repo (owner/repo)",dest="repo",type=str,required=True)
parser.add_argument("-t",help="gitlab personal access token",dest="token",type=str,required=True)
parser.add_argument("-f",help="file to save output",dest="file_add",type=str,required=True)

args=parser.parse_args()

r = [args.repo][0]
t = [args.token][0]
f_add = [args.file_add][0]

f = open(f_add, "w")
f.write("Details for : " + r + "\n")
f.close()

(owner,repo) = r.split("/")

gitObj= GitLab(owner=owner, repository=repo, api_token=args.token)

f = open(f_add, "a")

items = gitObj.fetch()

for item in items:
    json_dump = json.dumps(item,indent=4)
    f.write(json_dump)
    f.write("\n")
f.close()



