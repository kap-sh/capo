"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListActionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.action_summaries
    import capo_iotsitewise.types.next_token


class ListActionsResponse(TypedDict, closed=True):
    action_summaries: "capo_iotsitewise.types.action_summaries.ActionSummaries"
    """<p>A list that summarizes the actions associated with the specified asset.</p>"""
    next_token: "capo_iotsitewise.types.next_token.NextToken"
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListActionsResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.action_summaries

    out["actionSummaries"] = capo_iotsitewise.types.action_summaries.serialize_json(
        value["action_summaries"]
    )
    out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListActionsResponse:
    out: ListActionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("actionSummaries") is not None:
        import capo_iotsitewise.types.action_summaries

        out["action_summaries"] = (
            capo_iotsitewise.types.action_summaries.deserialize_json(
                data["actionSummaries"]
            )
        )
    else:
        out["action_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    else:
        out["next_token"] = ""
    return out
