"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#UserIntentCluster``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.user_intent_affected_session_list


class UserIntentCluster(TypedDict, closed=True):
    cluster_id: "int"
    """<p>The unique identifier of the user intent cluster.</p>"""
    name: "str"
    """<p>The name of the user intent cluster.</p>"""
    description: "str"
    """<p>A description of the user intent pattern.</p>"""
    affected_session_count: "int"
    """<p>The number of sessions with this user intent.</p>"""
    affected_sessions: "capo_bedrock_agentcore.types.user_intent_affected_session_list.UserIntentAffectedSessionList"
    """<p>The list of sessions with this user intent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserIntentCluster) -> dict:
    out: dict = {}
    out["clusterId"] = value["cluster_id"]
    out["name"] = value["name"]
    out["description"] = value["description"]
    out["affectedSessionCount"] = value["affected_session_count"]
    import capo_bedrock_agentcore.types.user_intent_affected_session_list

    out["affectedSessions"] = (
        capo_bedrock_agentcore.types.user_intent_affected_session_list.serialize_json(
            value["affected_sessions"]
        )
    )
    return out


def deserialize_json(data: dict) -> UserIntentCluster:
    out: UserIntentCluster = {}  # type: ignore[typeddict-item]
    if data.get("clusterId") is not None:
        out["cluster_id"] = data["clusterId"]
    else:
        out["cluster_id"] = 0
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    if data.get("affectedSessionCount") is not None:
        out["affected_session_count"] = data["affectedSessionCount"]
    else:
        out["affected_session_count"] = 0
    if data.get("affectedSessions") is not None:
        import capo_bedrock_agentcore.types.user_intent_affected_session_list

        out["affected_sessions"] = (
            capo_bedrock_agentcore.types.user_intent_affected_session_list.deserialize_json(
                data["affectedSessions"]
            )
        )
    else:
        out["affected_sessions"] = []
    return out
