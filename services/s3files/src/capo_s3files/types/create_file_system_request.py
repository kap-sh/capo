"""Generated from Smithy shape ``com.amazonaws.s3files#CreateFileSystemRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3files.types.bucket_arn
    import capo_s3files.types.creation_token
    import capo_s3files.types.kms_key_id
    import capo_s3files.types.role_arn
    import capo_s3files.types.tag_list


class CreateFileSystemRequest(TypedDict, closed=True):
    bucket: "capo_s3files.types.bucket_arn.BucketArn"
    """<p>The Amazon Resource Name (ARN) of the S3 bucket that will be accessible through the file system. The bucket must exist and be in the same Amazon Web Services Region as the file system.</p>"""
    prefix: NotRequired["str"]
    """<p>An optional prefix within the S3 bucket to scope the file system access. If specified, the file system provides access only to objects with keys that begin with this prefix. If not specified, the file system provides access to the entire bucket.</p>"""
    client_token: NotRequired["capo_s3files.types.creation_token.CreationToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure idempotent creation. Up to 64 ASCII characters are allowed. If you don't specify a client token, the Amazon Web Services SDK automatically generates one.</p>"""
    kms_key_id: NotRequired["capo_s3files.types.kms_key_id.KmsKeyId"]
    """<p>The ARN, key ID, or alias of the KMS key to use for encryption. If not specified, the service uses a service-owned key for encryption. You can specify a KMS key using the following formats: key ID, ARN, key alias, or key alias ARN. If you use <code>KmsKeyId</code>, the file system will be encrypted.</p>"""
    role_arn: "capo_s3files.types.role_arn.RoleArn"
    """<p>The ARN of the IAM role that grants the S3 Files service permission to read and write data between the file system and the S3 bucket. This role must have the necessary permissions to access the specified bucket and prefix.</p>"""
    tags: NotRequired["capo_s3files.types.tag_list.TagList"]
    """<p>An array of key-value pairs to apply as tags to the file system resource. Each tag is a user-defined key-value pair. You can use tags to categorize and manage your file systems. Each key must be unique for the resource.</p>"""
    accept_bucket_warning: NotRequired["bool"]
    """<p>Set to true to acknowledge and accept any warnings about the bucket configuration. If not specified, the operation may fail if there are bucket configuration warnings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFileSystemRequest) -> dict:
    out: dict = {}
    out["bucket"] = value["bucket"]
    if "prefix" in value:
        out["prefix"] = value["prefix"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    out["roleArn"] = value["role_arn"]
    if "tags" in value:
        import capo_s3files.types.tag_list

        out["tags"] = capo_s3files.types.tag_list.serialize_json(value["tags"])
    if "accept_bucket_warning" in value:
        out["acceptBucketWarning"] = value["accept_bucket_warning"]
    return out


def deserialize_json(data: dict) -> CreateFileSystemRequest:
    out: CreateFileSystemRequest = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    else:
        out["bucket"] = ""
    if data.get("prefix") is not None:
        out["prefix"] = data["prefix"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("tags") is not None:
        import capo_s3files.types.tag_list

        out["tags"] = capo_s3files.types.tag_list.deserialize_json(data["tags"])
    if data.get("acceptBucketWarning") is not None:
        out["accept_bucket_warning"] = data["acceptBucketWarning"]
    return out
