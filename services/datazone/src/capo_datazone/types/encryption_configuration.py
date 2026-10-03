"""Generated from Smithy shape ``com.amazonaws.datazone#EncryptionConfiguration``."""

from typing_extensions import NotRequired, TypedDict


class EncryptionConfiguration(TypedDict, closed=True):
    kms_key_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the KMS key to use for encryption. This field is required only when <code>sseAlgorithm</code> is set to <code>aws:kms</code>.</p>"""
    sse_algorithm: NotRequired["str"]
    """<p>The server-side encryption algorithm to use. Valid values are AES256 for S3-managed encryption keys, or aws:kms for Amazon Web Services KMS-managed encryption keys. If you choose SSE-KMS encryption you must grant the S3 Tables maintenance principal access to your KMS key. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-kms-permissions.html">Permissions requirements for S3 Tables SSE-KMS encryption</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionConfiguration) -> dict:
    out: dict = {}
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "sse_algorithm" in value:
        out["sseAlgorithm"] = value["sse_algorithm"]
    return out


def deserialize_json(data: dict) -> EncryptionConfiguration:
    out: EncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("sseAlgorithm") is not None:
        out["sse_algorithm"] = data["sseAlgorithm"]
    return out
