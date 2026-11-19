"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateNetworkingFlexCostAllocationPolicyResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.flex_cost_allocation_operation_failure_list
    import capo_ec2.types.flex_cost_allocation_policy_association_id_list


class DisassociateNetworkingFlexCostAllocationPolicyResult(TypedDict, closed=True):
    fca_policy_disassociations: NotRequired[
        "capo_ec2.types.flex_cost_allocation_policy_association_id_list.FlexCostAllocationPolicyAssociationIdList"
    ]
    """<p>The IDs of the policy associations that were removed.</p>"""
    fca_policy_disassociation_failures: NotRequired[
        "capo_ec2.types.flex_cost_allocation_operation_failure_list.FlexCostAllocationOperationFailureList"
    ]
    """<p>Information about the policy associations that could not be removed.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisassociateNetworkingFlexCostAllocationPolicyResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "fca_policy_disassociations" in value:
        import capo_ec2.types.flex_cost_allocation_policy_association_id_list

        capo_ec2.types.flex_cost_allocation_policy_association_id_list.serialize_ec2_query(
            value["fca_policy_disassociations"],
            pairs,
            f"{key_prefix}FcaPolicyDisassociations",
        )
    if "fca_policy_disassociation_failures" in value:
        import capo_ec2.types.flex_cost_allocation_operation_failure_list

        capo_ec2.types.flex_cost_allocation_operation_failure_list.serialize_ec2_query(
            value["fca_policy_disassociation_failures"],
            pairs,
            f"{key_prefix}FcaPolicyDisassociationFailures",
        )


def deserialize_ec2_query(
    el: Element,
) -> DisassociateNetworkingFlexCostAllocationPolicyResult:
    out: DisassociateNetworkingFlexCostAllocationPolicyResult = {}  # type: ignore[typeddict-item]
    child_fca_policy_disassociations = el.find("fcaPolicyDisassociations")
    if child_fca_policy_disassociations is not None:
        import capo_ec2.types.flex_cost_allocation_policy_association_id_list

        out["fca_policy_disassociations"] = (
            capo_ec2.types.flex_cost_allocation_policy_association_id_list.deserialize_ec2_query(
                child_fca_policy_disassociations
            )
        )
    child_fca_policy_disassociation_failures = el.find(
        "fcaPolicyDisassociationFailures"
    )
    if child_fca_policy_disassociation_failures is not None:
        import capo_ec2.types.flex_cost_allocation_operation_failure_list

        out["fca_policy_disassociation_failures"] = (
            capo_ec2.types.flex_cost_allocation_operation_failure_list.deserialize_ec2_query(
                child_fca_policy_disassociation_failures
            )
        )
    return out
