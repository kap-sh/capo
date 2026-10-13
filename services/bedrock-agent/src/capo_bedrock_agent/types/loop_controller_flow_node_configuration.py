"""Generated from Smithy shape ``com.amazonaws.bedrockagent#LoopControllerFlowNodeConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_condition


class LoopControllerFlowNodeConfiguration(TypedDict, closed=True):
    continue_condition: "capo_bedrock_agent.types.flow_condition.FlowCondition"
    """<p>Specifies the condition that determines when the flow exits the DoWhile loop. The loop executes until this condition evaluates to true.</p>"""
    max_iterations: "int"
    """<p>Specifies the maximum number of times the DoWhile loop can iterate before the flow exits the loop.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoopControllerFlowNodeConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.flow_condition

    out["continueCondition"] = capo_bedrock_agent.types.flow_condition.serialize_json(
        value["continue_condition"]
    )
    out["maxIterations"] = value.get("max_iterations", 10)
    return out


def deserialize_json(data: dict) -> LoopControllerFlowNodeConfiguration:
    out: LoopControllerFlowNodeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("continueCondition") is not None:
        import capo_bedrock_agent.types.flow_condition

        out["continue_condition"] = (
            capo_bedrock_agent.types.flow_condition.deserialize_json(
                data["continueCondition"]
            )
        )
    else:
        raise DeserializationError(
            "LoopControllerFlowNodeConfiguration.continue_condition required"
        )
    if data.get("maxIterations") is not None:
        out["max_iterations"] = data["maxIterations"]
    else:
        out["max_iterations"] = 10
    return out


def redact_sensitive(value: LoopControllerFlowNodeConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "continue_condition" in value:
        import capo_bedrock_agent.types.flow_condition

        out["continue_condition"] = (
            capo_bedrock_agent.types.flow_condition.redact_sensitive(
                value["continue_condition"]
            )
        )
    return out
