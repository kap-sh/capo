"""Generated from Smithy shape ``com.amazonaws.ec2#GetNetworkingFlexCostAllocationPolicyVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.flex_cost_allocation_policy_id
    import capo_ec2.types.flex_cost_allocation_versions_to_include_list


class GetNetworkingFlexCostAllocationPolicyVersionsRequest(TypedDict, closed=True):
    fca_policy_id: NotRequired[
        "capo_ec2.types.flex_cost_allocation_policy_id.FlexCostAllocationPolicyId"
    ]
    """<p>The ID of the flex cost allocation policy. This parameter is required.</p>"""
    versions_to_include: NotRequired[
        "capo_ec2.types.flex_cost_allocation_versions_to_include_list.FlexCostAllocationVersionsToIncludeList"
    ]
    """<p>The policy versions to include in the results.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetNetworkingFlexCostAllocationPolicyVersionsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "fca_policy_id" in value:
        pairs.append((f"{key_prefix}FcaPolicyId", str(value["fca_policy_id"])))
    if "versions_to_include" in value:
        import capo_ec2.types.flex_cost_allocation_versions_to_include_list

        capo_ec2.types.flex_cost_allocation_versions_to_include_list.serialize_ec2_query(
            value["versions_to_include"], pairs, f"{key_prefix}VersionsToInclude"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> GetNetworkingFlexCostAllocationPolicyVersionsRequest:
    out: GetNetworkingFlexCostAllocationPolicyVersionsRequest = {}  # type: ignore[typeddict-item]
    child_fca_policy_id = el.find("FcaPolicyId")
    if child_fca_policy_id is not None:
        out["fca_policy_id"] = str(child_fca_policy_id.text or "")
    child_versions_to_include = el.find("VersionsToInclude")
    if child_versions_to_include is not None:
        import capo_ec2.types.flex_cost_allocation_versions_to_include_list

        out["versions_to_include"] = (
            capo_ec2.types.flex_cost_allocation_versions_to_include_list.deserialize_ec2_query(
                child_versions_to_include
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
