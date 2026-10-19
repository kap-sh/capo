"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ListActorsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.actor_summary_list
    import capo_bedrock_agentcore.types.pagination_token


class ListActorsOutput(TypedDict, closed=True):
    actor_summaries: "capo_bedrock_agentcore.types.actor_summary_list.ActorSummaryList"
    """<p>The list of actor summaries.</p>"""
    next_token: NotRequired[
        "capo_bedrock_agentcore.types.pagination_token.PaginationToken"
    ]
    """<p>The token to use in a subsequent request to get the next set of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListActorsOutput) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.actor_summary_list

    out["actorSummaries"] = (
        capo_bedrock_agentcore.types.actor_summary_list.serialize_json(
            value["actor_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListActorsOutput:
    out: ListActorsOutput = {}  # type: ignore[typeddict-item]
    if data.get("actorSummaries") is not None:
        import capo_bedrock_agentcore.types.actor_summary_list

        out["actor_summaries"] = (
            capo_bedrock_agentcore.types.actor_summary_list.deserialize_json(
                data["actorSummaries"]
            )
        )
    else:
        out["actor_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
