"""Generated from Smithy shape ``com.amazonaws.ec2#FlexCostAllocationPolicyVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.date_time
    import capo_ec2.types.flex_cost_allocation_network_resource_type
    import capo_ec2.types.flex_cost_allocation_policy_id
    import capo_ec2.types.flex_cost_allocation_policy_version_number
    import capo_ec2.types.instance_flex_cost_allocation_policy_document
    import capo_ec2.types.nat_flex_cost_allocation_policy_document
    import capo_ec2.types.pcx_flex_cost_allocation_policy_document
    import capo_ec2.types.string


class FlexCostAllocationPolicyVersion(TypedDict, closed=True):
    fca_policy_id: NotRequired[
        "capo_ec2.types.flex_cost_allocation_policy_id.FlexCostAllocationPolicyId"
    ]
    """<p>The ID of the policy.</p>"""
    version: NotRequired[
        "capo_ec2.types.flex_cost_allocation_policy_version_number.FlexCostAllocationPolicyVersionNumber"
    ]
    """<p>The version number.</p>"""
    network_resource_type: NotRequired[
        "capo_ec2.types.flex_cost_allocation_network_resource_type.FlexCostAllocationNetworkResourceType"
    ]
    """<p>The type of network resource that the policy applies to.</p>"""
    nat_fca_policy_document: NotRequired[
        "capo_ec2.types.nat_flex_cost_allocation_policy_document.NatFlexCostAllocationPolicyDocument"
    ]
    """<p>The policy document that defines cost allocation for NAT gateways.</p>"""
    instance_fca_policy_document: NotRequired[
        "capo_ec2.types.instance_flex_cost_allocation_policy_document.InstanceFlexCostAllocationPolicyDocument"
    ]
    """<p>The policy document that defines cost allocation for EC2 instances.</p>"""
    pcx_fca_policy_document: NotRequired[
        "capo_ec2.types.pcx_flex_cost_allocation_policy_document.PcxFlexCostAllocationPolicyDocument"
    ]
    """<p>The policy document that defines cost allocation for Amazon VPC peering connections.</p>"""
    show_back_enabled: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether showback reporting is enabled for this version of the policy.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The description of this version of the policy.</p>"""
    expected_effective_at: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The date and time when this version of the policy is expected to apply to network traffic.</p>"""
    created_at: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The date and time when this version of the policy was created.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FlexCostAllocationPolicyVersion, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "fca_policy_id" in value:
        pairs.append((f"{key_prefix}FcaPolicyId", str(value["fca_policy_id"])))
    if "version" in value:
        pairs.append((f"{key_prefix}Version", str(value["version"])))
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
    if "expected_effective_at" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["expected_effective_at"], pairs, f"{key_prefix}ExpectedEffectiveAt"
        )
    if "created_at" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["created_at"], pairs, f"{key_prefix}CreatedAt"
        )


def deserialize_ec2_query(el: Element) -> FlexCostAllocationPolicyVersion:
    out: FlexCostAllocationPolicyVersion = {}  # type: ignore[typeddict-item]
    child_fca_policy_id = el.find("fcaPolicyId")
    if child_fca_policy_id is not None:
        out["fca_policy_id"] = str(child_fca_policy_id.text or "")
    child_version = el.find("version")
    if child_version is not None:
        out["version"] = int(child_version.text or "")
    child_network_resource_type = el.find("networkResourceType")
    if child_network_resource_type is not None:
        import capo_ec2.types.flex_cost_allocation_network_resource_type

        out["network_resource_type"] = (
            capo_ec2.types.flex_cost_allocation_network_resource_type.deserialize_ec2_query(
                child_network_resource_type
            )
        )
    child_nat_fca_policy_document = el.find("natFcaPolicyDocument")
    if child_nat_fca_policy_document is not None:
        import capo_ec2.types.nat_flex_cost_allocation_policy_document

        out["nat_fca_policy_document"] = (
            capo_ec2.types.nat_flex_cost_allocation_policy_document.deserialize_ec2_query(
                child_nat_fca_policy_document
            )
        )
    child_instance_fca_policy_document = el.find("instanceFcaPolicyDocument")
    if child_instance_fca_policy_document is not None:
        import capo_ec2.types.instance_flex_cost_allocation_policy_document

        out["instance_fca_policy_document"] = (
            capo_ec2.types.instance_flex_cost_allocation_policy_document.deserialize_ec2_query(
                child_instance_fca_policy_document
            )
        )
    child_pcx_fca_policy_document = el.find("pcxFcaPolicyDocument")
    if child_pcx_fca_policy_document is not None:
        import capo_ec2.types.pcx_flex_cost_allocation_policy_document

        out["pcx_fca_policy_document"] = (
            capo_ec2.types.pcx_flex_cost_allocation_policy_document.deserialize_ec2_query(
                child_pcx_fca_policy_document
            )
        )
    child_show_back_enabled = el.find("showBackEnabled")
    if child_show_back_enabled is not None:
        out["show_back_enabled"] = (
            child_show_back_enabled.text or ""
        ).lower() == "true"
    child_description = el.find("description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_expected_effective_at = el.find("expectedEffectiveAt")
    if child_expected_effective_at is not None:
        import capo_ec2.types.date_time

        out["expected_effective_at"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_expected_effective_at
        )
    child_created_at = el.find("createdAt")
    if child_created_at is not None:
        import capo_ec2.types.date_time

        out["created_at"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_created_at
        )
    return out
