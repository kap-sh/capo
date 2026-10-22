"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#SampleSession``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore.types.session_finding_list
    import capo_bedrock_agentcore.types.session_id


class SampleSession(TypedDict, closed=True):
    session_id: "capo_bedrock_agentcore.types.session_id.SessionId"
    """<p>The unique identifier of the session.</p>"""
    last_seen_at: NotRequired["datetime.datetime"]
    """<p>The latest timestamp observed for the session in the batch evaluation input.</p>"""
    findings: NotRequired[
        "capo_bedrock_agentcore.types.session_finding_list.SessionFindingList"
    ]
    """<p>The failures found in the session that belong to the insight or root cause, up to 10.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SampleSession) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    if "last_seen_at" in value:
        import capo_bedrock_agentcore._protocol.serialize

        out["lastSeenAt"] = capo_bedrock_agentcore._protocol.serialize.fmt_date_time(
            value["last_seen_at"]
        )
    if "findings" in value:
        import capo_bedrock_agentcore.types.session_finding_list

        out["findings"] = (
            capo_bedrock_agentcore.types.session_finding_list.serialize_json(
                value["findings"]
            )
        )
    return out


def deserialize_json(data: dict) -> SampleSession:
    out: SampleSession = {}  # type: ignore[typeddict-item]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    if data.get("lastSeenAt") is not None:
        import datetime

        out["last_seen_at"] = datetime.datetime.fromisoformat(
            data["lastSeenAt"].replace("Z", "+00:00")
        )
    if data.get("findings") is not None:
        import capo_bedrock_agentcore.types.session_finding_list

        out["findings"] = (
            capo_bedrock_agentcore.types.session_finding_list.deserialize_json(
                data["findings"]
            )
        )
    return out


def redact_sensitive(value: SampleSession) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "findings" in value:
        import capo_bedrock_agentcore.types.session_finding_list

        out["findings"] = (
            capo_bedrock_agentcore.types.session_finding_list.redact_sensitive(
                value["findings"]
            )
        )
    return out
