Bigquery Github Trends
---

Example for building a data pipeline using Google Cloud BigQuery and Airflow.

## Setup

This example does assume you will have an Airflow Environment up and running. But first
a quick rundown of what you need:

* Running Airflow
* Create a service account (Cloud Console)
* Setup a Google Cloud Connection in Airflow
* Enter the config variables

### Running Airflow

- Check out the master branch of this tutorial
- Start the Airflow environment with docker

```
bash run_gcloud_example.sh
```

- Stop the Airflow environment when you are finished

```
bash stop_gcloud_example.sh
```

### Google Cloud Service Key

Go to the console:

![console](img/console_service_account.png?raw=true)

Create the service account. Make sure the JSON private key has Editor's rights:

![console](img/create_service_account.png?raw=true)

Also, the service account needs to have permission to access the GCS bucket and Bigquery dataset.

### Airflow Connection

After having the GCP key, you need to create a connection in `Admin -> Connections` using your key.

In Airflow you need to define the *my_gcp_conn* named connection to your project:

![console](img/airflow_connection.png?raw=true)

Supply the path to the downloaded private key, supply the *project_id* and define the
minimum scope of *https://www.googleapis.com/auth/cloud-platform*

### Enter the config variables

After connection has been set up, you can go to the [bigquery_github_trends DAG](../../gcloud-example/bigquery_github/bigquery_github_trends.py), and enter the value of config variables:
- __BQ_PROJECT__: the bigquery project you are working on
- __BQ_DATASET__: the bigquery dataset you are working on

### Test the DAG

After connection and config variables has been set up, you can now test and run your DAG. 

- Using the command below to test specific task in the DAG:

```
docker-compose -f docker-compose-gcloud.yml run --rm webserver airflow test [DAG_ID] [TASK_ID] [EXECUTION_DATE]
```

- Examples: 

```
# Task 1
docker-compose -f docker-compose-gcloud.yml run --rm webserver airflow test bigquery_github_trends bq_check_githubarchive_day 2018-12-01

# Task 2
docker-compose -f docker-compose-gcloud.yml run --rm webserver airflow test bigquery_github_trends bq_check_hackernews_full 2018-12-01
```
