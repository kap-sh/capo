"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Code``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.s3_location


class _Code_s3(TypedDict, closed=True):
    s3: "capo_bedrock_agentcore_control.types.s3_location.S3Location"


Code: TypeAlias = _Code_s3 | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: Code) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Code: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "s3" in value:
        import capo_bedrock_agentcore_control.types.s3_location

        return {
            "s3": capo_bedrock_agentcore_control.types.s3_location.serialize_json(
                value["s3"]
            )
        }
    else:
        raise SerializationError("Code: no variant present")


def deserialize_json(data: dict) -> Code:
    if data.get("s3") is not None:
        import capo_bedrock_agentcore_control.types.s3_location

        return {
            "s3": capo_bedrock_agentcore_control.types.s3_location.deserialize_json(
                data["s3"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Code: no recognized variant key")
