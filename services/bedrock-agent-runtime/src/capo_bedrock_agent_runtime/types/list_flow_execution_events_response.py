"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ListFlowExecutionEventsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.flow_execution_events
    import capo_bedrock_agent_runtime.types.next_token


class ListFlowExecutionEventsResponse(TypedDict, closed=True):
    flow_execution_events: (
        "capo_bedrock_agent_runtime.types.flow_execution_events.FlowExecutionEvents"
    )
    """<p>A list of events that occurred during the flow execution. Events can include node inputs and outputs, flow inputs and outputs, condition results, and failure events.</p>"""
    next_token: NotRequired["capo_bedrock_agent_runtime.types.next_token.NextToken"]
    """<p>A token to retrieve the next set of results. This value is returned if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFlowExecutionEventsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.flow_execution_events

    out["flowExecutionEvents"] = (
        capo_bedrock_agent_runtime.types.flow_execution_events.serialize_json(
            value["flow_execution_events"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFlowExecutionEventsResponse:
    out: ListFlowExecutionEventsResponse = {}  # type: ignore[typeddict-item]
    if data.get("flowExecutionEvents") is not None:
        import capo_bedrock_agent_runtime.types.flow_execution_events

        out["flow_execution_events"] = (
            capo_bedrock_agent_runtime.types.flow_execution_events.deserialize_json(
                data["flowExecutionEvents"]
            )
        )
    else:
        out["flow_execution_events"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListFlowExecutionEventsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "flow_execution_events" in value:
        import capo_bedrock_agent_runtime.types.flow_execution_events

        out["flow_execution_events"] = (
            capo_bedrock_agent_runtime.types.flow_execution_events.redact_sensitive(
                value["flow_execution_events"]
            )
        )
    return out
