"""Generated from Smithy shape ``com.amazonaws.directoryservice#DirectorySizeUpdateSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.directory_size


class DirectorySizeUpdateSettings(TypedDict, closed=True):
    directory_size: NotRequired[
        "capo_directory_service.types.directory_size.DirectorySize"
    ]
    """<p>The target directory size for the update operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectorySizeUpdateSettings) -> dict:
    out: dict = {}
    if "directory_size" in value:
        import capo_directory_service.types.directory_size

        out["DirectorySize"] = (
            capo_directory_service.types.directory_size.serialize_aws_json_1_1(
                value["directory_size"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DirectorySizeUpdateSettings:
    out: DirectorySizeUpdateSettings = {}  # type: ignore[typeddict-item]
    if data.get("DirectorySize") is not None:
        import capo_directory_service.types.directory_size

        out["directory_size"] = (
            capo_directory_service.types.directory_size.deserialize_aws_json_1_1(
                data["DirectorySize"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DirectorySizeUpdateSettings) -> dict:
    out: dict = {}
    if "directory_size" in value:
        import capo_directory_service.types.directory_size

        out["DirectorySize"] = (
            capo_directory_service.types.directory_size.serialize_cbor(
                value["directory_size"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DirectorySizeUpdateSettings:
    out: DirectorySizeUpdateSettings = {}  # type: ignore[typeddict-item]
    if data.get("DirectorySize") is not None:
        import capo_directory_service.types.directory_size

        out["directory_size"] = (
            capo_directory_service.types.directory_size.deserialize_cbor(
                data["DirectorySize"]
            )
        )
    return out
