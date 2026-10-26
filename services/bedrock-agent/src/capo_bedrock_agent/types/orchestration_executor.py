"""Generated from Smithy shape ``com.amazonaws.bedrockagent#OrchestrationExecutor``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError, SerializationError
from capo_bedrock_agent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agent.types.lambda_arn

_OrchestrationExecutor_lambda = TypedDict(
    "_OrchestrationExecutor_lambda",
    {
        "lambda": "capo_bedrock_agent.types.lambda_arn.LambdaArn",
    },
    closed=True,
)

OrchestrationExecutor: TypeAlias = _OrchestrationExecutor_lambda | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: OrchestrationExecutor) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"OrchestrationExecutor: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "lambda" in value:
        return {"lambda": value["lambda"]}
    else:
        raise SerializationError("OrchestrationExecutor: no variant present")


def deserialize_json(data: dict) -> OrchestrationExecutor:
    if data.get("lambda") is not None:
        return {"lambda": data["lambda"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("OrchestrationExecutor: no recognized variant key")
