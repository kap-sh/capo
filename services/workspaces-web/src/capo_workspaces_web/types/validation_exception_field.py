"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ValidationExceptionField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.exception_message
    import capo_workspaces_web.types.field_name


class ValidationExceptionField(TypedDict, closed=True):
    name: "capo_workspaces_web.types.field_name.FieldName"
    """<p>The name of the field that failed validation.</p>"""
    message: "capo_workspaces_web.types.exception_message.ExceptionMessage"
    """<p>The message describing why the field failed validation.</p>"""


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
