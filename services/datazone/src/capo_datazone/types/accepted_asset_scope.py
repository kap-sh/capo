"""Generated from Smithy shape ``com.amazonaws.datazone#AcceptedAssetScope``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.asset_id
    import capo_datazone.types.filter_ids


class AcceptedAssetScope(TypedDict, closed=True):
    asset_id: "capo_datazone.types.asset_id.AssetId"
    """<p>The asset ID of the accepted asset scope.</p>"""
    filter_ids: "capo_datazone.types.filter_ids.FilterIds"
    """<p>The filter IDs of the accepted asset scope.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcceptedAssetScope) -> dict:
    out: dict = {}
    out["assetId"] = value["asset_id"]
    import capo_datazone.types.filter_ids

    out["filterIds"] = capo_datazone.types.filter_ids.serialize_json(
        value["filter_ids"]
    )
    return out


def deserialize_json(data: dict) -> AcceptedAssetScope:
    out: AcceptedAssetScope = {}  # type: ignore[typeddict-item]
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
    return out
