"""Generated from Smithy shape ``com.amazonaws.healthlake#InputDataConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_healthlake.errors import DeserializationError, SerializationError
from capo_healthlake.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_healthlake.types.s3_uri


class _InputDataConfig_S3Uri(TypedDict, closed=True):
    S3Uri: "capo_healthlake.types.s3_uri.S3Uri"


InputDataConfig: TypeAlias = _InputDataConfig_S3Uri | UnknownUnionMember


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InputDataConfig) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"InputDataConfig: cannot serialize unknown variant {value.name!r}"
        )
    elif "S3Uri" in value:
        return {"S3Uri": value["S3Uri"]}
    else:
        raise SerializationError("InputDataConfig: no variant present")


def deserialize_aws_json_1_0(data: dict) -> InputDataConfig:
    if data.get("S3Uri") is not None:
        return {"S3Uri": data["S3Uri"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("InputDataConfig: no recognized variant key")
