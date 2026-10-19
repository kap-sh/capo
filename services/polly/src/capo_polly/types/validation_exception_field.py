"""Generated from Smithy shape ``com.amazonaws.polly#ValidationExceptionField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_polly.types.validation_exception_field_message
    import capo_polly.types.validation_exception_field_name


class ValidationExceptionField(TypedDict, closed=True):
    name: (
        "capo_polly.types.validation_exception_field_name.ValidationExceptionFieldName"
    )
    """<p>The name of the field that failed validation.</p>"""
    message: "capo_polly.types.validation_exception_field_message.ValidationExceptionFieldMessage"
    """<p>A message describing why the field failed validation.</p>"""


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
