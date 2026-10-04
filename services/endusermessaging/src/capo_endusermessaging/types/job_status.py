"""Generated from Smithy shape ``com.amazonaws.endusermessaging#JobStatus``."""

from typing import Literal, TypeAlias, cast

"""Processing status of an async job."""
JobStatus: TypeAlias = Literal[
    "SUCCESS",
    "PROCESSING",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobStatus) -> str:
    return value


def deserialize_json(data: str) -> JobStatus:
    return cast(JobStatus, data)
