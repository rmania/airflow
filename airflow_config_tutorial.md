### setting up an Airflow cluster 

**check Ubuntu version**
`lsb_release -a` 
Description:	Ubuntu 18.04.1 LTS

**give airflow a home dir**
`export AIRFLOW_HOME=~/airflow`

**export ENV variables**
`export AIRFLOW_HOME=~/airflow`
`export AIRFLOW_GPL_UNIDECODE=yes` sublime install
`export SLUGIFY_USES_TEXT_UNIDECODE=yes` to be specified during all upgrades

**install the module** 
`pip3 install apache-airflow`

**start the web server**, default http://localhost:8080/admin/**
`airflow webserver -p 8080`

**start the scheduler**
`airflow scheduler`