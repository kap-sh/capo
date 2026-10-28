"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#AsyncInvokeOutputDataConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_runtime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.async_invoke_s3_output_data_config


class AsyncInvokeOutputDataConfigS3OutputDataConfigMember(TypedDict, closed=True):
    s3OutputDataConfig: "capo_bedrock_runtime.types.async_invoke_s3_output_data_config.AsyncInvokeS3OutputDataConfig"


AsyncInvokeOutputDataConfig: TypeAlias = (
    AsyncInvokeOutputDataConfigS3OutputDataConfigMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AsyncInvokeOutputDataConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AsyncInvokeOutputDataConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "s3OutputDataConfig" in value:
        import capo_bedrock_runtime.types.async_invoke_s3_output_data_config

        return {
            "s3OutputDataConfig": capo_bedrock_runtime.types.async_invoke_s3_output_data_config.serialize_json(
                value["s3OutputDataConfig"]
            )
        }
    else:
        raise SerializationError("AsyncInvokeOutputDataConfig: no variant present")


def deserialize_json(data: dict) -> AsyncInvokeOutputDataConfig:
    if data.get("s3OutputDataConfig") is not None:
        import capo_bedrock_runtime.types.async_invoke_s3_output_data_config

        return {
            "s3OutputDataConfig": capo_bedrock_runtime.types.async_invoke_s3_output_data_config.deserialize_json(
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
            "AsyncInvokeOutputDataConfig: no recognized variant key"
        )
