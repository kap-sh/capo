"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ExtractionJob``."""

from typing_extensions import TypedDict


class ExtractionJob(TypedDict, closed=True):
    job_id: "str"
    """<p>The unique identifier of the extraction job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExtractionJob) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    return out


def deserialize_json(data: dict) -> ExtractionJob:
    out: ExtractionJob = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        out["job_id"] = ""
    return out
