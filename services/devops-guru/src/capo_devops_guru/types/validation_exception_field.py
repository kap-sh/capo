"""Generated from Smithy shape ``com.amazonaws.devopsguru#ValidationExceptionField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.error_message_string
    import capo_devops_guru.types.error_name_string


class ValidationExceptionField(TypedDict, closed=True):
    name: "capo_devops_guru.types.error_name_string.ErrorNameString"
    """<p> The name of the field. </p>"""
    message: "capo_devops_guru.types.error_message_string.ErrorMessageString"
    """<p> The message associated with the validation exception with information to help determine its cause. </p>"""


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
