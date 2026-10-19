"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#StreamDeliveryResource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.kinesis_resource


class _StreamDeliveryResource_kinesis(TypedDict, closed=True):
    kinesis: "capo_bedrock_agentcore_control.types.kinesis_resource.KinesisResource"


StreamDeliveryResource: TypeAlias = _StreamDeliveryResource_kinesis | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: StreamDeliveryResource) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"StreamDeliveryResource: cannot serialize unknown variant {value.name!r}"
        )
    elif "kinesis" in value:
        import capo_bedrock_agentcore_control.types.kinesis_resource

        return {
            "kinesis": capo_bedrock_agentcore_control.types.kinesis_resource.serialize_json(
                value["kinesis"]
            )
        }
    else:
        raise SerializationError("StreamDeliveryResource: no variant present")


def deserialize_json(data: dict) -> StreamDeliveryResource:
    if data.get("kinesis") is not None:
        import capo_bedrock_agentcore_control.types.kinesis_resource

        return {
            "kinesis": capo_bedrock_agentcore_control.types.kinesis_resource.deserialize_json(
                data["kinesis"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("StreamDeliveryResource: no recognized variant key")
