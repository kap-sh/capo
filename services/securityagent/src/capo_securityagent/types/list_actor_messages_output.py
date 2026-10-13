"""Generated from Smithy shape ``com.amazonaws.securityagent#ListActorMessagesOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.actor_message_list
    import capo_securityagent.types.next_token


class ListActorMessagesOutput(TypedDict, closed=True):
    messages: NotRequired[
        "capo_securityagent.types.actor_message_list.ActorMessageList"
    ]
    """<p>The list of messages received for the actor, most recent first.</p>"""
    next_token: NotRequired["capo_securityagent.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListActorMessagesOutput) -> dict:
    out: dict = {}
    if "messages" in value:
        import capo_securityagent.types.actor_message_list

        out["messages"] = capo_securityagent.types.actor_message_list.serialize_json(
            value["messages"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListActorMessagesOutput:
    out: ListActorMessagesOutput = {}  # type: ignore[typeddict-item]
    if data.get("messages") is not None:
        import capo_securityagent.types.actor_message_list

        out["messages"] = capo_securityagent.types.actor_message_list.deserialize_json(
            data["messages"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListActorMessagesOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "messages" in value:
        import capo_securityagent.types.actor_message_list

        out["messages"] = capo_securityagent.types.actor_message_list.redact_sensitive(
            value["messages"]
        )
    return out
