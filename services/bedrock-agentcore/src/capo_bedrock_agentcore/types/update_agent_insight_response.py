"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#UpdateAgentInsightResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore.types.agent_insight_archive_status
    import capo_bedrock_agentcore.types.agent_insight_id


class UpdateAgentInsightResponse(TypedDict, closed=True):
    agent_insight_id: "capo_bedrock_agentcore.types.agent_insight_id.AgentInsightId"
    """<p>The unique identifier of the updated Agent Insight.</p>"""
    archive_status: "capo_bedrock_agentcore.types.agent_insight_archive_status.AgentInsightArchiveStatus"
    """<p>The archive status of the updated Agent Insight. Valid values:</p> <ul> <li> <p> <code>ACTIVE</code> - The insight is active.</p> </li> <li> <p> <code>ARCHIVED</code> - The insight is archived.</p> </li> </ul>"""
    updated_at: "datetime.datetime"
    """<p>The date and time when the Agent Insight was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentInsightResponse) -> dict:
    out: dict = {}
    out["agentInsightId"] = value["agent_insight_id"]
    import capo_bedrock_agentcore.types.agent_insight_archive_status

    out["archiveStatus"] = (
        capo_bedrock_agentcore.types.agent_insight_archive_status.serialize_json(
            value["archive_status"]
        )
    )
    import capo_bedrock_agentcore._protocol.serialize

    out["updatedAt"] = capo_bedrock_agentcore._protocol.serialize.fmt_date_time(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> UpdateAgentInsightResponse:
    out: UpdateAgentInsightResponse = {}  # type: ignore[typeddict-item]
    if data.get("agentInsightId") is not None:
        out["agent_insight_id"] = data["agentInsightId"]
    else:
        out["agent_insight_id"] = ""
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
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
