"""Generated from Smithy shape ``com.amazonaws.b2bi#OutputSampleFileSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_b2bi.errors import DeserializationError, SerializationError
from capo_b2bi.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_b2bi.types.s3_location


class _OutputSampleFileSource_fileLocation(TypedDict, closed=True):
    fileLocation: "capo_b2bi.types.s3_location.S3Location"


OutputSampleFileSource: TypeAlias = (
    _OutputSampleFileSource_fileLocation | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OutputSampleFileSource) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"OutputSampleFileSource: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "fileLocation" in value:
        import capo_b2bi.types.s3_location

        return {
            "fileLocation": capo_b2bi.types.s3_location.serialize_aws_json_1_0(
                value["fileLocation"]
            )
        }
    else:
        raise SerializationError("OutputSampleFileSource: no variant present")


def deserialize_aws_json_1_0(data: dict) -> OutputSampleFileSource:
    if data.get("fileLocation") is not None:
        import capo_b2bi.types.s3_location

        return {
            "fileLocation": capo_b2bi.types.s3_location.deserialize_aws_json_1_0(
                data["fileLocation"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("OutputSampleFileSource: no recognized variant key")
