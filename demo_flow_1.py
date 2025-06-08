from prefect import flow, task

@task
def long_running_task(duration: int = 30):
    import time
    time.sleep(duration)
    return "Operation completed successfully"

@flow
def main_flow(duration: int = 30):
    return long_running_task(duration)
