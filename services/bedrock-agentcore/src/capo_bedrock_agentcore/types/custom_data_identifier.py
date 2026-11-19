"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CustomDataIdentifier``."""

from typing_extensions import TypedDict


class CustomDataIdentifier(TypedDict, closed=True):
    name: "str"
    """<p>The name of the custom data identifier. It can't be the same as the name of a managed data identifier.</p>"""
    regex: "str"
    """<p>The regular expression that matches the data to mask. Lookahead and lookbehind aren't supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomDataIdentifier) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["regex"] = value["regex"]
    return out


def deserialize_json(data: dict) -> CustomDataIdentifier:
    out: CustomDataIdentifier = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("regex") is not None:
        out["regex"] = data["regex"]
    else:
        out["regex"] = ""
    return out
