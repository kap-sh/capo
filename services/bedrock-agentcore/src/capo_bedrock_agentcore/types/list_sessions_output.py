"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ListSessionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.pagination_token
    import capo_bedrock_agentcore.types.session_summary_list


class ListSessionsOutput(TypedDict, closed=True):
    session_summaries: (
        "capo_bedrock_agentcore.types.session_summary_list.SessionSummaryList"
    )
    """<p>The list of session summaries that match the specified criteria.</p>"""
    next_token: NotRequired[
        "capo_bedrock_agentcore.types.pagination_token.PaginationToken"
    ]
    """<p>The token to use in a subsequent request to get the next set of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSessionsOutput) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.session_summary_list

    out["sessionSummaries"] = (
        capo_bedrock_agentcore.types.session_summary_list.serialize_json(
            value["session_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSessionsOutput:
    out: ListSessionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("sessionSummaries") is not None:
        import capo_bedrock_agentcore.types.session_summary_list

        out["session_summaries"] = (
            capo_bedrock_agentcore.types.session_summary_list.deserialize_json(
                data["sessionSummaries"]
            )
        )
    else:
        out["session_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
