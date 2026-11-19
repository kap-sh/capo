"""Generated from Smithy shape ``com.amazonaws.ec2#CreateNetworkingFlexCostAllocationPolicyResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.date_time
    import capo_ec2.types.flex_cost_allocation_policy_arn
    import capo_ec2.types.flex_cost_allocation_policy_id


class CreateNetworkingFlexCostAllocationPolicyResult(TypedDict, closed=True):
    fca_policy_id: NotRequired[
        "capo_ec2.types.flex_cost_allocation_policy_id.FlexCostAllocationPolicyId"
    ]
    """<p>The ID of the flex cost allocation policy.</p>"""
    fca_policy_arn: NotRequired[
        "capo_ec2.types.flex_cost_allocation_policy_arn.FlexCostAllocationPolicyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the flex cost allocation policy.</p>"""
    created_at: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The date and time when the policy was created.</p>"""
    expected_effective_at: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The date and time when the policy is expected to apply to network traffic.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateNetworkingFlexCostAllocationPolicyResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "fca_policy_id" in value:
        pairs.append((f"{key_prefix}FcaPolicyId", str(value["fca_policy_id"])))
    if "fca_policy_arn" in value:
        pairs.append((f"{key_prefix}FcaPolicyArn", str(value["fca_policy_arn"])))
    if "created_at" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["created_at"], pairs, f"{key_prefix}CreatedAt"
        )
    if "expected_effective_at" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["expected_effective_at"], pairs, f"{key_prefix}ExpectedEffectiveAt"
        )


def deserialize_ec2_query(
    el: Element,
) -> CreateNetworkingFlexCostAllocationPolicyResult:
    out: CreateNetworkingFlexCostAllocationPolicyResult = {}  # type: ignore[typeddict-item]
    child_fca_policy_id = el.find("fcaPolicyId")
    if child_fca_policy_id is not None:
        out["fca_policy_id"] = str(child_fca_policy_id.text or "")
    child_fca_policy_arn = el.find("fcaPolicyArn")
    if child_fca_policy_arn is not None:
        out["fca_policy_arn"] = str(child_fca_policy_arn.text or "")
    child_created_at = el.find("createdAt")
    if child_created_at is not None:
        import capo_ec2.types.date_time

        out["created_at"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_created_at
        )
    child_expected_effective_at = el.find("expectedEffectiveAt")
    if child_expected_effective_at is not None:
        import capo_ec2.types.date_time

        out["expected_effective_at"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_expected_effective_at
        )
    return out
