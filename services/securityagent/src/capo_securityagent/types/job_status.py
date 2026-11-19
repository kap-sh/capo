"""Generated from Smithy shape ``com.amazonaws.securityagent#JobStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>Status of a pentest job.</p>"""
JobStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "STOPPING",
    "STOPPED",
    "PAUSING",
    "PAUSED",
    "FAILED",
    "COMPLETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobStatus) -> str:
    return value


def deserialize_json(data: str) -> JobStatus:
    return cast(JobStatus, data)
