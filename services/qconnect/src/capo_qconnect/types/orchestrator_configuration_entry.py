"""Generated from Smithy shape ``com.amazonaws.qconnect#OrchestratorConfigurationEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.non_empty_string
    import capo_qconnect.types.uuid_or_arn_or_either_with_qualifier


class OrchestratorConfigurationEntry(TypedDict, closed=True):
    ai_agent_id: NotRequired[
        "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier"
    ]
    """<p>The identifier of the AI Agent in the orchestrator configuration.</p>"""
    orchestrator_use_case: "capo_qconnect.types.non_empty_string.NonEmptyString"
    """<p>The use case for the orchestrator configuration. (for example Connect.SelfService, Connect.AgentAssistance)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrchestratorConfigurationEntry) -> dict:
    out: dict = {}
    if "ai_agent_id" in value:
        out["aiAgentId"] = value["ai_agent_id"]
    out["orchestratorUseCase"] = value["orchestrator_use_case"]
    return out


def deserialize_json(data: dict) -> OrchestratorConfigurationEntry:
    out: OrchestratorConfigurationEntry = {}  # type: ignore[typeddict-item]
    if data.get("aiAgentId") is not None:
        out["ai_agent_id"] = data["aiAgentId"]
    if data.get("orchestratorUseCase") is not None:
        out["orchestrator_use_case"] = data["orchestratorUseCase"]
    else:
        out["orchestrator_use_case"] = ""
    return out
