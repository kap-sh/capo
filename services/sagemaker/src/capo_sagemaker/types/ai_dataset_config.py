"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIDatasetConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_sagemaker.errors import DeserializationError, SerializationError
from capo_sagemaker.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_sagemaker.types.ai_workload_input_data_config_list


class _AIDatasetConfig_InputDataConfig(TypedDict, closed=True):
    InputDataConfig: "capo_sagemaker.types.ai_workload_input_data_config_list.AIWorkloadInputDataConfigList"


AIDatasetConfig: TypeAlias = _AIDatasetConfig_InputDataConfig | UnknownUnionMember


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIDatasetConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AIDatasetConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "InputDataConfig" in value:
        import capo_sagemaker.types.ai_workload_input_data_config_list

        return {
            "InputDataConfig": capo_sagemaker.types.ai_workload_input_data_config_list.serialize_aws_json_1_1(
                value["InputDataConfig"]
            )
        }
    else:
        raise SerializationError("AIDatasetConfig: no variant present")


def deserialize_aws_json_1_1(data: dict) -> AIDatasetConfig:
    if data.get("InputDataConfig") is not None:
        import capo_sagemaker.types.ai_workload_input_data_config_list

        return {
            "InputDataConfig": capo_sagemaker.types.ai_workload_input_data_config_list.deserialize_aws_json_1_1(
                data["InputDataConfig"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AIDatasetConfig: no recognized variant key")
