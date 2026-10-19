"""Generated from Smithy shape ``com.amazonaws.connectcases#FieldOptionError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.field_option_value


class FieldOptionError(TypedDict, closed=True):
    message: "str"
    """<p>Error message from creating or updating field option.</p>"""
    error_code: "str"
    """<p>Error code from creating or updating field option.</p>"""
    value: "capo_connectcases.types.field_option_value.FieldOptionValue"
    """<p>The field option value that caused the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldOptionError) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["errorCode"] = value["error_code"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> FieldOptionError:
    out: FieldOptionError = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    else:
        out["error_code"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
