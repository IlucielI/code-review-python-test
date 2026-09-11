from fastapi import FastAPI

app = FastAPI(
    title="Benchmark Python API",
    version="1.0.0",
    description="Python FastAPI benchmark service for automated code review validation",
)


@app.get("/healthz")
def health_check():
    return {"status": "ok", "service": "code-review-python-test"}
