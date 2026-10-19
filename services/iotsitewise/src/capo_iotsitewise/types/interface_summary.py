"""Generated from Smithy shape ``com.amazonaws.iotsitewise#InterfaceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.id


class InterfaceSummary(TypedDict, closed=True):
    interface_asset_model_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the interface asset model that contains this property.</p>"""
    interface_asset_model_property_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the property in the interface asset model that corresponds to this property.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InterfaceSummary) -> dict:
    out: dict = {}
    out["interfaceAssetModelId"] = value["interface_asset_model_id"]
    out["interfaceAssetModelPropertyId"] = value["interface_asset_model_property_id"]
    return out


def deserialize_json(data: dict) -> InterfaceSummary:
    out: InterfaceSummary = {}  # type: ignore[typeddict-item]
    if data.get("interfaceAssetModelId") is not None:
        out["interface_asset_model_id"] = data["interfaceAssetModelId"]
    else:
        out["interface_asset_model_id"] = ""
    if data.get("interfaceAssetModelPropertyId") is not None:
        out["interface_asset_model_property_id"] = data["interfaceAssetModelPropertyId"]
    else:
        out["interface_asset_model_property_id"] = ""
    return out
