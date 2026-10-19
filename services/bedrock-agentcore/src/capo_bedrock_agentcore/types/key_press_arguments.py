"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#KeyPressArguments``."""

from typing_extensions import NotRequired, TypedDict


class KeyPressArguments(TypedDict, closed=True):
    key: "str"
    """<p>The key name to press (for example, <code>enter</code>, <code>tab</code>, <code>escape</code>).</p>"""
    presses: NotRequired["int"]
    """<p>The number of times to press the key. Valid range: 1–100. Defaults to 1.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KeyPressArguments) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    if "presses" in value:
        out["presses"] = value["presses"]
    return out


def deserialize_json(data: dict) -> KeyPressArguments:
    out: KeyPressArguments = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("presses") is not None:
        out["presses"] = data["presses"]
    return out
