"""Generated from Smithy shape ``com.amazonaws.ec2#GetNetworkingFlexCostAllocationPolicyVersionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.flex_cost_allocation_policy_version_set


class GetNetworkingFlexCostAllocationPolicyVersionsResult(TypedDict, closed=True):
    fca_policy_versions: NotRequired[
        "capo_ec2.types.flex_cost_allocation_policy_version_set.FlexCostAllocationPolicyVersionSet"
    ]
    """<p>Information about the policy versions.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetNetworkingFlexCostAllocationPolicyVersionsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "fca_policy_versions" in value:
        import capo_ec2.types.flex_cost_allocation_policy_version_set

        capo_ec2.types.flex_cost_allocation_policy_version_set.serialize_ec2_query(
            value["fca_policy_versions"], pairs, f"{key_prefix}FcaPolicyVersions"
        )


def deserialize_ec2_query(
    el: Element,
) -> GetNetworkingFlexCostAllocationPolicyVersionsResult:
    out: GetNetworkingFlexCostAllocationPolicyVersionsResult = {}  # type: ignore[typeddict-item]
    child_fca_policy_versions = el.find("fcaPolicyVersions")
    if child_fca_policy_versions is not None:
        import capo_ec2.types.flex_cost_allocation_policy_version_set

        out["fca_policy_versions"] = (
            capo_ec2.types.flex_cost_allocation_policy_version_set.deserialize_ec2_query(
                child_fca_policy_versions
            )
        )
    return out
