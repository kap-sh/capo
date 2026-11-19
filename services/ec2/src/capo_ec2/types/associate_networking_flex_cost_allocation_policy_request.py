"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateNetworkingFlexCostAllocationPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.flex_cost_allocation_network_resource_id_list
    import capo_ec2.types.flex_cost_allocation_network_resource_scope
    import capo_ec2.types.flex_cost_allocation_policy_id
    import capo_ec2.types.string


class AssociateNetworkingFlexCostAllocationPolicyRequest(TypedDict, closed=True):
    fca_policy_id: NotRequired[
        "capo_ec2.types.flex_cost_allocation_policy_id.FlexCostAllocationPolicyId"
    ]
    """<p>The ID of the flex cost allocation policy to associate. This parameter is required.</p>"""
    network_resource_ids: NotRequired[
        "capo_ec2.types.flex_cost_allocation_network_resource_id_list.FlexCostAllocationNetworkResourceIdList"
    ]
    """<p>The IDs of the network resources to associate with the policy. You can specify from 1 to 20 resource IDs.</p> <p>You must specify <code>NetworkResourceIds</code>, <code>NetworkResourceScope</code>, or both. A request can include at most 20 distinct resources in total.</p>"""
    network_resource_scope: NotRequired[
        "capo_ec2.types.flex_cost_allocation_network_resource_scope.FlexCostAllocationNetworkResourceScope"
    ]
    """<p>The scope of network resources to associate with the policy. Use a scope to associate the policy with the resources in an account, Amazon VPC, or subnet.</p> <p>You must specify <code>NetworkResourceScope</code>, <code>NetworkResourceIds</code>, or both.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency</a>.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssociateNetworkingFlexCostAllocationPolicyRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "fca_policy_id" in value:
        pairs.append((f"{key_prefix}FcaPolicyId", str(value["fca_policy_id"])))
    if "network_resource_ids" in value:
        import capo_ec2.types.flex_cost_allocation_network_resource_id_list

        capo_ec2.types.flex_cost_allocation_network_resource_id_list.serialize_ec2_query(
            value["network_resource_ids"], pairs, f"{key_prefix}NetworkResourceIds"
        )
    if "network_resource_scope" in value:
        import capo_ec2.types.flex_cost_allocation_network_resource_scope

        capo_ec2.types.flex_cost_allocation_network_resource_scope.serialize_ec2_query(
            value["network_resource_scope"], pairs, f"{key_prefix}NetworkResourceScope"
        )
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> AssociateNetworkingFlexCostAllocationPolicyRequest:
    out: AssociateNetworkingFlexCostAllocationPolicyRequest = {}  # type: ignore[typeddict-item]
    child_fca_policy_id = el.find("FcaPolicyId")
    if child_fca_policy_id is not None:
        out["fca_policy_id"] = str(child_fca_policy_id.text or "")
    child_network_resource_ids = el.find("NetworkResourceIds")
    if child_network_resource_ids is not None:
        import capo_ec2.types.flex_cost_allocation_network_resource_id_list

        out["network_resource_ids"] = (
            capo_ec2.types.flex_cost_allocation_network_resource_id_list.deserialize_ec2_query(
                child_network_resource_ids
            )
        )
    child_network_resource_scope = el.find("NetworkResourceScope")
    if child_network_resource_scope is not None:
        import capo_ec2.types.flex_cost_allocation_network_resource_scope

        out["network_resource_scope"] = (
            capo_ec2.types.flex_cost_allocation_network_resource_scope.deserialize_ec2_query(
                child_network_resource_scope
            )
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
