"""Generated from Smithy shape ``com.amazonaws.securityagent#ActorList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.actor

ActorList: TypeAlias = list["capo_securityagent.types.actor.Actor"]


# --- restJson1 ser/de ---
def serialize_json(value: ActorList) -> list:
    import capo_securityagent.types.actor

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.actor.serialize_json(item))
    return out


def deserialize_json(data: list) -> ActorList:
    import capo_securityagent.types.actor

    out: ActorList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_securityagent.types.actor.deserialize_json(item))
    return out


def redact_sensitive(value: ActorList) -> list[Any]:
    import capo_securityagent.types.actor

    return [capo_securityagent.types.actor.redact_sensitive(item) for item in value]
