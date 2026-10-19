"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#StartMemoryExtractionJobOutput``."""

from typing_extensions import TypedDict


class StartMemoryExtractionJobOutput(TypedDict, closed=True):
    job_id: "str"
    """<p>Extraction Job ID that was attempted to start.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartMemoryExtractionJobOutput) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    return out


def deserialize_json(data: dict) -> StartMemoryExtractionJobOutput:
    out: StartMemoryExtractionJobOutput = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        out["job_id"] = ""
    return out
