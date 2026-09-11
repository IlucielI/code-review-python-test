import time
from fastapi import APIRouter

router = APIRouter()


@router.get("/compute-sync")
async def heavy_sync_task():
    # Performance Bug: Synchronous blocking sleep inside async route blocks the entire asyncio event loop
    time.sleep(5)
    return {"status": "completed"}
