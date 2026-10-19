"""Generated from Smithy shape ``com.amazonaws.qconnect#UpdateAssistantAIAgentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.ai_agent_configuration_data
    import capo_qconnect.types.ai_agent_type
    import capo_qconnect.types.non_empty_string
    import capo_qconnect.types.uuid_or_arn


class UpdateAssistantAIAgentRequest(TypedDict, closed=True):
    assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    ai_agent_type: "capo_qconnect.types.ai_agent_type.AIAgentType"
    """<p>The type of the AI Agent being updated for use by default on the Amazon Q in Connect Assistant.</p>"""
    configuration: (
        "capo_qconnect.types.ai_agent_configuration_data.AIAgentConfigurationData"
    )
    """<p>The configuration of the AI Agent being updated for use by default on the Amazon Q in Connect Assistant.</p>"""
    orchestrator_use_case: NotRequired[
        "capo_qconnect.types.non_empty_string.NonEmptyString"
    ]
    """<p>The orchestrator use case for the AI Agent being added.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssistantAIAgentRequest) -> dict:
    out: dict = {}
    out["aiAgentType"] = value["ai_agent_type"]
    import capo_qconnect.types.ai_agent_configuration_data

    out["configuration"] = (
        capo_qconnect.types.ai_agent_configuration_data.serialize_json(
            value["configuration"]
        )
    )
    if "orchestrator_use_case" in value:
        out["orchestratorUseCase"] = value["orchestrator_use_case"]
    return out


def deserialize_json(data: dict) -> UpdateAssistantAIAgentRequest:
    out: UpdateAssistantAIAgentRequest = {}  # type: ignore[typeddict-item]
    if data.get("aiAgentType") is not None:
        out["ai_agent_type"] = data["aiAgentType"]
    else:
        out["ai_agent_type"] = ""
    if data.get("configuration") is not None:
        import capo_qconnect.types.ai_agent_configuration_data

        out["configuration"] = (
            capo_qconnect.types.ai_agent_configuration_data.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAssistantAIAgentRequest.configuration required"
        )
    if data.get("orchestratorUseCase") is not None:
        out["orchestrator_use_case"] = data["orchestratorUseCase"]
    return out
