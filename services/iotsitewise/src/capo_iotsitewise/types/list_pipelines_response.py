"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListPipelinesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.pagination_token
    import capo_iotsitewise.types.pipeline_summaries


class ListPipelinesResponse(TypedDict, closed=True):
    pipeline_summaries: "capo_iotsitewise.types.pipeline_summaries.PipelineSummaries"
    """<p>A list that summarizes each pipeline in the workspace.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.pagination_token.PaginationToken"]
    """<p>The token to be used for the next set of paginated results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPipelinesResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.pipeline_summaries

    out["pipelineSummaries"] = capo_iotsitewise.types.pipeline_summaries.serialize_json(
        value["pipeline_summaries"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPipelinesResponse:
    out: ListPipelinesResponse = {}  # type: ignore[typeddict-item]
    if data.get("pipelineSummaries") is not None:
        import capo_iotsitewise.types.pipeline_summaries

        out["pipeline_summaries"] = (
            capo_iotsitewise.types.pipeline_summaries.deserialize_json(
                data["pipelineSummaries"]
            )
        )
    else:
        out["pipeline_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
