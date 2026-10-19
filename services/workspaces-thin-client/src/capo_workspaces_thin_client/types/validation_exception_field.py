"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#ValidationExceptionField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_thin_client.types.exception_message
    import capo_workspaces_thin_client.types.field_name


class ValidationExceptionField(TypedDict, closed=True):
    name: "capo_workspaces_thin_client.types.field_name.FieldName"
    """<p>The name of the exception.</p>"""
    message: "capo_workspaces_thin_client.types.exception_message.ExceptionMessage"
    """<p>A message that describes the reason for the exception.</p>"""


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
