# CHAOSS Microtasks


Microtasks for GSOC Idea : [Implement the Social Currency Metrics System in GrimoireLabs](https://github.com/chaoss/grimoirelab/issues/288)

***

0. Microtask #0

    Download PyCharm and get familiar with it (for instance, you can follow this tutorial).

    [Pycharm Installation](https://github.com/pugnator-12/Microtasks_GSoC_2020/tree/master/Microtask%200)

***

1. Microtask #1

    Set up Perceval to be executed from PyCharm.

    [Perceval in pycharm](https://github.com/pugnator-12/Microtasks_GSoC_2020/tree/master/Microtask%201)

***

2. Microtask #2

    Create a Python script to execute Perceval via its Python interface using the GitLab and GitHub backends. Feel free to select any target repository.

    [Script](https://github.com/pugnator-12/Microtasks_GSoC_2020/tree/master/Microtask%202)

***

3. Microtask #3

    Based on the JSON documents produced by Perceval and its source code, try to answer the following questions:

    * What is the meaning of the JSON attribute 'timestamp'?

    * What is the meaning of the JSON attribute 'updated_on'?

    * What is the meaning of the JSON attribute 'origin'?

    * What is the meaning of the JSON attribute 'category'?

    * How many categories do the GitHub and GitLab backends have?

    * What is the meaning of the JSON attribute 'uuid'?

    * What is the meaning of the JSON attribute search_fields?

    * What is stored in the attribute data of each JSON document produced by Perceval?

    Answers can be found [here](https://github.com/pugnator-12/Microtasks_GSoC_2020/tree/master/Microtask%203). 

***


4. Microtask #4

    Set up a dev environment to work on GrimoireLab. Have a look to https://github.com/chaoss/grimoirelab-sirmordred#setting-up-a-pycharm-dev-environment.

    Guidelines to set the environment can be found [here](https://github.com/pugnator-12/Microtasks_GSoC_2020/tree/master/Microtask%204).

***

5. Microtask #5

    Execute micro-mordred to collect, enrich and visualize data from Git and GitHub repositories.

    Execution can be found [here](https://github.com/pugnator-12/Microtasks_GSoC_2020/tree/master/Microtask%205).

***


6. Microtask #6

    Using the dev tools in Kibiter, create a query that counts the number of unique authors on a Git repository from 2018-01-01 until 2019-01-01.

    Query for elasticsearch can be found [here](https://github.com/pugnator-12/Microtasks_GSoC_2020/tree/master/Microtask%206)

***

7. Microtask #7

    Install and use elasticdump to download the mapping and data of an ElasticSearch index (it can be anyone created in Microtask 5).

    elasticdump execution can be found [here](https://github.com/pugnator-12/Microtasks_GSoC_2020/tree/master/Microtask%207).

***

8. Microtask #8

    Execute micro-mordred to collect and enrich data from a groupsio repository. You need to register to a group (e.g., https://lists.onap.org/g/main) and follow the instructions at https://github.com/chaoss/grimoirelab-sirmordred#groupsio. 
    
    Execution can be found [here](https://github.com/pugnator-12/Microtasks_GSoC_2020/tree/master/Microtask%208).
    
    Then, write a script to read the enriched index and import the attributes uuid, project, project_1, origin, grimoirelab_creation_date, body and subject_analyzed to a CSV file. Import the obtained file to an excel sheet (in a manual or automatic way).

    Script can be found [here](https://github.com/pugnator-12/Microtasks_GSoC_2020/blob/master/Microtask%208/groupsio.py).

***

9. Microtask #9

    Build a Data Table visualization in Kibiter (you can use the CHAOSS community dashboard) that shows for emails (mbox index) the text of emails (split row by Termbody_extract field).

    Execution can be found [here](https://github.com/pugnator-12/Microtasks_GSoC_2020/tree/master/Microtask%209).

***

10. Microtask #10

    Submit at least a PR to one of the GrimoireLab repositories to fix an issue, improve the documentation, etc.

    Fixed docker-compose yaml file for mariadb : [details](https://github.com/pugnator-12/Microtasks_GSoC_2020/tree/master/Microtask%2010).

***



