"""Generated from Smithy shape ``com.amazonaws.connect#AttachedFile``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.created_by_info
    import capo_connect.types.file_id
    import capo_connect.types.file_name
    import capo_connect.types.file_size_in_bytes
    import capo_connect.types.file_status_type
    import capo_connect.types.file_use_case_type
    import capo_connect.types.iso8601_datetime
    import capo_connect.types.tag_map


class AttachedFile(TypedDict, closed=True):
    creation_time: "capo_connect.types.iso8601_datetime.ISO8601Datetime"
    """<p>The time of Creation of the file resource as an ISO timestamp. It's specified in ISO 8601 format: <code>yyyy-MM-ddThh:mm:ss.SSSZ</code>. For example, <code>2024-05-03T02:41:28.172Z</code>.</p>"""
    file_arn: "capo_connect.types.arn.ARN"
    """<p>The unique identifier of the attached file resource (ARN).</p>"""
    file_id: "capo_connect.types.file_id.FileId"
    """<p>The unique identifier of the attached file resource.</p>"""
    file_name: "capo_connect.types.file_name.FileName"
    """<p>A case-sensitive name of the attached file being uploaded.</p>"""
    file_size_in_bytes: "capo_connect.types.file_size_in_bytes.FileSizeInBytes"
    """<p>The size of the attached file in bytes.</p>"""
    file_status: "capo_connect.types.file_status_type.FileStatusType"
    """<p>The current status of the attached file.</p>"""
    created_by: NotRequired["capo_connect.types.created_by_info.CreatedByInfo"]
    """<p>Represents the identity that created the file.</p>"""
    file_use_case_type: NotRequired[
        "capo_connect.types.file_use_case_type.FileUseCaseType"
    ]
    """<p>The use case for the file.</p>"""
    associated_resource_arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The resource to which the attached file is (being) uploaded to. The supported resources are <a href="https://docs.aws.amazon.com/connect/latest/adminguide/cases.html">Cases</a>, <a href="https://docs.aws.amazon.com/connect/latest/adminguide/setup-email-channel.html">Email</a>, and <a href="https://docs.aws.amazon.com/connect/latest/adminguide/concepts-getting-started-tasks.html">Task</a>.</p> <note> <p>This value must be a valid ARN.</p> </note>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, <code>{ "Tags": {"key1":"value1", "key2":"value2"} }</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttachedFile) -> dict:
    out: dict = {}
    out["CreationTime"] = value["creation_time"]
    out["FileArn"] = value["file_arn"]
    out["FileId"] = value["file_id"]
    out["FileName"] = value["file_name"]
    out["FileSizeInBytes"] = value["file_size_in_bytes"]
    import capo_connect.types.file_status_type

    out["FileStatus"] = capo_connect.types.file_status_type.serialize_json(
        value["file_status"]
    )
    if "created_by" in value:
        import capo_connect.types.created_by_info

        out["CreatedBy"] = capo_connect.types.created_by_info.serialize_json(
            value["created_by"]
        )
    if "file_use_case_type" in value:
        import capo_connect.types.file_use_case_type

        out["FileUseCaseType"] = capo_connect.types.file_use_case_type.serialize_json(
            value["file_use_case_type"]
        )
    if "associated_resource_arn" in value:
        out["AssociatedResourceArn"] = value["associated_resource_arn"]
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> AttachedFile:
    out: AttachedFile = {}  # type: ignore[typeddict-item]
    if data.get("CreationTime") is not None:
        out["creation_time"] = data["CreationTime"]
    else:
        raise DeserializationError("AttachedFile.creation_time required")
    if data.get("FileArn") is not None:
        out["file_arn"] = data["FileArn"]
    else:
        raise DeserializationError("AttachedFile.file_arn required")
    if data.get("FileId") is not None:
        out["file_id"] = data["FileId"]
    else:
        raise DeserializationError("AttachedFile.file_id required")
    if data.get("FileName") is not None:
        out["file_name"] = data["FileName"]
    else:
        raise DeserializationError("AttachedFile.file_name required")
    if data.get("FileSizeInBytes") is not None:
        out["file_size_in_bytes"] = data["FileSizeInBytes"]
    else:
        raise DeserializationError("AttachedFile.file_size_in_bytes required")
    if data.get("FileStatus") is not None:
        import capo_connect.types.file_status_type

        out["file_status"] = capo_connect.types.file_status_type.deserialize_json(
            data["FileStatus"]
        )
    else:
        raise DeserializationError("AttachedFile.file_status required")
    if data.get("CreatedBy") is not None:
        import capo_connect.types.created_by_info

        out["created_by"] = capo_connect.types.created_by_info.deserialize_json(
            data["CreatedBy"]
        )
    if data.get("FileUseCaseType") is not None:
        import capo_connect.types.file_use_case_type

        out["file_use_case_type"] = (
            capo_connect.types.file_use_case_type.deserialize_json(
                data["FileUseCaseType"]
            )
        )
    if data.get("AssociatedResourceArn") is not None:
        out["associated_resource_arn"] = data["AssociatedResourceArn"]
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
