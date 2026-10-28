"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#StreamUpdate``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.automation_stream_update


class StreamUpdateAutomationStreamUpdateMember(TypedDict, closed=True):
    automationStreamUpdate: (
        "capo_bedrock_agentcore.types.automation_stream_update.AutomationStreamUpdate"
    )


StreamUpdate: TypeAlias = StreamUpdateAutomationStreamUpdateMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: StreamUpdate) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"StreamUpdate: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "automationStreamUpdate" in value:
        import capo_bedrock_agentcore.types.automation_stream_update

        return {
            "automationStreamUpdate": capo_bedrock_agentcore.types.automation_stream_update.serialize_json(
                value["automationStreamUpdate"]
            )
        }
    else:
        raise SerializationError("StreamUpdate: no variant present")


def deserialize_json(data: dict) -> StreamUpdate:
    if data.get("automationStreamUpdate") is not None:
        import capo_bedrock_agentcore.types.automation_stream_update

        return {
            "automationStreamUpdate": capo_bedrock_agentcore.types.automation_stream_update.deserialize_json(
                data["automationStreamUpdate"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("StreamUpdate: no recognized variant key")
