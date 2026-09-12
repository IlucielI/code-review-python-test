from fastapi import APIRouter
from fastapi.responses import RedirectResponse

router = APIRouter()


@router.get("/redirect")
def redirect_to_url(url: str):
    # Vulnerability: Open redirect without host validation
    return RedirectResponse(url=url)
