"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateInstanceMetadataOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.integer
    import capo_ec2.types.launch_template_http_tokens_state
    import capo_ec2.types.launch_template_instance_metadata_endpoint_state
    import capo_ec2.types.launch_template_instance_metadata_options_state
    import capo_ec2.types.launch_template_instance_metadata_protocol_ipv6
    import capo_ec2.types.launch_template_instance_metadata_tags_state


class LaunchTemplateInstanceMetadataOptions(TypedDict, closed=True):
    state: NotRequired[
        "capo_ec2.types.launch_template_instance_metadata_options_state.LaunchTemplateInstanceMetadataOptionsState"
    ]
    """<p>The state of the metadata option changes.</p> <p> <code>pending</code> - The metadata options are being updated and the instance is not ready to process metadata traffic with the new selection.</p> <p> <code>applied</code> - The metadata options have been successfully applied on the instance.</p>"""
    http_tokens: NotRequired[
        "capo_ec2.types.launch_template_http_tokens_state.LaunchTemplateHttpTokensState"
    ]
    """<p>Indicates whether IMDSv2 is required.</p> <ul> <li> <p> <code>optional</code> - IMDSv2 is optional. You can choose whether to send a session token in your instance metadata retrieval requests. If you retrieve IAM role credentials without a session token, you receive the IMDSv1 role credentials. If you retrieve IAM role credentials using a valid session token, you receive the IMDSv2 role credentials.</p> </li> <li> <p> <code>required</code> - IMDSv2 is required. You must send a session token in your instance metadata retrieval requests. With this option, retrieving the IAM role credentials always returns IMDSv2 credentials; IMDSv1 credentials are not available.</p> </li> </ul>"""
    http_put_response_hop_limit: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The desired HTTP PUT response hop limit for instance metadata requests. The larger the number, the further instance metadata requests can travel.</p> <p>Possible values: Integers from 1 to 64</p>"""
    http_endpoint: NotRequired[
        "capo_ec2.types.launch_template_instance_metadata_endpoint_state.LaunchTemplateInstanceMetadataEndpointState"
    ]
    """<p>Enables or disables the HTTP metadata endpoint on your instances. If the parameter is not specified, the default state is <code>enabled</code>.</p> <note> <p>If you specify a value of <code>disabled</code>, you will not be able to access your instance metadata. </p> </note>"""
    http_protocol_ipv6: NotRequired[
        "capo_ec2.types.launch_template_instance_metadata_protocol_ipv6.LaunchTemplateInstanceMetadataProtocolIpv6"
    ]
    """<p>Enables or disables the IPv6 endpoint for the instance metadata service.</p> <p>Default: <code>disabled</code> </p>"""
    instance_metadata_tags: NotRequired[
        "capo_ec2.types.launch_template_instance_metadata_tags_state.LaunchTemplateInstanceMetadataTagsState"
    ]
    """<p>Set to <code>enabled</code> to allow access to instance tags from the instance metadata. Set to <code>disabled</code> to turn off access to instance tags from the instance metadata. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/work-with-tags-in-IMDS.html">View tags for your EC2 instances using instance metadata</a>.</p> <p>Default: <code>disabled</code> </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateInstanceMetadataOptions,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "state" in value:
        import capo_ec2.types.launch_template_instance_metadata_options_state

        capo_ec2.types.launch_template_instance_metadata_options_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "http_tokens" in value:
        import capo_ec2.types.launch_template_http_tokens_state

        capo_ec2.types.launch_template_http_tokens_state.serialize_ec2_query(
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
        import capo_ec2.types.launch_template_instance_metadata_endpoint_state

        capo_ec2.types.launch_template_instance_metadata_endpoint_state.serialize_ec2_query(
            value["http_endpoint"], pairs, f"{key_prefix}HttpEndpoint"
        )
    if "http_protocol_ipv6" in value:
        import capo_ec2.types.launch_template_instance_metadata_protocol_ipv6

        capo_ec2.types.launch_template_instance_metadata_protocol_ipv6.serialize_ec2_query(
            value["http_protocol_ipv6"], pairs, f"{key_prefix}HttpProtocolIpv6"
        )
    if "instance_metadata_tags" in value:
        import capo_ec2.types.launch_template_instance_metadata_tags_state

        capo_ec2.types.launch_template_instance_metadata_tags_state.serialize_ec2_query(
            value["instance_metadata_tags"], pairs, f"{key_prefix}InstanceMetadataTags"
        )


def deserialize_ec2_query(el: Element) -> LaunchTemplateInstanceMetadataOptions:
    out: LaunchTemplateInstanceMetadataOptions = {}  # type: ignore[typeddict-item]
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.launch_template_instance_metadata_options_state

        out["state"] = (
            capo_ec2.types.launch_template_instance_metadata_options_state.deserialize_ec2_query(
                child_state
            )
        )
    child_http_tokens = el.find("httpTokens")
    if child_http_tokens is not None:
        import capo_ec2.types.launch_template_http_tokens_state

        out["http_tokens"] = (
            capo_ec2.types.launch_template_http_tokens_state.deserialize_ec2_query(
                child_http_tokens
            )
        )
    child_http_put_response_hop_limit = el.find("httpPutResponseHopLimit")
    if child_http_put_response_hop_limit is not None:
        out["http_put_response_hop_limit"] = int(
            child_http_put_response_hop_limit.text or ""
        )
    child_http_endpoint = el.find("httpEndpoint")
    if child_http_endpoint is not None:
        import capo_ec2.types.launch_template_instance_metadata_endpoint_state

        out["http_endpoint"] = (
            capo_ec2.types.launch_template_instance_metadata_endpoint_state.deserialize_ec2_query(
                child_http_endpoint
            )
        )
    child_http_protocol_ipv6 = el.find("httpProtocolIpv6")
    if child_http_protocol_ipv6 is not None:
        import capo_ec2.types.launch_template_instance_metadata_protocol_ipv6

        out["http_protocol_ipv6"] = (
            capo_ec2.types.launch_template_instance_metadata_protocol_ipv6.deserialize_ec2_query(
                child_http_protocol_ipv6
            )
        )
    child_instance_metadata_tags = el.find("instanceMetadataTags")
    if child_instance_metadata_tags is not None:
        import capo_ec2.types.launch_template_instance_metadata_tags_state

        out["instance_metadata_tags"] = (
            capo_ec2.types.launch_template_instance_metadata_tags_state.deserialize_ec2_query(
                child_instance_metadata_tags
            )
        )
    return out
