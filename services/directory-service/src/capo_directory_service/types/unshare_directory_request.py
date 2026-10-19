"""Generated from Smithy shape ``com.amazonaws.directoryservice#UnshareDirectoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.unshare_target


class UnshareDirectoryRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>The identifier of the Managed Microsoft AD directory that you want to stop sharing.</p>"""
    unshare_target: "capo_directory_service.types.unshare_target.UnshareTarget"
    """<p>Identifier for the directory consumer account with whom the directory has to be unshared.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnshareDirectoryRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    import capo_directory_service.types.unshare_target

    out["UnshareTarget"] = (
        capo_directory_service.types.unshare_target.serialize_aws_json_1_1(
            value["unshare_target"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UnshareDirectoryRequest:
    out: UnshareDirectoryRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        out["directory_id"] = ""
    if data.get("UnshareTarget") is not None:
        import capo_directory_service.types.unshare_target

        out["unshare_target"] = (
            capo_directory_service.types.unshare_target.deserialize_aws_json_1_1(
                data["UnshareTarget"]
            )
        )
    else:
        raise DeserializationError("UnshareDirectoryRequest.unshare_target required")
    return out
