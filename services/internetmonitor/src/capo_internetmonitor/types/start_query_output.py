"""Generated from Smithy shape ``com.amazonaws.internetmonitor#StartQueryOutput``."""

from typing_extensions import TypedDict


class StartQueryOutput(TypedDict, closed=True):
    query_id: "str"
    """<p>The internally-generated identifier of a specific query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartQueryOutput) -> dict:
    out: dict = {}
    out["QueryId"] = value["query_id"]
    return out


def deserialize_json(data: dict) -> StartQueryOutput:
    out: StartQueryOutput = {}  # type: ignore[typeddict-item]
    if data.get("QueryId") is not None:
        out["query_id"] = data["QueryId"]
    else:
        out["query_id"] = ""
    return out
