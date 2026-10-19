"""Generated from Smithy shape ``com.amazonaws.s3files#ListFileSystemsDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_s3files.types.aws_account_id
    import capo_s3files.types.bucket_arn
    import capo_s3files.types.file_system_arn
    import capo_s3files.types.file_system_id
    import capo_s3files.types.life_cycle_state
    import capo_s3files.types.role_arn
    import capo_s3files.types.status_message
    import capo_s3files.types.tag_value


class ListFileSystemsDescription(TypedDict, closed=True):
    creation_time: "datetime.datetime"
    """<p>The time when the file system was created.</p>"""
    file_system_arn: "capo_s3files.types.file_system_arn.FileSystemArn"
    """<p>The Amazon Resource Name (ARN) of the file system.</p>"""
    file_system_id: "capo_s3files.types.file_system_id.FileSystemId"
    """<p>The ID of the file system.</p>"""
    name: NotRequired["capo_s3files.types.tag_value.TagValue"]
    """<p>The name of the file system.</p>"""
    bucket: "capo_s3files.types.bucket_arn.BucketArn"
    """<p>The Amazon Resource Name (ARN) of the S3 bucket.</p>"""
    status: "capo_s3files.types.life_cycle_state.LifeCycleState"
    """<p>The current status of the file system.</p>"""
    status_message: NotRequired["capo_s3files.types.status_message.StatusMessage"]
    """<p>Additional information about the file system status.</p>"""
    role_arn: "capo_s3files.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role used for S3 access.</p>"""
    owner_id: "capo_s3files.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID of the file system owner.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFileSystemsDescription) -> dict:
    out: dict = {}
    import capo_s3files.types._prelude.timestamp

    out["creationTime"] = capo_s3files.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    out["fileSystemArn"] = value["file_system_arn"]
    out["fileSystemId"] = value["file_system_id"]
    if "name" in value:
        out["name"] = value["name"]
    out["bucket"] = value["bucket"]
    import capo_s3files.types.life_cycle_state

    out["status"] = capo_s3files.types.life_cycle_state.serialize_json(value["status"])
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    out["roleArn"] = value["role_arn"]
    out["ownerId"] = value["owner_id"]
    return out


def deserialize_json(data: dict) -> ListFileSystemsDescription:
    out: ListFileSystemsDescription = {}  # type: ignore[typeddict-item]
    if data.get("creationTime") is not None:
        import capo_s3files.types._prelude.timestamp

        out["creation_time"] = capo_s3files.types._prelude.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("fileSystemArn") is not None:
        out["file_system_arn"] = data["fileSystemArn"]
    else:
        out["file_system_arn"] = ""
    if data.get("fileSystemId") is not None:
        out["file_system_id"] = data["fileSystemId"]
    else:
        out["file_system_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    else:
        out["bucket"] = ""
    if data.get("status") is not None:
        import capo_s3files.types.life_cycle_state

        out["status"] = capo_s3files.types.life_cycle_state.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_s3files.types.life_cycle_state.LifeCycleState", ""
        )
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("ownerId") is not None:
        out["owner_id"] = data["ownerId"]
    else:
        out["owner_id"] = ""
    return out
