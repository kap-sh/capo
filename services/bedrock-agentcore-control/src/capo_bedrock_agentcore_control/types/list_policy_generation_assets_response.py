"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListPolicyGenerationAssetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.next_token
    import capo_bedrock_agentcore_control.types.policy_generation_assets


class ListPolicyGenerationAssetsResponse(TypedDict, closed=True):
    policy_generation_assets: NotRequired[
        "capo_bedrock_agentcore_control.types.policy_generation_assets.PolicyGenerationAssets"
    ]
    """<p>An array of generated policy assets including Dogwood policies and related artifacts from the AI-powered policy generation process. Each asset represents a different policy option or variation generated from the original natural language input.</p>"""
    next_token: NotRequired["capo_bedrock_agentcore_control.types.next_token.NextToken"]
    """<p>A pagination token that can be used in subsequent <a href="https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicyGenerationAssets.html">ListPolicyGenerationAssets</a> calls to retrieve additional assets. This token is only present when there are more generated policy assets available beyond the current response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPolicyGenerationAssetsResponse) -> dict:
    out: dict = {}
    if "policy_generation_assets" in value:
        import capo_bedrock_agentcore_control.types.policy_generation_assets

        out["policyGenerationAssets"] = (
            capo_bedrock_agentcore_control.types.policy_generation_assets.serialize_json(
                value["policy_generation_assets"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPolicyGenerationAssetsResponse:
    out: ListPolicyGenerationAssetsResponse = {}  # type: ignore[typeddict-item]
    if data.get("policyGenerationAssets") is not None:
        import capo_bedrock_agentcore_control.types.policy_generation_assets

        out["policy_generation_assets"] = (
            capo_bedrock_agentcore_control.types.policy_generation_assets.deserialize_json(
                data["policyGenerationAssets"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
