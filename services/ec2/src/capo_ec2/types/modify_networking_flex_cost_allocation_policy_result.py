"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyNetworkingFlexCostAllocationPolicyResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.date_time
    import capo_ec2.types.flex_cost_allocation_policy_id
    import capo_ec2.types.flex_cost_allocation_policy_version_number


class ModifyNetworkingFlexCostAllocationPolicyResult(TypedDict, closed=True):
    fca_policy_id: NotRequired[
        "capo_ec2.types.flex_cost_allocation_policy_id.FlexCostAllocationPolicyId"
    ]
    """<p>The ID of the flex cost allocation policy.</p>"""
    updated_at: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The date and time when the policy was updated.</p>"""
    version: NotRequired[
        "capo_ec2.types.flex_cost_allocation_policy_version_number.FlexCostAllocationPolicyVersionNumber"
    ]
    """<p>The version number of the policy that this modification created.</p>"""
    version_expected_effective_at: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The date and time when the new version of the policy is expected to apply to network traffic.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyNetworkingFlexCostAllocationPolicyResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "fca_policy_id" in value:
        pairs.append((f"{key_prefix}FcaPolicyId", str(value["fca_policy_id"])))
    if "updated_at" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["updated_at"], pairs, f"{key_prefix}UpdatedAt"
        )
    if "version" in value:
        pairs.append((f"{key_prefix}Version", str(value["version"])))
    if "version_expected_effective_at" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["version_expected_effective_at"],
            pairs,
            f"{key_prefix}VersionExpectedEffectiveAt",
        )


def deserialize_ec2_query(
    el: Element,
) -> ModifyNetworkingFlexCostAllocationPolicyResult:
    out: ModifyNetworkingFlexCostAllocationPolicyResult = {}  # type: ignore[typeddict-item]
    child_fca_policy_id = el.find("fcaPolicyId")
    if child_fca_policy_id is not None:
        out["fca_policy_id"] = str(child_fca_policy_id.text or "")
    child_updated_at = el.find("updatedAt")
    if child_updated_at is not None:
        import capo_ec2.types.date_time

        out["updated_at"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_updated_at
        )
    child_version = el.find("version")
    if child_version is not None:
        out["version"] = int(child_version.text or "")
    child_version_expected_effective_at = el.find("versionExpectedEffectiveAt")
    if child_version_expected_effective_at is not None:
        import capo_ec2.types.date_time

        out["version_expected_effective_at"] = (
            capo_ec2.types.date_time.deserialize_ec2_query(
                child_version_expected_effective_at
            )
        )
    return out
