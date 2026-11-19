"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteNetworkingFlexCostAllocationPoliciesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.flex_cost_allocation_operation_failure_list
    import capo_ec2.types.flex_cost_allocation_policy_id_list


class DeleteNetworkingFlexCostAllocationPoliciesResult(TypedDict, closed=True):
    successful: NotRequired[
        "capo_ec2.types.flex_cost_allocation_policy_id_list.FlexCostAllocationPolicyIdList"
    ]
    """<p>The IDs of the policies that were successfully deleted.</p>"""
    failed: NotRequired[
        "capo_ec2.types.flex_cost_allocation_operation_failure_list.FlexCostAllocationOperationFailureList"
    ]
    """<p>Information about the policies that could not be deleted.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteNetworkingFlexCostAllocationPoliciesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "successful" in value:
        import capo_ec2.types.flex_cost_allocation_policy_id_list

        capo_ec2.types.flex_cost_allocation_policy_id_list.serialize_ec2_query(
            value["successful"], pairs, f"{key_prefix}Successful"
        )
    if "failed" in value:
        import capo_ec2.types.flex_cost_allocation_operation_failure_list

        capo_ec2.types.flex_cost_allocation_operation_failure_list.serialize_ec2_query(
            value["failed"], pairs, f"{key_prefix}Failed"
        )


def deserialize_ec2_query(
    el: Element,
) -> DeleteNetworkingFlexCostAllocationPoliciesResult:
    out: DeleteNetworkingFlexCostAllocationPoliciesResult = {}  # type: ignore[typeddict-item]
    child_successful = el.find("successful")
    if child_successful is not None:
        import capo_ec2.types.flex_cost_allocation_policy_id_list

        out["successful"] = (
            capo_ec2.types.flex_cost_allocation_policy_id_list.deserialize_ec2_query(
                child_successful
            )
        )
    child_failed = el.find("failed")
    if child_failed is not None:
        import capo_ec2.types.flex_cost_allocation_operation_failure_list

        out["failed"] = (
            capo_ec2.types.flex_cost_allocation_operation_failure_list.deserialize_ec2_query(
                child_failed
            )
        )
    return out
