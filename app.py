from fastapi import FastAPI

app = FastAPI(title="Model 1 API")


@app.get("/")
def root():
    return {
        "model": "model-1",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
