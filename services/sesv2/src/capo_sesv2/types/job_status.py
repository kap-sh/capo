"""Generated from Smithy shape ``com.amazonaws.sesv2#JobStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a job.</p> <ul> <li> <p> <code>CREATED</code> – Job has just been created.</p> </li> <li> <p> <code>PROCESSING</code> – Job is processing.</p> </li> <li> <p> <code>COMPLETED</code> – Job has completed processing successfully.</p> </li> <li> <p> <code>FAILED</code> – An error occurred during processing.</p> </li> <li> <p> <code>CANCELLED</code> – Job has been canceled.</p> </li> </ul>"""
JobStatus: TypeAlias = Literal[
    "CREATED",
    "PROCESSING",
    "COMPLETED",
    "FAILED",
    "CANCELLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobStatus) -> str:
    return value


def deserialize_json(data: str) -> JobStatus:
    return cast(JobStatus, data)
