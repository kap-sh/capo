"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#RootCauseCluster``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.affected_session_list


class RootCauseCluster(TypedDict, closed=True):
    cluster_id: "int"
    """<p>The unique identifier of the root cause cluster.</p>"""
    name: "str"
    """<p>The name of the root cause cluster.</p>"""
    root_cause: "str"
    """<p>The root cause explanation for this cluster of failures.</p>"""
    recommendation: "str"
    """<p>The recommended fix for this root cause.</p>"""
    affected_session_count: "int"
    """<p>The number of sessions affected by this root cause.</p>"""
    affected_sessions: (
        "capo_bedrock_agentcore.types.affected_session_list.AffectedSessionList"
    )
    """<p>The list of sessions affected by this root cause.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RootCauseCluster) -> dict:
    out: dict = {}
    out["clusterId"] = value["cluster_id"]
    out["name"] = value["name"]
    out["rootCause"] = value["root_cause"]
    out["recommendation"] = value["recommendation"]
    out["affectedSessionCount"] = value["affected_session_count"]
    import capo_bedrock_agentcore.types.affected_session_list

    out["affectedSessions"] = (
        capo_bedrock_agentcore.types.affected_session_list.serialize_json(
            value["affected_sessions"]
        )
    )
    return out


def deserialize_json(data: dict) -> RootCauseCluster:
    out: RootCauseCluster = {}  # type: ignore[typeddict-item]
    if data.get("clusterId") is not None:
        out["cluster_id"] = data["clusterId"]
    else:
        out["cluster_id"] = 0
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("rootCause") is not None:
        out["root_cause"] = data["rootCause"]
    else:
        out["root_cause"] = ""
    if data.get("recommendation") is not None:
        out["recommendation"] = data["recommendation"]
    else:
        out["recommendation"] = ""
    if data.get("affectedSessionCount") is not None:
        out["affected_session_count"] = data["affectedSessionCount"]
    else:
        out["affected_session_count"] = 0
    if data.get("affectedSessions") is not None:
        import capo_bedrock_agentcore.types.affected_session_list

        out["affected_sessions"] = (
            capo_bedrock_agentcore.types.affected_session_list.deserialize_json(
                data["affectedSessions"]
            )
        )
    else:
        out["affected_sessions"] = []
    return out
