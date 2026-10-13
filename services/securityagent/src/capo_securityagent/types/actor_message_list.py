"""Generated from Smithy shape ``com.amazonaws.securityagent#ActorMessageList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.actor_message

ActorMessageList: TypeAlias = list[
    "capo_securityagent.types.actor_message.ActorMessage"
]


# --- restJson1 ser/de ---
def serialize_json(value: ActorMessageList) -> list:
    import capo_securityagent.types.actor_message

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.actor_message.serialize_json(item))
    return out


def deserialize_json(data: list) -> ActorMessageList:
    import capo_securityagent.types.actor_message

    out: ActorMessageList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_securityagent.types.actor_message.deserialize_json(item))
    return out


def redact_sensitive(value: ActorMessageList) -> list[Any]:
    import capo_securityagent.types.actor_message

    return [
        capo_securityagent.types.actor_message.redact_sensitive(item) for item in value
    ]
