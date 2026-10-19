"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetPropertyBindingValue``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.id


class AssetPropertyBindingValue(TypedDict, closed=True):
    asset_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the asset containing the property. This identifies the specific asset instance's property value used in the computation model.</p>"""
    property_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the property within the asset. This identifies the specific property's value used in the computation model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetPropertyBindingValue) -> dict:
    out: dict = {}
    out["assetId"] = value["asset_id"]
    out["propertyId"] = value["property_id"]
    return out


def deserialize_json(data: dict) -> AssetPropertyBindingValue:
    out: AssetPropertyBindingValue = {}  # type: ignore[typeddict-item]
    if data.get("assetId") is not None:
        out["asset_id"] = data["assetId"]
    else:
        out["asset_id"] = ""
    if data.get("propertyId") is not None:
        out["property_id"] = data["propertyId"]
    else:
        out["property_id"] = ""
    return out
