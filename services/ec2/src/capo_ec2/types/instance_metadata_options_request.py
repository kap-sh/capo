"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceMetadataOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.http_tokens_state
    import capo_ec2.types.instance_metadata_endpoint_state
    import capo_ec2.types.instance_metadata_protocol_state
    import capo_ec2.types.instance_metadata_tags_state
    import capo_ec2.types.integer


class InstanceMetadataOptionsRequest(TypedDict, closed=True):
    http_tokens: NotRequired["capo_ec2.types.http_tokens_state.HttpTokensState"]
    """<p>Indicates whether IMDSv2 is required.</p> <ul> <li> <p> <code>optional</code> - IMDSv2 is optional, which means that you can use either IMDSv2 or IMDSv1.</p> </li> <li> <p> <code>required</code> - IMDSv2 is required, which means that IMDSv1 is disabled, and you must use IMDSv2.</p> </li> </ul> <p>Default:</p> <ul> <li> <p>If the value of <code>ImdsSupport</code> for the Amazon Machine Image (AMI) for your instance is <code>v2.0</code> and the account level default is set to <code>no-preference</code>, the default is <code>required</code>.</p> </li> <li> <p>If the value of <code>ImdsSupport</code> for the Amazon Machine Image (AMI) for your instance is <code>v2.0</code>, but the account level default is set to <code>V1 or V2</code>, the default is <code>optional</code>.</p> </li> </ul> <p>The default value can also be affected by other combinations of parameters. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html#instance-metadata-options-order-of-precedence">Order of precedence for instance metadata options</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    http_put_response_hop_limit: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The maximum number of hops that the metadata token can travel.</p> <p>Possible values: Integers from 1 to 64</p>"""
    http_endpoint: NotRequired[
        "capo_ec2.types.instance_metadata_endpoint_state.InstanceMetadataEndpointState"
    ]
    """<p>Enables or disables the HTTP metadata endpoint on your instances.</p> <p>If you specify a value of <code>disabled</code>, you cannot access your instance metadata.</p> <p>Default: <code>enabled</code> </p>"""
    http_protocol_ipv6: NotRequired[
        "capo_ec2.types.instance_metadata_protocol_state.InstanceMetadataProtocolState"
    ]
    """<p>Enables or disables the IPv6 endpoint for the instance metadata service.</p> <p>Default: <code>disabled</code> </p>"""
    instance_metadata_tags: NotRequired[
        "capo_ec2.types.instance_metadata_tags_state.InstanceMetadataTagsState"
    ]
    """<p>Set to <code>enabled</code> to allow access to instance tags from the instance metadata. Set to <code>disabled</code> to turn off access to instance tags from the instance metadata. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/work-with-tags-in-IMDS.html">View tags for your EC2 instances using instance metadata</a>.</p> <p>Default: <code>disabled</code> </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceMetadataOptionsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "http_tokens" in value:
        import capo_ec2.types.http_tokens_state

        capo_ec2.types.http_tokens_state.serialize_ec2_query(
            value["http_tokens"], pairs, f"{key_prefix}HttpTokens"
        )
    if "http_put_response_hop_limit" in value:
        pairs.append(
            (
                f"{key_prefix}HttpPutResponseHopLimit",
                str(value["http_put_response_hop_limit"]),
            )
        )
    if "http_endpoint" in value:
        import capo_ec2.types.instance_metadata_endpoint_state

        capo_ec2.types.instance_metadata_endpoint_state.serialize_ec2_query(
            value["http_endpoint"], pairs, f"{key_prefix}HttpEndpoint"
        )
    if "http_protocol_ipv6" in value:
        import capo_ec2.types.instance_metadata_protocol_state

        capo_ec2.types.instance_metadata_protocol_state.serialize_ec2_query(
            value["http_protocol_ipv6"], pairs, f"{key_prefix}HttpProtocolIpv6"
        )
    if "instance_metadata_tags" in value:
        import capo_ec2.types.instance_metadata_tags_state

        capo_ec2.types.instance_metadata_tags_state.serialize_ec2_query(
            value["instance_metadata_tags"], pairs, f"{key_prefix}InstanceMetadataTags"
        )


def deserialize_ec2_query(el: Element) -> InstanceMetadataOptionsRequest:
    out: InstanceMetadataOptionsRequest = {}  # type: ignore[typeddict-item]
    child_http_tokens = el.find("HttpTokens")
    if child_http_tokens is not None:
        import capo_ec2.types.http_tokens_state

        out["http_tokens"] = capo_ec2.types.http_tokens_state.deserialize_ec2_query(
            child_http_tokens
        )
    child_http_put_response_hop_limit = el.find("HttpPutResponseHopLimit")
    if child_http_put_response_hop_limit is not None:
        out["http_put_response_hop_limit"] = int(
            child_http_put_response_hop_limit.text or ""
        )
    child_http_endpoint = el.find("HttpEndpoint")
    if child_http_endpoint is not None:
        import capo_ec2.types.instance_metadata_endpoint_state

        out["http_endpoint"] = (
            capo_ec2.types.instance_metadata_endpoint_state.deserialize_ec2_query(
                child_http_endpoint
            )
        )
    child_http_protocol_ipv6 = el.find("HttpProtocolIpv6")
    if child_http_protocol_ipv6 is not None:
        import capo_ec2.types.instance_metadata_protocol_state

        out["http_protocol_ipv6"] = (
            capo_ec2.types.instance_metadata_protocol_state.deserialize_ec2_query(
                child_http_protocol_ipv6
            )
        )
    child_instance_metadata_tags = el.find("InstanceMetadataTags")
    if child_instance_metadata_tags is not None:
        import capo_ec2.types.instance_metadata_tags_state

        out["instance_metadata_tags"] = (
            capo_ec2.types.instance_metadata_tags_state.deserialize_ec2_query(
                child_instance_metadata_tags
            )
        )
    return out
