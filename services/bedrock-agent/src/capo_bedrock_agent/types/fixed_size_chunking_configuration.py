"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FixedSizeChunkingConfiguration``."""

from typing_extensions import TypedDict


class FixedSizeChunkingConfiguration(TypedDict, closed=True):
    max_tokens: "int"
    """<p>The maximum number of tokens to include in a chunk.</p>"""
    overlap_percentage: "int"
    """<p>The percentage of overlap between adjacent chunks of a data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FixedSizeChunkingConfiguration) -> dict:
    out: dict = {}
    out["maxTokens"] = value["max_tokens"]
    out["overlapPercentage"] = value["overlap_percentage"]
    return out


def deserialize_json(data: dict) -> FixedSizeChunkingConfiguration:
    out: FixedSizeChunkingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("maxTokens") is not None:
        out["max_tokens"] = data["maxTokens"]
    else:
        out["max_tokens"] = 0
    if data.get("overlapPercentage") is not None:
        out["overlap_percentage"] = data["overlapPercentage"]
    else:
        out["overlap_percentage"] = 0
    return out
