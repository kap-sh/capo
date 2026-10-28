"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CodeBasedEvaluatorConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.lambda_evaluator_config


class CodeBasedEvaluatorConfigLambdaConfigMember(TypedDict, closed=True):
    lambdaConfig: "capo_bedrock_agentcore_control.types.lambda_evaluator_config.LambdaEvaluatorConfig"


CodeBasedEvaluatorConfig: TypeAlias = (
    CodeBasedEvaluatorConfigLambdaConfigMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: CodeBasedEvaluatorConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CodeBasedEvaluatorConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "lambdaConfig" in value:
        import capo_bedrock_agentcore_control.types.lambda_evaluator_config

        return {
            "lambdaConfig": capo_bedrock_agentcore_control.types.lambda_evaluator_config.serialize_json(
                value["lambdaConfig"]
            )
        }
    else:
        raise SerializationError("CodeBasedEvaluatorConfig: no variant present")


def deserialize_json(data: dict) -> CodeBasedEvaluatorConfig:
    if data.get("lambdaConfig") is not None:
        import capo_bedrock_agentcore_control.types.lambda_evaluator_config

        return {
            "lambdaConfig": capo_bedrock_agentcore_control.types.lambda_evaluator_config.deserialize_json(
                data["lambdaConfig"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "CodeBasedEvaluatorConfig: no recognized variant key"
        )
