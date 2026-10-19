"""Generated from Smithy shape ``com.amazonaws.neptunedata#ExecuteOpenCypherQueryOutput``."""

from typing_extensions import TypedDict


class ExecuteOpenCypherQueryOutput(TypedDict, closed=True):
    results: "object"
    """<p>The openCypherquery results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecuteOpenCypherQueryOutput) -> dict:
    out: dict = {}
    out["results"] = value["results"]
    return out


def deserialize_json(data: dict) -> ExecuteOpenCypherQueryOutput:
    out: ExecuteOpenCypherQueryOutput = {}  # type: ignore[typeddict-item]
    if data.get("results") is not None:
        out["results"] = data["results"]
    else:
        out["results"] = None
    return out
