"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#InterceptorConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.lambda_interceptor_configuration

_InterceptorConfiguration_lambda = TypedDict(
    "_InterceptorConfiguration_lambda",
    {
        "lambda": "capo_bedrock_agentcore_control.types.lambda_interceptor_configuration.LambdaInterceptorConfiguration",
    },
    closed=True,
)

InterceptorConfiguration: TypeAlias = (
    _InterceptorConfiguration_lambda | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: InterceptorConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"InterceptorConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "lambda" in value:
        import capo_bedrock_agentcore_control.types.lambda_interceptor_configuration

        return {
            "lambda": capo_bedrock_agentcore_control.types.lambda_interceptor_configuration.serialize_json(
                value["lambda"]
            )
        }
    else:
        raise SerializationError("InterceptorConfiguration: no variant present")


def deserialize_json(data: dict) -> InterceptorConfiguration:
    if data.get("lambda") is not None:
        import capo_bedrock_agentcore_control.types.lambda_interceptor_configuration

        return {
            "lambda": capo_bedrock_agentcore_control.types.lambda_interceptor_configuration.deserialize_json(
                data["lambda"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "InterceptorConfiguration: no recognized variant key"
        )
