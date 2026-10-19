"""Generated from Smithy shape ``com.amazonaws.networkmanager#ValidationExceptionField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.server_side_string


class ValidationExceptionField(TypedDict, closed=True):
    name: "capo_networkmanager.types.server_side_string.ServerSideString"
    """<p>The name of the field.</p>"""
    message: "capo_networkmanager.types.server_side_string.ServerSideString"
    """<p>The message for the field.</p>"""


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
