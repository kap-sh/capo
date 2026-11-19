"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateNetworkingFlexCostAllocationPolicyResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.flex_cost_allocation_operation_failure_list
    import capo_ec2.types.flex_cost_allocation_policy_association_set


class AssociateNetworkingFlexCostAllocationPolicyResult(TypedDict, closed=True):
    fca_policy_associations: NotRequired[
        "capo_ec2.types.flex_cost_allocation_policy_association_set.FlexCostAllocationPolicyAssociationSet"
    ]
    """<p>Information about the policy associations that were created.</p>"""
    fca_policy_association_failures: NotRequired[
        "capo_ec2.types.flex_cost_allocation_operation_failure_list.FlexCostAllocationOperationFailureList"
    ]
    """<p>Information about the network resources that could not be associated with the policy.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssociateNetworkingFlexCostAllocationPolicyResult,
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
    if "fca_policy_association_failures" in value:
        import capo_ec2.types.flex_cost_allocation_operation_failure_list

        capo_ec2.types.flex_cost_allocation_operation_failure_list.serialize_ec2_query(
            value["fca_policy_association_failures"],
            pairs,
            f"{key_prefix}FcaPolicyAssociationFailures",
        )


def deserialize_ec2_query(
    el: Element,
) -> AssociateNetworkingFlexCostAllocationPolicyResult:
    out: AssociateNetworkingFlexCostAllocationPolicyResult = {}  # type: ignore[typeddict-item]
    child_fca_policy_associations = el.find("fcaPolicyAssociations")
    if child_fca_policy_associations is not None:
        import capo_ec2.types.flex_cost_allocation_policy_association_set

        out["fca_policy_associations"] = (
            capo_ec2.types.flex_cost_allocation_policy_association_set.deserialize_ec2_query(
                child_fca_policy_associations
            )
        )
    child_fca_policy_association_failures = el.find("fcaPolicyAssociationFailures")
    if child_fca_policy_association_failures is not None:
        import capo_ec2.types.flex_cost_allocation_operation_failure_list

        out["fca_policy_association_failures"] = (
            capo_ec2.types.flex_cost_allocation_operation_failure_list.deserialize_ec2_query(
                child_fca_policy_association_failures
            )
        )
    return out
