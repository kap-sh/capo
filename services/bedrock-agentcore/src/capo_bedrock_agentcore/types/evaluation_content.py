"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EvaluationContent``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember


class EvaluationContentTextMember(TypedDict, closed=True):
    text: "str"


EvaluationContent: TypeAlias = EvaluationContentTextMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationContent) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"EvaluationContent: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "text" in value:
        return {"text": value["text"]}
    else:
        raise SerializationError("EvaluationContent: no variant present")


def deserialize_json(data: dict) -> EvaluationContent:
    if data.get("text") is not None:
        return {"text": data["text"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("EvaluationContent: no recognized variant key")
