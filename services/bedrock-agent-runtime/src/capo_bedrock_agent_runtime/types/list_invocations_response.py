"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ListInvocationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.invocation_summaries
    import capo_bedrock_agent_runtime.types.next_token


class ListInvocationsResponse(TypedDict, closed=True):
    invocation_summaries: (
        "capo_bedrock_agent_runtime.types.invocation_summaries.InvocationSummaries"
    )
    """<p>A list of invocation summaries associated with the session.</p>"""
    next_token: NotRequired["capo_bedrock_agent_runtime.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInvocationsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.invocation_summaries

    out["invocationSummaries"] = (
        capo_bedrock_agent_runtime.types.invocation_summaries.serialize_json(
            value["invocation_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInvocationsResponse:
    out: ListInvocationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("invocationSummaries") is not None:
        import capo_bedrock_agent_runtime.types.invocation_summaries

        out["invocation_summaries"] = (
            capo_bedrock_agent_runtime.types.invocation_summaries.deserialize_json(
                data["invocationSummaries"]
            )
        )
    else:
        out["invocation_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
