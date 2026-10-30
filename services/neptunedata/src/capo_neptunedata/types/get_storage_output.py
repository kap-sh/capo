"""Generated from Smithy shape ``com.amazonaws.neptunedata#GetStorageOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptunedata.types.dictionaries_info
    import capo_neptunedata.types.quads_indexes_info
    import capo_neptunedata.types.storage_metrics
    import capo_neptunedata.types.undo_logs_metrics


class GetStorageOutput(TypedDict, closed=True):
    total_storage_bytes_used: NotRequired["int"]
    """<p>The approximate total amount of storage used by the Neptune database instance, in bytes.</p>"""
    quads: NotRequired["capo_neptunedata.types.quads_indexes_info.QuadsIndexesInfo"]
    """<p>Contains information about the quad indexes, including counts and sizes for both RDF (SPARQL) and Property Graph (Gremlin/openCypher) data.</p>"""
    dictionaries: NotRequired[
        "capo_neptunedata.types.dictionaries_info.DictionariesInfo"
    ]
    """<p>Contains information about the dictionaries, including total dictionary storage and the portion used by blob entries. For additional details on the storage of the Neptune dictionary, see <a href="https://docs.aws.amazon.com/neptune/latest/userguide/feature-overview-storage.html#feature-overview-storage-billing">Neptune Storage Billing</a>.</p>"""
    undo_logs: NotRequired["capo_neptunedata.types.undo_logs_metrics.UndoLogsMetrics"]
    """<p>Contains information about the undo logs. The <code>sizeInBytes</code> field represents the total size of the undo logs in bytes, and the <code>listSize</code> field represents the number of entries in the undo log list.</p>"""
    streams: NotRequired["capo_neptunedata.types.storage_metrics.StorageMetrics"]
    """<p>Contains storage metrics for the Neptune change-log streams, including size in bytes and entry count.</p>"""
    dfe_statistics: NotRequired["capo_neptunedata.types.storage_metrics.StorageMetrics"]
    """<p>Contains storage metrics for the Neptune DFE engine statistics, including size in bytes and entry count.</p>"""
    schema: NotRequired["capo_neptunedata.types.storage_metrics.StorageMetrics"]
    """<p>Contains storage metrics for the Neptune schema, including size in bytes and entry count.</p>"""
    internals: NotRequired["capo_neptunedata.types.storage_metrics.StorageMetrics"]
    """<p>Contains storage metrics for Neptune system metadata, including size in bytes and entry count.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStorageOutput) -> dict:
    out: dict = {}
    if "total_storage_bytes_used" in value:
        out["totalStorageBytesUsed"] = value["total_storage_bytes_used"]
    if "quads" in value:
        import capo_neptunedata.types.quads_indexes_info

        out["quads"] = capo_neptunedata.types.quads_indexes_info.serialize_json(
            value["quads"]
        )
    if "dictionaries" in value:
        import capo_neptunedata.types.dictionaries_info

        out["dictionaries"] = capo_neptunedata.types.dictionaries_info.serialize_json(
            value["dictionaries"]
        )
    if "undo_logs" in value:
        import capo_neptunedata.types.undo_logs_metrics

        out["undoLogs"] = capo_neptunedata.types.undo_logs_metrics.serialize_json(
            value["undo_logs"]
        )
    if "streams" in value:
        import capo_neptunedata.types.storage_metrics

        out["streams"] = capo_neptunedata.types.storage_metrics.serialize_json(
            value["streams"]
        )
    if "dfe_statistics" in value:
        import capo_neptunedata.types.storage_metrics

        out["dfeStatistics"] = capo_neptunedata.types.storage_metrics.serialize_json(
            value["dfe_statistics"]
        )
    if "schema" in value:
        import capo_neptunedata.types.storage_metrics

        out["schema"] = capo_neptunedata.types.storage_metrics.serialize_json(
            value["schema"]
        )
    if "internals" in value:
        import capo_neptunedata.types.storage_metrics

        out["internals"] = capo_neptunedata.types.storage_metrics.serialize_json(
            value["internals"]
        )
    return out


def deserialize_json(data: dict) -> GetStorageOutput:
    out: GetStorageOutput = {}  # type: ignore[typeddict-item]
    if data.get("totalStorageBytesUsed") is not None:
        out["total_storage_bytes_used"] = data["totalStorageBytesUsed"]
    if data.get("quads") is not None:
        import capo_neptunedata.types.quads_indexes_info

        out["quads"] = capo_neptunedata.types.quads_indexes_info.deserialize_json(
            data["quads"]
        )
    if data.get("dictionaries") is not None:
        import capo_neptunedata.types.dictionaries_info

        out["dictionaries"] = capo_neptunedata.types.dictionaries_info.deserialize_json(
            data["dictionaries"]
        )
    if data.get("undoLogs") is not None:
        import capo_neptunedata.types.undo_logs_metrics

        out["undo_logs"] = capo_neptunedata.types.undo_logs_metrics.deserialize_json(
            data["undoLogs"]
        )
    if data.get("streams") is not None:
        import capo_neptunedata.types.storage_metrics

        out["streams"] = capo_neptunedata.types.storage_metrics.deserialize_json(
            data["streams"]
        )
    if data.get("dfeStatistics") is not None:
        import capo_neptunedata.types.storage_metrics

        out["dfe_statistics"] = capo_neptunedata.types.storage_metrics.deserialize_json(
            data["dfeStatistics"]
        )
    if data.get("schema") is not None:
        import capo_neptunedata.types.storage_metrics

        out["schema"] = capo_neptunedata.types.storage_metrics.deserialize_json(
            data["schema"]
        )
    if data.get("internals") is not None:
        import capo_neptunedata.types.storage_metrics

        out["internals"] = capo_neptunedata.types.storage_metrics.deserialize_json(
            data["internals"]
        )
    return out
