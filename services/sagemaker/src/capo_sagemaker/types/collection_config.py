"""Generated from Smithy shape ``com.amazonaws.sagemaker#CollectionConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_sagemaker.errors import DeserializationError, SerializationError
from capo_sagemaker.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_sagemaker.types.vector_config


class _CollectionConfig_VectorConfig(TypedDict, closed=True):
    VectorConfig: "capo_sagemaker.types.vector_config.VectorConfig"


CollectionConfig: TypeAlias = _CollectionConfig_VectorConfig | UnknownUnionMember


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CollectionConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CollectionConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "VectorConfig" in value:
        import capo_sagemaker.types.vector_config

        return {
            "VectorConfig": capo_sagemaker.types.vector_config.serialize_aws_json_1_1(
                value["VectorConfig"]
            )
        }
    else:
        raise SerializationError("CollectionConfig: no variant present")


def deserialize_aws_json_1_1(data: dict) -> CollectionConfig:
    if data.get("VectorConfig") is not None:
        import capo_sagemaker.types.vector_config

        return {
            "VectorConfig": capo_sagemaker.types.vector_config.deserialize_aws_json_1_1(
                data["VectorConfig"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("CollectionConfig: no recognized variant key")
