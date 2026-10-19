"""Generated from Smithy shape ``com.amazonaws.bedrockagent#HierarchicalChunkingLevelConfiguration``."""

from typing_extensions import TypedDict


class HierarchicalChunkingLevelConfiguration(TypedDict, closed=True):
    max_tokens: "int"
    """<p>The maximum number of tokens that a chunk can contain in this layer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HierarchicalChunkingLevelConfiguration) -> dict:
    out: dict = {}
    out["maxTokens"] = value["max_tokens"]
    return out


def deserialize_json(data: dict) -> HierarchicalChunkingLevelConfiguration:
    out: HierarchicalChunkingLevelConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("maxTokens") is not None:
        out["max_tokens"] = data["maxTokens"]
    else:
        out["max_tokens"] = 0
    return out
