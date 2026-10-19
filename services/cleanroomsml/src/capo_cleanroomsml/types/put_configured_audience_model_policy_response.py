"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#PutConfiguredAudienceModelPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.hash
    import capo_cleanroomsml.types.resource_policy


class PutConfiguredAudienceModelPolicyResponse(TypedDict, closed=True):
    configured_audience_model_policy: (
        "capo_cleanroomsml.types.resource_policy.ResourcePolicy"
    )
    """<p>The IAM resource policy.</p>"""
    policy_hash: "capo_cleanroomsml.types.hash.Hash"
    """<p>A cryptographic hash of the contents of the policy used to prevent unexpected concurrent modification of the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutConfiguredAudienceModelPolicyResponse) -> dict:
    out: dict = {}
    out["configuredAudienceModelPolicy"] = value["configured_audience_model_policy"]
    out["policyHash"] = value["policy_hash"]
    return out


def deserialize_json(data: dict) -> PutConfiguredAudienceModelPolicyResponse:
    out: PutConfiguredAudienceModelPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("configuredAudienceModelPolicy") is not None:
        out["configured_audience_model_policy"] = data["configuredAudienceModelPolicy"]
    else:
        out["configured_audience_model_policy"] = ""
    if data.get("policyHash") is not None:
        out["policy_hash"] = data["policyHash"]
    else:
        out["policy_hash"] = ""
    return out
