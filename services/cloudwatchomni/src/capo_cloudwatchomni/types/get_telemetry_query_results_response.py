"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#GetTelemetryQueryResultsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.query_statistics
    import capo_cloudwatchomni.types.query_status
    import capo_cloudwatchomni.types.row_list


class GetTelemetryQueryResultsResponse(TypedDict, closed=True):
    status: "capo_cloudwatchomni.types.query_status.QueryStatus"
    """The current execution status of the query."""
    rows: NotRequired["capo_cloudwatchomni.types.row_list.RowList"]
    """The result rows returned by the query."""
    next_token: NotRequired["str"]
    """A token to retrieve the next page of results, or null if there are no more results."""
    statistics: NotRequired[
        "capo_cloudwatchomni.types.query_statistics.QueryStatistics"
    ]
    """Statistics about the query execution."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetTelemetryQueryResultsResponse) -> dict:
    out: dict = {}
    import capo_cloudwatchomni.types.query_status

    out["status"] = capo_cloudwatchomni.types.query_status.serialize_cbor(
        value["status"]
    )
    if "rows" in value:
        import capo_cloudwatchomni.types.row_list

        out["rows"] = capo_cloudwatchomni.types.row_list.serialize_cbor(value["rows"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "statistics" in value:
        import capo_cloudwatchomni.types.query_statistics

        out["statistics"] = capo_cloudwatchomni.types.query_statistics.serialize_cbor(
            value["statistics"]
        )
    return out


def deserialize_cbor(data: dict) -> GetTelemetryQueryResultsResponse:
    out: GetTelemetryQueryResultsResponse = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_cloudwatchomni.types.query_status

        out["status"] = capo_cloudwatchomni.types.query_status.deserialize_cbor(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_cloudwatchomni.types.query_status.QueryStatus", ""
        )
    if data.get("rows") is not None:
        import capo_cloudwatchomni.types.row_list

        out["rows"] = capo_cloudwatchomni.types.row_list.deserialize_cbor(data["rows"])
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("statistics") is not None:
        import capo_cloudwatchomni.types.query_statistics

        out["statistics"] = capo_cloudwatchomni.types.query_statistics.deserialize_cbor(
            data["statistics"]
        )
    return out
