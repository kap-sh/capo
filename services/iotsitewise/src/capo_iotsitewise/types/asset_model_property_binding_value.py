"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelPropertyBindingValue``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.id


class AssetModelPropertyBindingValue(TypedDict, closed=True):
    asset_model_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the asset model, in UUID format.</p>"""
    property_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the asset model property used in data binding value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelPropertyBindingValue) -> dict:
    out: dict = {}
    out["assetModelId"] = value["asset_model_id"]
    out["propertyId"] = value["property_id"]
    return out


def deserialize_json(data: dict) -> AssetModelPropertyBindingValue:
    out: AssetModelPropertyBindingValue = {}  # type: ignore[typeddict-item]
    if data.get("assetModelId") is not None:
        out["asset_model_id"] = data["assetModelId"]
    else:
        out["asset_model_id"] = ""
    if data.get("propertyId") is not None:
        out["property_id"] = data["propertyId"]
    else:
        out["property_id"] = ""
    return out
