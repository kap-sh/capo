"""Generated from Smithy shape ``com.amazonaws.connect#GetAttachedFileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.created_by_info
    import capo_connect.types.download_url_metadata
    import capo_connect.types.file_id
    import capo_connect.types.file_name
    import capo_connect.types.file_size_in_bytes
    import capo_connect.types.file_status_type
    import capo_connect.types.file_use_case_type
    import capo_connect.types.iso8601_datetime
    import capo_connect.types.tag_map


class GetAttachedFileResponse(TypedDict, closed=True):
    file_arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The unique identifier of the attached file resource (ARN).</p>"""
    file_id: NotRequired["capo_connect.types.file_id.FileId"]
    """<p>The unique identifier of the attached file resource.</p>"""
    creation_time: NotRequired["capo_connect.types.iso8601_datetime.ISO8601Datetime"]
    """<p>The time of Creation of the file resource as an ISO timestamp. It's specified in ISO 8601 format: <code>yyyy-MM-ddThh:mm:ss.SSSZ</code>. For example, <code>2024-05-03T02:41:28.172Z</code>.</p>"""
    file_status: NotRequired["capo_connect.types.file_status_type.FileStatusType"]
    """<p>The current status of the attached file.</p>"""
    file_name: NotRequired["capo_connect.types.file_name.FileName"]
    """<p>A case-sensitive name of the attached file being uploaded.</p>"""
    file_size_in_bytes: "capo_connect.types.file_size_in_bytes.FileSizeInBytes"
    """<p>The size of the attached file in bytes.</p>"""
    associated_resource_arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The resource to which the attached file is (being) uploaded to. The supported resources are <a href="https://docs.aws.amazon.com/connect/latest/adminguide/cases.html">Cases</a>, <a href="https://docs.aws.amazon.com/connect/latest/adminguide/setup-email-channel.html">Email</a>, and <a href="https://docs.aws.amazon.com/connect/latest/adminguide/concepts-getting-started-tasks.html">Task</a>.</p>"""
    file_use_case_type: NotRequired[
        "capo_connect.types.file_use_case_type.FileUseCaseType"
    ]
    """<p>The use case for the file.</p>"""
    created_by: NotRequired["capo_connect.types.created_by_info.CreatedByInfo"]
    """<p>Represents the identity that created the file.</p>"""
    download_url_metadata: NotRequired[
        "capo_connect.types.download_url_metadata.DownloadUrlMetadata"
    ]
    """<p>URL and expiry to be used when downloading the attached file. </p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, <code>{ "Tags": {"key1":"value1", "key2":"value2"} }</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAttachedFileResponse) -> dict:
    out: dict = {}
    if "file_arn" in value:
        out["FileArn"] = value["file_arn"]
    if "file_id" in value:
        out["FileId"] = value["file_id"]
    if "creation_time" in value:
        out["CreationTime"] = value["creation_time"]
    if "file_status" in value:
        import capo_connect.types.file_status_type

        out["FileStatus"] = capo_connect.types.file_status_type.serialize_json(
            value["file_status"]
        )
    if "file_name" in value:
        out["FileName"] = value["file_name"]
    out["FileSizeInBytes"] = value["file_size_in_bytes"]
    if "associated_resource_arn" in value:
        out["AssociatedResourceArn"] = value["associated_resource_arn"]
    if "file_use_case_type" in value:
        import capo_connect.types.file_use_case_type

        out["FileUseCaseType"] = capo_connect.types.file_use_case_type.serialize_json(
            value["file_use_case_type"]
        )
    if "created_by" in value:
        import capo_connect.types.created_by_info

        out["CreatedBy"] = capo_connect.types.created_by_info.serialize_json(
            value["created_by"]
        )
    if "download_url_metadata" in value:
        import capo_connect.types.download_url_metadata

        out["DownloadUrlMetadata"] = (
            capo_connect.types.download_url_metadata.serialize_json(
                value["download_url_metadata"]
            )
        )
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetAttachedFileResponse:
    out: GetAttachedFileResponse = {}  # type: ignore[typeddict-item]
    if data.get("FileArn") is not None:
        out["file_arn"] = data["FileArn"]
    if data.get("FileId") is not None:
        out["file_id"] = data["FileId"]
    if data.get("CreationTime") is not None:
        out["creation_time"] = data["CreationTime"]
    if data.get("FileStatus") is not None:
        import capo_connect.types.file_status_type

        out["file_status"] = capo_connect.types.file_status_type.deserialize_json(
            data["FileStatus"]
        )
    if data.get("FileName") is not None:
        out["file_name"] = data["FileName"]
    if data.get("FileSizeInBytes") is not None:
        out["file_size_in_bytes"] = data["FileSizeInBytes"]
    else:
        raise DeserializationError(
            "GetAttachedFileResponse.file_size_in_bytes required"
        )
    if data.get("AssociatedResourceArn") is not None:
        out["associated_resource_arn"] = data["AssociatedResourceArn"]
    if data.get("FileUseCaseType") is not None:
        import capo_connect.types.file_use_case_type

        out["file_use_case_type"] = (
            capo_connect.types.file_use_case_type.deserialize_json(
                data["FileUseCaseType"]
            )
        )
    if data.get("CreatedBy") is not None:
        import capo_connect.types.created_by_info

        out["created_by"] = capo_connect.types.created_by_info.deserialize_json(
            data["CreatedBy"]
        )
    if data.get("DownloadUrlMetadata") is not None:
        import capo_connect.types.download_url_metadata

        out["download_url_metadata"] = (
            capo_connect.types.download_url_metadata.deserialize_json(
                data["DownloadUrlMetadata"]
            )
        )
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
