"""Generated from Smithy shape ``com.amazonaws.s3files#CreateFileSystemResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_s3files.types.aws_account_id
    import capo_s3files.types.bucket_arn
    import capo_s3files.types.client_token
    import capo_s3files.types.file_system_arn
    import capo_s3files.types.file_system_id
    import capo_s3files.types.kms_key_id
    import capo_s3files.types.life_cycle_state
    import capo_s3files.types.role_arn
    import capo_s3files.types.status_message
    import capo_s3files.types.tag_list
    import capo_s3files.types.tag_value


class CreateFileSystemResponse(TypedDict, closed=True):
    creation_time: NotRequired["datetime.datetime"]
    """<p>The time when the file system was created, in seconds since 1970-01-01T00:00:00Z (Unix epoch time).</p>"""
    file_system_arn: NotRequired["capo_s3files.types.file_system_arn.FileSystemArn"]
    """<p>The ARN for the S3 file system, in the format <code>arn:aws:s3files:region:account-id:file-system/file-system-id</code>.</p>"""
    file_system_id: NotRequired["capo_s3files.types.file_system_id.FileSystemId"]
    """<p>The ID of the file system, assigned by S3 Files. This ID is used to reference the file system in subsequent API calls.</p>"""
    bucket: NotRequired["capo_s3files.types.bucket_arn.BucketArn"]
    """<p>The Amazon Resource Name (ARN) of the S3 bucket associated with the file system.</p>"""
    prefix: "str"
    """<p>The prefix within the S3 bucket that scopes the file system access.</p>"""
    client_token: NotRequired["capo_s3files.types.client_token.ClientToken"]
    """<p>The client token used for idempotency.</p>"""
    kms_key_id: NotRequired["capo_s3files.types.kms_key_id.KmsKeyId"]
    """<p>The ARN or alias of the KMS key used for encryption.</p>"""
    status: NotRequired["capo_s3files.types.life_cycle_state.LifeCycleState"]
    """<p>The lifecycle state of the file system. Valid values are: <code>AVAILABLE</code> (the file system is available for use), <code>CREATING</code> (the file system is being created), <code>DELETING</code> (the file system is being deleted), <code>DELETED</code> (the file system has been deleted), <code>ERROR</code> (the file system is in an error state), <code>MISCONFIGURED</code> (the file system has a misconfiguration), or <code>UPDATING</code> (the file system is being updated).</p>"""
    status_message: NotRequired["capo_s3files.types.status_message.StatusMessage"]
    """<p>Additional information about the file system status. This field provides more details when the status is <code>ERROR</code>, or during state transitions.</p>"""
    role_arn: NotRequired["capo_s3files.types.role_arn.RoleArn"]
    """<p>The ARN of the IAM role used for S3 access.</p>"""
    owner_id: NotRequired["capo_s3files.types.aws_account_id.AwsAccountId"]
    """<p>The Amazon Web Services account ID of the file system owner.</p>"""
    tags: NotRequired["capo_s3files.types.tag_list.TagList"]
    """<p>The tags associated with the file system.</p>"""
    name: NotRequired["capo_s3files.types.tag_value.TagValue"]
    """<p>The name of the file system, derived from the <code>Name</code> tag if present.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFileSystemResponse) -> dict:
    out: dict = {}
    if "creation_time" in value:
        import capo_s3files.types._prelude.timestamp

        out["creationTime"] = capo_s3files.types._prelude.timestamp.serialize_json(
            value["creation_time"]
        )
    if "file_system_arn" in value:
        out["fileSystemArn"] = value["file_system_arn"]
    if "file_system_id" in value:
        out["fileSystemId"] = value["file_system_id"]
    if "bucket" in value:
        out["bucket"] = value["bucket"]
    out["prefix"] = value.get("prefix", "")
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "status" in value:
        import capo_s3files.types.life_cycle_state

        out["status"] = capo_s3files.types.life_cycle_state.serialize_json(
            value["status"]
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "owner_id" in value:
        out["ownerId"] = value["owner_id"]
    if "tags" in value:
        import capo_s3files.types.tag_list

        out["tags"] = capo_s3files.types.tag_list.serialize_json(value["tags"])
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> CreateFileSystemResponse:
    out: CreateFileSystemResponse = {}  # type: ignore[typeddict-item]
    if data.get("creationTime") is not None:
        import capo_s3files.types._prelude.timestamp

        out["creation_time"] = capo_s3files.types._prelude.timestamp.deserialize_json(
            data["creationTime"]
        )
    if data.get("fileSystemArn") is not None:
        out["file_system_arn"] = data["fileSystemArn"]
    if data.get("fileSystemId") is not None:
        out["file_system_id"] = data["fileSystemId"]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    if data.get("prefix") is not None:
        out["prefix"] = data["prefix"]
    else:
        out["prefix"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("status") is not None:
        import capo_s3files.types.life_cycle_state

        out["status"] = capo_s3files.types.life_cycle_state.deserialize_json(
            data["status"]
        )
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("ownerId") is not None:
        out["owner_id"] = data["ownerId"]
    if data.get("tags") is not None:
        import capo_s3files.types.tag_list

        out["tags"] = capo_s3files.types.tag_list.deserialize_json(data["tags"])
    if data.get("name") is not None:
        out["name"] = data["name"]
    return out
