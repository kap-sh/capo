"""Generated from Smithy shape ``com.amazonaws.directoryservice#UnshareDirectoryResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.directory_id


class UnshareDirectoryResult(TypedDict, closed=True):
    shared_directory_id: NotRequired[
        "capo_directory_service.types.directory_id.DirectoryId"
    ]
    """<p>Identifier of the directory stored in the directory consumer account that is to be unshared from the specified directory (<code>DirectoryId</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnshareDirectoryResult) -> dict:
    out: dict = {}
    if "shared_directory_id" in value:
        out["SharedDirectoryId"] = value["shared_directory_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnshareDirectoryResult:
    out: UnshareDirectoryResult = {}  # type: ignore[typeddict-item]
    if data.get("SharedDirectoryId") is not None:
        out["shared_directory_id"] = data["SharedDirectoryId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UnshareDirectoryResult) -> dict:
    out: dict = {}
    if "shared_directory_id" in value:
        out["SharedDirectoryId"] = value["shared_directory_id"]
    return out


def deserialize_cbor(data: dict) -> UnshareDirectoryResult:
    out: UnshareDirectoryResult = {}  # type: ignore[typeddict-item]
    if data.get("SharedDirectoryId") is not None:
        out["shared_directory_id"] = data["SharedDirectoryId"]
    return out
