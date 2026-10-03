"""Generated from Smithy shape ``com.amazonaws.iotwireless#AssociateAwsAccountWithPartnerAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_wireless.types.client_request_token
    import capo_iot_wireless.types.sidewalk_account_info
    import capo_iot_wireless.types.tag_list


class AssociateAwsAccountWithPartnerAccountRequest(TypedDict, closed=True):
    sidewalk: "capo_iot_wireless.types.sidewalk_account_info.SidewalkAccountInfo"
    """<p>The Sidewalk account credentials.</p>"""
    client_request_token: NotRequired[
        "capo_iot_wireless.types.client_request_token.ClientRequestToken"
    ]
    """<p>Each resource must have a unique client request token. The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you try to create a new resource using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. For more information about idempotency, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency in Amazon EC2 API requests</a>.</p>"""
    tags: NotRequired["capo_iot_wireless.types.tag_list.TagList"]
    """<p>The tags to attach to the specified resource. Tags are metadata that you can use to manage a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateAwsAccountWithPartnerAccountRequest) -> dict:
    out: dict = {}
    import capo_iot_wireless.types.sidewalk_account_info

    out["Sidewalk"] = capo_iot_wireless.types.sidewalk_account_info.serialize_json(
        value["sidewalk"]
    )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import capo_iot_wireless.types.tag_list

        out["Tags"] = capo_iot_wireless.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> AssociateAwsAccountWithPartnerAccountRequest:
    out: AssociateAwsAccountWithPartnerAccountRequest = {}  # type: ignore[typeddict-item]
    if data.get("Sidewalk") is not None:
        import capo_iot_wireless.types.sidewalk_account_info

        out["sidewalk"] = (
            capo_iot_wireless.types.sidewalk_account_info.deserialize_json(
                data["Sidewalk"]
            )
        )
    else:
        raise DeserializationError(
            "AssociateAwsAccountWithPartnerAccountRequest.sidewalk required"
        )
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("Tags") is not None:
        import capo_iot_wireless.types.tag_list

        out["tags"] = capo_iot_wireless.types.tag_list.deserialize_json(data["Tags"])
    return out
