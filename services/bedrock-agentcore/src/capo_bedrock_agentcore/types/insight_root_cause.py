"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InsightRootCause``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.insight_sample_session_list
    import capo_bedrock_agentcore.types.root_cause_explanation
    import capo_bedrock_agentcore.types.root_cause_name
    import capo_bedrock_agentcore.types.suggested_fix


class InsightRootCause(TypedDict, closed=True):
    name: "capo_bedrock_agentcore.types.root_cause_name.RootCauseName"
    """<p>A generated label for the root cause.</p>"""
    explanation: (
        "capo_bedrock_agentcore.types.root_cause_explanation.RootCauseExplanation"
    )
    """<p>An explanation of how the root cause leads to the failures in the insight.</p>"""
    affected_session_count: NotRequired["int"]
    """<p>The number of distinct sessions affected by the root cause. A session can be affected by more than one root cause of the same insight.</p>"""
    suggested_fix: NotRequired[
        "capo_bedrock_agentcore.types.suggested_fix.SuggestedFix"
    ]
    """<p>A suggested change to the agent that addresses the root cause.</p>"""
    sample_sessions: NotRequired[
        "capo_bedrock_agentcore.types.insight_sample_session_list.InsightSampleSessionList"
    ]
    """<p>A sample of up to 10 sessions affected by the root cause.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsightRootCause) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["explanation"] = value["explanation"]
    if "affected_session_count" in value:
        out["affectedSessionCount"] = value["affected_session_count"]
    if "suggested_fix" in value:
        out["suggestedFix"] = value["suggested_fix"]
    if "sample_sessions" in value:
        import capo_bedrock_agentcore.types.insight_sample_session_list

        out["sampleSessions"] = (
            capo_bedrock_agentcore.types.insight_sample_session_list.serialize_json(
                value["sample_sessions"]
            )
        )
    return out


def deserialize_json(data: dict) -> InsightRootCause:
    out: InsightRootCause = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("explanation") is not None:
        out["explanation"] = data["explanation"]
    else:
        out["explanation"] = ""
    if data.get("affectedSessionCount") is not None:
        out["affected_session_count"] = data["affectedSessionCount"]
    if data.get("suggestedFix") is not None:
        out["suggested_fix"] = data["suggestedFix"]
    if data.get("sampleSessions") is not None:
        import capo_bedrock_agentcore.types.insight_sample_session_list

        out["sample_sessions"] = (
            capo_bedrock_agentcore.types.insight_sample_session_list.deserialize_json(
                data["sampleSessions"]
            )
        )
    return out


def redact_sensitive(value: InsightRootCause) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "explanation" in value:
        out["explanation"] = "*** Sensitive Data Redacted ***"
    if "suggested_fix" in value:
        out["suggested_fix"] = "*** Sensitive Data Redacted ***"
    if "sample_sessions" in value:
        import capo_bedrock_agentcore.types.insight_sample_session_list

        out["sample_sessions"] = (
            capo_bedrock_agentcore.types.insight_sample_session_list.redact_sensitive(
                value["sample_sessions"]
            )
        )
    return out
