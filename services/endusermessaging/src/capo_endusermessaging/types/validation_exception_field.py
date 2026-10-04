"""Generated from Smithy shape ``com.amazonaws.endusermessaging#ValidationExceptionField``."""

from typing_extensions import TypedDict

from capo_endusermessaging.errors import DeserializationError


class ValidationExceptionField(TypedDict, closed=True):
    path: "str"
    """A JSONPointer expression to the structure member whose value failed to satisfy the modeled constraints."""
    message: "str"
    """A detailed description of the validation failure."""


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
        raise DeserializationError("ValidationExceptionField.path required")
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ValidationExceptionField.message required")
    return out
