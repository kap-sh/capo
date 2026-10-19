"""Generated from Smithy shape ``com.amazonaws.kinesis#DeadLetterQueueS3Configuration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.bucket_arn
    import capo_kinesis.types.expected_bucket_owner
    import capo_kinesis.types.s3_error_output_prefix


class DeadLetterQueueS3Configuration(TypedDict, closed=True):
    bucket_arn: "capo_kinesis.types.bucket_arn.BucketARN"
    """<p>The Amazon Resource Name (ARN) of the dead-letter queue Amazon S3 bucket.</p>"""
    expected_bucket_owner: (
        "capo_kinesis.types.expected_bucket_owner.ExpectedBucketOwner"
    )
    """<p>The Amazon Web Services account ID of the expected owner of the dead-letter queue bucket.</p>"""
    error_output_prefix: NotRequired[
        "capo_kinesis.types.s3_error_output_prefix.S3ErrorOutputPrefix"
    ]
    """<p>The Amazon S3 key prefix for error records.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeadLetterQueueS3Configuration) -> dict:
    out: dict = {}
    out["BucketARN"] = value["bucket_arn"]
    out["ExpectedBucketOwner"] = value["expected_bucket_owner"]
    if "error_output_prefix" in value:
        out["ErrorOutputPrefix"] = value["error_output_prefix"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeadLetterQueueS3Configuration:
    out: DeadLetterQueueS3Configuration = {}  # type: ignore[typeddict-item]
    if data.get("BucketARN") is not None:
        out["bucket_arn"] = data["BucketARN"]
    else:
        out["bucket_arn"] = ""
    if data.get("ExpectedBucketOwner") is not None:
        out["expected_bucket_owner"] = data["ExpectedBucketOwner"]
    else:
        out["expected_bucket_owner"] = ""
    if data.get("ErrorOutputPrefix") is not None:
        out["error_output_prefix"] = data["ErrorOutputPrefix"]
    return out
