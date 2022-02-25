Airflow tutorial
---

This is the code for [Apache Airflow Tutorials](https://www.youtube.com/playlist?list=PLYizQ5FvN6pvIOcOd6dFZu3lQqc6zBGp2) playlist by Tuan Vu on Youtube

## Contents

| Part |      Title                | Git Tag |
|------|---------------------------|---------|
| 1    | [Introduction to Apache Airflow](https://youtu.be/AHMm1wfGuHE) ([blog post](https://www.applydatascience.com/airflow/airflow-tutorial-introduction/)) | [v0.1](https://github.com/tuanavu/airflow-tutorial/tree/v0.1) |
| 2    | [Set up airflow environment with docker](https://youtu.be/vvr_WNzEXBE) ([blog post](https://www.applydatascience.com/airflow/set-up-airflow-env-with-docker/)) | [v0.2](https://github.com/tuanavu/airflow-tutorial/tree/v0.2) |
| 3    | [Set up airflow environment using Google Cloud Composer](https://youtu.be/ld6JO3MiuPQ) ([blog post](https://www.applydatascience.com/airflow/set-up-airflow-with-google-composer/)) | N/A |
| 4    | [Writing your first pipeline](https://youtu.be/43wHwwZhJMo) ([blog post](https://www.applydatascience.com/airflow/writing-your-first-pipeline/)) | N/A |
| 5    | [Airflow concept](https://youtu.be/4rQSa2zEWfw) ([blog post](https://www.applydatascience.com/airflow/airflow-concept/)) | N/A |
| 6    | [Build a data pipeline using Google Cloud Bigquery](https://youtu.be/wAyu5BN3VpY) ([blog post](https://www.applydatascience.com/airflow/bigquery-pipeline-airflow/)) | [v0.6](https://github.com/tuanavu/airflow-tutorial/tree/v0.6) |
| 7    | [Airflow variables](https://youtu.be/bHQ7nzn0j6k) ([blog post](https://www.applydatascience.com/airflow/airflow-variables/)) | [v0.7](https://github.com/tuanavu/airflow-tutorial/tree/v0.7) |


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

- Clone this repo
- Install the prerequisites
- Run the service
- Check http://localhost:8080
- Done! :tada:

### Prerequisites

- Install [Docker](https://www.docker.com/)
- Install [Docker Compose](https://docs.docker.com/compose/install/)
- Following the Airflow release from [Python Package Index](https://pypi.python.org/pypi/apache-airflow)

### Usage

Run the web service with docker

```
docker-compose up -d

# Build the image
# docker-compose up -d --build
```

Check http://localhost:8080/

- `docker-compose logs` - Displays log output
- `docker-compose ps` - List containers
- `docker-compose down` - Stop containers

## Other commands

If you want to run airflow sub-commands, you can do so like this:

- `docker-compose run --rm webserver airflow list_dags` - List dags
- `docker-compose run --rm webserver airflow test [DAG_ID] [TASK_ID] [EXECUTION_DATE]` - Test specific task

If you want to run/test python script, you can do so like this:
- `docker-compose run --rm webserver python /usr/local/airflow/dags/[PYTHON-FILE].py` - Test python script

## Connect to database

If you want to use Ad hoc query, make sure you've configured connections:
Go to Admin -> Connections and Edit "postgres_default" set this values:
- Host : postgres
- Schema : airflow
- Login : airflow
- Password : airflow


## Credits

- [Apache Airflow](https://github.com/apache/incubator-airflow)
- [docker-airflow](https://github.com/puckel/docker-airflow/tree/1.10.0-5)
