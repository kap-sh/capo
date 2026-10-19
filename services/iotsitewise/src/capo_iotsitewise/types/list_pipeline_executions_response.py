"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListPipelineExecutionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.pagination_token
    import capo_iotsitewise.types.pipeline_execution_summary_list


class ListPipelineExecutionsResponse(TypedDict, closed=True):
    pipeline_execution_summaries: "capo_iotsitewise.types.pipeline_execution_summary_list.PipelineExecutionSummaryList"
    """<p>A list that summarizes each pipeline execution.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.pagination_token.PaginationToken"]
    """<p>The token to be used for the next set of paginated results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPipelineExecutionsResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.pipeline_execution_summary_list

    out["pipelineExecutionSummaries"] = (
        capo_iotsitewise.types.pipeline_execution_summary_list.serialize_json(
            value["pipeline_execution_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPipelineExecutionsResponse:
    out: ListPipelineExecutionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("pipelineExecutionSummaries") is not None:
        import capo_iotsitewise.types.pipeline_execution_summary_list

        out["pipeline_execution_summaries"] = (
            capo_iotsitewise.types.pipeline_execution_summary_list.deserialize_json(
                data["pipelineExecutionSummaries"]
            )
        )
    else:
        out["pipeline_execution_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
