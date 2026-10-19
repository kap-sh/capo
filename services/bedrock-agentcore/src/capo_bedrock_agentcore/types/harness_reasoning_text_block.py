"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessReasoningTextBlock``."""

from typing_extensions import NotRequired, TypedDict


class HarnessReasoningTextBlock(TypedDict, closed=True):
    text: "str"
    """<p>The reasoning text.</p>"""
    signature: NotRequired["str"]
    """<p>Signature for verifying the reasoning content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessReasoningTextBlock) -> dict:
    out: dict = {}
    out["text"] = value["text"]
    if "signature" in value:
        out["signature"] = value["signature"]
    return out


def deserialize_json(data: dict) -> HarnessReasoningTextBlock:
    out: HarnessReasoningTextBlock = {}  # type: ignore[typeddict-item]
    if data.get("text") is not None:
        out["text"] = data["text"]
    else:
        out["text"] = ""
    if data.get("signature") is not None:
        out["signature"] = data["signature"]
    return out
