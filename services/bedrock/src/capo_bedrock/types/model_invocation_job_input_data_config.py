"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelInvocationJobInputDataConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError
from capo_bedrock.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock.types.model_invocation_job_s3_input_data_config


class _ModelInvocationJobInputDataConfig_s3InputDataConfig(TypedDict, closed=True):
    s3InputDataConfig: "capo_bedrock.types.model_invocation_job_s3_input_data_config.ModelInvocationJobS3InputDataConfig"


ModelInvocationJobInputDataConfig: TypeAlias = (
    _ModelInvocationJobInputDataConfig_s3InputDataConfig | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ModelInvocationJobInputDataConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ModelInvocationJobInputDataConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "s3InputDataConfig" in value:
        import capo_bedrock.types.model_invocation_job_s3_input_data_config

        return {
            "s3InputDataConfig": capo_bedrock.types.model_invocation_job_s3_input_data_config.serialize_json(
                value["s3InputDataConfig"]
            )
        }
    else:
        raise SerializationError(
            "ModelInvocationJobInputDataConfig: no variant present"
        )


def deserialize_json(data: dict) -> ModelInvocationJobInputDataConfig:
    if data.get("s3InputDataConfig") is not None:
        import capo_bedrock.types.model_invocation_job_s3_input_data_config

        return {
            "s3InputDataConfig": capo_bedrock.types.model_invocation_job_s3_input_data_config.deserialize_json(
                data["s3InputDataConfig"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "ModelInvocationJobInputDataConfig: no recognized variant key"
        )
