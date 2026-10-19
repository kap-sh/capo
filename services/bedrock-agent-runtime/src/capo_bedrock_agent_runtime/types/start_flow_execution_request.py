"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#StartFlowExecutionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.flow_alias_identifier
    import capo_bedrock_agent_runtime.types.flow_execution_name
    import capo_bedrock_agent_runtime.types.flow_identifier
    import capo_bedrock_agent_runtime.types.flow_inputs
    import capo_bedrock_agent_runtime.types.model_performance_configuration


class StartFlowExecutionRequest(TypedDict, closed=True):
    flow_identifier: "capo_bedrock_agent_runtime.types.flow_identifier.FlowIdentifier"
    """<p>The unique identifier of the flow to execute.</p>"""
    flow_alias_identifier: (
        "capo_bedrock_agent_runtime.types.flow_alias_identifier.FlowAliasIdentifier"
    )
    """<p>The unique identifier of the flow alias to use for the flow execution.</p>"""
    flow_execution_name: NotRequired[
        "capo_bedrock_agent_runtime.types.flow_execution_name.FlowExecutionName"
    ]
    """<p>The unique name for the flow execution. If you don't provide one, a system-generated name is used.</p>"""
    inputs: "capo_bedrock_agent_runtime.types.flow_inputs.FlowInputs"
    """<p>The input data required for the flow execution. This must match the input schema defined in the flow.</p>"""
    model_performance_configuration: NotRequired[
        "capo_bedrock_agent_runtime.types.model_performance_configuration.ModelPerformanceConfiguration"
    ]
    """<p>The performance settings for the foundation model used in the flow execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartFlowExecutionRequest) -> dict:
    out: dict = {}
    if "flow_execution_name" in value:
        out["flowExecutionName"] = value["flow_execution_name"]
    import capo_bedrock_agent_runtime.types.flow_inputs

    out["inputs"] = capo_bedrock_agent_runtime.types.flow_inputs.serialize_json(
        value["inputs"]
    )
    if "model_performance_configuration" in value:
        import capo_bedrock_agent_runtime.types.model_performance_configuration

        out["modelPerformanceConfiguration"] = (
            capo_bedrock_agent_runtime.types.model_performance_configuration.serialize_json(
                value["model_performance_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartFlowExecutionRequest:
    out: StartFlowExecutionRequest = {}  # type: ignore[typeddict-item]
    if data.get("flowExecutionName") is not None:
        out["flow_execution_name"] = data["flowExecutionName"]
    if data.get("inputs") is not None:
        import capo_bedrock_agent_runtime.types.flow_inputs

        out["inputs"] = capo_bedrock_agent_runtime.types.flow_inputs.deserialize_json(
            data["inputs"]
        )
    else:
        out["inputs"] = []
    if data.get("modelPerformanceConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.model_performance_configuration

        out["model_performance_configuration"] = (
            capo_bedrock_agent_runtime.types.model_performance_configuration.deserialize_json(
                data["modelPerformanceConfiguration"]
            )
        )
    return out


def redact_sensitive(value: StartFlowExecutionRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "inputs" in value:
        import capo_bedrock_agent_runtime.types.flow_inputs

        out["inputs"] = capo_bedrock_agent_runtime.types.flow_inputs.redact_sensitive(
            value["inputs"]
        )
    return out
