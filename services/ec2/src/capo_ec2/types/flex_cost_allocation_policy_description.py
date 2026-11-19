"""Generated from Smithy shape ``com.amazonaws.ec2#FlexCostAllocationPolicyDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.date_time
    import capo_ec2.types.flex_cost_allocation_network_resource_type
    import capo_ec2.types.flex_cost_allocation_policy_arn
    import capo_ec2.types.flex_cost_allocation_policy_id
    import capo_ec2.types.flex_cost_allocation_policy_version_number
    import capo_ec2.types.instance_flex_cost_allocation_policy_document
    import capo_ec2.types.managed_by
    import capo_ec2.types.nat_flex_cost_allocation_policy_document
    import capo_ec2.types.pcx_flex_cost_allocation_policy_document
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class FlexCostAllocationPolicyDescription(TypedDict, closed=True):
    fca_policy_id: NotRequired[
        "capo_ec2.types.flex_cost_allocation_policy_id.FlexCostAllocationPolicyId"
    ]
    """<p>The ID of the policy.</p>"""
    fca_policy_arn: NotRequired[
        "capo_ec2.types.flex_cost_allocation_policy_arn.FlexCostAllocationPolicyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the policy.</p>"""
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
    """<p>Indicates whether showback reporting is enabled for the policy.</p>"""
    owner_account: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the account that owns the policy.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The description of the policy.</p>"""
    latest_version: NotRequired[
        "capo_ec2.types.flex_cost_allocation_policy_version_number.FlexCostAllocationPolicyVersionNumber"
    ]
    """<p>The number of the latest version of the policy.</p>"""
    version_expected_effective_at: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The date and time when the latest version of the policy is expected to apply to network traffic. The policy configuration in this response is from the latest version.</p>"""
    policy_created_at: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The date and time when the policy was created.</p>"""
    updated_at: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The date and time when the policy was last updated.</p>"""
    managed_by: NotRequired["capo_ec2.types.managed_by.ManagedBy"]
    """<p>The entity that manages the policy. Valid values are:</p> <ul> <li> <p> <code>account</code> - The account that owns the policy created it.</p> </li> <li> <p> <code>declarative-policy</code> - An Amazon Web Services Organizations declarative policy created the policy. You can't modify or delete the policy.</p> </li> </ul>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the policy.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FlexCostAllocationPolicyDescription,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "fca_policy_id" in value:
        pairs.append((f"{key_prefix}FcaPolicyId", str(value["fca_policy_id"])))
    if "fca_policy_arn" in value:
        pairs.append((f"{key_prefix}FcaPolicyArn", str(value["fca_policy_arn"])))
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
    if "owner_account" in value:
        pairs.append((f"{key_prefix}OwnerAccount", str(value["owner_account"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "latest_version" in value:
        pairs.append((f"{key_prefix}LatestVersion", str(value["latest_version"])))
    if "version_expected_effective_at" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["version_expected_effective_at"],
            pairs,
            f"{key_prefix}VersionExpectedEffectiveAt",
        )
    if "policy_created_at" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["policy_created_at"], pairs, f"{key_prefix}PolicyCreatedAt"
        )
    if "updated_at" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["updated_at"], pairs, f"{key_prefix}UpdatedAt"
        )
    if "managed_by" in value:
        import capo_ec2.types.managed_by

        capo_ec2.types.managed_by.serialize_ec2_query(
            value["managed_by"], pairs, f"{key_prefix}ManagedBy"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_ec2_query(el: Element) -> FlexCostAllocationPolicyDescription:
    out: FlexCostAllocationPolicyDescription = {}  # type: ignore[typeddict-item]
    child_fca_policy_id = el.find("fcaPolicyId")
    if child_fca_policy_id is not None:
        out["fca_policy_id"] = str(child_fca_policy_id.text or "")
    child_fca_policy_arn = el.find("fcaPolicyArn")
    if child_fca_policy_arn is not None:
        out["fca_policy_arn"] = str(child_fca_policy_arn.text or "")
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
    child_owner_account = el.find("ownerAccount")
    if child_owner_account is not None:
        out["owner_account"] = str(child_owner_account.text or "")
    child_description = el.find("description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_latest_version = el.find("latestVersion")
    if child_latest_version is not None:
        out["latest_version"] = int(child_latest_version.text or "")
    child_version_expected_effective_at = el.find("versionExpectedEffectiveAt")
    if child_version_expected_effective_at is not None:
        import capo_ec2.types.date_time

        out["version_expected_effective_at"] = (
            capo_ec2.types.date_time.deserialize_ec2_query(
                child_version_expected_effective_at
            )
        )
    child_policy_created_at = el.find("policyCreatedAt")
    if child_policy_created_at is not None:
        import capo_ec2.types.date_time

        out["policy_created_at"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_policy_created_at
        )
    child_updated_at = el.find("updatedAt")
    if child_updated_at is not None:
        import capo_ec2.types.date_time

        out["updated_at"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_updated_at
        )
    child_managed_by = el.find("managedBy")
    if child_managed_by is not None:
        import capo_ec2.types.managed_by

        out["managed_by"] = capo_ec2.types.managed_by.deserialize_ec2_query(
            child_managed_by
        )
    child_tags = el.find("tags")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    return out
