"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceMetadataDefaultsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.boxed_integer
    import capo_ec2.types.default_http_tokens_enforced_state
    import capo_ec2.types.default_instance_metadata_endpoint_state
    import capo_ec2.types.default_instance_metadata_tags_state
    import capo_ec2.types.metadata_default_http_tokens_state


class ModifyInstanceMetadataDefaultsRequest(TypedDict, closed=True):
    http_tokens: NotRequired[
        "capo_ec2.types.metadata_default_http_tokens_state.MetadataDefaultHttpTokensState"
    ]
    """<p>Indicates whether IMDSv2 is required.</p> <ul> <li> <p> <code>optional</code> – IMDSv2 is optional, which means that you can use either IMDSv2 or IMDSv1.</p> </li> <li> <p> <code>required</code> – IMDSv2 is required, which means that IMDSv1 is disabled, and you must use IMDSv2.</p> </li> </ul>"""
    http_put_response_hop_limit: NotRequired[
        "capo_ec2.types.boxed_integer.BoxedInteger"
    ]
    """<p>The maximum number of hops that the metadata token can travel. To indicate no preference, specify <code>-1</code>.</p> <p>Possible values: Integers from <code>1</code> to <code>64</code>, and <code>-1</code> to indicate no preference</p>"""
    http_endpoint: NotRequired[
        "capo_ec2.types.default_instance_metadata_endpoint_state.DefaultInstanceMetadataEndpointState"
    ]
    """<p>Enables or disables the IMDS endpoint on an instance. When disabled, the instance metadata can't be accessed.</p>"""
    instance_metadata_tags: NotRequired[
        "capo_ec2.types.default_instance_metadata_tags_state.DefaultInstanceMetadataTagsState"
    ]
    """<p>Enables or disables access to an instance's tags from the instance metadata. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/work-with-tags-in-IMDS.html">View tags for your EC2 instances using instance metadata</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    http_tokens_enforced: NotRequired[
        "capo_ec2.types.default_http_tokens_enforced_state.DefaultHttpTokensEnforcedState"
    ]
    """<p>Specifies whether to enforce the requirement of IMDSv2 on an instance at the time of launch. When enforcement is enabled, the instance can't launch unless IMDSv2 (<code>HttpTokens</code>) is set to <code>required</code>. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html#enforce-imdsv2-at-the-account-level">Enforce IMDSv2 at the account level</a> in the <i>Amazon EC2 User Guide</i>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyInstanceMetadataDefaultsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "http_tokens" in value:
        import capo_ec2.types.metadata_default_http_tokens_state

        capo_ec2.types.metadata_default_http_tokens_state.serialize_ec2_query(
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
        import capo_ec2.types.default_instance_metadata_endpoint_state

        capo_ec2.types.default_instance_metadata_endpoint_state.serialize_ec2_query(
            value["http_endpoint"], pairs, f"{key_prefix}HttpEndpoint"
        )
    if "instance_metadata_tags" in value:
        import capo_ec2.types.default_instance_metadata_tags_state

        capo_ec2.types.default_instance_metadata_tags_state.serialize_ec2_query(
            value["instance_metadata_tags"], pairs, f"{key_prefix}InstanceMetadataTags"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "http_tokens_enforced" in value:
        import capo_ec2.types.default_http_tokens_enforced_state

        capo_ec2.types.default_http_tokens_enforced_state.serialize_ec2_query(
            value["http_tokens_enforced"], pairs, f"{key_prefix}HttpTokensEnforced"
        )


def deserialize_ec2_query(el: Element) -> ModifyInstanceMetadataDefaultsRequest:
    out: ModifyInstanceMetadataDefaultsRequest = {}  # type: ignore[typeddict-item]
    child_http_tokens = el.find("HttpTokens")
    if child_http_tokens is not None:
        import capo_ec2.types.metadata_default_http_tokens_state

        out["http_tokens"] = (
            capo_ec2.types.metadata_default_http_tokens_state.deserialize_ec2_query(
                child_http_tokens
            )
        )
    child_http_put_response_hop_limit = el.find("HttpPutResponseHopLimit")
    if child_http_put_response_hop_limit is not None:
        out["http_put_response_hop_limit"] = int(
            child_http_put_response_hop_limit.text or ""
        )
    child_http_endpoint = el.find("HttpEndpoint")
    if child_http_endpoint is not None:
        import capo_ec2.types.default_instance_metadata_endpoint_state

        out["http_endpoint"] = (
            capo_ec2.types.default_instance_metadata_endpoint_state.deserialize_ec2_query(
                child_http_endpoint
            )
        )
    child_instance_metadata_tags = el.find("InstanceMetadataTags")
    if child_instance_metadata_tags is not None:
        import capo_ec2.types.default_instance_metadata_tags_state

        out["instance_metadata_tags"] = (
            capo_ec2.types.default_instance_metadata_tags_state.deserialize_ec2_query(
                child_instance_metadata_tags
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_http_tokens_enforced = el.find("HttpTokensEnforced")
    if child_http_tokens_enforced is not None:
        import capo_ec2.types.default_http_tokens_enforced_state

        out["http_tokens_enforced"] = (
            capo_ec2.types.default_http_tokens_enforced_state.deserialize_ec2_query(
                child_http_tokens_enforced
            )
        )
    return out
