from prefect import flow, task


@task
def hello_task():
	print('Hello task!')

@flow
def hello_prefect():
    print('Hello flow!')
    hello_task()
    print('Bye flow!')


if __name__ == "__main__":
    hello_prefect()