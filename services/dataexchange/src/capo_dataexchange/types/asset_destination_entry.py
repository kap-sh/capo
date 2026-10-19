"""Generated from Smithy shape ``com.amazonaws.dataexchange#AssetDestinationEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.__string
    import capo_dataexchange.types.id


class AssetDestinationEntry(TypedDict, closed=True):
    asset_id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for the asset.</p>"""
    bucket: "capo_dataexchange.types.__string.__string"
    """<p>The Amazon S3 bucket that is the destination for the asset.</p>"""
    key: NotRequired["capo_dataexchange.types.__string.__string"]
    """<p>The name of the object in Amazon S3 for the asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetDestinationEntry) -> dict:
    out: dict = {}
    out["AssetId"] = value["asset_id"]
    out["Bucket"] = value["bucket"]
    if "key" in value:
        out["Key"] = value["key"]
    return out


def deserialize_json(data: dict) -> AssetDestinationEntry:
    out: AssetDestinationEntry = {}  # type: ignore[typeddict-item]
    if data.get("AssetId") is not None:
        out["asset_id"] = data["AssetId"]
    else:
        out["asset_id"] = ""
    if data.get("Bucket") is not None:
        out["bucket"] = data["Bucket"]
    else:
        out["bucket"] = ""
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    return out
