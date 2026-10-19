"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ResolveTo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.id


class ResolveTo(TypedDict, closed=True):
    asset_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the asset that the resource resolves to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResolveTo) -> dict:
    out: dict = {}
    out["assetId"] = value["asset_id"]
    return out


def deserialize_json(data: dict) -> ResolveTo:
    out: ResolveTo = {}  # type: ignore[typeddict-item]
    if data.get("assetId") is not None:
        out["asset_id"] = data["assetId"]
    else:
        out["asset_id"] = ""
    return out
