"""Generated from Smithy shape ``com.amazonaws.fsx#ReleaseFileSystemNfsV3LocksResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.file_system


class ReleaseFileSystemNfsV3LocksResponse(TypedDict, closed=True):
    file_system: NotRequired["capo_fsx.types.file_system.FileSystem"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReleaseFileSystemNfsV3LocksResponse) -> dict:
    out: dict = {}
    if "file_system" in value:
        import capo_fsx.types.file_system

        out["FileSystem"] = capo_fsx.types.file_system.serialize_aws_json_1_1(
            value["file_system"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReleaseFileSystemNfsV3LocksResponse:
    out: ReleaseFileSystemNfsV3LocksResponse = {}  # type: ignore[typeddict-item]
    if data.get("FileSystem") is not None:
        import capo_fsx.types.file_system

        out["file_system"] = capo_fsx.types.file_system.deserialize_aws_json_1_1(
            data["FileSystem"]
        )
    return out


def redact_sensitive(value: ReleaseFileSystemNfsV3LocksResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "file_system" in value:
        import capo_fsx.types.file_system

        out["file_system"] = capo_fsx.types.file_system.redact_sensitive(
            value["file_system"]
        )
    return out
