"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#AsyncInvokeS3OutputDataConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.account_id
    import capo_bedrock_runtime.types.kms_key_id
    import capo_bedrock_runtime.types.s3_uri


class AsyncInvokeS3OutputDataConfig(TypedDict, closed=True):
    s3_uri: "capo_bedrock_runtime.types.s3_uri.S3Uri"
    """<p>An object URI starting with <code>s3://</code>.</p>"""
    kms_key_id: NotRequired["capo_bedrock_runtime.types.kms_key_id.KmsKeyId"]
    """<p>A KMS encryption key ID.</p>"""
    bucket_owner: NotRequired["capo_bedrock_runtime.types.account_id.AccountId"]
    """<p>If the bucket belongs to another AWS account, specify that account's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AsyncInvokeS3OutputDataConfig) -> dict:
    out: dict = {}
    out["s3Uri"] = value["s3_uri"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "bucket_owner" in value:
        out["bucketOwner"] = value["bucket_owner"]
    return out


def deserialize_json(data: dict) -> AsyncInvokeS3OutputDataConfig:
    out: AsyncInvokeS3OutputDataConfig = {}  # type: ignore[typeddict-item]
    if data.get("s3Uri") is not None:
        out["s3_uri"] = data["s3Uri"]
    else:
        out["s3_uri"] = ""
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("bucketOwner") is not None:
        out["bucket_owner"] = data["bucketOwner"]
    return out
