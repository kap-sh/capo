"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EvaluatorReference``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.evaluator_id


class _EvaluatorReference_evaluatorId(TypedDict, closed=True):
    evaluatorId: "capo_bedrock_agentcore_control.types.evaluator_id.EvaluatorId"


EvaluatorReference: TypeAlias = _EvaluatorReference_evaluatorId | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: EvaluatorReference) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"EvaluatorReference: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "evaluatorId" in value:
        return {"evaluatorId": value["evaluatorId"]}
    else:
        raise SerializationError("EvaluatorReference: no variant present")


def deserialize_json(data: dict) -> EvaluatorReference:
    if data.get("evaluatorId") is not None:
        return {"evaluatorId": data["evaluatorId"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("EvaluatorReference: no recognized variant key")
