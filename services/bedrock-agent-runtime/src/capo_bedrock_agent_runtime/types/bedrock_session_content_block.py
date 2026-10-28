"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#BedrockSessionContentBlock``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_agent_runtime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.image_block


class BedrockSessionContentBlockTextMember(TypedDict, closed=True):
    text: "str"


class BedrockSessionContentBlockImageMember(TypedDict, closed=True):
    image: "capo_bedrock_agent_runtime.types.image_block.ImageBlock"


BedrockSessionContentBlock: TypeAlias = (
    BedrockSessionContentBlockTextMember
    | BedrockSessionContentBlockImageMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: BedrockSessionContentBlock) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"BedrockSessionContentBlock: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "text" in value:
        return {"text": value["text"]}
    elif "image" in value:
        import capo_bedrock_agent_runtime.types.image_block

        return {
            "image": capo_bedrock_agent_runtime.types.image_block.serialize_json(
                value["image"]
            )
        }
    else:
        raise SerializationError("BedrockSessionContentBlock: no variant present")


def deserialize_json(data: dict) -> BedrockSessionContentBlock:
    if data.get("text") is not None:
        return {"text": data["text"]}
    elif data.get("image") is not None:
        import capo_bedrock_agent_runtime.types.image_block

        return {
            "image": capo_bedrock_agent_runtime.types.image_block.deserialize_json(
                data["image"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "BedrockSessionContentBlock: no recognized variant key"
        )
