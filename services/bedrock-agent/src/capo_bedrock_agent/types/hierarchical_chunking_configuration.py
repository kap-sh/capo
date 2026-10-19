"""Generated from Smithy shape ``com.amazonaws.bedrockagent#HierarchicalChunkingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.hierarchical_chunking_level_configurations


class HierarchicalChunkingConfiguration(TypedDict, closed=True):
    level_configurations: "capo_bedrock_agent.types.hierarchical_chunking_level_configurations.HierarchicalChunkingLevelConfigurations"
    """<p>Token settings for each layer.</p>"""
    overlap_tokens: "int"
    """<p>The number of tokens to repeat across chunks in the same layer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HierarchicalChunkingConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.hierarchical_chunking_level_configurations

    out["levelConfigurations"] = (
        capo_bedrock_agent.types.hierarchical_chunking_level_configurations.serialize_json(
            value["level_configurations"]
        )
    )
    out["overlapTokens"] = value["overlap_tokens"]
    return out


def deserialize_json(data: dict) -> HierarchicalChunkingConfiguration:
    out: HierarchicalChunkingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("levelConfigurations") is not None:
        import capo_bedrock_agent.types.hierarchical_chunking_level_configurations

        out["level_configurations"] = (
            capo_bedrock_agent.types.hierarchical_chunking_level_configurations.deserialize_json(
                data["levelConfigurations"]
            )
        )
    else:
        out["level_configurations"] = []
    if data.get("overlapTokens") is not None:
        out["overlap_tokens"] = data["overlapTokens"]
    else:
        out["overlap_tokens"] = 0
    return out
