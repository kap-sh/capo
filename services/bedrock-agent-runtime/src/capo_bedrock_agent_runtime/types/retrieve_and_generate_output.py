"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrieveAndGenerateOutput``."""

from typing_extensions import TypedDict


class RetrieveAndGenerateOutput(TypedDict, closed=True):
    text: "str"
    """<p>The response generated from querying the knowledge base.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrieveAndGenerateOutput) -> dict:
    out: dict = {}
    out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> RetrieveAndGenerateOutput:
    out: RetrieveAndGenerateOutput = {}  # type: ignore[typeddict-item]
    if data.get("text") is not None:
        out["text"] = data["text"]
    else:
        out["text"] = ""
    return out
