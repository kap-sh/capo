"""Generated from Smithy shape ``com.amazonaws.dynamodb#OutputS3Configuration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.output_type_list
    import capo_dynamodb.types.s3_bucket
    import capo_dynamodb.types.s3_bucket_owner
    import capo_dynamodb.types.s3_prefix
    import capo_dynamodb.types.s3_sse_algorithm
    import capo_dynamodb.types.s3_sse_kms_key_id


class OutputS3Configuration(TypedDict, closed=True):
    s3_bucket_owner: NotRequired["capo_dynamodb.types.s3_bucket_owner.S3BucketOwner"]
    """<p>The Amazon Web Services account ID of the output bucket owner. If you omit this value, DynamoDB uses the Amazon Web Services account ID of the requester.</p> <note> <p> <code>S3BucketOwner</code> is required when the bucket is owned by another Amazon Web Services account.</p> </note>"""
    s3_bucket: NotRequired["capo_dynamodb.types.s3_bucket.S3Bucket"]
    """<p>The name of the Amazon S3 bucket where DynamoDB writes output records.</p>"""
    s3_key_prefix: NotRequired["capo_dynamodb.types.s3_prefix.S3Prefix"]
    """<p>An optional key prefix under which DynamoDB writes the output records.</p>"""
    s3_sse_algorithm: NotRequired["capo_dynamodb.types.s3_sse_algorithm.S3SseAlgorithm"]
    """<p>The server-side encryption algorithm for the output objects. Valid values are <code>AES256</code> and <code>KMS</code>. If you don't specify a value, Amazon S3 applies the destination bucket's default encryption settings.</p>"""
    s3_sse_kms_key_id: NotRequired[
        "capo_dynamodb.types.s3_sse_kms_key_id.S3SseKmsKeyId"
    ]
    """<p>The identifier of the KMS key that encrypts the output objects. Specify this value when <code>S3SseAlgorithm</code> is <code>KMS</code>. Don't specify it when the algorithm is <code>AES256</code>.</p>"""
    output_type: "capo_dynamodb.types.output_type_list.OutputTypeList"
    """<p>The following values describe the types of output that DynamoDB writes for individual input items. Include one or both values.</p> <dl> <dt> ERROR </dt> <dd> <p>Reports input records or input objects that DynamoDB couldn't process. This includes malformed input and item validation failures, such as a missing or incorrectly typed primary key attribute or an item that exceeds a DynamoDB limit.</p> </dd> <dt> CONDITION_CHECK_FAILURE </dt> <dd> <p>Reports the attempted item and, when present, the existing item for a write whose condition expression evaluates to false.</p> </dd> </dl>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OutputS3Configuration) -> dict:
    out: dict = {}
    if "s3_bucket_owner" in value:
        out["S3BucketOwner"] = value["s3_bucket_owner"]
    if "s3_bucket" in value:
        out["S3Bucket"] = value["s3_bucket"]
    if "s3_key_prefix" in value:
        out["S3KeyPrefix"] = value["s3_key_prefix"]
    if "s3_sse_algorithm" in value:
        import capo_dynamodb.types.s3_sse_algorithm

        out["S3SseAlgorithm"] = (
            capo_dynamodb.types.s3_sse_algorithm.serialize_aws_json_1_0(
                value["s3_sse_algorithm"]
            )
        )
    if "s3_sse_kms_key_id" in value:
        out["S3SseKmsKeyId"] = value["s3_sse_kms_key_id"]
    import capo_dynamodb.types.output_type_list

    out["OutputType"] = capo_dynamodb.types.output_type_list.serialize_aws_json_1_0(
        value["output_type"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> OutputS3Configuration:
    out: OutputS3Configuration = {}  # type: ignore[typeddict-item]
    if data.get("S3BucketOwner") is not None:
        out["s3_bucket_owner"] = data["S3BucketOwner"]
    if data.get("S3Bucket") is not None:
        out["s3_bucket"] = data["S3Bucket"]
    if data.get("S3KeyPrefix") is not None:
        out["s3_key_prefix"] = data["S3KeyPrefix"]
    if data.get("S3SseAlgorithm") is not None:
        import capo_dynamodb.types.s3_sse_algorithm

        out["s3_sse_algorithm"] = (
            capo_dynamodb.types.s3_sse_algorithm.deserialize_aws_json_1_0(
                data["S3SseAlgorithm"]
            )
        )
    if data.get("S3SseKmsKeyId") is not None:
        out["s3_sse_kms_key_id"] = data["S3SseKmsKeyId"]
    if data.get("OutputType") is not None:
        import capo_dynamodb.types.output_type_list

        out["output_type"] = (
            capo_dynamodb.types.output_type_list.deserialize_aws_json_1_0(
                data["OutputType"]
            )
        )
    else:
        out["output_type"] = []
    return out
