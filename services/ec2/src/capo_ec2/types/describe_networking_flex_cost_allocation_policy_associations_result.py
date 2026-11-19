"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeNetworkingFlexCostAllocationPolicyAssociationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.flex_cost_allocation_policy_association_set
    import capo_ec2.types.next_token


class DescribeNetworkingFlexCostAllocationPolicyAssociationsResult(
    TypedDict, closed=True
):
    fca_policy_associations: NotRequired[
        "capo_ec2.types.flex_cost_allocation_policy_association_set.FlexCostAllocationPolicyAssociationSet"
    ]
    """<p>Information about the policy associations.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeNetworkingFlexCostAllocationPolicyAssociationsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "fca_policy_associations" in value:
        import capo_ec2.types.flex_cost_allocation_policy_association_set

        capo_ec2.types.flex_cost_allocation_policy_association_set.serialize_ec2_query(
            value["fca_policy_associations"],
            pairs,
            f"{key_prefix}FcaPolicyAssociations",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(
    el: Element,
) -> DescribeNetworkingFlexCostAllocationPolicyAssociationsResult:
    out: DescribeNetworkingFlexCostAllocationPolicyAssociationsResult = {}  # type: ignore[typeddict-item]
    child_fca_policy_associations = el.find("fcaPolicyAssociations")
    if child_fca_policy_associations is not None:
        import capo_ec2.types.flex_cost_allocation_policy_association_set

        out["fca_policy_associations"] = (
            capo_ec2.types.flex_cost_allocation_policy_association_set.deserialize_ec2_query(
                child_fca_policy_associations
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
