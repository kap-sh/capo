"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessTokenUsage``."""

from typing_extensions import NotRequired, TypedDict


class HarnessTokenUsage(TypedDict, closed=True):
    input_tokens: "int"
    """<p>The number of input tokens consumed.</p>"""
    output_tokens: "int"
    """<p>The number of output tokens generated.</p>"""
    total_tokens: "int"
    """<p>The total number of tokens consumed.</p>"""
    cache_read_input_tokens: NotRequired["int"]
    """<p>The number of input tokens read from cache.</p>"""
    cache_write_input_tokens: NotRequired["int"]
    """<p>The number of input tokens written to cache.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessTokenUsage) -> dict:
    out: dict = {}
    out["inputTokens"] = value["input_tokens"]
    out["outputTokens"] = value["output_tokens"]
    out["totalTokens"] = value["total_tokens"]
    if "cache_read_input_tokens" in value:
        out["cacheReadInputTokens"] = value["cache_read_input_tokens"]
    if "cache_write_input_tokens" in value:
        out["cacheWriteInputTokens"] = value["cache_write_input_tokens"]
    return out


def deserialize_json(data: dict) -> HarnessTokenUsage:
    out: HarnessTokenUsage = {}  # type: ignore[typeddict-item]
    if data.get("inputTokens") is not None:
        out["input_tokens"] = data["inputTokens"]
    else:
        out["input_tokens"] = 0
    if data.get("outputTokens") is not None:
        out["output_tokens"] = data["outputTokens"]
    else:
        out["output_tokens"] = 0
    if data.get("totalTokens") is not None:
        out["total_tokens"] = data["totalTokens"]
    else:
        out["total_tokens"] = 0
    if data.get("cacheReadInputTokens") is not None:
        out["cache_read_input_tokens"] = data["cacheReadInputTokens"]
    if data.get("cacheWriteInputTokens") is not None:
        out["cache_write_input_tokens"] = data["cacheWriteInputTokens"]
    return out
