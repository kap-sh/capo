"""Generated from Smithy shape ``com.amazonaws.datazone#S3FileList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.s3_file

S3FileList: TypeAlias = list["capo_datazone.types.s3_file.S3File"]


# --- restJson1 ser/de ---
def serialize_json(value: S3FileList) -> list:
    import capo_datazone.types.s3_file

    out: list = []
    for item in value:
        out.append(capo_datazone.types.s3_file.serialize_json(item))
    return out


def deserialize_json(data: list) -> S3FileList:
    import capo_datazone.types.s3_file

    out: S3FileList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datazone.types.s3_file.deserialize_json(item))
    return out


def redact_sensitive(value: S3FileList) -> list[Any]:
    import capo_datazone.types.s3_file

    return [capo_datazone.types.s3_file.redact_sensitive(item) for item in value]
