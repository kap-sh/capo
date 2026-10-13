"""Generated from Smithy shape ``com.amazonaws.bedrock#HumanWorkflowConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.human_task_instructions
    import capo_bedrock.types.sage_maker_flow_definition_arn


class HumanWorkflowConfig(TypedDict, closed=True):
    flow_definition_arn: (
        "capo_bedrock.types.sage_maker_flow_definition_arn.SageMakerFlowDefinitionArn"
    )
    """<p>The Amazon Resource Number (ARN) for the flow definition</p>"""
    instructions: NotRequired[
        "capo_bedrock.types.human_task_instructions.HumanTaskInstructions"
    ]
    """<p>Instructions for the flow definition</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HumanWorkflowConfig) -> dict:
    out: dict = {}
    out["flowDefinitionArn"] = value["flow_definition_arn"]
    if "instructions" in value:
        out["instructions"] = value["instructions"]
    return out


def deserialize_json(data: dict) -> HumanWorkflowConfig:
    out: HumanWorkflowConfig = {}  # type: ignore[typeddict-item]
    if data.get("flowDefinitionArn") is not None:
        out["flow_definition_arn"] = data["flowDefinitionArn"]
    else:
        raise DeserializationError("HumanWorkflowConfig.flow_definition_arn required")
    if data.get("instructions") is not None:
        out["instructions"] = data["instructions"]
    return out


def redact_sensitive(value: HumanWorkflowConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "instructions" in value:
        out["instructions"] = "*** Sensitive Data Redacted ***"
    return out
