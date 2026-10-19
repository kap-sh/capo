"""Generated from Smithy shape ``com.amazonaws.connectcases#FieldError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.field_id


class FieldError(TypedDict, closed=True):
    id: "capo_connectcases.types.field_id.FieldId"
    """<p>The field identifier that caused the error.</p>"""
    error_code: "str"
    """<p>The error code from getting a field.</p>"""
    message: NotRequired["str"]
    """<p>The error message from getting a field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldError) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["errorCode"] = value["error_code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> FieldError:
    out: FieldError = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    else:
        out["error_code"] = ""
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
