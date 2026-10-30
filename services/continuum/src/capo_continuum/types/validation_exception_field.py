"""Generated from Smithy shape ``com.amazonaws.continuum#ValidationExceptionField``."""

from typing_extensions import TypedDict


class ValidationExceptionField(TypedDict, closed=True):
    path: "str"
    message: "str"


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
