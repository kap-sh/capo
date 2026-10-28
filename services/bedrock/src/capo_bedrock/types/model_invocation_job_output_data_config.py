"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelInvocationJobOutputDataConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError
from capo_bedrock.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock.types.model_invocation_job_s3_output_data_config


class ModelInvocationJobOutputDataConfigS3OutputDataConfigMember(
    TypedDict, closed=True
):
    s3OutputDataConfig: "capo_bedrock.types.model_invocation_job_s3_output_data_config.ModelInvocationJobS3OutputDataConfig"


ModelInvocationJobOutputDataConfig: TypeAlias = (
    ModelInvocationJobOutputDataConfigS3OutputDataConfigMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ModelInvocationJobOutputDataConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ModelInvocationJobOutputDataConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "s3OutputDataConfig" in value:
        import capo_bedrock.types.model_invocation_job_s3_output_data_config

        return {
            "s3OutputDataConfig": capo_bedrock.types.model_invocation_job_s3_output_data_config.serialize_json(
                value["s3OutputDataConfig"]
            )
        }
    else:
        raise SerializationError(
            "ModelInvocationJobOutputDataConfig: no variant present"
        )


def deserialize_json(data: dict) -> ModelInvocationJobOutputDataConfig:
    if data.get("s3OutputDataConfig") is not None:
        import capo_bedrock.types.model_invocation_job_s3_output_data_config

        return {
            "s3OutputDataConfig": capo_bedrock.types.model_invocation_job_s3_output_data_config.deserialize_json(
                data["s3OutputDataConfig"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "ModelInvocationJobOutputDataConfig: no recognized variant key"
        )
