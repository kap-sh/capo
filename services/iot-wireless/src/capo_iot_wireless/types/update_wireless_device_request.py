"""Generated from Smithy shape ``com.amazonaws.iotwireless#UpdateWirelessDeviceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.description
    import capo_iot_wireless.types.destination_name
    import capo_iot_wireless.types.lo_ra_wan_update_device
    import capo_iot_wireless.types.positioning_config_status
    import capo_iot_wireless.types.sidewalk_update_wireless_device
    import capo_iot_wireless.types.wireless_device_id
    import capo_iot_wireless.types.wireless_device_name


class UpdateWirelessDeviceRequest(TypedDict, closed=True):
    id: "capo_iot_wireless.types.wireless_device_id.WirelessDeviceId"
    """<p>The ID of the resource to update.</p>"""
    destination_name: NotRequired[
        "capo_iot_wireless.types.destination_name.DestinationName"
    ]
    """<p>The name of the new destination for the device.</p>"""
    name: NotRequired["capo_iot_wireless.types.wireless_device_name.WirelessDeviceName"]
    """<p>The new name of the resource.</p> <note> <p>The following special characters aren't accepted: <code>&lt;&gt;^#~$</code> </p> </note>"""
    description: NotRequired["capo_iot_wireless.types.description.Description"]
    """<p>A new description of the resource.</p>"""
    lo_ra_wan: NotRequired[
        "capo_iot_wireless.types.lo_ra_wan_update_device.LoRaWANUpdateDevice"
    ]
    """<p>The updated wireless device's configuration.</p>"""
    positioning: NotRequired[
        "capo_iot_wireless.types.positioning_config_status.PositioningConfigStatus"
    ]
    """<p>The integration status of the Device Location feature for LoRaWAN and Sidewalk devices.</p>"""
    sidewalk: NotRequired[
        "capo_iot_wireless.types.sidewalk_update_wireless_device.SidewalkUpdateWirelessDevice"
    ]
    """<p>The updated sidewalk properties.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWirelessDeviceRequest) -> dict:
    out: dict = {}
    if "destination_name" in value:
        out["DestinationName"] = value["destination_name"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "lo_ra_wan" in value:
        import capo_iot_wireless.types.lo_ra_wan_update_device

        out["LoRaWAN"] = capo_iot_wireless.types.lo_ra_wan_update_device.serialize_json(
            value["lo_ra_wan"]
        )
    if "positioning" in value:
        import capo_iot_wireless.types.positioning_config_status

        out["Positioning"] = (
            capo_iot_wireless.types.positioning_config_status.serialize_json(
                value["positioning"]
            )
        )
    if "sidewalk" in value:
        import capo_iot_wireless.types.sidewalk_update_wireless_device

        out["Sidewalk"] = (
            capo_iot_wireless.types.sidewalk_update_wireless_device.serialize_json(
                value["sidewalk"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateWirelessDeviceRequest:
    out: UpdateWirelessDeviceRequest = {}  # type: ignore[typeddict-item]
    if data.get("DestinationName") is not None:
        out["destination_name"] = data["DestinationName"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("LoRaWAN") is not None:
        import capo_iot_wireless.types.lo_ra_wan_update_device

        out["lo_ra_wan"] = (
            capo_iot_wireless.types.lo_ra_wan_update_device.deserialize_json(
                data["LoRaWAN"]
            )
        )
    if data.get("Positioning") is not None:
        import capo_iot_wireless.types.positioning_config_status

        out["positioning"] = (
            capo_iot_wireless.types.positioning_config_status.deserialize_json(
                data["Positioning"]
            )
        )
    if data.get("Sidewalk") is not None:
        import capo_iot_wireless.types.sidewalk_update_wireless_device

        out["sidewalk"] = (
            capo_iot_wireless.types.sidewalk_update_wireless_device.deserialize_json(
                data["Sidewalk"]
            )
        )
    return out
