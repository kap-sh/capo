"""Generated from Smithy shape ``com.amazonaws.iotwireless#CreateWirelessDeviceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_wireless.types.client_request_token
    import capo_iot_wireless.types.description
    import capo_iot_wireless.types.destination_name
    import capo_iot_wireless.types.lo_ra_wan_device
    import capo_iot_wireless.types.positioning_config_status
    import capo_iot_wireless.types.sidewalk_create_wireless_device
    import capo_iot_wireless.types.tag_list
    import capo_iot_wireless.types.wireless_device_name
    import capo_iot_wireless.types.wireless_device_type


class CreateWirelessDeviceRequest(TypedDict, closed=True):
    type: "capo_iot_wireless.types.wireless_device_type.WirelessDeviceType"
    """<p>The wireless device type.</p>"""
    name: NotRequired["capo_iot_wireless.types.wireless_device_name.WirelessDeviceName"]
    """<p>The name of the new resource.</p> <note> <p>The following special characters aren't accepted: <code><>^#~$</code> </p> </note>"""
    description: NotRequired["capo_iot_wireless.types.description.Description"]
    """<p>The description of the new resource.</p>"""
    destination_name: "capo_iot_wireless.types.destination_name.DestinationName"
    """<p>The name of the destination to assign to the new wireless device.</p>"""
    client_request_token: NotRequired[
        "capo_iot_wireless.types.client_request_token.ClientRequestToken"
    ]
    """<p>Each resource must have a unique client request token. The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you try to create a new resource using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. For more information about idempotency, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency in Amazon EC2 API requests</a>.</p>"""
    lo_ra_wan: NotRequired["capo_iot_wireless.types.lo_ra_wan_device.LoRaWANDevice"]
    """<p>The device configuration information to use to create the wireless device.</p>"""
    tags: NotRequired["capo_iot_wireless.types.tag_list.TagList"]
    """<p>The tags to attach to the new wireless device. Tags are metadata that you can use to manage a resource.</p>"""
    positioning: NotRequired[
        "capo_iot_wireless.types.positioning_config_status.PositioningConfigStatus"
    ]
    """<p>The integration status of the Device Location feature for LoRaWAN and Sidewalk devices.</p>"""
    sidewalk: NotRequired[
        "capo_iot_wireless.types.sidewalk_create_wireless_device.SidewalkCreateWirelessDevice"
    ]
    """<p>The device configuration information to use to create the Sidewalk device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWirelessDeviceRequest) -> dict:
    out: dict = {}
    import capo_iot_wireless.types.wireless_device_type

    out["Type"] = capo_iot_wireless.types.wireless_device_type.serialize_json(
        value["type"]
    )
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["DestinationName"] = value["destination_name"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "lo_ra_wan" in value:
        import capo_iot_wireless.types.lo_ra_wan_device

        out["LoRaWAN"] = capo_iot_wireless.types.lo_ra_wan_device.serialize_json(
            value["lo_ra_wan"]
        )
    if "tags" in value:
        import capo_iot_wireless.types.tag_list

        out["Tags"] = capo_iot_wireless.types.tag_list.serialize_json(value["tags"])
    if "positioning" in value:
        import capo_iot_wireless.types.positioning_config_status

        out["Positioning"] = (
            capo_iot_wireless.types.positioning_config_status.serialize_json(
                value["positioning"]
            )
        )
    if "sidewalk" in value:
        import capo_iot_wireless.types.sidewalk_create_wireless_device

        out["Sidewalk"] = (
            capo_iot_wireless.types.sidewalk_create_wireless_device.serialize_json(
                value["sidewalk"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateWirelessDeviceRequest:
    out: CreateWirelessDeviceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_iot_wireless.types.wireless_device_type

        out["type"] = capo_iot_wireless.types.wireless_device_type.deserialize_json(
            data["Type"]
        )
    else:
        raise DeserializationError("CreateWirelessDeviceRequest.type required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DestinationName") is not None:
        out["destination_name"] = data["DestinationName"]
    else:
        raise DeserializationError(
            "CreateWirelessDeviceRequest.destination_name required"
        )
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("LoRaWAN") is not None:
        import capo_iot_wireless.types.lo_ra_wan_device

        out["lo_ra_wan"] = capo_iot_wireless.types.lo_ra_wan_device.deserialize_json(
            data["LoRaWAN"]
        )
    if data.get("Tags") is not None:
        import capo_iot_wireless.types.tag_list

        out["tags"] = capo_iot_wireless.types.tag_list.deserialize_json(data["Tags"])
    if data.get("Positioning") is not None:
        import capo_iot_wireless.types.positioning_config_status

        out["positioning"] = (
            capo_iot_wireless.types.positioning_config_status.deserialize_json(
                data["Positioning"]
            )
        )
    if data.get("Sidewalk") is not None:
        import capo_iot_wireless.types.sidewalk_create_wireless_device

        out["sidewalk"] = (
            capo_iot_wireless.types.sidewalk_create_wireless_device.deserialize_json(
                data["Sidewalk"]
            )
        )
    return out
