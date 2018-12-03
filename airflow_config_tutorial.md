## Curated list of blogs, tutorials and articles on Airflow:

* A great place to start [#use_cases](https://github.com/jghoman/awesome-apache-airflow#best-practices-lessons-learned-and-cool-use-cases)


## Submitting a Pull Request

1. Fork it.
2. Create a branch (`git checkout -b my_markup`)
3. Commit your changes (`git commit -am "Added Snarkdown"`)
4. Push to the branch (`git push origin my_markup`)
5. Open a [Pull Request][1]
6. Enjoy a refreshing Diet Coke and wait

## setting up an Airflow cluster 

**check Ubuntu version**

    lsb_release -a

Description:	Ubuntu 18.04.1 LTS

**give airflow a home dir**

    export AIRFLOW_HOME=~/airflow

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