"""Generated from Smithy shape ``com.amazonaws.wellarchitected#AgentProfileSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_profile_summary

AgentProfileSummaries: TypeAlias = list[
    "capo_wellarchitected.types.agent_profile_summary.AgentProfileSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentProfileSummaries) -> list:
    import capo_wellarchitected.types.agent_profile_summary

    out: list = []
    for item in value:
        out.append(
            capo_wellarchitected.types.agent_profile_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AgentProfileSummaries:
    import capo_wellarchitected.types.agent_profile_summary

    out: AgentProfileSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_wellarchitected.types.agent_profile_summary.deserialize_json(item)
        )
    return out


def redact_sensitive(value: AgentProfileSummaries) -> list[Any]:
    import capo_wellarchitected.types.agent_profile_summary

    return [
        capo_wellarchitected.types.agent_profile_summary.redact_sensitive(item)
        for item in value
    ]
