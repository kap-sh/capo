"""Generated from Smithy shape ``com.amazonaws.iotwireless#StartWirelessDeviceImportTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_wireless.types.client_request_token
    import capo_iot_wireless.types.destination_name
    import capo_iot_wireless.types.positioning_config_status
    import capo_iot_wireless.types.sidewalk_start_import_info
    import capo_iot_wireless.types.tag_list


class StartWirelessDeviceImportTaskRequest(TypedDict, closed=True):
    destination_name: "capo_iot_wireless.types.destination_name.DestinationName"
    """<p>The name of the Sidewalk destination that describes the IoT rule to route messages from the devices in the import task that are onboarded to AWS IoT Wireless.</p>"""
    client_request_token: NotRequired[
        "capo_iot_wireless.types.client_request_token.ClientRequestToken"
    ]
    tags: NotRequired["capo_iot_wireless.types.tag_list.TagList"]
    positioning: NotRequired[
        "capo_iot_wireless.types.positioning_config_status.PositioningConfigStatus"
    ]
    """<p>The integration status of the Device Location feature for Sidewalk devices.</p>"""
    sidewalk: (
        "capo_iot_wireless.types.sidewalk_start_import_info.SidewalkStartImportInfo"
    )
    """<p>The Sidewalk-related parameters for importing wireless devices that need to be provisioned in bulk.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartWirelessDeviceImportTaskRequest) -> dict:
    out: dict = {}
    out["DestinationName"] = value["destination_name"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
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
    import capo_iot_wireless.types.sidewalk_start_import_info

    out["Sidewalk"] = capo_iot_wireless.types.sidewalk_start_import_info.serialize_json(
        value["sidewalk"]
    )
    return out


def deserialize_json(data: dict) -> StartWirelessDeviceImportTaskRequest:
    out: StartWirelessDeviceImportTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("DestinationName") is not None:
        out["destination_name"] = data["DestinationName"]
    else:
        out["destination_name"] = ""
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
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
        import capo_iot_wireless.types.sidewalk_start_import_info

        out["sidewalk"] = (
            capo_iot_wireless.types.sidewalk_start_import_info.deserialize_json(
                data["Sidewalk"]
            )
        )
    else:
        raise DeserializationError(
            "StartWirelessDeviceImportTaskRequest.sidewalk required"
        )
    return out
