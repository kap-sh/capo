"""Generated from Smithy shape ``com.amazonaws.opensearch#SavedObjectIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.string


class SavedObjectIdentifier(TypedDict, closed=True):
    type: "capo_opensearch.types.string.String"
    """<p>The type of the saved object, such as <code>dashboard</code>, <code>visualization</code>, <code>index-pattern</code>, <code>search</code>, or <code>query</code>.</p>"""
    id: "capo_opensearch.types.string.String"
    """<p>The unique identifier of the saved object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SavedObjectIdentifier) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> SavedObjectIdentifier:
    out: SavedObjectIdentifier = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    return out
