"""Generated from Smithy shape ``com.amazonaws.iotwireless#SendDataToMulticastGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_wireless.types.multicast_group_id
    import capo_iot_wireless.types.multicast_wireless_metadata
    import capo_iot_wireless.types.payload_data


class SendDataToMulticastGroupRequest(TypedDict, closed=True):
    id: "capo_iot_wireless.types.multicast_group_id.MulticastGroupId"
    payload_data: "capo_iot_wireless.types.payload_data.PayloadData"
    wireless_metadata: (
        "capo_iot_wireless.types.multicast_wireless_metadata.MulticastWirelessMetadata"
    )


# --- restJson1 ser/de ---
def serialize_json(value: SendDataToMulticastGroupRequest) -> dict:
    out: dict = {}
    out["PayloadData"] = value["payload_data"]
    import capo_iot_wireless.types.multicast_wireless_metadata

    out["WirelessMetadata"] = (
        capo_iot_wireless.types.multicast_wireless_metadata.serialize_json(
            value["wireless_metadata"]
        )
    )
    return out


def deserialize_json(data: dict) -> SendDataToMulticastGroupRequest:
    out: SendDataToMulticastGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("PayloadData") is not None:
        out["payload_data"] = data["PayloadData"]
    else:
        out["payload_data"] = ""
    if data.get("WirelessMetadata") is not None:
        import capo_iot_wireless.types.multicast_wireless_metadata

        out["wireless_metadata"] = (
            capo_iot_wireless.types.multicast_wireless_metadata.deserialize_json(
                data["WirelessMetadata"]
            )
        )
    else:
        raise DeserializationError(
            "SendDataToMulticastGroupRequest.wireless_metadata required"
        )
    return out
