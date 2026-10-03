"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIpamExternalResourceVerificationTokensRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.filter_list
    import capo_ec2.types.ipam_max_results
    import capo_ec2.types.next_token
    import capo_ec2.types.value_string_list


class DescribeIpamExternalResourceVerificationTokensRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>One or more filters for the request. For more information about filtering, see <a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-filter.html">Filtering CLI output</a>.</p> <p>Available filters:</p> <ul> <li> <p> <code>ipam-arn</code> </p> </li> <li> <p> <code>ipam-external-resource-verification-token-arn</code> </p> </li> <li> <p> <code>ipam-external-resource-verification-token-id</code> </p> </li> <li> <p> <code>ipam-id</code> </p> </li> <li> <p> <code>ipam-region</code> </p> </li> <li> <p> <code>state</code> </p> </li> <li> <p> <code>status</code> </p> </li> <li> <p> <code>token-name</code> </p> </li> <li> <p> <code>token-value</code> </p> </li> </ul>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
    max_results: NotRequired["capo_ec2.types.ipam_max_results.IpamMaxResults"]
    """<p>The maximum number of tokens to return in one page of results.</p>"""
    ipam_external_resource_verification_token_ids: NotRequired[
        "capo_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>Verification token IDs.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeIpamExternalResourceVerificationTokensRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "ipam_external_resource_verification_token_ids" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["ipam_external_resource_verification_token_ids"],
            pairs,
            f"{key_prefix}IpamExternalResourceVerificationTokenId",
        )


def deserialize_ec2_query(
    el: Element,
) -> DescribeIpamExternalResourceVerificationTokensRequest:
    out: DescribeIpamExternalResourceVerificationTokensRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_filters = el.find("Filter")
    if child_filters is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(child_filters)
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_ipam_external_resource_verification_token_ids = el.find(
        "IpamExternalResourceVerificationTokenId"
    )
    if child_ipam_external_resource_verification_token_ids is not None:
        import capo_ec2.types.value_string_list

        out["ipam_external_resource_verification_token_ids"] = (
            capo_ec2.types.value_string_list.deserialize_ec2_query(
                child_ipam_external_resource_verification_token_ids
            )
        )
    return out
