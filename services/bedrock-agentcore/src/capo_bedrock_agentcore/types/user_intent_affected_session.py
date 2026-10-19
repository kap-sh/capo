"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#UserIntentAffectedSession``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.user_intent_list


class UserIntentAffectedSession(TypedDict, closed=True):
    session_id: "str"
    """<p>The unique identifier of the session.</p>"""
    user_messages: "capo_bedrock_agentcore.types.user_intent_list.UserIntentList"
    """<p>The user messages from this session that contributed to the intent cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserIntentAffectedSession) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    import capo_bedrock_agentcore.types.user_intent_list

    out["userMessages"] = capo_bedrock_agentcore.types.user_intent_list.serialize_json(
        value["user_messages"]
    )
    return out


def deserialize_json(data: dict) -> UserIntentAffectedSession:
    out: UserIntentAffectedSession = {}  # type: ignore[typeddict-item]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    if data.get("userMessages") is not None:
        import capo_bedrock_agentcore.types.user_intent_list

        out["user_messages"] = (
            capo_bedrock_agentcore.types.user_intent_list.deserialize_json(
                data["userMessages"]
            )
        )
    else:
        out["user_messages"] = []
    return out
