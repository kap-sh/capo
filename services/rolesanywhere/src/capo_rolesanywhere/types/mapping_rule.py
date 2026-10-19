"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#MappingRule``."""

from typing_extensions import TypedDict


class MappingRule(TypedDict, closed=True):
    specifier: "str"
    """<p>Specifier within a certificate field, such as CN, OU, or UID from the Subject field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MappingRule) -> dict:
    out: dict = {}
    out["specifier"] = value["specifier"]
    return out


def deserialize_json(data: dict) -> MappingRule:
    out: MappingRule = {}  # type: ignore[typeddict-item]
    if data.get("specifier") is not None:
        out["specifier"] = data["specifier"]
    else:
        out["specifier"] = ""
    return out
