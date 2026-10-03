"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InvokeFlowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.flow_alias_identifier
    import capo_bedrock_agent_runtime.types.flow_execution_id
    import capo_bedrock_agent_runtime.types.flow_identifier
    import capo_bedrock_agent_runtime.types.flow_inputs
    import capo_bedrock_agent_runtime.types.model_performance_configuration


class InvokeFlowRequest(TypedDict, closed=True):
    flow_identifier: "capo_bedrock_agent_runtime.types.flow_identifier.FlowIdentifier"
    """<p>The unique identifier of the flow.</p>"""
    flow_alias_identifier: (
        "capo_bedrock_agent_runtime.types.flow_alias_identifier.FlowAliasIdentifier"
    )
    """<p>The unique identifier of the flow alias.</p>"""
    inputs: "capo_bedrock_agent_runtime.types.flow_inputs.FlowInputs"
    """<p>A list of objects, each containing information about an input into the flow.</p>"""
    enable_trace: NotRequired["bool"]
    """<p>Specifies whether to return the trace for the flow or not. Traces track inputs and outputs for nodes in the flow. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-trace.html">Track each step in your prompt flow by viewing its trace in Amazon Bedrock</a>.</p>"""
    model_performance_configuration: NotRequired[
        "capo_bedrock_agent_runtime.types.model_performance_configuration.ModelPerformanceConfiguration"
    ]
    """<p>Model performance settings for the request.</p>"""
    execution_id: NotRequired[
        "capo_bedrock_agent_runtime.types.flow_execution_id.FlowExecutionId"
    ]
    """<p>The unique identifier for the current flow execution. If you don't provide a value, Amazon Bedrock creates the identifier for you. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeFlowRequest) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.flow_inputs

    out["inputs"] = capo_bedrock_agent_runtime.types.flow_inputs.serialize_json(
        value["inputs"]
    )
    if "enable_trace" in value:
        out["enableTrace"] = value["enable_trace"]
    if "model_performance_configuration" in value:
        import capo_bedrock_agent_runtime.types.model_performance_configuration

        out["modelPerformanceConfiguration"] = (
            capo_bedrock_agent_runtime.types.model_performance_configuration.serialize_json(
                value["model_performance_configuration"]
            )
        )
    if "execution_id" in value:
        out["executionId"] = value["execution_id"]
    return out


def deserialize_json(data: dict) -> InvokeFlowRequest:
    out: InvokeFlowRequest = {}  # type: ignore[typeddict-item]
    if data.get("inputs") is not None:
        import capo_bedrock_agent_runtime.types.flow_inputs

        out["inputs"] = capo_bedrock_agent_runtime.types.flow_inputs.deserialize_json(
            data["inputs"]
        )
    else:
        raise DeserializationError("InvokeFlowRequest.inputs required")
    if data.get("enableTrace") is not None:
        out["enable_trace"] = data["enableTrace"]
    if data.get("modelPerformanceConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.model_performance_configuration

        out["model_performance_configuration"] = (
            capo_bedrock_agent_runtime.types.model_performance_configuration.deserialize_json(
                data["modelPerformanceConfiguration"]
            )
        )
    if data.get("executionId") is not None:
        out["execution_id"] = data["executionId"]
    return out
