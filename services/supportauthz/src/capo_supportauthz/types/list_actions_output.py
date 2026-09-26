"""Generated from Smithy shape ``com.amazonaws.supportauthz#ListActionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_supportauthz.errors import DeserializationError

if TYPE_CHECKING:
    import capo_supportauthz.types.action_summaries
    import capo_supportauthz.types.next_token


class ListActionsOutput(TypedDict, closed=True):
    action_summaries: "capo_supportauthz.types.action_summaries.ActionSummaries"
    """<p>The list of support actions.</p>"""
    next_token: NotRequired["capo_supportauthz.types.next_token.NextToken"]
    """<p>The token for the next page of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListActionsOutput) -> dict:
    out: dict = {}
    import capo_supportauthz.types.action_summaries

    out["actionSummaries"] = capo_supportauthz.types.action_summaries.serialize_json(
        value["action_summaries"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListActionsOutput:
    out: ListActionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("actionSummaries") is not None:
        import capo_supportauthz.types.action_summaries

        out["action_summaries"] = (
            capo_supportauthz.types.action_summaries.deserialize_json(
                data["actionSummaries"]
            )
        )
    else:
        raise DeserializationError("ListActionsOutput.action_summaries required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
