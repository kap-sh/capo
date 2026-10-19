"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelPropertyBindingValueFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.id


class AssetModelPropertyBindingValueFilter(TypedDict, closed=True):
    asset_model_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the asset model containing the filter property. This identifies the specific asset model that contains the property of interest.</p>"""
    property_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the property within the asset model to filter by. Only data bindings referencing this specific property of the specified asset model are matched.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelPropertyBindingValueFilter) -> dict:
    out: dict = {}
    out["assetModelId"] = value["asset_model_id"]
    out["propertyId"] = value["property_id"]
    return out


def deserialize_json(data: dict) -> AssetModelPropertyBindingValueFilter:
    out: AssetModelPropertyBindingValueFilter = {}  # type: ignore[typeddict-item]
    if data.get("assetModelId") is not None:
        out["asset_model_id"] = data["assetModelId"]
    else:
        out["asset_model_id"] = ""
    if data.get("propertyId") is not None:
        out["property_id"] = data["propertyId"]
    else:
        out["property_id"] = ""
    return out
