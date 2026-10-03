"""Generated from Smithy shape ``com.amazonaws.iotwireless#CreateMulticastGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_wireless.types.client_request_token
    import capo_iot_wireless.types.description
    import capo_iot_wireless.types.lo_ra_wan_multicast
    import capo_iot_wireless.types.multicast_group_name
    import capo_iot_wireless.types.tag_list


class CreateMulticastGroupRequest(TypedDict, closed=True):
    name: NotRequired["capo_iot_wireless.types.multicast_group_name.MulticastGroupName"]
    description: NotRequired["capo_iot_wireless.types.description.Description"]
    """<p>The description of the multicast group.</p>"""
    client_request_token: NotRequired[
        "capo_iot_wireless.types.client_request_token.ClientRequestToken"
    ]
    """<p>Each resource must have a unique client request token. The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you try to create a new resource using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. For more information about idempotency, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency in Amazon EC2 API requests</a>.</p>"""
    lo_ra_wan: "capo_iot_wireless.types.lo_ra_wan_multicast.LoRaWANMulticast"
    tags: NotRequired["capo_iot_wireless.types.tag_list.TagList"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateMulticastGroupRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    import capo_iot_wireless.types.lo_ra_wan_multicast

    out["LoRaWAN"] = capo_iot_wireless.types.lo_ra_wan_multicast.serialize_json(
        value["lo_ra_wan"]
    )
    if "tags" in value:
        import capo_iot_wireless.types.tag_list

        out["Tags"] = capo_iot_wireless.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateMulticastGroupRequest:
    out: CreateMulticastGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("LoRaWAN") is not None:
        import capo_iot_wireless.types.lo_ra_wan_multicast

        out["lo_ra_wan"] = capo_iot_wireless.types.lo_ra_wan_multicast.deserialize_json(
            data["LoRaWAN"]
        )
    else:
        raise DeserializationError("CreateMulticastGroupRequest.lo_ra_wan required")
    if data.get("Tags") is not None:
        import capo_iot_wireless.types.tag_list

        out["tags"] = capo_iot_wireless.types.tag_list.deserialize_json(data["Tags"])
    return out
