"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeNetworkingFlexCostAllocationPoliciesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.flex_cost_allocation_policy_set
    import capo_ec2.types.next_token


class DescribeNetworkingFlexCostAllocationPoliciesResult(TypedDict, closed=True):
    flex_cost_allocation_policies: NotRequired[
        "capo_ec2.types.flex_cost_allocation_policy_set.FlexCostAllocationPolicySet"
    ]
    """<p>Information about the flex cost allocation policies.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeNetworkingFlexCostAllocationPoliciesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "flex_cost_allocation_policies" in value:
        import capo_ec2.types.flex_cost_allocation_policy_set

        capo_ec2.types.flex_cost_allocation_policy_set.serialize_ec2_query(
            value["flex_cost_allocation_policies"],
            pairs,
            f"{key_prefix}FlexCostAllocationPolicies",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(
    el: Element,
) -> DescribeNetworkingFlexCostAllocationPoliciesResult:
    out: DescribeNetworkingFlexCostAllocationPoliciesResult = {}  # type: ignore[typeddict-item]
    child_flex_cost_allocation_policies = el.find("flexCostAllocationPolicies")
    if child_flex_cost_allocation_policies is not None:
        import capo_ec2.types.flex_cost_allocation_policy_set

        out["flex_cost_allocation_policies"] = (
            capo_ec2.types.flex_cost_allocation_policy_set.deserialize_ec2_query(
                child_flex_cost_allocation_policies
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
