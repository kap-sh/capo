"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InsightResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore.types.insight_description
    import capo_bedrock_agentcore.types.insight_name
    import capo_bedrock_agentcore.types.insight_root_cause_list
    import capo_bedrock_agentcore.types.insight_sample_session_list
    import capo_bedrock_agentcore.types.insight_type


class InsightResult(TypedDict, closed=True):
    type: "capo_bedrock_agentcore.types.insight_type.InsightType"
    """<p>The type of insight. <code>FAILURE</code> indicates a group of related failures.</p>"""
    name: "capo_bedrock_agentcore.types.insight_name.InsightName"
    """<p>A generated label for the insight. The name is not an identifier and can differ between batch evaluations.</p>"""
    description: "capo_bedrock_agentcore.types.insight_description.InsightDescription"
    """<p>A description of the failure pattern that the insight represents.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the insight was generated.</p>"""
    affected_session_count: NotRequired["int"]
    """<p>The number of distinct sessions affected by the insight.</p>"""
    sample_sessions: NotRequired[
        "capo_bedrock_agentcore.types.insight_sample_session_list.InsightSampleSessionList"
    ]
    """<p>A sample of up to 10 sessions affected by the insight. Returned only when the insight has no root causes. Otherwise, sample sessions are returned for each root cause.</p>"""
    root_causes: NotRequired[
        "capo_bedrock_agentcore.types.insight_root_cause_list.InsightRootCauseList"
    ]
    """<p>The root causes identified for the insight.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsightResult) -> dict:
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
    return out


def deserialize_json(data: dict) -> InsightResult:
    out: InsightResult = {}  # type: ignore[typeddict-item]
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
    return out


def redact_sensitive(value: InsightResult) -> dict[str, Any]:
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
