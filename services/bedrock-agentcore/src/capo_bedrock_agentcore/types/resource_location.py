"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ResourceLocation``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.s3_location


class _ResourceLocation_s3(TypedDict, closed=True):
    s3: "capo_bedrock_agentcore.types.s3_location.S3Location"


ResourceLocation: TypeAlias = _ResourceLocation_s3 | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: ResourceLocation) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"ResourceLocation: cannot serialize unknown variant {value.name!r}"
        )
    elif "s3" in value:
        import capo_bedrock_agentcore.types.s3_location

        return {
            "s3": capo_bedrock_agentcore.types.s3_location.serialize_json(value["s3"])
        }
    else:
        raise SerializationError("ResourceLocation: no variant present")


def deserialize_json(data: dict) -> ResourceLocation:
    if data.get("s3") is not None:
        import capo_bedrock_agentcore.types.s3_location

        return {
            "s3": capo_bedrock_agentcore.types.s3_location.deserialize_json(data["s3"])
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("ResourceLocation: no recognized variant key")
