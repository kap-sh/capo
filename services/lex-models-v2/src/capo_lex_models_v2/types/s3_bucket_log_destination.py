"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#S3BucketLogDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.kms_key_arn
    import capo_lex_models_v2.types.log_prefix
    import capo_lex_models_v2.types.s3_bucket_arn


class S3BucketLogDestination(TypedDict, closed=True):
    kms_key_arn: NotRequired["capo_lex_models_v2.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of an Amazon Web Services Key Management Service (KMS) key for encrypting audio log files stored in an S3 bucket.</p>"""
    s3_bucket_arn: "capo_lex_models_v2.types.s3_bucket_arn.S3BucketArn"
    """<p>The Amazon Resource Name (ARN) of an Amazon S3 bucket where audio log files are stored.</p>"""
    log_prefix: "capo_lex_models_v2.types.log_prefix.LogPrefix"
    """<p>The S3 prefix to assign to audio log files.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3BucketLogDestination) -> dict:
    out: dict = {}
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    out["s3BucketArn"] = value["s3_bucket_arn"]
    out["logPrefix"] = value["log_prefix"]
    return out


def deserialize_json(data: dict) -> S3BucketLogDestination:
    out: S3BucketLogDestination = {}  # type: ignore[typeddict-item]
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("s3BucketArn") is not None:
        out["s3_bucket_arn"] = data["s3BucketArn"]
    else:
        out["s3_bucket_arn"] = ""
    if data.get("logPrefix") is not None:
        out["log_prefix"] = data["logPrefix"]
    else:
        out["log_prefix"] = ""
    return out
