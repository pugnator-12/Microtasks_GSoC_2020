# python3 git_script.py -backend gitlab -repo silentprogrammers/vacation_system -t <gitlab_token> -f gitlab_op.output
# python3 git_script.py -backend github -repo Sentdex/sentdebot -t <github_token> -f github_op.output

import argparse
from perceval.backends.core.github import GitHub
from perceval.backends.core.gitlab import GitLab
import json


class PercevalBackends:
    """
    This is a class to is used to execute Perceval using the GitLab and GitHub backends.
    Attributes:
        owner (string): owner of the repo.
        repo (string):  name of the repo to be fetched.
        token (string): GitLab token or GitHub personal access token.
        op_file (string): path of file where fetched items are to be stored.
        backend (string): name of the backend (gitlab / github)
    """

    def __init__(self, owner, repo, token, op_file, backend):
        self.owner = owner
        self.repo = repo
        self.token = token
        self.op_file = op_file
        self.backend = backend

    def write_to_file(self, obj):

        """
        :param obj: perceval json object to be written to the output file.
        """

        f = open(self.op_file, "w")
        f.write("Details for : " + self.repo + "\n")
        f.close()

        f = open(self.op_file, "a")
        items = obj.fetch()
        for item in items:
            json_dump = json.dumps(item, indent=4)
            f.write(json_dump)
            f.write("\n")
        f.close()

    def __get_gitlab_data(self):
        gitlabObj = GitLab(
            owner=self.owner, repository=self.repo, api_token=self.token)
        return gitlabObj

    def __get_github_data(self):
        gitlabObj = GitHub(
            owner=self.owner, repository=self.repo, api_token=[self.token])
        return gitlabObj

    def store_data(self):
        """
        Fetches objects for the respective backends and executes storage of perceval objects in respective json file.
        """
        if (self.backend == "gitlab"):
            perceval_obj = self.__get_gitlab_data()

        elif (self.backend == "github"):
            perceval_obj = self.__get_github_data()

        self.write_to_file(perceval_obj)
        print("Done!!")


parser = argparse.ArgumentParser(
    description="perceval for github and gitlab backends")
parser.add_argument("-backend", choices=['github', 'gitlab'],
                    help="enter backend(gitlab/github)", dest="backend", type=str, required=True)
parser.add_argument("-repo", help="enter repo (owner/repo)",
                    dest="repo", type=str, required=True)
parser.add_argument("-t", help="github/gitlab personal access token",
                    dest="token", type=str, required=True)
parser.add_argument("-f", help="file to save output",
                    dest="file_add", type=str, required=True)

args = parser.parse_args()

r = args.repo
t = args.token
f_add = args.file_add
backend = args.backend

(owner, repo) = r.split("/")

perceval_obj = PercevalBackends(owner, repo, t, f_add, backend)

perceval_obj.store_data()