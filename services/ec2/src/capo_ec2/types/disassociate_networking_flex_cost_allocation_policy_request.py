"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateNetworkingFlexCostAllocationPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.flex_cost_allocation_policy_disassociate_association_id_list


class DisassociateNetworkingFlexCostAllocationPolicyRequest(TypedDict, closed=True):
    fca_policy_association_ids: NotRequired[
        "capo_ec2.types.flex_cost_allocation_policy_disassociate_association_id_list.FlexCostAllocationPolicyDisassociateAssociationIdList"
    ]
    """<p>The IDs of the policy associations to remove. You can specify up to 100 association IDs. This parameter is required.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisassociateNetworkingFlexCostAllocationPolicyRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "fca_policy_association_ids" in value:
        import capo_ec2.types.flex_cost_allocation_policy_disassociate_association_id_list

        capo_ec2.types.flex_cost_allocation_policy_disassociate_association_id_list.serialize_ec2_query(
            value["fca_policy_association_ids"],
            pairs,
            f"{key_prefix}FcaPolicyAssociationIds",
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> DisassociateNetworkingFlexCostAllocationPolicyRequest:
    out: DisassociateNetworkingFlexCostAllocationPolicyRequest = {}  # type: ignore[typeddict-item]
    child_fca_policy_association_ids = el.find("FcaPolicyAssociationIds")
    if child_fca_policy_association_ids is not None:
        import capo_ec2.types.flex_cost_allocation_policy_disassociate_association_id_list

        out["fca_policy_association_ids"] = (
            capo_ec2.types.flex_cost_allocation_policy_disassociate_association_id_list.deserialize_ec2_query(
                child_fca_policy_association_ids
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
