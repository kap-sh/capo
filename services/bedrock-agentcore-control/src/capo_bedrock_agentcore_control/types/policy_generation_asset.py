"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PolicyGenerationAsset``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.findings
    import capo_bedrock_agentcore_control.types.natural_language
    import capo_bedrock_agentcore_control.types.policy_definition
    import capo_bedrock_agentcore_control.types.resource_id


class PolicyGenerationAsset(TypedDict, closed=True):
    policy_generation_asset_id: (
        "capo_bedrock_agentcore_control.types.resource_id.ResourceId"
    )
    """<p>The unique identifier for this generated policy asset within the policy generation request. This ID can be used to reference specific generated policy options when creating actual policies from the generation results.</p>"""
    definition: NotRequired[
        "capo_bedrock_agentcore_control.types.policy_definition.PolicyDefinition"
    ]
    raw_text_fragment: (
        "capo_bedrock_agentcore_control.types.natural_language.NaturalLanguage"
    )
    """<p>The portion of the original natural language input that this generated policy asset addresses. This helps users understand which part of their policy description was translated into this specific Dogwood policy statement, enabling better policy selection and refinement. When a single natural language input describes multiple authorization requirements, the generation process creates separate policy assets for each requirement, with each asset's rawTextFragment showing which requirement it addresses. Use this mapping to verify that all parts of your natural language input were correctly translated into Dogwood policies.</p>"""
    findings: "capo_bedrock_agentcore_control.types.findings.Findings"
    """<p>Analysis findings and insights related to this specific generated policy asset. These findings may include validation results, potential issues, or recommendations for improvement to help users evaluate the quality and appropriateness of the generated policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolicyGenerationAsset) -> dict:
    out: dict = {}
    out["policyGenerationAssetId"] = value["policy_generation_asset_id"]
    if "definition" in value:
        import capo_bedrock_agentcore_control.types.policy_definition

        out["definition"] = (
            capo_bedrock_agentcore_control.types.policy_definition.serialize_json(
                value["definition"]
            )
        )
    out["rawTextFragment"] = value["raw_text_fragment"]
    import capo_bedrock_agentcore_control.types.findings

    out["findings"] = capo_bedrock_agentcore_control.types.findings.serialize_json(
        value["findings"]
    )
    return out


def deserialize_json(data: dict) -> PolicyGenerationAsset:
    out: PolicyGenerationAsset = {}  # type: ignore[typeddict-item]
    if data.get("policyGenerationAssetId") is not None:
        out["policy_generation_asset_id"] = data["policyGenerationAssetId"]
    else:
        out["policy_generation_asset_id"] = ""
    if data.get("definition") is not None:
        import capo_bedrock_agentcore_control.types.policy_definition

        out["definition"] = (
            capo_bedrock_agentcore_control.types.policy_definition.deserialize_json(
                data["definition"]
            )
        )
    if data.get("rawTextFragment") is not None:
        out["raw_text_fragment"] = data["rawTextFragment"]
    else:
        out["raw_text_fragment"] = ""
    if data.get("findings") is not None:
        import capo_bedrock_agentcore_control.types.findings

        out["findings"] = (
            capo_bedrock_agentcore_control.types.findings.deserialize_json(
                data["findings"]
            )
        )
    else:
        out["findings"] = []
    return out
