"""Generated from Smithy shape ``com.amazonaws.datazone#AssetPermission``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.asset_id
    import capo_datazone.types.permissions


class AssetPermission(TypedDict, closed=True):
    asset_id: "capo_datazone.types.asset_id.AssetId"
    """<p>The asset ID as part of the asset permissions.</p>"""
    permissions: "capo_datazone.types.permissions.Permissions"
    """<p>The details as part of the asset permissions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetPermission) -> dict:
    out: dict = {}
    out["assetId"] = value["asset_id"]
    import capo_datazone.types.permissions

    out["permissions"] = capo_datazone.types.permissions.serialize_json(
        value["permissions"]
    )
    return out


def deserialize_json(data: dict) -> AssetPermission:
    out: AssetPermission = {}  # type: ignore[typeddict-item]
    if data.get("assetId") is not None:
        out["asset_id"] = data["assetId"]
    else:
        out["asset_id"] = ""
    if data.get("permissions") is not None:
        import capo_datazone.types.permissions

        out["permissions"] = capo_datazone.types.permissions.deserialize_json(
            data["permissions"]
        )
    else:
        out["permissions"] = {"$unknown": {"name": ""}}
    return out
