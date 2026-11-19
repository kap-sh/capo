"""Generated from Smithy shape ``com.amazonaws.appstream#DeleteDirectoryConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.directory_name


class DeleteDirectoryConfigRequest(TypedDict, closed=True):
    directory_name: NotRequired["capo_appstream.types.directory_name.DirectoryName"]
    """<p>The name of the directory configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDirectoryConfigRequest) -> dict:
    out: dict = {}
    if "directory_name" in value:
        out["DirectoryName"] = value["directory_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDirectoryConfigRequest:
    out: DeleteDirectoryConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryName") is not None:
        out["directory_name"] = data["DirectoryName"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteDirectoryConfigRequest) -> dict:
    out: dict = {}
    if "directory_name" in value:
        out["DirectoryName"] = value["directory_name"]
    return out


def deserialize_cbor(data: dict) -> DeleteDirectoryConfigRequest:
    out: DeleteDirectoryConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryName") is not None:
        out["directory_name"] = data["DirectoryName"]
    return out
