"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListExecutionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.execution_summaries
    import capo_iotsitewise.types.next_token


class ListExecutionsResponse(TypedDict, closed=True):
    execution_summaries: "capo_iotsitewise.types.execution_summaries.ExecutionSummaries"
    """<p>Contains the list of execution summaries of the computation models.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListExecutionsResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.execution_summaries

    out["executionSummaries"] = (
        capo_iotsitewise.types.execution_summaries.serialize_json(
            value["execution_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListExecutionsResponse:
    out: ListExecutionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("executionSummaries") is not None:
        import capo_iotsitewise.types.execution_summaries

        out["execution_summaries"] = (
            capo_iotsitewise.types.execution_summaries.deserialize_json(
                data["executionSummaries"]
            )
        )
    else:
        out["execution_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
