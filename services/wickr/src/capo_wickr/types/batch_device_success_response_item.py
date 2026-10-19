"""Generated from Smithy shape ``com.amazonaws.wickr#BatchDeviceSuccessResponseItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.generic_string


class BatchDeviceSuccessResponseItem(TypedDict, closed=True):
    app_id: "capo_wickr.types.generic_string.GenericString"
    """<p>The application ID of the device that was successfully processed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeviceSuccessResponseItem) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    return out


def deserialize_json(data: dict) -> BatchDeviceSuccessResponseItem:
    out: BatchDeviceSuccessResponseItem = {}  # type: ignore[typeddict-item]
    if data.get("appId") is not None:
        out["app_id"] = data["appId"]
    else:
        out["app_id"] = ""
    return out
