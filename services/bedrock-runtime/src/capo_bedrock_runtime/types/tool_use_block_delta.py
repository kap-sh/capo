"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ToolUseBlockDelta``."""

from typing_extensions import TypedDict


class ToolUseBlockDelta(TypedDict, closed=True):
    input: "str"
    """<p>The input for a requested tool.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolUseBlockDelta) -> dict:
    out: dict = {}
    out["input"] = value["input"]
    return out


def deserialize_json(data: dict) -> ToolUseBlockDelta:
    out: ToolUseBlockDelta = {}  # type: ignore[typeddict-item]
    if data.get("input") is not None:
        out["input"] = data["input"]
    else:
        out["input"] = ""
    return out
