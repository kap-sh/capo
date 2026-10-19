"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetPropertyBindingValueFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.id


class AssetPropertyBindingValueFilter(TypedDict, closed=True):
    asset_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the asset containing the property to filter by. This identifies the specific asset instance containing the property of interest.</p>"""
    property_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the property within the asset to filter by. Only data bindings referencing this specific property of the specified asset are matched.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetPropertyBindingValueFilter) -> dict:
    out: dict = {}
    out["assetId"] = value["asset_id"]
    out["propertyId"] = value["property_id"]
    return out


def deserialize_json(data: dict) -> AssetPropertyBindingValueFilter:
    out: AssetPropertyBindingValueFilter = {}  # type: ignore[typeddict-item]
    if data.get("assetId") is not None:
        out["asset_id"] = data["assetId"]
    else:
        out["asset_id"] = ""
    if data.get("propertyId") is not None:
        out["property_id"] = data["propertyId"]
    else:
        out["property_id"] = ""
    return out
