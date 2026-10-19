"""Generated from Smithy shape ``com.amazonaws.entityresolution#OutputAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.attribute_name


class OutputAttribute(TypedDict, closed=True):
    name: "capo_entityresolution.types.attribute_name.AttributeName"
    """<p>A name of a column to be written to the output. This must be an <code>InputField</code> name in the schema mapping.</p>"""
    hashed: NotRequired["bool"]
    """<p>Enables the ability to hash the column values in the output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputAttribute) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "hashed" in value:
        out["hashed"] = value["hashed"]
    return out


def deserialize_json(data: dict) -> OutputAttribute:
    out: OutputAttribute = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("hashed") is not None:
        out["hashed"] = data["hashed"]
    return out
