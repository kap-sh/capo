"""Generated from Smithy shape ``com.amazonaws.s3tables#EncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3tables.types.sse_algorithm


class EncryptionConfiguration(TypedDict, closed=True):
    sse_algorithm: "capo_s3tables.types.sse_algorithm.SSEAlgorithm"
    """<p>The server-side encryption algorithm to use. Valid values are <code>AES256</code> for S3-managed encryption keys, or <code>aws:kms</code> for Amazon Web Services KMS-managed encryption keys. If you choose SSE-KMS encryption you must grant the S3 Tables maintenance principal access to your KMS key. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-kms-permissions.html">Permissions requirements for S3 Tables SSE-KMS encryption</a>.</p>"""
    kms_key_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the KMS key to use for encryption. This field is required only when <code>sseAlgorithm</code> is set to <code>aws:kms</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionConfiguration) -> dict:
    out: dict = {}
    import capo_s3tables.types.sse_algorithm

    out["sseAlgorithm"] = capo_s3tables.types.sse_algorithm.serialize_json(
        value["sse_algorithm"]
    )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> EncryptionConfiguration:
    out: EncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("sseAlgorithm") is not None:
        import capo_s3tables.types.sse_algorithm

        out["sse_algorithm"] = capo_s3tables.types.sse_algorithm.deserialize_json(
            data["sseAlgorithm"]
        )
    else:
        raise DeserializationError("EncryptionConfiguration.sse_algorithm required")
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
