"""Generated from Smithy shape ``com.amazonaws.cloudfrontkeyvaluestore#DeleteKeyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudfront_keyvaluestore.types.etag


class DeleteKeyResponse(TypedDict, closed=True):
    item_count: "int"
    """<p>Number of key value pairs in the Key Value Store after the successful delete.</p>"""
    total_size_in_bytes: "int"
    """<p>Total size of the Key Value Store after the successful delete, in bytes.</p>"""
    e_tag: "capo_cloudfront_keyvaluestore.types.etag.Etag"
    """<p>The current version identifier of the Key Value Store after the successful delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteKeyResponse) -> dict:
    out: dict = {}
    out["ItemCount"] = value["item_count"]
    out["TotalSizeInBytes"] = value["total_size_in_bytes"]
    return out


def deserialize_json(data: dict) -> DeleteKeyResponse:
    out: DeleteKeyResponse = {}  # type: ignore[typeddict-item]
    if data.get("ItemCount") is not None:
        out["item_count"] = data["ItemCount"]
    else:
        out["item_count"] = 0
    if data.get("TotalSizeInBytes") is not None:
        out["total_size_in_bytes"] = data["TotalSizeInBytes"]
    else:
        out["total_size_in_bytes"] = 0
    return out
