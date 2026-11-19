"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetAgentInsightResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore.types.agent_application_name
    import capo_bedrock_agentcore.types.agent_insight_archive_status
    import capo_bedrock_agentcore.types.agent_insight_customer_metadata_status
    import capo_bedrock_agentcore.types.agent_insight_id
    import capo_bedrock_agentcore.types.batch_evaluation_id
    import capo_bedrock_agentcore.types.insight_description
    import capo_bedrock_agentcore.types.insight_name
    import capo_bedrock_agentcore.types.insight_root_cause_list
    import capo_bedrock_agentcore.types.insight_sample_session_list
    import capo_bedrock_agentcore.types.insight_type


class GetAgentInsightResponse(TypedDict, closed=True):
    type: "capo_bedrock_agentcore.types.insight_type.InsightType"
    name: "capo_bedrock_agentcore.types.insight_name.InsightName"
    """<p>A generated display label for the Agent Insight. This is a human-readable summary of the detected pattern, not an identifier.</p>"""
    description: "capo_bedrock_agentcore.types.insight_description.InsightDescription"
    """<p>A generated description of the Agent Insight that explains the detected pattern and its observed behavior across sessions.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time when the Agent Insight was first created.</p>"""
    affected_session_count: NotRequired["int"]
    """<p>The number of sessions affected by the insight pattern.</p>"""
    sample_sessions: NotRequired[
        "capo_bedrock_agentcore.types.insight_sample_session_list.InsightSampleSessionList"
    ]
    """<p>A list of sample sessions that illustrate the Agent Insight, including per-session findings that point to the relevant spans or traces.</p>"""
    root_causes: NotRequired[
        "capo_bedrock_agentcore.types.insight_root_cause_list.InsightRootCauseList"
    ]
    """<p>The root causes identified for the Agent Insight, each with an explanation, an affected session count, an optional suggested fix, and sample sessions that illustrate the root cause.</p>"""
    agent_insight_id: "capo_bedrock_agentcore.types.agent_insight_id.AgentInsightId"
    """<p>The unique identifier of the Agent Insight.</p>"""
    application_name: (
        "capo_bedrock_agentcore.types.agent_application_name.AgentApplicationName"
    )
    """<p>The application that the Agent Insight belongs to.</p>"""
    batch_evaluation_id: NotRequired[
        "capo_bedrock_agentcore.types.batch_evaluation_id.BatchEvaluationId"
    ]
    """The Batch Evaluation that produced this Insight, when applicable."""
    customer_metadata_status: "capo_bedrock_agentcore.types.agent_insight_customer_metadata_status.AgentInsightCustomerMetadataStatus"
    """<p>Specifies whether customer-encrypted metadata is available for the Agent Insight.</p>"""
    updated_at: "datetime.datetime"
    """<p>The date and time when the Agent Insight was last updated.</p>"""
    archive_status: "capo_bedrock_agentcore.types.agent_insight_archive_status.AgentInsightArchiveStatus"
    """<p>Specifies whether the Agent Insight is active or archived. Valid values:</p> <ul> <li> <p> <code>ACTIVE</code> - The insight is currently active.</p> </li> <li> <p> <code>ARCHIVED</code> - The insight has been archived.</p> </li> </ul>"""
    last_seen_at: NotRequired["datetime.datetime"]
    """<p>The most recent date and time when the insight pattern was observed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentInsightResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.insight_type

    out["type"] = capo_bedrock_agentcore.types.insight_type.serialize_json(
        value["type"]
    )
    out["name"] = value["name"]
    out["description"] = value["description"]
    import capo_bedrock_agentcore._protocol.serialize

    out["createdAt"] = capo_bedrock_agentcore._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    if "affected_session_count" in value:
        out["affectedSessionCount"] = value["affected_session_count"]
    if "sample_sessions" in value:
        import capo_bedrock_agentcore.types.insight_sample_session_list

        out["sampleSessions"] = (
            capo_bedrock_agentcore.types.insight_sample_session_list.serialize_json(
                value["sample_sessions"]
            )
        )
    if "root_causes" in value:
        import capo_bedrock_agentcore.types.insight_root_cause_list

        out["rootCauses"] = (
            capo_bedrock_agentcore.types.insight_root_cause_list.serialize_json(
                value["root_causes"]
            )
        )
    out["agentInsightId"] = value["agent_insight_id"]
    out["applicationName"] = value["application_name"]
    if "batch_evaluation_id" in value:
        out["batchEvaluationId"] = value["batch_evaluation_id"]
    import capo_bedrock_agentcore.types.agent_insight_customer_metadata_status

    out["customerMetadataStatus"] = (
        capo_bedrock_agentcore.types.agent_insight_customer_metadata_status.serialize_json(
            value["customer_metadata_status"]
        )
    )
    import capo_bedrock_agentcore._protocol.serialize

    out["updatedAt"] = capo_bedrock_agentcore._protocol.serialize.fmt_date_time(
        value["updated_at"]
    )
    import capo_bedrock_agentcore.types.agent_insight_archive_status

    out["archiveStatus"] = (
        capo_bedrock_agentcore.types.agent_insight_archive_status.serialize_json(
            value["archive_status"]
        )
    )
    if "last_seen_at" in value:
        import capo_bedrock_agentcore._protocol.serialize

        out["lastSeenAt"] = capo_bedrock_agentcore._protocol.serialize.fmt_date_time(
            value["last_seen_at"]
        )
    return out


def deserialize_json(data: dict) -> GetAgentInsightResponse:
    out: GetAgentInsightResponse = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_agentcore.types.insight_type

        out["type"] = capo_bedrock_agentcore.types.insight_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_agentcore.types.insight_type.InsightType", ""
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("affectedSessionCount") is not None:
        out["affected_session_count"] = data["affectedSessionCount"]
    if data.get("sampleSessions") is not None:
        import capo_bedrock_agentcore.types.insight_sample_session_list

        out["sample_sessions"] = (
            capo_bedrock_agentcore.types.insight_sample_session_list.deserialize_json(
                data["sampleSessions"]
            )
        )
    if data.get("rootCauses") is not None:
        import capo_bedrock_agentcore.types.insight_root_cause_list

        out["root_causes"] = (
            capo_bedrock_agentcore.types.insight_root_cause_list.deserialize_json(
                data["rootCauses"]
            )
        )
    if data.get("agentInsightId") is not None:
        out["agent_insight_id"] = data["agentInsightId"]
    else:
        out["agent_insight_id"] = ""
    if data.get("applicationName") is not None:
        out["application_name"] = data["applicationName"]
    else:
        out["application_name"] = ""
    if data.get("batchEvaluationId") is not None:
        out["batch_evaluation_id"] = data["batchEvaluationId"]
    if data.get("customerMetadataStatus") is not None:
        import capo_bedrock_agentcore.types.agent_insight_customer_metadata_status

        out["customer_metadata_status"] = (
            capo_bedrock_agentcore.types.agent_insight_customer_metadata_status.deserialize_json(
                data["customerMetadataStatus"]
            )
        )
    else:
        import typing

        out["customer_metadata_status"] = typing.cast(
            "capo_bedrock_agentcore.types.agent_insight_customer_metadata_status.AgentInsightCustomerMetadataStatus",
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
    if data.get("lastSeenAt") is not None:
        import datetime

        out["last_seen_at"] = datetime.datetime.fromisoformat(
            data["lastSeenAt"].replace("Z", "+00:00")
        )
    return out


def redact_sensitive(value: GetAgentInsightResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "sample_sessions" in value:
        import capo_bedrock_agentcore.types.insight_sample_session_list

        out["sample_sessions"] = (
            capo_bedrock_agentcore.types.insight_sample_session_list.redact_sensitive(
                value["sample_sessions"]
            )
        )
    if "root_causes" in value:
        import capo_bedrock_agentcore.types.insight_root_cause_list

        out["root_causes"] = (
            capo_bedrock_agentcore.types.insight_root_cause_list.redact_sensitive(
                value["root_causes"]
            )
        )
    return out
