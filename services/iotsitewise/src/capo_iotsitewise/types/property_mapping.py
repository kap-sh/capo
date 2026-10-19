"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PropertyMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.custom_id


class PropertyMapping(TypedDict, closed=True):
    asset_model_property_id: "capo_iotsitewise.types.custom_id.CustomID"
    """<p>The ID of the property in the asset model where the interface is applied.</p>"""
    interface_asset_model_property_id: "capo_iotsitewise.types.custom_id.CustomID"
    """<p>The ID of the property in the interface asset model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PropertyMapping) -> dict:
    out: dict = {}
    out["assetModelPropertyId"] = value["asset_model_property_id"]
    out["interfaceAssetModelPropertyId"] = value["interface_asset_model_property_id"]
    return out


def deserialize_json(data: dict) -> PropertyMapping:
    out: PropertyMapping = {}  # type: ignore[typeddict-item]
    if data.get("assetModelPropertyId") is not None:
        out["asset_model_property_id"] = data["assetModelPropertyId"]
    else:
        out["asset_model_property_id"] = ""
    if data.get("interfaceAssetModelPropertyId") is not None:
        out["interface_asset_model_property_id"] = data["interfaceAssetModelPropertyId"]
    else:
        out["interface_asset_model_property_id"] = ""
    return out
