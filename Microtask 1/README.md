# Microtask #1

Set up Perceval to be executed from PyCharm.

## Development Purpose

* git clone [grimoirelab-perceval](https://github.com/chaoss/grimoirelab-perceval)

* Create a pycharm project .

* Add 'grimoirelab-perceval' to the project structure 

    ```
    file => settings => Project:<your project name> => Project structure => Add Content Root
    ```

    ![project_structure](./images/mt1_project_structure.png)

    ```
    => browse to the cloned 'grimoirelab-perceval' directory 
    ```

    ![add_perceval](./images/mt1_proj_struc_path.jpg)

    ```
    => Apply => Okay
    ```

    Refer the video 'project_structure.mp4' for this step. 

* Install its dependencies using -

    ```
    pip3 install -r <path to grimoirelab-perceval's requirements.txt> 
    ```

* Add configuration for running perceval.

    ```
    run => edit configurations
    ```
    
    ![config](./images/edit_config.png)

    ![add_config](./images/add_config.jpg)

    ```
    Script path - mention path to 'grimoirelab-perceval/bin/perceval.py' file.

    github <owner> <repo> --sleep-for-rate -t <github-token>
    ```

    ![config_details](./images/config_details.png)

    ```
    Apply => Okay
    ```

    Run 

    ![run](./images/locate_config.png)

    Output

    ![op](./images/mt1_op.png)


***

## For Exploration

* Create a Pycharm project

* Execute 
```
pip3 install perceval
``` 

* Verify installation using
```
perceval --help
```

![help](./images/perceval_help.png)

* Run script

```
perceval github <owner> <repo> --sleep-for-rate -t <github-token>
```

![run](./images/perceval_run.jpg)

***

### More on perceval [here](https://chaoss.github.io/grimoirelab-tutorial/perceval/intro.html) !
