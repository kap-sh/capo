"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#BlobSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_opensearchmemory.errors import DeserializationError, SerializationError
from capo_opensearchmemory.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_opensearchmemory.types.s3_location


class BlobSourceS3LocationMember(TypedDict, closed=True):
    s3Location: "capo_opensearchmemory.types.s3_location.S3Location"


BlobSource: TypeAlias = BlobSourceS3LocationMember | UnknownUnionMember


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BlobSource) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"BlobSource: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "s3Location" in value:
        import capo_opensearchmemory.types.s3_location

        return {
            "s3Location": capo_opensearchmemory.types.s3_location.serialize_aws_json_1_0(
                value["s3Location"]
            )
        }
    else:
        raise SerializationError("BlobSource: no variant present")


def deserialize_aws_json_1_0(data: dict) -> BlobSource:
    if data.get("s3Location") is not None:
        import capo_opensearchmemory.types.s3_location

        return {
            "s3Location": capo_opensearchmemory.types.s3_location.deserialize_aws_json_1_0(
                data["s3Location"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("BlobSource: no recognized variant key")
