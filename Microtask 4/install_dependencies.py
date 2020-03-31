# python3 install_dependencies.py -choice install -file dependencies_list

import argparse
import os


class install_dependencies:
    """
    This is a class to install griomoirelab dependencies :
    grimoirelab-sirmordred
    grimoirelab-elk
    grimoirelab-graal
    grimoirelab-perceval
    grimoirelab-perceval-mozilla
    grimoirelab-perceval-opnfv
    perceval-puppet
    grimoirelab-perceval-puppet
    grimoirelab-sortinghat
    grimoirelab-sigils
    grimoirelab-kidash
    grimoirelab-toolkit
    grimoirelab-cereslib
    grimoirelab-manuscripts

    Attributes:
	    file_path:path of file having urls of dependencies.
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def generate_list_of_URL(self):
        """
        This function reads the file and generates a list of URLs and a list the respective dependency name.
        Returns:
            libs: list of dependency names.
            urls: list of dependency URLs.
        """
        f = open(self.file_path, "r")
        urls = []
        libs = []
        for x in f:
            # to prevent 'https:' we use split (": ")
            (lib, link) = x.split(": ")
            lib = lib.strip()
            link = link.strip()
            urls.append(link)
            libs.append(lib)
        f.close()
        return (libs, urls)

    def clone_forked(self):
        """
		The function ceates a "sources" directory and clones the grimoirelab dependency repos in it.
		"""
        print("First time installation.....")
        # Install dependencies from forked git repo
        os.mkdir("sources")
        libs, urls = self.generate_list_of_URL()

        for i in range(0, len(urls)):
            print("Cloning  " + libs[i] + " ...")
            command = "git clone " + urls[i] + " sources/" + libs[i]
            os.system(command)

    def update_repo(self):
        """
		The function adds upstream to the cloned repos and updates the repo with parent repo.
		"""
        print("Updating repos....")
        # Updates cloned repos from master
        libs, urls = self.generate_list_of_URL()
        for i in range(0, len(urls)):
            os.chdir('sources/' + libs[i])
            add_remote = "git remote add upstream " + urls[i]
            os.system(add_remote)
            cmd1 = "git fetch upstream"
            os.system(cmd1)
            cmd2 = "git rebase upstream/master"
            os.system(cmd2)
            cmd3 = "git push origin master --force"
            os.system(cmd3)

            os.chdir("../")
            os.chdir("../")


# For first time install - fork the respective repos and paste the URL of each repo(maintain spaces) as per the sample.
# For update - paste the URL of parent repo (maintain spaces) as per sample.

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="git clone repos in source folder")
    parser.add_argument("-choice", choices=['update', 'install'],
                        help="use 'update' if you have already installed the repos in sources folder else use 'install' for first time use.", dest="choice", type=str, required=True)
    parser.add_argument("-file", help="Enter the path of file having dependencies URL",
                        dest="file_path", type=str, required=True)

    args = parser.parse_args()

    choice = args.choice
    file_path = args.file_path

    obj = install_dependencies(file_path)

    if (choice == 'update'):
        obj.update_repo()

    elif (choice == 'install'):
        obj.clone_forked()
