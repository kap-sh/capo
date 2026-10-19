"""Generated from Smithy shape ``com.amazonaws.panorama#ConflictExceptionErrorArgument``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.string


class ConflictExceptionErrorArgument(TypedDict, closed=True):
    name: "capo_panorama.types.string.String"
    """<p>The error argument's name.</p>"""
    value: "capo_panorama.types.string.String"
    """<p>The error argument's value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictExceptionErrorArgument) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> ConflictExceptionErrorArgument:
    out: ConflictExceptionErrorArgument = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
