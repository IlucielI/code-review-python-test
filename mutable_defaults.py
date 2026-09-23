from typing import List, Optional
import asyncio

# Vulnerable: mutable default argument retains items across multiple function calls
def append_to_audit_log(entry: str, log_list: List[str] = []) -> List[str]:
    log_list.append(entry) # BUG: shared state mutation across requests!
    return log_list

# Vulnerable: unawaited coroutine
async def send_telemetry_event(event_name: str):
    await asyncio.sleep(0.01)

def trigger_background_telemetry(event: str):
    send_telemetry_event(event) # BUG: coroutine created but never awaited or scheduled with asyncio.create_task!
