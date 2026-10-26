"""Generated from Smithy shape ``com.amazonaws.sagemaker#OptimizationConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_sagemaker.errors import DeserializationError, SerializationError
from capo_sagemaker.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_sagemaker.types.model_compilation_config
    import capo_sagemaker.types.model_quantization_config
    import capo_sagemaker.types.model_sharding_config
    import capo_sagemaker.types.model_speculative_decoding_config


class _OptimizationConfig_ModelQuantizationConfig(TypedDict, closed=True):
    ModelQuantizationConfig: (
        "capo_sagemaker.types.model_quantization_config.ModelQuantizationConfig"
    )


class _OptimizationConfig_ModelCompilationConfig(TypedDict, closed=True):
    ModelCompilationConfig: (
        "capo_sagemaker.types.model_compilation_config.ModelCompilationConfig"
    )


class _OptimizationConfig_ModelShardingConfig(TypedDict, closed=True):
    ModelShardingConfig: (
        "capo_sagemaker.types.model_sharding_config.ModelShardingConfig"
    )


class _OptimizationConfig_ModelSpeculativeDecodingConfig(TypedDict, closed=True):
    ModelSpeculativeDecodingConfig: "capo_sagemaker.types.model_speculative_decoding_config.ModelSpeculativeDecodingConfig"


OptimizationConfig: TypeAlias = (
    _OptimizationConfig_ModelQuantizationConfig
    | _OptimizationConfig_ModelCompilationConfig
    | _OptimizationConfig_ModelShardingConfig
    | _OptimizationConfig_ModelSpeculativeDecodingConfig
    | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OptimizationConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"OptimizationConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "ModelQuantizationConfig" in value:
        import capo_sagemaker.types.model_quantization_config

        return {
            "ModelQuantizationConfig": capo_sagemaker.types.model_quantization_config.serialize_aws_json_1_1(
                value["ModelQuantizationConfig"]
            )
        }
    elif "ModelCompilationConfig" in value:
        import capo_sagemaker.types.model_compilation_config

        return {
            "ModelCompilationConfig": capo_sagemaker.types.model_compilation_config.serialize_aws_json_1_1(
                value["ModelCompilationConfig"]
            )
        }
    elif "ModelShardingConfig" in value:
        import capo_sagemaker.types.model_sharding_config

        return {
            "ModelShardingConfig": capo_sagemaker.types.model_sharding_config.serialize_aws_json_1_1(
                value["ModelShardingConfig"]
            )
        }
    elif "ModelSpeculativeDecodingConfig" in value:
        import capo_sagemaker.types.model_speculative_decoding_config

        return {
            "ModelSpeculativeDecodingConfig": capo_sagemaker.types.model_speculative_decoding_config.serialize_aws_json_1_1(
                value["ModelSpeculativeDecodingConfig"]
            )
        }
    else:
        raise SerializationError("OptimizationConfig: no variant present")


def deserialize_aws_json_1_1(data: dict) -> OptimizationConfig:
    if data.get("ModelQuantizationConfig") is not None:
        import capo_sagemaker.types.model_quantization_config

        return {
            "ModelQuantizationConfig": capo_sagemaker.types.model_quantization_config.deserialize_aws_json_1_1(
                data["ModelQuantizationConfig"]
            )
        }
    elif data.get("ModelCompilationConfig") is not None:
        import capo_sagemaker.types.model_compilation_config

        return {
            "ModelCompilationConfig": capo_sagemaker.types.model_compilation_config.deserialize_aws_json_1_1(
                data["ModelCompilationConfig"]
            )
        }
    elif data.get("ModelShardingConfig") is not None:
        import capo_sagemaker.types.model_sharding_config

        return {
            "ModelShardingConfig": capo_sagemaker.types.model_sharding_config.deserialize_aws_json_1_1(
                data["ModelShardingConfig"]
            )
        }
    elif data.get("ModelSpeculativeDecodingConfig") is not None:
        import capo_sagemaker.types.model_speculative_decoding_config

        return {
            "ModelSpeculativeDecodingConfig": capo_sagemaker.types.model_speculative_decoding_config.deserialize_aws_json_1_1(
                data["ModelSpeculativeDecodingConfig"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("OptimizationConfig: no recognized variant key")
