"""Generated from Smithy shape ``com.amazonaws.neptunedata#DictionariesInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptunedata.types.storage_metrics


class DictionariesInfo(TypedDict, closed=True):
    total: NotRequired["capo_neptunedata.types.storage_metrics.StorageMetrics"]
    """<p>The total size and entry count across all dictionary entries.</p>"""
    blobs: NotRequired["capo_neptunedata.types.storage_metrics.StorageMetrics"]
    """<p>The size and entry count for the blob (large value) dictionary entries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DictionariesInfo) -> dict:
    out: dict = {}
    if "total" in value:
        import capo_neptunedata.types.storage_metrics

        out["total"] = capo_neptunedata.types.storage_metrics.serialize_json(
            value["total"]
        )
    if "blobs" in value:
        import capo_neptunedata.types.storage_metrics

        out["blobs"] = capo_neptunedata.types.storage_metrics.serialize_json(
            value["blobs"]
        )
    return out


def deserialize_json(data: dict) -> DictionariesInfo:
    out: DictionariesInfo = {}  # type: ignore[typeddict-item]
    if data.get("total") is not None:
        import capo_neptunedata.types.storage_metrics

        out["total"] = capo_neptunedata.types.storage_metrics.deserialize_json(
            data["total"]
        )
    if data.get("blobs") is not None:
        import capo_neptunedata.types.storage_metrics

        out["blobs"] = capo_neptunedata.types.storage_metrics.deserialize_json(
            data["blobs"]
        )
    return out
