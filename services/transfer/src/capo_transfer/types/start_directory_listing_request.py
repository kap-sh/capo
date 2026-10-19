"""Generated from Smithy shape ``com.amazonaws.transfer#StartDirectoryListingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.connector_id
    import capo_transfer.types.file_path
    import capo_transfer.types.max_items


class StartDirectoryListingRequest(TypedDict, closed=True):
    connector_id: "capo_transfer.types.connector_id.ConnectorId"
    """<p>The unique identifier for the connector.</p>"""
    remote_directory_path: "capo_transfer.types.file_path.FilePath"
    """<p>Specifies the directory on the remote SFTP server for which you want to list its contents.</p>"""
    max_items: NotRequired["capo_transfer.types.max_items.MaxItems"]
    """<p>An optional parameter where you can specify the maximum number of file/directory names to retrieve. The default value is 1,000.</p>"""
    output_directory_path: "capo_transfer.types.file_path.FilePath"
    """<p>Specifies the path (bucket and prefix) in Amazon S3 storage to store the results of the directory listing.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartDirectoryListingRequest) -> dict:
    out: dict = {}
    out["ConnectorId"] = value["connector_id"]
    out["RemoteDirectoryPath"] = value["remote_directory_path"]
    if "max_items" in value:
        out["MaxItems"] = value["max_items"]
    out["OutputDirectoryPath"] = value["output_directory_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartDirectoryListingRequest:
    out: StartDirectoryListingRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConnectorId") is not None:
        out["connector_id"] = data["ConnectorId"]
    else:
        out["connector_id"] = ""
    if data.get("RemoteDirectoryPath") is not None:
        out["remote_directory_path"] = data["RemoteDirectoryPath"]
    else:
        out["remote_directory_path"] = ""
    if data.get("MaxItems") is not None:
        out["max_items"] = data["MaxItems"]
    if data.get("OutputDirectoryPath") is not None:
        out["output_directory_path"] = data["OutputDirectoryPath"]
    else:
        out["output_directory_path"] = ""
    return out
