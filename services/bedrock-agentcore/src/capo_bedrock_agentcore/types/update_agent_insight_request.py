"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#UpdateAgentInsightRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.agent_application_name
    import capo_bedrock_agentcore.types.agent_insight_archive_status
    import capo_bedrock_agentcore.types.agent_insight_id


class UpdateAgentInsightRequest(TypedDict, closed=True):
    application_name: (
        "capo_bedrock_agentcore.types.agent_application_name.AgentApplicationName"
    )
    """<p>The application that the Agent Insight belongs to.</p>"""
    agent_insight_id: "capo_bedrock_agentcore.types.agent_insight_id.AgentInsightId"
    """<p>The unique identifier of the Agent Insight to update.</p>"""
    archive_status: "capo_bedrock_agentcore.types.agent_insight_archive_status.AgentInsightArchiveStatus"
    """<p>The archive status to apply to the Agent Insight. Valid values:</p> <ul> <li> <p> <code>ACTIVE</code> - Marks the insight as active.</p> </li> <li> <p> <code>ARCHIVED</code> - Marks the insight as archived.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentInsightRequest) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.agent_insight_archive_status

    out["archiveStatus"] = (
        capo_bedrock_agentcore.types.agent_insight_archive_status.serialize_json(
            value["archive_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateAgentInsightRequest:
    out: UpdateAgentInsightRequest = {}  # type: ignore[typeddict-item]
    if data.get("archiveStatus") is not None:
        import capo_bedrock_agentcore.types.agent_insight_archive_status

        out["archive_status"] = (
            capo_bedrock_agentcore.types.agent_insight_archive_status.deserialize_json(
                data["archiveStatus"]
            )
        )
    else:
        import typing

        out["archive_status"] = typing.cast(
            "capo_bedrock_agentcore.types.agent_insight_archive_status.AgentInsightArchiveStatus",
            "",
        )
    return out
