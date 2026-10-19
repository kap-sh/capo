"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelInvocationJobS3OutputDataConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.account_id
    import capo_bedrock.types.kms_key_id
    import capo_bedrock.types.s3_uri


class ModelInvocationJobS3OutputDataConfig(TypedDict, closed=True):
    s3_uri: "capo_bedrock.types.s3_uri.S3Uri"
    """<p>The S3 location of the output data.</p>"""
    s3_encryption_key_id: NotRequired["capo_bedrock.types.kms_key_id.KmsKeyId"]
    """<p>The unique identifier of the key that encrypts the S3 location of the output data.</p>"""
    s3_bucket_owner: NotRequired["capo_bedrock.types.account_id.AccountId"]
    """<p>The ID of the Amazon Web Services account that owns the S3 bucket containing the output data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelInvocationJobS3OutputDataConfig) -> dict:
    out: dict = {}
    out["s3Uri"] = value["s3_uri"]
    if "s3_encryption_key_id" in value:
        out["s3EncryptionKeyId"] = value["s3_encryption_key_id"]
    if "s3_bucket_owner" in value:
        out["s3BucketOwner"] = value["s3_bucket_owner"]
    return out


def deserialize_json(data: dict) -> ModelInvocationJobS3OutputDataConfig:
    out: ModelInvocationJobS3OutputDataConfig = {}  # type: ignore[typeddict-item]
    if data.get("s3Uri") is not None:
        out["s3_uri"] = data["s3Uri"]
    else:
        out["s3_uri"] = ""
    if data.get("s3EncryptionKeyId") is not None:
        out["s3_encryption_key_id"] = data["s3EncryptionKeyId"]
    if data.get("s3BucketOwner") is not None:
        out["s3_bucket_owner"] = data["s3BucketOwner"]
    return out
