"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIModelSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_sagemaker.errors import DeserializationError, SerializationError
from capo_sagemaker.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_sagemaker.types.ai_model_source_s3


class _AIModelSource_S3(TypedDict, closed=True):
    S3: "capo_sagemaker.types.ai_model_source_s3.AIModelSourceS3"


AIModelSource: TypeAlias = _AIModelSource_S3 | UnknownUnionMember


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIModelSource) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"AIModelSource: cannot serialize unknown variant {value.name!r}"
        )
    elif "S3" in value:
        import capo_sagemaker.types.ai_model_source_s3

        return {
            "S3": capo_sagemaker.types.ai_model_source_s3.serialize_aws_json_1_1(
                value["S3"]
            )
        }
    else:
        raise SerializationError("AIModelSource: no variant present")


def deserialize_aws_json_1_1(data: dict) -> AIModelSource:
    if data.get("S3") is not None:
        import capo_sagemaker.types.ai_model_source_s3

        return {
            "S3": capo_sagemaker.types.ai_model_source_s3.deserialize_aws_json_1_1(
                data["S3"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("AIModelSource: no recognized variant key")
