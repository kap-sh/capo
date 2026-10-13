"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EventList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.event

EventList: TypeAlias = list["capo_bedrock_agentcore.types.event.Event"]


# --- restJson1 ser/de ---
def serialize_json(value: EventList) -> list:
    import capo_bedrock_agentcore.types.event

    out: list = []
    for item in value:
        out.append(capo_bedrock_agentcore.types.event.serialize_json(item))
    return out


def deserialize_json(data: list) -> EventList:
    import capo_bedrock_agentcore.types.event

    out: EventList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agentcore.types.event.deserialize_json(item))
    return out


def redact_sensitive(value: EventList) -> list[Any]:
    import capo_bedrock_agentcore.types.event

    return [capo_bedrock_agentcore.types.event.redact_sensitive(item) for item in value]
