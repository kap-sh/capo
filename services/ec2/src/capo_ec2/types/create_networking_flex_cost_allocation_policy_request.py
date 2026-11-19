"""Generated from Smithy shape ``com.amazonaws.ec2#CreateNetworkingFlexCostAllocationPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.flex_cost_allocation_network_resource_type
    import capo_ec2.types.instance_flex_cost_allocation_policy_document
    import capo_ec2.types.nat_flex_cost_allocation_policy_document
    import capo_ec2.types.pcx_flex_cost_allocation_policy_document
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class CreateNetworkingFlexCostAllocationPolicyRequest(TypedDict, closed=True):
    network_resource_type: NotRequired[
        "capo_ec2.types.flex_cost_allocation_network_resource_type.FlexCostAllocationNetworkResourceType"
    ]
    """<p>The type of network resource that the policy applies to. This parameter is required. Valid values are <code>natgw</code> (NAT gateway), <code>pcx</code> (Amazon VPC peering connection), and <code>ec2</code> (EC2 instance).</p> <p>Specify the policy document that matches the resource type: <code>NatFcaPolicyDocument</code> for <code>natgw</code>, <code>InstanceFcaPolicyDocument</code> for <code>ec2</code>, or <code>PcxFcaPolicyDocument</code> for <code>pcx</code>. Don't specify a policy document for a different resource type.</p>"""
    nat_fca_policy_document: NotRequired[
        "capo_ec2.types.nat_flex_cost_allocation_policy_document.NatFlexCostAllocationPolicyDocument"
    ]
    """<p>The policy document that defines cost allocation for NAT gateways. Provide this document when <code>NetworkResourceType</code> is <code>natgw</code>.</p>"""
    instance_fca_policy_document: NotRequired[
        "capo_ec2.types.instance_flex_cost_allocation_policy_document.InstanceFlexCostAllocationPolicyDocument"
    ]
    """<p>The policy document that defines cost allocation for EC2 instances. Provide this document when <code>NetworkResourceType</code> is <code>ec2</code>.</p>"""
    pcx_fca_policy_document: NotRequired[
        "capo_ec2.types.pcx_flex_cost_allocation_policy_document.PcxFlexCostAllocationPolicyDocument"
    ]
    """<p>The policy document that defines cost allocation for Amazon VPC peering connections. Provide this document when <code>NetworkResourceType</code> is <code>pcx</code>.</p>"""
    show_back_enabled: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Specifies whether showback reporting is enabled for the policy.</p> <p>Default: <code>true</code> </p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description for the policy. The description can be up to 1024 characters long.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to assign to the policy.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency</a>.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateNetworkingFlexCostAllocationPolicyRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "network_resource_type" in value:
        import capo_ec2.types.flex_cost_allocation_network_resource_type

        capo_ec2.types.flex_cost_allocation_network_resource_type.serialize_ec2_query(
            value["network_resource_type"], pairs, f"{key_prefix}NetworkResourceType"
        )
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
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecifications"
        )
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> CreateNetworkingFlexCostAllocationPolicyRequest:
    out: CreateNetworkingFlexCostAllocationPolicyRequest = {}  # type: ignore[typeddict-item]
    child_network_resource_type = el.find("NetworkResourceType")
    if child_network_resource_type is not None:
        import capo_ec2.types.flex_cost_allocation_network_resource_type

        out["network_resource_type"] = (
            capo_ec2.types.flex_cost_allocation_network_resource_type.deserialize_ec2_query(
                child_network_resource_type
            )
        )
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
    child_tag_specifications = el.find("TagSpecifications")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
