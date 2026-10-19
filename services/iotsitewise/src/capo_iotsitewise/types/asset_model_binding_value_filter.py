"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelBindingValueFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.id


class AssetModelBindingValueFilter(TypedDict, closed=True):
    asset_model_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the asset model to filter data bindings by. Only data bindings referemncing this specific asset model are matched.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelBindingValueFilter) -> dict:
    out: dict = {}
    out["assetModelId"] = value["asset_model_id"]
    return out


def deserialize_json(data: dict) -> AssetModelBindingValueFilter:
    out: AssetModelBindingValueFilter = {}  # type: ignore[typeddict-item]
    if data.get("assetModelId") is not None:
        out["asset_model_id"] = data["assetModelId"]
    else:
        out["asset_model_id"] = ""
    return out
