"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GroundTruthTurnInput``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember


class _GroundTruthTurnInput_prompt(TypedDict, closed=True):
    prompt: "str"


GroundTruthTurnInput: TypeAlias = _GroundTruthTurnInput_prompt | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: GroundTruthTurnInput) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"GroundTruthTurnInput: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "prompt" in value:
        return {"prompt": value["prompt"]}
    else:
        raise SerializationError("GroundTruthTurnInput: no variant present")


def deserialize_json(data: dict) -> GroundTruthTurnInput:
    if data.get("prompt") is not None:
        return {"prompt": data["prompt"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("GroundTruthTurnInput: no recognized variant key")
