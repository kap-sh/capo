"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrieveAndGenerateInput``."""

from typing_extensions import TypedDict


class RetrieveAndGenerateInput(TypedDict, closed=True):
    text: "str"
    """<p>The query made to the knowledge base, in characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrieveAndGenerateInput) -> dict:
    out: dict = {}
    out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> RetrieveAndGenerateInput:
    out: RetrieveAndGenerateInput = {}  # type: ignore[typeddict-item]
    if data.get("text") is not None:
        out["text"] = data["text"]
    else:
        out["text"] = ""
    return out
