"""Generated from Smithy shape ``com.amazonaws.neptunedata#GetLoaderJobStatusOutput``."""

from typing_extensions import TypedDict


class GetLoaderJobStatusOutput(TypedDict, closed=True):
    status: "str"
    """<p>The HTTP response code for the request.</p>"""
    payload: "object"
    """<p>Status information about the load job, in a layout that could look like this:</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLoaderJobStatusOutput) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    out["payload"] = value["payload"]
    return out


def deserialize_json(data: dict) -> GetLoaderJobStatusOutput:
    out: GetLoaderJobStatusOutput = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("payload") is not None:
        out["payload"] = data["payload"]
    else:
        out["payload"] = None
    return out
