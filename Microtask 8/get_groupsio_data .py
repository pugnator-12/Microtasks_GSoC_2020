import argparse
import pandas as pd
import os
import json


class groupsio:
    """
    This is a class to read the enriched index of a groupsio repository and import the attributes uuid, project, project_1, origin,grimoirelab_creation_date, body and subject_analyzed to a CSV file.

    Attributes:
       index (string): index for which the CSV file has to be generated.
       csv_file (string): path of csv file .
       json_file (string): path of json file.
    """

    def __init__(self, index, csv_file, json_file):
        """
        The constructor for groupsio class.

        Parameters:
            index (string): index for which the CSV file has to be generated.
            csv_file (string): path of csv file .
        json_file (string): path of json file.
        """

        self.index = index
        self.csv_file = csv_file
        self.json_file = json_file

    def get_json(self):
        """
        The function executes elasticdump to get data for the index and stores it in the json file.
        """

        cm = "elasticdump --input=http://localhost:9200/" + \
            self.index+"/"+" --output="+self.json_file + " --type=data"
        os.system(cm)

    def get_csv(self):
        """
        The function extracts respective attributes from the json file and stores it in a dataframe which is further exported as a CSV file.
        """

        f = open(json_file, "r")
        data = json.load(f)
        subset = data["_source"]
        uuid = subset["uuid"]
        project = subset["project"]
        project_1 = subset["project_1"]
        origin = subset["origin"]
        grimoire_creation_date = subset["grimoire_creation_date"]
        body_extract = subset["body_extract"]
        Subject_analyzed = subset["Subject_analyzed"]

        myDict = {
            "uuid": uuid,
            "project": project,
            "project_1": project_1,
            "origin": origin,
            "grimoire_creation_date": grimoire_creation_date,
            "body_extract": body_extract,
            "Subject_analyzed": Subject_analyzed
        }

        df = pd.DataFrame(columns=['uuid', 'project', 'project_1', 'origin',
                                   'grimoire_creation_date', 'body_extract', 'Subject_analyzed'])
        df = df.append(myDict, ignore_index=True)
        df.to_csv(self.csv_file, index=False)

        print("Your csv file is ready!")


parser = argparse.ArgumentParser(
    description="generate csv file for given index")
parser.add_argument("-index", help="Enter the index for which you want to generate csv file",
                    dest="index", type=str, required=True)
parser.add_argument("-csv", help="Enter path of csv file",
                    dest="csv", type=str, required=True)
parser.add_argument("-json", help="Enter path of json file",
                    dest="json", type=str, required=True)

args = parser.parse_args()

index = args.index
csv_file = args.csv
json_file = args.json

obj = groupsio(index, csv_file, json_file)
obj.get_json()
obj.get_csv()
