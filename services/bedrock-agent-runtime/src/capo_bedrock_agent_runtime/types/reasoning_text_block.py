"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ReasoningTextBlock``."""

from typing_extensions import NotRequired, TypedDict


class ReasoningTextBlock(TypedDict, closed=True):
    text: "str"
    """<p>Text describing the reasoning that the model used to return the content in the content block.</p>"""
    signature: NotRequired["str"]
    """<p>A hash of all the messages in the conversation to ensure that the content in the reasoning text block isn't tampered with. You must submit the signature in subsequent <code>Converse</code> requests, in addition to the previous messages. If the previous messages are tampered with, the response throws an error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReasoningTextBlock) -> dict:
    out: dict = {}
    out["text"] = value["text"]
    if "signature" in value:
        out["signature"] = value["signature"]
    return out


def deserialize_json(data: dict) -> ReasoningTextBlock:
    out: ReasoningTextBlock = {}  # type: ignore[typeddict-item]
    if data.get("text") is not None:
        out["text"] = data["text"]
    else:
        out["text"] = ""
    if data.get("signature") is not None:
        out["signature"] = data["signature"]
    return out
