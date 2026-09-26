"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ValidationExceptionField``."""

from typing_extensions import TypedDict

from capo_network_security_manager.errors import DeserializationError


class ValidationExceptionField(TypedDict, closed=True):
    name: "str"
    """<p>The name of the field that failed validation.</p>"""
    message: "str"
    """<p>A message describing the validation error for the field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationExceptionField) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ValidationExceptionField:
    out: ValidationExceptionField = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ValidationExceptionField.name required")
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ValidationExceptionField.message required")
    return out
