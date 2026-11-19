"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeNetworkingFlexCostAllocationPoliciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.describe_flex_cost_allocation_policies_max_results
    import capo_ec2.types.filter_list
    import capo_ec2.types.flex_cost_allocation_policy_id_set
    import capo_ec2.types.next_token


class DescribeNetworkingFlexCostAllocationPoliciesRequest(TypedDict, closed=True):
    fca_policy_ids: NotRequired[
        "capo_ec2.types.flex_cost_allocation_policy_id_set.FlexCostAllocationPolicyIdSet"
    ]
    """<p>The IDs of the flex cost allocation policies to describe.</p>"""
    max_results: NotRequired[
        "capo_ec2.types.describe_flex_cost_allocation_policies_max_results.DescribeFlexCostAllocationPoliciesMaxResults"
    ]
    """<p>The maximum number of results to return in a single call. The range is 5 to 1000. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>Default: 100</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>fca-policy-id</code> - The ID of the policy.</p> </li> <li> <p> <code>managed-by</code> - The entity that manages the policy (<code>account</code> | <code>declarative-policy</code>).</p> </li> <li> <p> <code>network-resource-type</code> - The type of network resource that the policy applies to (<code>natgw</code> | <code>ec2</code> | <code>pcx</code>).</p> </li> <li> <p> <code>showback-enabled</code> - Indicates whether showback reporting is enabled for the policy (<code>true</code> | <code>false</code>).</p> </li> </ul>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeNetworkingFlexCostAllocationPoliciesRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "fca_policy_ids" in value:
        import capo_ec2.types.flex_cost_allocation_policy_id_set

        capo_ec2.types.flex_cost_allocation_policy_id_set.serialize_ec2_query(
            value["fca_policy_ids"], pairs, f"{key_prefix}FcaPolicyIds"
        )
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filters"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> DescribeNetworkingFlexCostAllocationPoliciesRequest:
    out: DescribeNetworkingFlexCostAllocationPoliciesRequest = {}  # type: ignore[typeddict-item]
    child_fca_policy_ids = el.find("FcaPolicyIds")
    if child_fca_policy_ids is not None:
        import capo_ec2.types.flex_cost_allocation_policy_id_set

        out["fca_policy_ids"] = (
            capo_ec2.types.flex_cost_allocation_policy_id_set.deserialize_ec2_query(
                child_fca_policy_ids
            )
        )
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_filters = el.find("Filters")
    if child_filters is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(child_filters)
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
