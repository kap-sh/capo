"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GroundTruthSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.inline_ground_truth


class GroundTruthSourceInlineMember(TypedDict, closed=True):
    inline: "capo_bedrock_agentcore.types.inline_ground_truth.InlineGroundTruth"


GroundTruthSource: TypeAlias = GroundTruthSourceInlineMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: GroundTruthSource) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"GroundTruthSource: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "inline" in value:
        import capo_bedrock_agentcore.types.inline_ground_truth

        return {
            "inline": capo_bedrock_agentcore.types.inline_ground_truth.serialize_json(
                value["inline"]
            )
        }
    else:
        raise SerializationError("GroundTruthSource: no variant present")


def deserialize_json(data: dict) -> GroundTruthSource:
    if data.get("inline") is not None:
        import capo_bedrock_agentcore.types.inline_ground_truth

        return {
            "inline": capo_bedrock_agentcore.types.inline_ground_truth.deserialize_json(
                data["inline"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("GroundTruthSource: no recognized variant key")
