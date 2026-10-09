"""Generated from Smithy shape ``com.amazonaws.datazone#SourceLocation``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_datazone.types.s3_files_location
    import capo_datazone.types.s3_source_location


class _SourceLocation_s3(TypedDict, closed=True):
    s3: "capo_datazone.types.s3_source_location.S3SourceLocation"


class _SourceLocation_s3Files(TypedDict, closed=True):
    s3Files: "capo_datazone.types.s3_files_location.S3FilesLocation"


SourceLocation: TypeAlias = _SourceLocation_s3 | _SourceLocation_s3Files


# --- restJson1 ser/de ---
def serialize_json(value: SourceLocation) -> dict:
    if "s3" in value:
        return {"s3": value["s3"]}
    elif "s3Files" in value:
        import capo_datazone.types.s3_files_location

        return {
            "s3Files": capo_datazone.types.s3_files_location.serialize_json(
                value["s3Files"]
            )
        }
    else:
        raise SerializationError("SourceLocation: no variant present")


def deserialize_json(data: dict) -> SourceLocation:
    if data.get("s3") is not None:
        return {"s3": data["s3"]}
    elif data.get("s3Files") is not None:
        import capo_datazone.types.s3_files_location

        return {
            "s3Files": capo_datazone.types.s3_files_location.deserialize_json(
                data["s3Files"]
            )
        }
    else:
        raise DeserializationError("SourceLocation: no recognized variant key")
