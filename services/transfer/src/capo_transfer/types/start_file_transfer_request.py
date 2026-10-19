"""Generated from Smithy shape ``com.amazonaws.transfer#StartFileTransferRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.connector_id
    import capo_transfer.types.custom_http_headers
    import capo_transfer.types.file_path
    import capo_transfer.types.file_paths


class StartFileTransferRequest(TypedDict, closed=True):
    connector_id: "capo_transfer.types.connector_id.ConnectorId"
    """<p>The unique identifier for the connector.</p>"""
    send_file_paths: NotRequired["capo_transfer.types.file_paths.FilePaths"]
    """<p>One or more source paths for the Amazon S3 storage. Each string represents a source file path for one outbound file transfer. For example, <code> <i>amzn-s3-demo-bucket</i>/<i>myfile.txt</i> </code>.</p> <note> <p>Replace <code> <i>amzn-s3-demo-bucket</i> </code> with one of your actual buckets.</p> </note>"""
    retrieve_file_paths: NotRequired["capo_transfer.types.file_paths.FilePaths"]
    """<p>One or more source paths for the partner's SFTP server. Each string represents a source file path for one inbound file transfer.</p>"""
    local_directory_path: NotRequired["capo_transfer.types.file_path.FilePath"]
    """<p>For an inbound transfer, the <code>LocaDirectoryPath</code> specifies the destination for one or more files that are transferred from the partner's SFTP server.</p>"""
    remote_directory_path: NotRequired["capo_transfer.types.file_path.FilePath"]
    """<p>For an outbound transfer, the <code>RemoteDirectoryPath</code> specifies the destination for one or more files that are transferred to the partner's SFTP server. If you don't specify a <code>RemoteDirectoryPath</code>, the destination for transferred files is the SFTP user's home directory.</p>"""
    custom_http_headers: NotRequired[
        "capo_transfer.types.custom_http_headers.CustomHttpHeaders"
    ]
    """<p>An array of key-value pairs that represent custom HTTP headers to include in AS2 messages. These headers are added to the AS2 message when sending files to your trading partner.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartFileTransferRequest) -> dict:
    out: dict = {}
    out["ConnectorId"] = value["connector_id"]
    if "send_file_paths" in value:
        import capo_transfer.types.file_paths

        out["SendFilePaths"] = capo_transfer.types.file_paths.serialize_aws_json_1_1(
            value["send_file_paths"]
        )
    if "retrieve_file_paths" in value:
        import capo_transfer.types.file_paths

        out["RetrieveFilePaths"] = (
            capo_transfer.types.file_paths.serialize_aws_json_1_1(
                value["retrieve_file_paths"]
            )
        )
    if "local_directory_path" in value:
        out["LocalDirectoryPath"] = value["local_directory_path"]
    if "remote_directory_path" in value:
        out["RemoteDirectoryPath"] = value["remote_directory_path"]
    if "custom_http_headers" in value:
        import capo_transfer.types.custom_http_headers

        out["CustomHttpHeaders"] = (
            capo_transfer.types.custom_http_headers.serialize_aws_json_1_1(
                value["custom_http_headers"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartFileTransferRequest:
    out: StartFileTransferRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConnectorId") is not None:
        out["connector_id"] = data["ConnectorId"]
    else:
        out["connector_id"] = ""
    if data.get("SendFilePaths") is not None:
        import capo_transfer.types.file_paths

        out["send_file_paths"] = (
            capo_transfer.types.file_paths.deserialize_aws_json_1_1(
                data["SendFilePaths"]
            )
        )
    if data.get("RetrieveFilePaths") is not None:
        import capo_transfer.types.file_paths

        out["retrieve_file_paths"] = (
            capo_transfer.types.file_paths.deserialize_aws_json_1_1(
                data["RetrieveFilePaths"]
            )
        )
    if data.get("LocalDirectoryPath") is not None:
        out["local_directory_path"] = data["LocalDirectoryPath"]
    if data.get("RemoteDirectoryPath") is not None:
        out["remote_directory_path"] = data["RemoteDirectoryPath"]
    if data.get("CustomHttpHeaders") is not None:
        import capo_transfer.types.custom_http_headers

        out["custom_http_headers"] = (
            capo_transfer.types.custom_http_headers.deserialize_aws_json_1_1(
                data["CustomHttpHeaders"]
            )
        )
    return out


def redact_sensitive(value: StartFileTransferRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "custom_http_headers" in value:
        import capo_transfer.types.custom_http_headers

        out["custom_http_headers"] = (
            capo_transfer.types.custom_http_headers.redact_sensitive(
                value["custom_http_headers"]
            )
        )
    return out
