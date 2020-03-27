# Microtask #8

Execute micro-mordred to collect and enrich data from a groupsio repository. You need to register to a group (e.g., https://lists.onap.org/g/main) and follow the instructions at https://github.com/chaoss/grimoirelab-sirmordred#groupsio. 

### Add the following to 'projects.json' file

```
[groupsio]
raw_index = groupsio_raw
enriched_index = groupsio_enriched
email = <email_id>
password = <password>
```

### Modify the configuration as follows

   ```
   micro.py --raw --enrich --cfg ./setup.cfg --backends groupsio
   ```

   ```
   micro.py --panels --cfg setup.cfg
   ```

### Finally run the configurations!

### Visit localhost:5601 for the results.

![dashboard](./images/mt8_1.png)

![op](./images/mt8_2.png)

![op](./images/mt8_3.png)

***

Then, write a script to read the enriched index and import the attributes uuid, project, project_1, origin, grimoirelab_creation_date, body and subject_analyzed to a CSV file. Import the obtained file to an excel sheet (in a manual or automatic way).

### Run the script using following command

```
python3 get_groupsio_data.py -index groupsio_enriched -csv <csv_file_path> -json <json_file_path>
```
> The file paths of csv and json are the locations where the respective generated files will be stored after running the script.

![script](./images/mt8_script_op.png)

Output csv file

![csv_file](./images/csv_file1.png)

![csv_file](./images/csv_file2.png)

***


