"""Generated from Smithy shape ``com.amazonaws.ec2#FlexCostAllocationPolicyAssociationDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.date_time
    import capo_ec2.types.flex_cost_allocation_association_mode
    import capo_ec2.types.flex_cost_allocation_policy_association_id
    import capo_ec2.types.flex_cost_allocation_policy_id
    import capo_ec2.types.managed_by
    import capo_ec2.types.string


class FlexCostAllocationPolicyAssociationDescription(TypedDict, closed=True):
    fca_policy_association_id: NotRequired[
        "capo_ec2.types.flex_cost_allocation_policy_association_id.FlexCostAllocationPolicyAssociationId"
    ]
    """<p>The ID of the policy association.</p>"""
    fca_policy_id: NotRequired[
        "capo_ec2.types.flex_cost_allocation_policy_id.FlexCostAllocationPolicyId"
    ]
    """<p>The ID of the policy.</p>"""
    network_resource_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the associated network resource.</p>"""
    owner_account: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the account that owns the association.</p>"""
    associated_at: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The date and time when the association was created.</p>"""
    expected_effective_at: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The date and time when the association is expected to apply to network traffic.</p>"""
    association_mode: NotRequired[
        "capo_ec2.types.flex_cost_allocation_association_mode.FlexCostAllocationAssociationMode"
    ]
    """<p>The mode of the association. Valid values:</p> <ul> <li> <p> <code>direct</code> - The policy is associated with specific resources by resource ID.</p> </li> <li> <p> <code>scope</code> - The policy is associated with a scope of resources in an account, Amazon VPC, or subnet.</p> </li> </ul>"""
    managed_by: NotRequired["capo_ec2.types.managed_by.ManagedBy"]
    """<p>The entity that manages the association. Valid values are:</p> <ul> <li> <p> <code>account</code> - The account that owns the association created it.</p> </li> <li> <p> <code>declarative-policy</code> - An Amazon Web Services Organizations declarative policy created the association. You can't remove the association.</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FlexCostAllocationPolicyAssociationDescription,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "fca_policy_association_id" in value:
        pairs.append(
            (
                f"{key_prefix}FcaPolicyAssociationId",
                str(value["fca_policy_association_id"]),
            )
        )
    if "fca_policy_id" in value:
        pairs.append((f"{key_prefix}FcaPolicyId", str(value["fca_policy_id"])))
    if "network_resource_id" in value:
        pairs.append(
            (f"{key_prefix}NetworkResourceId", str(value["network_resource_id"]))
        )
    if "owner_account" in value:
        pairs.append((f"{key_prefix}OwnerAccount", str(value["owner_account"])))
    if "associated_at" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["associated_at"], pairs, f"{key_prefix}AssociatedAt"
        )
    if "expected_effective_at" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["expected_effective_at"], pairs, f"{key_prefix}ExpectedEffectiveAt"
        )
    if "association_mode" in value:
        import capo_ec2.types.flex_cost_allocation_association_mode

        capo_ec2.types.flex_cost_allocation_association_mode.serialize_ec2_query(
            value["association_mode"], pairs, f"{key_prefix}AssociationMode"
        )
    if "managed_by" in value:
        import capo_ec2.types.managed_by

        capo_ec2.types.managed_by.serialize_ec2_query(
            value["managed_by"], pairs, f"{key_prefix}ManagedBy"
        )


def deserialize_ec2_query(
    el: Element,
) -> FlexCostAllocationPolicyAssociationDescription:
    out: FlexCostAllocationPolicyAssociationDescription = {}  # type: ignore[typeddict-item]
    child_fca_policy_association_id = el.find("fcaPolicyAssociationId")
    if child_fca_policy_association_id is not None:
        out["fca_policy_association_id"] = str(
            child_fca_policy_association_id.text or ""
        )
    child_fca_policy_id = el.find("fcaPolicyId")
    if child_fca_policy_id is not None:
        out["fca_policy_id"] = str(child_fca_policy_id.text or "")
    child_network_resource_id = el.find("networkResourceId")
    if child_network_resource_id is not None:
        out["network_resource_id"] = str(child_network_resource_id.text or "")
    child_owner_account = el.find("ownerAccount")
    if child_owner_account is not None:
        out["owner_account"] = str(child_owner_account.text or "")
    child_associated_at = el.find("associatedAt")
    if child_associated_at is not None:
        import capo_ec2.types.date_time

        out["associated_at"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_associated_at
        )
    child_expected_effective_at = el.find("expectedEffectiveAt")
    if child_expected_effective_at is not None:
        import capo_ec2.types.date_time

        out["expected_effective_at"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_expected_effective_at
        )
    child_association_mode = el.find("associationMode")
    if child_association_mode is not None:
        import capo_ec2.types.flex_cost_allocation_association_mode

        out["association_mode"] = (
            capo_ec2.types.flex_cost_allocation_association_mode.deserialize_ec2_query(
                child_association_mode
            )
        )
    child_managed_by = el.find("managedBy")
    if child_managed_by is not None:
        import capo_ec2.types.managed_by

        out["managed_by"] = capo_ec2.types.managed_by.deserialize_ec2_query(
            child_managed_by
        )
    return out
