"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ListInvocationStepsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.invocation_step_summaries
    import capo_bedrock_agent_runtime.types.next_token


class ListInvocationStepsResponse(TypedDict, closed=True):
    invocation_step_summaries: "capo_bedrock_agent_runtime.types.invocation_step_summaries.InvocationStepSummaries"
    """<p>A list of summaries for each invocation step associated with a session and if you specified it, an invocation within the session.</p>"""
    next_token: NotRequired["capo_bedrock_agent_runtime.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInvocationStepsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.invocation_step_summaries

    out["invocationStepSummaries"] = (
        capo_bedrock_agent_runtime.types.invocation_step_summaries.serialize_json(
            value["invocation_step_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInvocationStepsResponse:
    out: ListInvocationStepsResponse = {}  # type: ignore[typeddict-item]
    if data.get("invocationStepSummaries") is not None:
        import capo_bedrock_agent_runtime.types.invocation_step_summaries

        out["invocation_step_summaries"] = (
            capo_bedrock_agent_runtime.types.invocation_step_summaries.deserialize_json(
                data["invocationStepSummaries"]
            )
        )
    else:
        out["invocation_step_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
