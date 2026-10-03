"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyAggregatesSkippedEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.batch_entry_completion_status
    import capo_iotsitewise.types.batch_get_asset_property_aggregates_error_info
    import capo_iotsitewise.types.entry_id


class BatchGetAssetPropertyAggregatesSkippedEntry(TypedDict, closed=True):
    entry_id: "capo_iotsitewise.types.entry_id.EntryId"
    """<p>The ID of the entry.</p>"""
    completion_status: "capo_iotsitewise.types.batch_entry_completion_status.BatchEntryCompletionStatus"
    """<p>The completion status of each entry that is associated with the <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchGetAssetPropertyAggregates.html">BatchGetAssetPropertyAggregates</a> API.</p>"""
    error_info: NotRequired[
        "capo_iotsitewise.types.batch_get_asset_property_aggregates_error_info.BatchGetAssetPropertyAggregatesErrorInfo"
    ]
    """<p>The error information, such as the error code and the timestamp.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAssetPropertyAggregatesSkippedEntry) -> dict:
    out: dict = {}
    out["entryId"] = value["entry_id"]
    import capo_iotsitewise.types.batch_entry_completion_status

    out["completionStatus"] = (
        capo_iotsitewise.types.batch_entry_completion_status.serialize_json(
            value["completion_status"]
        )
    )
    if "error_info" in value:
        import capo_iotsitewise.types.batch_get_asset_property_aggregates_error_info

        out["errorInfo"] = (
            capo_iotsitewise.types.batch_get_asset_property_aggregates_error_info.serialize_json(
                value["error_info"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetAssetPropertyAggregatesSkippedEntry:
    out: BatchGetAssetPropertyAggregatesSkippedEntry = {}  # type: ignore[typeddict-item]
    if data.get("entryId") is not None:
        out["entry_id"] = data["entryId"]
    else:
        raise DeserializationError(
            "BatchGetAssetPropertyAggregatesSkippedEntry.entry_id required"
        )
    if data.get("completionStatus") is not None:
        import capo_iotsitewise.types.batch_entry_completion_status

        out["completion_status"] = (
            capo_iotsitewise.types.batch_entry_completion_status.deserialize_json(
                data["completionStatus"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetAssetPropertyAggregatesSkippedEntry.completion_status required"
        )
    if data.get("errorInfo") is not None:
        import capo_iotsitewise.types.batch_get_asset_property_aggregates_error_info

        out["error_info"] = (
            capo_iotsitewise.types.batch_get_asset_property_aggregates_error_info.deserialize_json(
                data["errorInfo"]
            )
        )
    return out
