"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ErrorDetails``."""

from typing_extensions import TypedDict


class ErrorDetails(TypedDict, closed=True):
    code: "str"
    """<p>The status code identifying the type of error.</p>"""
    message: "str"
    """<p>A human-readable description of the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorDetails) -> dict:
    out: dict = {}
    out["code"] = value["code"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ErrorDetails:
    out: ErrorDetails = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        out["code"] = ""
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
