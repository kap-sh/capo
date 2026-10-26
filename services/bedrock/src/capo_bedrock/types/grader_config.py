"""Generated from Smithy shape ``com.amazonaws.bedrock#GraderConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError
from capo_bedrock.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock.types.lambda_grader_config


class _GraderConfig_lambdaGrader(TypedDict, closed=True):
    lambdaGrader: "capo_bedrock.types.lambda_grader_config.LambdaGraderConfig"


GraderConfig: TypeAlias = _GraderConfig_lambdaGrader | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: GraderConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"GraderConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "lambdaGrader" in value:
        import capo_bedrock.types.lambda_grader_config

        return {
            "lambdaGrader": capo_bedrock.types.lambda_grader_config.serialize_json(
                value["lambdaGrader"]
            )
        }
    else:
        raise SerializationError("GraderConfig: no variant present")


def deserialize_json(data: dict) -> GraderConfig:
    if data.get("lambdaGrader") is not None:
        import capo_bedrock.types.lambda_grader_config

        return {
            "lambdaGrader": capo_bedrock.types.lambda_grader_config.deserialize_json(
                data["lambdaGrader"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("GraderConfig: no recognized variant key")
