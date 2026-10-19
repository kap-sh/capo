"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ListMemoryExtractionJobsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.extraction_job_filter_input
    import capo_bedrock_agentcore.types.memory_id
    import capo_bedrock_agentcore.types.pagination_token


class ListMemoryExtractionJobsInput(TypedDict, closed=True):
    memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId"
    """<p>The unique identifier of the memory to list extraction jobs for.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in a single call. The default value is 20.</p>"""
    filter: NotRequired[
        "capo_bedrock_agentcore.types.extraction_job_filter_input.ExtractionJobFilterInput"
    ]
    """<p>Filter criteria to apply when listing extraction jobs.</p>"""
    next_token: NotRequired[
        "capo_bedrock_agentcore.types.pagination_token.PaginationToken"
    ]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMemoryExtractionJobsInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "filter" in value:
        import capo_bedrock_agentcore.types.extraction_job_filter_input

        out["filter"] = (
            capo_bedrock_agentcore.types.extraction_job_filter_input.serialize_json(
                value["filter"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMemoryExtractionJobsInput:
    out: ListMemoryExtractionJobsInput = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("filter") is not None:
        import capo_bedrock_agentcore.types.extraction_job_filter_input

        out["filter"] = (
            capo_bedrock_agentcore.types.extraction_job_filter_input.deserialize_json(
                data["filter"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
