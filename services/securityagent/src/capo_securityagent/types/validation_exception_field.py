"""Generated from Smithy shape ``com.amazonaws.securityagent#ValidationExceptionField``."""

from typing_extensions import TypedDict


class ValidationExceptionField(TypedDict, closed=True):
    path: "str"
    """<p>A JSONPointer expression to the structure member whose value failed to satisfy the modeled constraint.</p>"""
    message: "str"
    """<p>A detailed description of the validation failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationExceptionField) -> dict:
    out: dict = {}
    out["path"] = value["path"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ValidationExceptionField:
    out: ValidationExceptionField = {}  # type: ignore[typeddict-item]
    if data.get("path") is not None:
        out["path"] = data["path"]
    else:
        out["path"] = ""
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
