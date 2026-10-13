"""Generated from Smithy shape ``com.amazonaws.qconnect#AIAgentSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.ai_agent_summary

AIAgentSummaryList: TypeAlias = list[
    "capo_qconnect.types.ai_agent_summary.AIAgentSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AIAgentSummaryList) -> list:
    import capo_qconnect.types.ai_agent_summary

    out: list = []
    for item in value:
        out.append(capo_qconnect.types.ai_agent_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AIAgentSummaryList:
    import capo_qconnect.types.ai_agent_summary

    out: AIAgentSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_qconnect.types.ai_agent_summary.deserialize_json(item))
    return out


def redact_sensitive(value: AIAgentSummaryList) -> list[Any]:
    import capo_qconnect.types.ai_agent_summary

    return [
        capo_qconnect.types.ai_agent_summary.redact_sensitive(item) for item in value
    ]
