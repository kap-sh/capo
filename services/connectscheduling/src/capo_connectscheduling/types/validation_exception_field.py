"""Generated from Smithy shape ``com.amazonaws.connectscheduling#ValidationExceptionField``."""

from typing_extensions import TypedDict


class ValidationExceptionField(TypedDict, closed=True):
    name: "str"
    """<p>The path to the field that failed validation, using JSON pointer-style dotted notation for nested members.</p>"""
    message: "str"
    """<p>A message describing why the field failed validation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationExceptionField) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ValidationExceptionField:
    out: ValidationExceptionField = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    return out
