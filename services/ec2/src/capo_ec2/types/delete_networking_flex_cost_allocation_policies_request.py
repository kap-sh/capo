"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteNetworkingFlexCostAllocationPoliciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.flex_cost_allocation_policy_id_list


class DeleteNetworkingFlexCostAllocationPoliciesRequest(TypedDict, closed=True):
    fca_policy_ids: NotRequired[
        "capo_ec2.types.flex_cost_allocation_policy_id_list.FlexCostAllocationPolicyIdList"
    ]
    """<p>The IDs of the flex cost allocation policies to delete. You can specify up to 50 policy IDs. This parameter is required.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteNetworkingFlexCostAllocationPoliciesRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "fca_policy_ids" in value:
        import capo_ec2.types.flex_cost_allocation_policy_id_list

        capo_ec2.types.flex_cost_allocation_policy_id_list.serialize_ec2_query(
            value["fca_policy_ids"], pairs, f"{key_prefix}FcaPolicyIds"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> DeleteNetworkingFlexCostAllocationPoliciesRequest:
    out: DeleteNetworkingFlexCostAllocationPoliciesRequest = {}  # type: ignore[typeddict-item]
    child_fca_policy_ids = el.find("FcaPolicyIds")
    if child_fca_policy_ids is not None:
        import capo_ec2.types.flex_cost_allocation_policy_id_list

        out["fca_policy_ids"] = (
            capo_ec2.types.flex_cost_allocation_policy_id_list.deserialize_ec2_query(
                child_fca_policy_ids
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
