"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PayloadType``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.conversational
    import capo_bedrock_agentcore.types.memory_document
    import capo_bedrock_agentcore.types.memory_json_data


class _PayloadType_conversational(TypedDict, closed=True):
    conversational: "capo_bedrock_agentcore.types.conversational.Conversational"


class _PayloadType_blob(TypedDict, closed=True):
    blob: "capo_bedrock_agentcore.types.memory_document.MemoryDocument"


class _PayloadType_json(TypedDict, closed=True):
    json: "capo_bedrock_agentcore.types.memory_json_data.MemoryJsonData"


PayloadType: TypeAlias = (
    _PayloadType_conversational
    | _PayloadType_blob
    | _PayloadType_json
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: PayloadType) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"PayloadType: cannot serialize unknown variant {value.name!r}"
        )
    elif "conversational" in value:
        import capo_bedrock_agentcore.types.conversational

        return {
            "conversational": capo_bedrock_agentcore.types.conversational.serialize_json(
                value["conversational"]
            )
        }
    elif "blob" in value:
        return {"blob": value["blob"]}
    elif "json" in value:
        import capo_bedrock_agentcore.types.memory_json_data

        return {
            "json": capo_bedrock_agentcore.types.memory_json_data.serialize_json(
                value["json"]
            )
        }
    else:
        raise SerializationError("PayloadType: no variant present")


def deserialize_json(data: dict) -> PayloadType:
    if data.get("conversational") is not None:
        import capo_bedrock_agentcore.types.conversational

        return {
            "conversational": capo_bedrock_agentcore.types.conversational.deserialize_json(
                data["conversational"]
            )
        }
    elif data.get("blob") is not None:
        return {"blob": data["blob"]}
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
            return UnknownUnionMember(name)
        raise DeserializationError("PayloadType: no recognized variant key")


def redact_sensitive(value: PayloadType) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "conversational" in value:
        import capo_bedrock_agentcore.types.conversational

        out["conversational"] = (
            capo_bedrock_agentcore.types.conversational.redact_sensitive(
                value["conversational"]
            )
        )
    if "blob" in value:
        out["blob"] = "*** Sensitive Data Redacted ***"
    if "json" in value:
        out["json"] = "*** Sensitive Data Redacted ***"
    return out
