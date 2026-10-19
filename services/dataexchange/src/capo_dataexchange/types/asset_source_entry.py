"""Generated from Smithy shape ``com.amazonaws.dataexchange#AssetSourceEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.__string


class AssetSourceEntry(TypedDict, closed=True):
    bucket: "capo_dataexchange.types.__string.__string"
    """<p>The Amazon S3 bucket that's part of the source of the asset.</p>"""
    key: "capo_dataexchange.types.__string.__string"
    """<p>The name of the object in Amazon S3 for the asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetSourceEntry) -> dict:
    out: dict = {}
    out["Bucket"] = value["bucket"]
    out["Key"] = value["key"]
    return out


def deserialize_json(data: dict) -> AssetSourceEntry:
    out: AssetSourceEntry = {}  # type: ignore[typeddict-item]
    if data.get("Bucket") is not None:
        out["bucket"] = data["Bucket"]
    else:
        out["bucket"] = ""
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        out["key"] = ""
    return out
