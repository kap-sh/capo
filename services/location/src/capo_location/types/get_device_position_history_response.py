"""Generated from Smithy shape ``com.amazonaws.location#GetDevicePositionHistoryResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.device_position_list
    import capo_location.types.token


class GetDevicePositionHistoryResponse(TypedDict, closed=True):
    device_positions: "capo_location.types.device_position_list.DevicePositionList"
    """<p>Contains the position history details for the requested device.</p>"""
    next_token: NotRequired["capo_location.types.token.Token"]
    """<p>A pagination token indicating there are additional pages available. You can use the token in a following request to fetch the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDevicePositionHistoryResponse) -> dict:
    out: dict = {}
    import capo_location.types.device_position_list

    out["DevicePositions"] = capo_location.types.device_position_list.serialize_json(
        value["device_positions"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetDevicePositionHistoryResponse:
    out: GetDevicePositionHistoryResponse = {}  # type: ignore[typeddict-item]
    if data.get("DevicePositions") is not None:
        import capo_location.types.device_position_list

        out["device_positions"] = (
            capo_location.types.device_position_list.deserialize_json(
                data["DevicePositions"]
            )
        )
    else:
        raise DeserializationError(
            "GetDevicePositionHistoryResponse.device_positions required"
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: GetDevicePositionHistoryResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "device_positions" in value:
        import capo_location.types.device_position_list

        out["device_positions"] = (
            capo_location.types.device_position_list.redact_sensitive(
                value["device_positions"]
            )
        )
    return out
