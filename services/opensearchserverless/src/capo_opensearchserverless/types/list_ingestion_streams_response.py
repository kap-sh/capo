"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#ListIngestionStreamsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.ingestion_stream_summaries


class ListIngestionStreamsResponse(TypedDict, closed=True):
    ingestion_stream_summaries: NotRequired[
        "capo_opensearchserverless.types.ingestion_stream_summaries.IngestionStreamSummaries"
    ]
    """<p>Summary information about each ingestion stream.</p>"""
    next_token: NotRequired["str"]
    """<p>When <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListIngestionStreamsResponse) -> dict:
    out: dict = {}
    if "ingestion_stream_summaries" in value:
        import capo_opensearchserverless.types.ingestion_stream_summaries

        out["ingestionStreamSummaries"] = (
            capo_opensearchserverless.types.ingestion_stream_summaries.serialize_aws_json_1_0(
                value["ingestion_stream_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListIngestionStreamsResponse:
    out: ListIngestionStreamsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ingestionStreamSummaries") is not None:
        import capo_opensearchserverless.types.ingestion_stream_summaries

        out["ingestion_stream_summaries"] = (
            capo_opensearchserverless.types.ingestion_stream_summaries.deserialize_aws_json_1_0(
                data["ingestionStreamSummaries"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
