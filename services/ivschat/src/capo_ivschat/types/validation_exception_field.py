"""Generated from Smithy shape ``com.amazonaws.ivschat#ValidationExceptionField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivschat.types.error_message
    import capo_ivschat.types.field_name


class ValidationExceptionField(TypedDict, closed=True):
    name: "capo_ivschat.types.field_name.FieldName"
    """<p>Name of the field which failed validation.</p>"""
    message: "capo_ivschat.types.error_message.ErrorMessage"
    """<p>Explanation of the reason for the validation error.</p>"""


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
        out["name"] = ""
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
