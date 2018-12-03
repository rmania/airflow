## Curated list of blogs, tutorials and articles on Airflow:

* A great place to start [airflow_best_practices](https://github.com/jghoman/awesome-apache-airflow#best-practices-lessons-learned-and-cool-use-cases)

* data testing in 7 steps with Airflow [datas-inferno-7-circles-of-data-testing-hell-with-airflow](https://medium.com/wbaa/datas-inferno-7-circles-of-data-testing-hell-with-airflow-cef4adff58d8)


## Submitting a Pull Request

1. Fork it (or clone)
2. Create a branch (`git checkout -b my_airflow`)
3. Commit your changes (`git commit -am "Added airflow feature"`)
4. Push to the branch (`git push origin my_airflow`)
5. Open a [Pull Request][1]
6. Enjoy a drink

## setting up an Airflow cluster 

**check Ubuntu version**

    lsb_release -a

Mine is : Ubuntu 18.04.1 LTS

**airflow needs a home, ~/airflow is the default**

    export AIRFLOW_HOME=~/airflow

**create workspace dir + virtualenv**

	$ cd ~/airflow
	$ virtualenv -p `which python3` venv
	$ source venv/bin/activate
	(venv) $ 

**export ENV variables**

    export AIRFLOW_HOME=~/airflow
    export AIRFLOW_GPL_UNIDECODE=yes
    export SLUGIFY_USES_TEXT_UNIDECODE=yes 

**install the module** 

    pip3 install apache-airflow

**start the web server**, default http://localhost:8080/admin/**

    airflow webserver -p 8080

**start the scheduler**

    airflow scheduler

**Initialize the database**

Defaults to SQLite option. Subpackages can be installed depending on what will be useful in your environment. For instance, if you don’t need connectivity with Postgres, you won’t have to go through the trouble of installing the postgres-devel yum package, or whatever equivalent applies on the distribution you are using.

To see list of dependent extra packages  [airflow_extra_packaes](https://airflow.apache.org/installation.html)

	airflow initdb
