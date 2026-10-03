"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataMetadataOptionsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string


class AwsEc2LaunchTemplateDataMetadataOptionsDetails(TypedDict, closed=True):
    http_endpoint: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> Enables or disables the HTTP metadata endpoint on your instances. If the parameter is not specified, the default state is enabled, and you won't be able to access your instance metadata. </p>"""
    http_protocol_ipv6: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> Enables or disables the IPv6 endpoint for the instance metadata service. </p>"""
    http_tokens: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The state of token usage for your instance metadata requests. </p>"""
    http_put_response_hop_limit: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p> The desired HTTP PUT response hop limit for instance metadata requests. The larger the number, the further instance metadata requests can travel. </p>"""
    instance_metadata_tags: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> When set to <code>enabled</code>, this parameter allows access to instance tags from the instance metadata. When set to <code>disabled</code>, it turns off access to instance tags from the instance metadata. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#work-with-tags-in-IMDS">Work with instance tags in instance metadata</a> in the <i>Amazon EC2 User Guide</i>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2LaunchTemplateDataMetadataOptionsDetails) -> dict:
    out: dict = {}
    if "http_endpoint" in value:
        out["HttpEndpoint"] = value["http_endpoint"]
    if "http_protocol_ipv6" in value:
        out["HttpProtocolIpv6"] = value["http_protocol_ipv6"]
    if "http_tokens" in value:
        out["HttpTokens"] = value["http_tokens"]
    if "http_put_response_hop_limit" in value:
        out["HttpPutResponseHopLimit"] = value["http_put_response_hop_limit"]
    if "instance_metadata_tags" in value:
        out["InstanceMetadataTags"] = value["instance_metadata_tags"]
    return out


def deserialize_json(data: dict) -> AwsEc2LaunchTemplateDataMetadataOptionsDetails:
    out: AwsEc2LaunchTemplateDataMetadataOptionsDetails = {}  # type: ignore[typeddict-item]
    if data.get("HttpEndpoint") is not None:
        out["http_endpoint"] = data["HttpEndpoint"]
    if data.get("HttpProtocolIpv6") is not None:
        out["http_protocol_ipv6"] = data["HttpProtocolIpv6"]
    if data.get("HttpTokens") is not None:
        out["http_tokens"] = data["HttpTokens"]
    if data.get("HttpPutResponseHopLimit") is not None:
        out["http_put_response_hop_limit"] = data["HttpPutResponseHopLimit"]
    if data.get("InstanceMetadataTags") is not None:
        out["instance_metadata_tags"] = data["InstanceMetadataTags"]
    return out
