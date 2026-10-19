"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyAggregatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.batch_get_asset_property_aggregates_error_entries
    import capo_iotsitewise.types.batch_get_asset_property_aggregates_skipped_entries
    import capo_iotsitewise.types.batch_get_asset_property_aggregates_success_entries
    import capo_iotsitewise.types.next_token


class BatchGetAssetPropertyAggregatesResponse(TypedDict, closed=True):
    error_entries: "capo_iotsitewise.types.batch_get_asset_property_aggregates_error_entries.BatchGetAssetPropertyAggregatesErrorEntries"
    """<p>A list of the errors (if any) associated with the batch request. Each error entry contains the <code>entryId</code> of the entry that failed.</p>"""
    success_entries: "capo_iotsitewise.types.batch_get_asset_property_aggregates_success_entries.BatchGetAssetPropertyAggregatesSuccessEntries"
    """<p>A list of entries that were processed successfully by this batch request. Each success entry contains the <code>entryId</code> of the entry that succeeded and the latest query result.</p>"""
    skipped_entries: "capo_iotsitewise.types.batch_get_asset_property_aggregates_skipped_entries.BatchGetAssetPropertyAggregatesSkippedEntries"
    """<p>A list of entries that were not processed by this batch request. because these entries had been completely processed by previous paginated requests. Each skipped entry contains the <code>entryId</code> of the entry that skipped.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAssetPropertyAggregatesResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.batch_get_asset_property_aggregates_error_entries

    out["errorEntries"] = (
        capo_iotsitewise.types.batch_get_asset_property_aggregates_error_entries.serialize_json(
            value["error_entries"]
        )
    )
    import capo_iotsitewise.types.batch_get_asset_property_aggregates_success_entries

    out["successEntries"] = (
        capo_iotsitewise.types.batch_get_asset_property_aggregates_success_entries.serialize_json(
            value["success_entries"]
        )
    )
    import capo_iotsitewise.types.batch_get_asset_property_aggregates_skipped_entries

    out["skippedEntries"] = (
        capo_iotsitewise.types.batch_get_asset_property_aggregates_skipped_entries.serialize_json(
            value["skipped_entries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> BatchGetAssetPropertyAggregatesResponse:
    out: BatchGetAssetPropertyAggregatesResponse = {}  # type: ignore[typeddict-item]
    if data.get("errorEntries") is not None:
        import capo_iotsitewise.types.batch_get_asset_property_aggregates_error_entries

        out["error_entries"] = (
            capo_iotsitewise.types.batch_get_asset_property_aggregates_error_entries.deserialize_json(
                data["errorEntries"]
            )
        )
    else:
        out["error_entries"] = []
    if data.get("successEntries") is not None:
        import capo_iotsitewise.types.batch_get_asset_property_aggregates_success_entries

        out["success_entries"] = (
            capo_iotsitewise.types.batch_get_asset_property_aggregates_success_entries.deserialize_json(
                data["successEntries"]
            )
        )
    else:
        out["success_entries"] = []
    if data.get("skippedEntries") is not None:
        import capo_iotsitewise.types.batch_get_asset_property_aggregates_skipped_entries

        out["skipped_entries"] = (
            capo_iotsitewise.types.batch_get_asset_property_aggregates_skipped_entries.deserialize_json(
                data["skippedEntries"]
            )
        )
    else:
        out["skipped_entries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
