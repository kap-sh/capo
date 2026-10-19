"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#KeyTypeArguments``."""

from typing_extensions import TypedDict


class KeyTypeArguments(TypedDict, closed=True):
    text: "str"
    """<p>The text string to type. Maximum length: 10,000 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KeyTypeArguments) -> dict:
    out: dict = {}
    out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> KeyTypeArguments:
    out: KeyTypeArguments = {}  # type: ignore[typeddict-item]
    if data.get("text") is not None:
        out["text"] = data["text"]
    else:
        out["text"] = ""
    return out
