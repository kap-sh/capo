"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#GetAlertInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.alert_id
    import capo_cloudwatchomni.types.space_id


class GetAlertInput(TypedDict, closed=True):
    space_id: "capo_cloudwatchomni.types.space_id.SpaceId"
    """The unique ID of the space."""
    alert_id: "capo_cloudwatchomni.types.alert_id.AlertId"
    """The alert to retrieve."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetAlertInput) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    out["alertId"] = value["alert_id"]
    return out


def deserialize_cbor(data: dict) -> GetAlertInput:
    out: GetAlertInput = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    if data.get("alertId") is not None:
        out["alert_id"] = data["alertId"]
    else:
        out["alert_id"] = ""
    return out
