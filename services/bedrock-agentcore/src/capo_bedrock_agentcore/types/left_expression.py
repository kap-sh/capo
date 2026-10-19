"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#LeftExpression``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.metadata_key


class _LeftExpression_metadataKey(TypedDict, closed=True):
    metadataKey: "capo_bedrock_agentcore.types.metadata_key.MetadataKey"


LeftExpression: TypeAlias = _LeftExpression_metadataKey | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: LeftExpression) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"LeftExpression: cannot serialize unknown variant {value.name!r}"
        )
    elif "metadataKey" in value:
        return {"metadataKey": value["metadataKey"]}
    else:
        raise SerializationError("LeftExpression: no variant present")


def deserialize_json(data: dict) -> LeftExpression:
    if data.get("metadataKey") is not None:
        return {"metadataKey": data["metadataKey"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("LeftExpression: no recognized variant key")
