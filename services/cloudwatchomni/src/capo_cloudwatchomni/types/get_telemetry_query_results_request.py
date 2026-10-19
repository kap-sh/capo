"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#GetTelemetryQueryResultsRequest``."""

from typing_extensions import NotRequired, TypedDict


class GetTelemetryQueryResultsRequest(TypedDict, closed=True):
    query_id: "str"
    """The unique ID of the query."""
    next_token: NotRequired["str"]
    """A token to retrieve the next page of results."""
    max_results: NotRequired["int"]
    """The maximum number of result rows to return per page."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetTelemetryQueryResultsRequest) -> dict:
    out: dict = {}
    out["queryId"] = value["query_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_cbor(data: dict) -> GetTelemetryQueryResultsRequest:
    out: GetTelemetryQueryResultsRequest = {}  # type: ignore[typeddict-item]
    if data.get("queryId") is not None:
        out["query_id"] = data["queryId"]
    else:
        out["query_id"] = ""
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
