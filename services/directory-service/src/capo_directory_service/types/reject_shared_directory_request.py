"""Generated from Smithy shape ``com.amazonaws.directoryservice#RejectSharedDirectoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.directory_id


class RejectSharedDirectoryRequest(TypedDict, closed=True):
    shared_directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>Identifier of the shared directory in the directory consumer account. This identifier is different for each directory owner account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RejectSharedDirectoryRequest) -> dict:
    out: dict = {}
    out["SharedDirectoryId"] = value["shared_directory_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RejectSharedDirectoryRequest:
    out: RejectSharedDirectoryRequest = {}  # type: ignore[typeddict-item]
    if data.get("SharedDirectoryId") is not None:
        out["shared_directory_id"] = data["SharedDirectoryId"]
    else:
        out["shared_directory_id"] = ""
    return out
