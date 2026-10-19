"""Generated from Smithy shape ``com.amazonaws.iotsitewise#HierarchyMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.id


class HierarchyMapping(TypedDict, closed=True):
    asset_model_hierarchy_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the hierarchy in the asset model where the interface is applied.</p>"""
    interface_asset_model_hierarchy_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the hierarchy in the interface asset model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HierarchyMapping) -> dict:
    out: dict = {}
    out["assetModelHierarchyId"] = value["asset_model_hierarchy_id"]
    out["interfaceAssetModelHierarchyId"] = value["interface_asset_model_hierarchy_id"]
    return out


def deserialize_json(data: dict) -> HierarchyMapping:
    out: HierarchyMapping = {}  # type: ignore[typeddict-item]
    if data.get("assetModelHierarchyId") is not None:
        out["asset_model_hierarchy_id"] = data["assetModelHierarchyId"]
    else:
        out["asset_model_hierarchy_id"] = ""
    if data.get("interfaceAssetModelHierarchyId") is not None:
        out["interface_asset_model_hierarchy_id"] = data[
            "interfaceAssetModelHierarchyId"
        ]
    else:
        out["interface_asset_model_hierarchy_id"] = ""
    return out
