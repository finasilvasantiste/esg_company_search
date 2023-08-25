from prefect import flow

@flow
def hello_prefect():
    print('Hello prefect!')


if __name__ == "__main__":
    hello_prefect()