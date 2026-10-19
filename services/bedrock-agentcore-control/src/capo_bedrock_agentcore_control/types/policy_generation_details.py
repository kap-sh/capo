"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PolicyGenerationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.resource_id


class PolicyGenerationDetails(TypedDict, closed=True):
    policy_generation_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The unique identifier for this policy generation request.</p>"""
    policy_generation_asset_id: (
        "capo_bedrock_agentcore_control.types.resource_id.ResourceId"
    )
    """<p>The unique identifier for this generated policy asset within the policy generation request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolicyGenerationDetails) -> dict:
    out: dict = {}
    out["policyGenerationId"] = value["policy_generation_id"]
    out["policyGenerationAssetId"] = value["policy_generation_asset_id"]
    return out


def deserialize_json(data: dict) -> PolicyGenerationDetails:
    out: PolicyGenerationDetails = {}  # type: ignore[typeddict-item]
    if data.get("policyGenerationId") is not None:
        out["policy_generation_id"] = data["policyGenerationId"]
    else:
        out["policy_generation_id"] = ""
    if data.get("policyGenerationAssetId") is not None:
        out["policy_generation_asset_id"] = data["policyGenerationAssetId"]
    else:
        out["policy_generation_asset_id"] = ""
    return out
