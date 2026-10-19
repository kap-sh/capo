"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#UserIntentClusteringResultContent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.user_intent_cluster_list


class UserIntentClusteringResultContent(TypedDict, closed=True):
    user_intents: (
        "capo_bedrock_agentcore.types.user_intent_cluster_list.UserIntentClusterList"
    )
    """<p>The list of user intent clusters identified across analyzed sessions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserIntentClusteringResultContent) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.user_intent_cluster_list

    out["userIntents"] = (
        capo_bedrock_agentcore.types.user_intent_cluster_list.serialize_json(
            value["user_intents"]
        )
    )
    return out


def deserialize_json(data: dict) -> UserIntentClusteringResultContent:
    out: UserIntentClusteringResultContent = {}  # type: ignore[typeddict-item]
    if data.get("userIntents") is not None:
        import capo_bedrock_agentcore.types.user_intent_cluster_list

        out["user_intents"] = (
            capo_bedrock_agentcore.types.user_intent_cluster_list.deserialize_json(
                data["userIntents"]
            )
        )
    else:
        out["user_intents"] = []
    return out
