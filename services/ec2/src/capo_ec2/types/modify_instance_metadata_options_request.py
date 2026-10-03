"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceMetadataOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.http_tokens_state
    import capo_ec2.types.instance_id
    import capo_ec2.types.instance_metadata_endpoint_state
    import capo_ec2.types.instance_metadata_protocol_state
    import capo_ec2.types.instance_metadata_tags_state
    import capo_ec2.types.integer


class ModifyInstanceMetadataOptionsRequest(TypedDict, closed=True):
    instance_id: NotRequired["capo_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance.</p>"""
    http_tokens: NotRequired["capo_ec2.types.http_tokens_state.HttpTokensState"]
    """<p>Indicates whether IMDSv2 is required.</p> <ul> <li> <p> <code>optional</code> - IMDSv2 is optional. You can choose whether to send a session token in your instance metadata retrieval requests. If you retrieve IAM role credentials without a session token, you receive the IMDSv1 role credentials. If you retrieve IAM role credentials using a valid session token, you receive the IMDSv2 role credentials.</p> </li> <li> <p> <code>required</code> - IMDSv2 is required. You must send a session token in your instance metadata retrieval requests. With this option, retrieving the IAM role credentials always returns IMDSv2 credentials; IMDSv1 credentials are not available.</p> </li> </ul> <p>Default:</p> <ul> <li> <p>If the value of <code>ImdsSupport</code> for the Amazon Machine Image (AMI) for your instance is <code>v2.0</code> and the account level default is set to <code>no-preference</code>, the default is <code>required</code>.</p> </li> <li> <p>If the value of <code>ImdsSupport</code> for the Amazon Machine Image (AMI) for your instance is <code>v2.0</code>, but the account level default is set to <code>V1 or V2</code>, the default is <code>optional</code>.</p> </li> </ul> <p>The default value can also be affected by other combinations of parameters. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html#instance-metadata-options-order-of-precedence">Order of precedence for instance metadata options</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    http_put_response_hop_limit: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The desired HTTP PUT response hop limit for instance metadata requests. The larger the number, the further instance metadata requests can travel. If no parameter is specified, the existing state is maintained.</p> <p>Possible values: Integers from 1 to 64</p>"""
    http_endpoint: NotRequired[
        "capo_ec2.types.instance_metadata_endpoint_state.InstanceMetadataEndpointState"
    ]
    """<p>Enables or disables the HTTP metadata endpoint on your instances. If this parameter is not specified, the existing state is maintained.</p> <p>If you specify a value of <code>disabled</code>, you cannot access your instance metadata.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    http_protocol_ipv6: NotRequired[
        "capo_ec2.types.instance_metadata_protocol_state.InstanceMetadataProtocolState"
    ]
    """<p>Enables or disables the IPv6 endpoint for the instance metadata service. Applies only if you enabled the HTTP metadata endpoint.</p>"""
    instance_metadata_tags: NotRequired[
        "capo_ec2.types.instance_metadata_tags_state.InstanceMetadataTagsState"
    ]
    """<p>Set to <code>enabled</code> to allow access to instance tags from the instance metadata. Set to <code>disabled</code> to turn off access to instance tags from the instance metadata. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/work-with-tags-in-IMDS.html">View tags for your EC2 instances using instance metadata</a>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyInstanceMetadataOptionsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
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
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
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


def deserialize_ec2_query(el: Element) -> ModifyInstanceMetadataOptionsRequest:
    out: ModifyInstanceMetadataOptionsRequest = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
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
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
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
