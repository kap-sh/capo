"""Generated from Smithy shape ``com.amazonaws.datazone#AssetTargetNameMap``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.asset_id


class AssetTargetNameMap(TypedDict, closed=True):
    asset_id: "capo_datazone.types.asset_id.AssetId"
    """<p>The identifier of the inventory asset.</p>"""
    target_name: "str"
    """<p>The target name in the asset target name map.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetTargetNameMap) -> dict:
    out: dict = {}
    out["assetId"] = value["asset_id"]
    out["targetName"] = value["target_name"]
    return out


def deserialize_json(data: dict) -> AssetTargetNameMap:
    out: AssetTargetNameMap = {}  # type: ignore[typeddict-item]
    if data.get("assetId") is not None:
        out["asset_id"] = data["assetId"]
    else:
        out["asset_id"] = ""
    if data.get("targetName") is not None:
        out["target_name"] = data["targetName"]
    else:
        out["target_name"] = ""
    return out
