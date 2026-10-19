"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#PutConfiguredAudienceModelPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.configured_audience_model_arn
    import capo_cleanroomsml.types.hash
    import capo_cleanroomsml.types.policy_existence_condition
    import capo_cleanroomsml.types.resource_policy


class PutConfiguredAudienceModelPolicyRequest(TypedDict, closed=True):
    configured_audience_model_arn: "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn"
    """<p>The Amazon Resource Name (ARN) of the configured audience model that the resource policy will govern.</p>"""
    configured_audience_model_policy: (
        "capo_cleanroomsml.types.resource_policy.ResourcePolicy"
    )
    """<p>The IAM resource policy.</p>"""
    previous_policy_hash: NotRequired["capo_cleanroomsml.types.hash.Hash"]
    """<p>A cryptographic hash of the contents of the policy used to prevent unexpected concurrent modification of the policy.</p>"""
    policy_existence_condition: NotRequired[
        "capo_cleanroomsml.types.policy_existence_condition.PolicyExistenceCondition"
    ]
    """<p>Use this to prevent unexpected concurrent modification of the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutConfiguredAudienceModelPolicyRequest) -> dict:
    out: dict = {}
    out["configuredAudienceModelPolicy"] = value["configured_audience_model_policy"]
    if "previous_policy_hash" in value:
        out["previousPolicyHash"] = value["previous_policy_hash"]
    if "policy_existence_condition" in value:
        import capo_cleanroomsml.types.policy_existence_condition

        out["policyExistenceCondition"] = (
            capo_cleanroomsml.types.policy_existence_condition.serialize_json(
                value["policy_existence_condition"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutConfiguredAudienceModelPolicyRequest:
    out: PutConfiguredAudienceModelPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("configuredAudienceModelPolicy") is not None:
        out["configured_audience_model_policy"] = data["configuredAudienceModelPolicy"]
    else:
        out["configured_audience_model_policy"] = ""
    if data.get("previousPolicyHash") is not None:
        out["previous_policy_hash"] = data["previousPolicyHash"]
    if data.get("policyExistenceCondition") is not None:
        import capo_cleanroomsml.types.policy_existence_condition

        out["policy_existence_condition"] = (
            capo_cleanroomsml.types.policy_existence_condition.deserialize_json(
                data["policyExistenceCondition"]
            )
        )
    return out
