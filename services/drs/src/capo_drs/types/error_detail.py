"""Generated from Smithy shape ``com.amazonaws.drs#ErrorDetail``."""

from typing_extensions import TypedDict


class ErrorDetail(TypedDict, closed=True):
    message: "str"
    """<p>The error message.</p>"""
    code: "str"
    """<p>The error code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorDetail) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> ErrorDetail:
    out: ErrorDetail = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        out["code"] = ""
    return out
