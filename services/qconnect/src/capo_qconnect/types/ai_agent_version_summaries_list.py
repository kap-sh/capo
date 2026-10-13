"""Generated from Smithy shape ``com.amazonaws.qconnect#AIAgentVersionSummariesList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.ai_agent_version_summary

AIAgentVersionSummariesList: TypeAlias = list[
    "capo_qconnect.types.ai_agent_version_summary.AIAgentVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AIAgentVersionSummariesList) -> list:
    import capo_qconnect.types.ai_agent_version_summary

    out: list = []
    for item in value:
        out.append(capo_qconnect.types.ai_agent_version_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AIAgentVersionSummariesList:
    import capo_qconnect.types.ai_agent_version_summary

    out: AIAgentVersionSummariesList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_qconnect.types.ai_agent_version_summary.deserialize_json(item))
    return out


def redact_sensitive(value: AIAgentVersionSummariesList) -> list[Any]:
    import capo_qconnect.types.ai_agent_version_summary

    return [
        capo_qconnect.types.ai_agent_version_summary.redact_sensitive(item)
        for item in value
    ]
