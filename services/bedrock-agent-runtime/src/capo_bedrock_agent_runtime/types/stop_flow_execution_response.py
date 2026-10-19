"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#StopFlowExecutionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.flow_execution_identifier
    import capo_bedrock_agent_runtime.types.flow_execution_status


class StopFlowExecutionResponse(TypedDict, closed=True):
    execution_arn: NotRequired[
        "capo_bedrock_agent_runtime.types.flow_execution_identifier.FlowExecutionIdentifier"
    ]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the flow execution that was stopped.</p>"""
    status: "capo_bedrock_agent_runtime.types.flow_execution_status.FlowExecutionStatus"
    """<p>The updated status of the flow execution after the stop request. This will typically be ABORTED if the execution was successfully stopped.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopFlowExecutionResponse) -> dict:
    out: dict = {}
    if "execution_arn" in value:
        out["executionArn"] = value["execution_arn"]
    import capo_bedrock_agent_runtime.types.flow_execution_status

    out["status"] = (
        capo_bedrock_agent_runtime.types.flow_execution_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> StopFlowExecutionResponse:
    out: StopFlowExecutionResponse = {}  # type: ignore[typeddict-item]
    if data.get("executionArn") is not None:
        out["execution_arn"] = data["executionArn"]
    if data.get("status") is not None:
        import capo_bedrock_agent_runtime.types.flow_execution_status

        out["status"] = (
            capo_bedrock_agent_runtime.types.flow_execution_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agent_runtime.types.flow_execution_status.FlowExecutionStatus",
            "",
        )
    return out
