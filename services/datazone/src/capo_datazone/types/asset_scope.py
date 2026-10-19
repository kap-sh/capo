"""Generated from Smithy shape ``com.amazonaws.datazone#AssetScope``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.asset_id
    import capo_datazone.types.filter_ids


class AssetScope(TypedDict, closed=True):
    asset_id: "capo_datazone.types.asset_id.AssetId"
    """<p>The asset ID of the asset scope.</p>"""
    filter_ids: "capo_datazone.types.filter_ids.FilterIds"
    """<p>The filter IDs of the asset scope.</p>"""
    status: "str"
    """<p>The status of the asset scope.</p>"""
    scope_name: NotRequired["str"]
    """<p>The name of the materialized asset scope.</p>"""
    error_message: NotRequired["str"]
    """<p>The error message of the asset scope.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetScope) -> dict:
    out: dict = {}
    out["assetId"] = value["asset_id"]
    import capo_datazone.types.filter_ids

    out["filterIds"] = capo_datazone.types.filter_ids.serialize_json(
        value["filter_ids"]
    )
    out["status"] = value["status"]
    if "scope_name" in value:
        out["scopeName"] = value["scope_name"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> AssetScope:
    out: AssetScope = {}  # type: ignore[typeddict-item]
    if data.get("assetId") is not None:
        out["asset_id"] = data["assetId"]
    else:
        out["asset_id"] = ""
    if data.get("filterIds") is not None:
        import capo_datazone.types.filter_ids

        out["filter_ids"] = capo_datazone.types.filter_ids.deserialize_json(
            data["filterIds"]
        )
    else:
        out["filter_ids"] = []
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("scopeName") is not None:
        out["scope_name"] = data["scopeName"]
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    return out
