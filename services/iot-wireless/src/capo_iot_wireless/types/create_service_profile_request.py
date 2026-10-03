"""Generated from Smithy shape ``com.amazonaws.iotwireless#CreateServiceProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.client_request_token
    import capo_iot_wireless.types.lo_ra_wan_service_profile
    import capo_iot_wireless.types.service_profile_name
    import capo_iot_wireless.types.tag_list


class CreateServiceProfileRequest(TypedDict, closed=True):
    name: NotRequired["capo_iot_wireless.types.service_profile_name.ServiceProfileName"]
    """<p>The name of the new resource.</p> <note> <p>The following special characters aren't accepted: <code><>^#~$</code> </p> </note>"""
    lo_ra_wan: NotRequired[
        "capo_iot_wireless.types.lo_ra_wan_service_profile.LoRaWANServiceProfile"
    ]
    """<p>The service profile information to use to create the service profile.</p>"""
    tags: NotRequired["capo_iot_wireless.types.tag_list.TagList"]
    """<p>The tags to attach to the new service profile. Tags are metadata that you can use to manage a resource.</p>"""
    client_request_token: NotRequired[
        "capo_iot_wireless.types.client_request_token.ClientRequestToken"
    ]
    """<p>Each resource must have a unique client request token. The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you try to create a new resource using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. For more information about idempotency, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency in Amazon EC2 API requests</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateServiceProfileRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "lo_ra_wan" in value:
        import capo_iot_wireless.types.lo_ra_wan_service_profile

        out["LoRaWAN"] = (
            capo_iot_wireless.types.lo_ra_wan_service_profile.serialize_json(
                value["lo_ra_wan"]
            )
        )
    if "tags" in value:
        import capo_iot_wireless.types.tag_list

        out["Tags"] = capo_iot_wireless.types.tag_list.serialize_json(value["tags"])
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> CreateServiceProfileRequest:
    out: CreateServiceProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("LoRaWAN") is not None:
        import capo_iot_wireless.types.lo_ra_wan_service_profile

        out["lo_ra_wan"] = (
            capo_iot_wireless.types.lo_ra_wan_service_profile.deserialize_json(
                data["LoRaWAN"]
            )
        )
    if data.get("Tags") is not None:
        import capo_iot_wireless.types.tag_list

        out["tags"] = capo_iot_wireless.types.tag_list.deserialize_json(data["Tags"])
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    return out
