"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyNetworkingFlexCostAllocationPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.flex_cost_allocation_policy_id
    import capo_ec2.types.instance_flex_cost_allocation_policy_document
    import capo_ec2.types.nat_flex_cost_allocation_policy_document
    import capo_ec2.types.pcx_flex_cost_allocation_policy_document
    import capo_ec2.types.string


class ModifyNetworkingFlexCostAllocationPolicyRequest(TypedDict, closed=True):
    fca_policy_id: NotRequired[
        "capo_ec2.types.flex_cost_allocation_policy_id.FlexCostAllocationPolicyId"
    ]
    """<p>The ID of the flex cost allocation policy to modify. This parameter is required.</p>"""
    nat_fca_policy_document: NotRequired[
        "capo_ec2.types.nat_flex_cost_allocation_policy_document.NatFlexCostAllocationPolicyDocument"
    ]
    """<p>The updated policy document that defines cost allocation for NAT gateways.</p>"""
    instance_fca_policy_document: NotRequired[
        "capo_ec2.types.instance_flex_cost_allocation_policy_document.InstanceFlexCostAllocationPolicyDocument"
    ]
    """<p>The updated policy document that defines cost allocation for EC2 instances.</p>"""
    pcx_fca_policy_document: NotRequired[
        "capo_ec2.types.pcx_flex_cost_allocation_policy_document.PcxFlexCostAllocationPolicyDocument"
    ]
    """<p>The updated policy document that defines cost allocation for Amazon VPC peering connections.</p>"""
    show_back_enabled: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Specifies whether showback reporting is enabled for the policy. If you omit this parameter, the current setting is unchanged.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description for the policy. The description can be up to 1024 characters long.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency</a>.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyNetworkingFlexCostAllocationPolicyRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "fca_policy_id" in value:
        pairs.append((f"{key_prefix}FcaPolicyId", str(value["fca_policy_id"])))
    if "nat_fca_policy_document" in value:
        import capo_ec2.types.nat_flex_cost_allocation_policy_document

        capo_ec2.types.nat_flex_cost_allocation_policy_document.serialize_ec2_query(
            value["nat_fca_policy_document"], pairs, f"{key_prefix}NatFcaPolicyDocument"
        )
    if "instance_fca_policy_document" in value:
        import capo_ec2.types.instance_flex_cost_allocation_policy_document

        capo_ec2.types.instance_flex_cost_allocation_policy_document.serialize_ec2_query(
            value["instance_fca_policy_document"],
            pairs,
            f"{key_prefix}InstanceFcaPolicyDocument",
        )
    if "pcx_fca_policy_document" in value:
        import capo_ec2.types.pcx_flex_cost_allocation_policy_document

        capo_ec2.types.pcx_flex_cost_allocation_policy_document.serialize_ec2_query(
            value["pcx_fca_policy_document"], pairs, f"{key_prefix}PcxFcaPolicyDocument"
        )
    if "show_back_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}ShowBackEnabled",
                "true" if value["show_back_enabled"] else "false",
            )
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> ModifyNetworkingFlexCostAllocationPolicyRequest:
    out: ModifyNetworkingFlexCostAllocationPolicyRequest = {}  # type: ignore[typeddict-item]
    child_fca_policy_id = el.find("FcaPolicyId")
    if child_fca_policy_id is not None:
        out["fca_policy_id"] = str(child_fca_policy_id.text or "")
    child_nat_fca_policy_document = el.find("NatFcaPolicyDocument")
    if child_nat_fca_policy_document is not None:
        import capo_ec2.types.nat_flex_cost_allocation_policy_document

        out["nat_fca_policy_document"] = (
            capo_ec2.types.nat_flex_cost_allocation_policy_document.deserialize_ec2_query(
                child_nat_fca_policy_document
            )
        )
    child_instance_fca_policy_document = el.find("InstanceFcaPolicyDocument")
    if child_instance_fca_policy_document is not None:
        import capo_ec2.types.instance_flex_cost_allocation_policy_document

        out["instance_fca_policy_document"] = (
            capo_ec2.types.instance_flex_cost_allocation_policy_document.deserialize_ec2_query(
                child_instance_fca_policy_document
            )
        )
    child_pcx_fca_policy_document = el.find("PcxFcaPolicyDocument")
    if child_pcx_fca_policy_document is not None:
        import capo_ec2.types.pcx_flex_cost_allocation_policy_document

        out["pcx_fca_policy_document"] = (
            capo_ec2.types.pcx_flex_cost_allocation_policy_document.deserialize_ec2_query(
                child_pcx_fca_policy_document
            )
        )
    child_show_back_enabled = el.find("ShowBackEnabled")
    if child_show_back_enabled is not None:
        out["show_back_enabled"] = (
            child_show_back_enabled.text or ""
        ).lower() == "true"
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
