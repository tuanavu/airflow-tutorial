from __future__ import print_function

from datetime import datetime

from airflow import DAG
from airflow.models import Variable
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2019, 2, 15),
    'end_date': datetime(2019, 2, 15)    
}

dag = DAG('example_variables', 
    schedule_interval="@once", 
    default_args=default_args)


# Config variables
## Common
# var1 = "value1"
# var2 = [1, 2, 3]
# var3 = {'k': 'value3'}

## 3 DB connections called
# var1 = Variable.get("var1")
# var2 = Variable.get("var2")
# var3 = Variable.get("var3")

## Recommended way
dag_config = Variable.get("example_variables_config", deserialize_json=True)
var1 = dag_config["var1"]
var2 = dag_config["var2"]
var3 = dag_config["var3"]

start = DummyOperator(
    task_id="start",
    dag=dag
)

# To test this task, run this command:
# docker-compose run --rm webserver airflow test example_variables get_dag_config 2019-02-15
t1 = BashOperator(
    task_id="get_dag_config",
    bash_command='echo "{0}"'.format(dag_config),
    dag=dag,
)

# You can directly use a variable from a jinja template
## {{ var.value.<variable_name> }}

t2 = BashOperator(
    task_id="get_variable_value",
    bash_command='echo {{ var.value.var3 }} ',
    dag=dag,
)

## {{ var.json.<variable_name> }}
t3 = BashOperator(
    task_id="get_variable_json",
    bash_command='echo {{ var.json.example_variables_config.var3 }} ',
    dag=dag,
)

start >> [t1, t2, t3]