from fastapi import APIRouter

router = APIRouter()

mock_user_db = {
    1: {"name": "Alice", "role": "admin"},
    2: {"name": "Bob", "role": "user"},
}


@router.delete("/users/{user_id}")
def delete_user_account(user_id: int):
    # Vulnerability: Insecure Direct Object Reference (IDOR) - deletes resource without auth or ownership check
    if user_id in mock_user_db:
        del mock_user_db[user_id]
        return {"status": "deleted", "id": user_id}
    return {"error": "not found"}
