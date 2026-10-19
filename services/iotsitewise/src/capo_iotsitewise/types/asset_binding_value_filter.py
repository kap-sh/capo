"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetBindingValueFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.id


class AssetBindingValueFilter(TypedDict, closed=True):
    asset_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the asset to filter data bindings by. Only data bindings referencing this specific asset are matched.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBindingValueFilter) -> dict:
    out: dict = {}
    out["assetId"] = value["asset_id"]
    return out


def deserialize_json(data: dict) -> AssetBindingValueFilter:
    out: AssetBindingValueFilter = {}  # type: ignore[typeddict-item]
    if data.get("assetId") is not None:
        out["asset_id"] = data["assetId"]
    else:
        out["asset_id"] = ""
    return out
