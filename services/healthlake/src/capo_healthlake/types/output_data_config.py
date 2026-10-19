"""Generated from Smithy shape ``com.amazonaws.healthlake#OutputDataConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_healthlake.errors import DeserializationError, SerializationError
from capo_healthlake.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_healthlake.types.s3_configuration


class _OutputDataConfig_S3Configuration(TypedDict, closed=True):
    S3Configuration: "capo_healthlake.types.s3_configuration.S3Configuration"


OutputDataConfig: TypeAlias = _OutputDataConfig_S3Configuration | UnknownUnionMember


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OutputDataConfig) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"OutputDataConfig: cannot serialize unknown variant {value.name!r}"
        )
    elif "S3Configuration" in value:
        import capo_healthlake.types.s3_configuration

        return {
            "S3Configuration": capo_healthlake.types.s3_configuration.serialize_aws_json_1_0(
                value["S3Configuration"]
            )
        }
    else:
        raise SerializationError("OutputDataConfig: no variant present")


def deserialize_aws_json_1_0(data: dict) -> OutputDataConfig:
    if data.get("S3Configuration") is not None:
        import capo_healthlake.types.s3_configuration

        return {
            "S3Configuration": capo_healthlake.types.s3_configuration.deserialize_aws_json_1_0(
                data["S3Configuration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("OutputDataConfig: no recognized variant key")
