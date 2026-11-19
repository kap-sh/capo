"""Generated from Smithy shape ``com.amazonaws.mediaconnect#AutoPidMapConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.pid


class AutoPidMapConfiguration(TypedDict, closed=True):
    start_pid: "capo_mediaconnect.types.pid.Pid"
    """<p>The first PID in the range for automatic PID assignment.</p>"""
    pids_per_program: "int"
    """<p>The number of PIDs in the range for automatic PID assignment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoPidMapConfiguration) -> dict:
    out: dict = {}
    out["startPid"] = value["start_pid"]
    out["pidsPerProgram"] = value["pids_per_program"]
    return out


def deserialize_json(data: dict) -> AutoPidMapConfiguration:
    out: AutoPidMapConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("startPid") is not None:
        out["start_pid"] = data["startPid"]
    else:
        out["start_pid"] = 0
    if data.get("pidsPerProgram") is not None:
        out["pids_per_program"] = data["pidsPerProgram"]
    else:
        out["pids_per_program"] = 0
    return out
