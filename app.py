from fastapi import FastAPI
from ml.main_pipeline import full_pipeline
from ml.executor import execute_command

app = FastAPI()

@app.post("/process-command")
def process_command(data: dict):
    text = data.get("text", "")

    results = full_pipeline(text)   # now returns list

    actions = []

    for res in results:
        action = execute_command(res)
        actions.append(action)

    return {
        "ml_output": results,
        "actions": actions
    }