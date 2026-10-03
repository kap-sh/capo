"""Generated from Smithy shape ``com.amazonaws.connect#StartAttachedFileUploadRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.client_token
    import capo_connect.types.created_by_info
    import capo_connect.types.file_name
    import capo_connect.types.file_size_in_bytes
    import capo_connect.types.file_use_case_type
    import capo_connect.types.instance_id
    import capo_connect.types.tag_map
    import capo_connect.types.url_expiry_in_seconds


class StartAttachedFileUploadRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The unique identifier of the Connect Customer instance.</p>"""
    file_name: "capo_connect.types.file_name.FileName"
    """<p>A case-sensitive name of the attached file being uploaded.</p>"""
    file_size_in_bytes: "capo_connect.types.file_size_in_bytes.FileSizeInBytes"
    """<p>The size of the attached file in bytes.</p>"""
    url_expiry_in_seconds: NotRequired[
        "capo_connect.types.url_expiry_in_seconds.URLExpiryInSeconds"
    ]
    """<p>Optional override for the expiry of the pre-signed S3 URL in seconds. The default value is 300.</p>"""
    file_use_case_type: "capo_connect.types.file_use_case_type.FileUseCaseType"
    """<p>The use case for the file.</p> <important> <p> Only <code>ATTACHMENTS</code> are supported.</p> </important>"""
    associated_resource_arn: "capo_connect.types.arn.ARN"
    """<p>The resource to which the attached file is (being) uploaded to. The supported resources are <a href="https://docs.aws.amazon.com/connect/latest/adminguide/cases.html">Cases</a>, <a href="https://docs.aws.amazon.com/connect/latest/adminguide/setup-email-channel.html">Email</a>, and <a href="https://docs.aws.amazon.com/connect/latest/adminguide/concepts-getting-started-tasks.html">Task</a>.</p> <note> <p>This value must be a valid ARN.</p> </note>"""
    created_by: NotRequired["capo_connect.types.created_by_info.CreatedByInfo"]
    """<p>Represents the identity that created the file.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, <code>{ "Tags": {"key1":"value1", "key2":"value2"} }</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAttachedFileUploadRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["FileName"] = value["file_name"]
    out["FileSizeInBytes"] = value["file_size_in_bytes"]
    if "url_expiry_in_seconds" in value:
        out["UrlExpiryInSeconds"] = value["url_expiry_in_seconds"]
    import capo_connect.types.file_use_case_type

    out["FileUseCaseType"] = capo_connect.types.file_use_case_type.serialize_json(
        value["file_use_case_type"]
    )
    if "created_by" in value:
        import capo_connect.types.created_by_info

        out["CreatedBy"] = capo_connect.types.created_by_info.serialize_json(
            value["created_by"]
        )
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartAttachedFileUploadRequest:
    out: StartAttachedFileUploadRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("FileName") is not None:
        out["file_name"] = data["FileName"]
    else:
        raise DeserializationError("StartAttachedFileUploadRequest.file_name required")
    if data.get("FileSizeInBytes") is not None:
        out["file_size_in_bytes"] = data["FileSizeInBytes"]
    else:
        raise DeserializationError(
            "StartAttachedFileUploadRequest.file_size_in_bytes required"
        )
    if data.get("UrlExpiryInSeconds") is not None:
        out["url_expiry_in_seconds"] = data["UrlExpiryInSeconds"]
    if data.get("FileUseCaseType") is not None:
        import capo_connect.types.file_use_case_type

        out["file_use_case_type"] = (
            capo_connect.types.file_use_case_type.deserialize_json(
                data["FileUseCaseType"]
            )
        )
    else:
        raise DeserializationError(
            "StartAttachedFileUploadRequest.file_use_case_type required"
        )
    if data.get("CreatedBy") is not None:
        import capo_connect.types.created_by_info

        out["created_by"] = capo_connect.types.created_by_info.deserialize_json(
            data["CreatedBy"]
        )
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
