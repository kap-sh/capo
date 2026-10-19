"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ListFlowExecutionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.flow_execution_summaries
    import capo_bedrock_agent_runtime.types.next_token


class ListFlowExecutionsResponse(TypedDict, closed=True):
    flow_execution_summaries: "capo_bedrock_agent_runtime.types.flow_execution_summaries.FlowExecutionSummaries"
    """<p>A list of flow execution summaries. Each summary includes the execution ARN, flow identifier, flow alias identifier, flow version, status, and timestamps.</p>"""
    next_token: NotRequired["capo_bedrock_agent_runtime.types.next_token.NextToken"]
    """<p>A token to retrieve the next set of results. This value is returned if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFlowExecutionsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.flow_execution_summaries

    out["flowExecutionSummaries"] = (
        capo_bedrock_agent_runtime.types.flow_execution_summaries.serialize_json(
            value["flow_execution_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFlowExecutionsResponse:
    out: ListFlowExecutionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("flowExecutionSummaries") is not None:
        import capo_bedrock_agent_runtime.types.flow_execution_summaries

        out["flow_execution_summaries"] = (
            capo_bedrock_agent_runtime.types.flow_execution_summaries.deserialize_json(
                data["flowExecutionSummaries"]
            )
        )
    else:
        out["flow_execution_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
