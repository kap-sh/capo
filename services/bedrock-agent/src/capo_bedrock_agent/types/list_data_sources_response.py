"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ListDataSourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.data_source_summaries
    import capo_bedrock_agent.types.next_token


class ListDataSourcesResponse(TypedDict, closed=True):
    data_source_summaries: (
        "capo_bedrock_agent.types.data_source_summaries.DataSourceSummaries"
    )
    """<p>A list of objects, each of which contains information about a data source.</p>"""
    next_token: NotRequired["capo_bedrock_agent.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataSourcesResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.data_source_summaries

    out["dataSourceSummaries"] = (
        capo_bedrock_agent.types.data_source_summaries.serialize_json(
            value["data_source_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataSourcesResponse:
    out: ListDataSourcesResponse = {}  # type: ignore[typeddict-item]
    if data.get("dataSourceSummaries") is not None:
        import capo_bedrock_agent.types.data_source_summaries

        out["data_source_summaries"] = (
            capo_bedrock_agent.types.data_source_summaries.deserialize_json(
                data["dataSourceSummaries"]
            )
        )
    else:
        out["data_source_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
