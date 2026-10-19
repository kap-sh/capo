"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobError``."""

from typing_extensions import TypedDict


class ProtectedJobError(TypedDict, closed=True):
    message: "str"
    """<p> The message for the protected job error.</p>"""
    code: "str"
    """<p> The error code for the protected job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobError) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> ProtectedJobError:
    out: ProtectedJobError = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        out["code"] = ""
    return out
