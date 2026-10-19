"""Generated from Smithy shape ``com.amazonaws.iotwireless#CreateNetworkAnalyzerConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.client_request_token
    import capo_iot_wireless.types.description
    import capo_iot_wireless.types.network_analyzer_configuration_name
    import capo_iot_wireless.types.network_analyzer_multicast_group_list
    import capo_iot_wireless.types.tag_list
    import capo_iot_wireless.types.trace_content
    import capo_iot_wireless.types.wireless_device_list
    import capo_iot_wireless.types.wireless_gateway_list


class CreateNetworkAnalyzerConfigurationRequest(TypedDict, closed=True):
    name: "capo_iot_wireless.types.network_analyzer_configuration_name.NetworkAnalyzerConfigurationName"
    trace_content: NotRequired["capo_iot_wireless.types.trace_content.TraceContent"]
    wireless_devices: NotRequired[
        "capo_iot_wireless.types.wireless_device_list.WirelessDeviceList"
    ]
    """<p>Wireless device resources to add to the network analyzer configuration. Provide the <code>WirelessDeviceId</code> of the resource to add in the input array.</p>"""
    wireless_gateways: NotRequired[
        "capo_iot_wireless.types.wireless_gateway_list.WirelessGatewayList"
    ]
    """<p>Wireless gateway resources to add to the network analyzer configuration. Provide the <code>WirelessGatewayId</code> of the resource to add in the input array.</p>"""
    description: NotRequired["capo_iot_wireless.types.description.Description"]
    tags: NotRequired["capo_iot_wireless.types.tag_list.TagList"]
    client_request_token: NotRequired[
        "capo_iot_wireless.types.client_request_token.ClientRequestToken"
    ]
    multicast_groups: NotRequired[
        "capo_iot_wireless.types.network_analyzer_multicast_group_list.NetworkAnalyzerMulticastGroupList"
    ]
    """<p>Multicast Group resources to add to the network analyzer configruation. Provide the <code>MulticastGroupId</code> of the resource to add in the input array.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNetworkAnalyzerConfigurationRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "trace_content" in value:
        import capo_iot_wireless.types.trace_content

        out["TraceContent"] = capo_iot_wireless.types.trace_content.serialize_json(
            value["trace_content"]
        )
    if "wireless_devices" in value:
        import capo_iot_wireless.types.wireless_device_list

        out["WirelessDevices"] = (
            capo_iot_wireless.types.wireless_device_list.serialize_json(
                value["wireless_devices"]
            )
        )
    if "wireless_gateways" in value:
        import capo_iot_wireless.types.wireless_gateway_list

        out["WirelessGateways"] = (
            capo_iot_wireless.types.wireless_gateway_list.serialize_json(
                value["wireless_gateways"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_iot_wireless.types.tag_list

        out["Tags"] = capo_iot_wireless.types.tag_list.serialize_json(value["tags"])
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "multicast_groups" in value:
        import capo_iot_wireless.types.network_analyzer_multicast_group_list

        out["MulticastGroups"] = (
            capo_iot_wireless.types.network_analyzer_multicast_group_list.serialize_json(
                value["multicast_groups"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateNetworkAnalyzerConfigurationRequest:
    out: CreateNetworkAnalyzerConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("TraceContent") is not None:
        import capo_iot_wireless.types.trace_content

        out["trace_content"] = capo_iot_wireless.types.trace_content.deserialize_json(
            data["TraceContent"]
        )
    if data.get("WirelessDevices") is not None:
        import capo_iot_wireless.types.wireless_device_list

        out["wireless_devices"] = (
            capo_iot_wireless.types.wireless_device_list.deserialize_json(
                data["WirelessDevices"]
            )
        )
    if data.get("WirelessGateways") is not None:
        import capo_iot_wireless.types.wireless_gateway_list

        out["wireless_gateways"] = (
            capo_iot_wireless.types.wireless_gateway_list.deserialize_json(
                data["WirelessGateways"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Tags") is not None:
        import capo_iot_wireless.types.tag_list

        out["tags"] = capo_iot_wireless.types.tag_list.deserialize_json(data["Tags"])
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("MulticastGroups") is not None:
        import capo_iot_wireless.types.network_analyzer_multicast_group_list

        out["multicast_groups"] = (
            capo_iot_wireless.types.network_analyzer_multicast_group_list.deserialize_json(
                data["MulticastGroups"]
            )
        )
    return out
