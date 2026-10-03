"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#GetOriginEndpointPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediapackagev2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediapackagev2.types.cdn_auth_configuration
    import capo_mediapackagev2.types.policy_text
    import capo_mediapackagev2.types.resource_name


class GetOriginEndpointPolicyResponse(TypedDict, closed=True):
    channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>"""
    channel_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.</p>"""
    origin_endpoint_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel.</p>"""
    policy: "capo_mediapackagev2.types.policy_text.PolicyText"
    """<p>The policy assigned to the origin endpoint.</p>"""
    cdn_auth_configuration: NotRequired[
        "capo_mediapackagev2.types.cdn_auth_configuration.CdnAuthConfiguration"
    ]
    """<p>The settings for using authorization headers between the MediaPackage endpoint and your CDN. </p> <p>For information about CDN authorization, see <a href="https://docs.aws.amazon.com/mediapackage/latest/userguide/cdn-auth.html">CDN authorization in Elemental MediaPackage</a> in the MediaPackage user guide.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOriginEndpointPolicyResponse) -> dict:
    out: dict = {}
    out["ChannelGroupName"] = value["channel_group_name"]
    out["ChannelName"] = value["channel_name"]
    out["OriginEndpointName"] = value["origin_endpoint_name"]
    out["Policy"] = value["policy"]
    if "cdn_auth_configuration" in value:
        import capo_mediapackagev2.types.cdn_auth_configuration

        out["CdnAuthConfiguration"] = (
            capo_mediapackagev2.types.cdn_auth_configuration.serialize_json(
                value["cdn_auth_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetOriginEndpointPolicyResponse:
    out: GetOriginEndpointPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("ChannelGroupName") is not None:
        out["channel_group_name"] = data["ChannelGroupName"]
    else:
        raise DeserializationError(
            "GetOriginEndpointPolicyResponse.channel_group_name required"
        )
    if data.get("ChannelName") is not None:
        out["channel_name"] = data["ChannelName"]
    else:
        raise DeserializationError(
            "GetOriginEndpointPolicyResponse.channel_name required"
        )
    if data.get("OriginEndpointName") is not None:
        out["origin_endpoint_name"] = data["OriginEndpointName"]
    else:
        raise DeserializationError(
            "GetOriginEndpointPolicyResponse.origin_endpoint_name required"
        )
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    else:
        raise DeserializationError("GetOriginEndpointPolicyResponse.policy required")
    if data.get("CdnAuthConfiguration") is not None:
        import capo_mediapackagev2.types.cdn_auth_configuration

        out["cdn_auth_configuration"] = (
            capo_mediapackagev2.types.cdn_auth_configuration.deserialize_json(
                data["CdnAuthConfiguration"]
            )
        )
    return out
