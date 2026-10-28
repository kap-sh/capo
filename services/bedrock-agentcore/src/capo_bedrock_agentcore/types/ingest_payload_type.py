"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#IngestPayloadType``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.conversational
    import capo_bedrock_agentcore.types.memory_json_data


class IngestPayloadTypeConversationalMember(TypedDict, closed=True):
    conversational: "capo_bedrock_agentcore.types.conversational.Conversational"


class IngestPayloadTypeJsonMember(TypedDict, closed=True):
    json: "capo_bedrock_agentcore.types.memory_json_data.MemoryJsonData"


IngestPayloadType: TypeAlias = (
    IngestPayloadTypeConversationalMember
    | IngestPayloadTypeJsonMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: IngestPayloadType) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"IngestPayloadType: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "conversational" in value:
        import capo_bedrock_agentcore.types.conversational

        return {
            "conversational": capo_bedrock_agentcore.types.conversational.serialize_json(
                value["conversational"]
            )
        }
    elif "json" in value:
        import capo_bedrock_agentcore.types.memory_json_data

        return {
            "json": capo_bedrock_agentcore.types.memory_json_data.serialize_json(
                value["json"]
            )
        }
    else:
        raise SerializationError("IngestPayloadType: no variant present")


def deserialize_json(data: dict) -> IngestPayloadType:
    if data.get("conversational") is not None:
        import capo_bedrock_agentcore.types.conversational

        return {
            "conversational": capo_bedrock_agentcore.types.conversational.deserialize_json(
                data["conversational"]
            )
        }
    elif data.get("json") is not None:
        import capo_bedrock_agentcore.types.memory_json_data

        return {
            "json": capo_bedrock_agentcore.types.memory_json_data.deserialize_json(
                data["json"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("IngestPayloadType: no recognized variant key")


def redact_sensitive(value: IngestPayloadType) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "conversational" in value:
        import capo_bedrock_agentcore.types.conversational

        out["conversational"] = (
            capo_bedrock_agentcore.types.conversational.redact_sensitive(
                value["conversational"]
            )
        )
    if "json" in value:
        out["json"] = "*** Sensitive Data Redacted ***"
    return out
