"""Generated from Smithy shape ``com.amazonaws.dynamodb#InputS3Configuration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.bulk_operation_input_format
    import capo_dynamodb.types.input_compression_type
    import capo_dynamodb.types.s3_bucket
    import capo_dynamodb.types.s3_bucket_owner
    import capo_dynamodb.types.s3_prefix


class InputS3Configuration(TypedDict, closed=True):
    s3_bucket_owner: NotRequired["capo_dynamodb.types.s3_bucket_owner.S3BucketOwner"]
    """<p>The Amazon Web Services account ID of the input bucket owner. If you omit this value, DynamoDB uses the Amazon Web Services account ID of the requester.</p> <note> <p> <code>S3BucketOwner</code> is required when the bucket is owned by another Amazon Web Services account.</p> </note>"""
    s3_bucket: "capo_dynamodb.types.s3_bucket.S3Bucket"
    """<p>The name of the Amazon S3 bucket that contains the input objects.</p>"""
    s3_key_prefix: NotRequired["capo_dynamodb.types.s3_prefix.S3Prefix"]
    """<p>An optional key prefix that limits the input to matching objects in the Amazon S3 bucket.</p>"""
    input_format: (
        "capo_dynamodb.types.bulk_operation_input_format.BulkOperationInputFormat"
    )
    """<p>The format of the input objects. <code>DYNAMODB_JSON</code> uses JSON Lines, with one JSON record per line. <code>ION</code> uses a sequence of Ion structs.</p>"""
    input_compression_type: NotRequired[
        "capo_dynamodb.types.input_compression_type.InputCompressionType"
    ]
    """<p>The compression type of the input objects. Valid values are <code>GZIP</code>, <code>ZSTD</code>, and <code>NONE</code>. If you don't specify a value, DynamoDB uses <code>NONE</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InputS3Configuration) -> dict:
    out: dict = {}
    if "s3_bucket_owner" in value:
        out["S3BucketOwner"] = value["s3_bucket_owner"]
    out["S3Bucket"] = value["s3_bucket"]
    if "s3_key_prefix" in value:
        out["S3KeyPrefix"] = value["s3_key_prefix"]
    import capo_dynamodb.types.bulk_operation_input_format

    out["InputFormat"] = (
        capo_dynamodb.types.bulk_operation_input_format.serialize_aws_json_1_0(
            value["input_format"]
        )
    )
    if "input_compression_type" in value:
        import capo_dynamodb.types.input_compression_type

        out["InputCompressionType"] = (
            capo_dynamodb.types.input_compression_type.serialize_aws_json_1_0(
                value["input_compression_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> InputS3Configuration:
    out: InputS3Configuration = {}  # type: ignore[typeddict-item]
    if data.get("S3BucketOwner") is not None:
        out["s3_bucket_owner"] = data["S3BucketOwner"]
    if data.get("S3Bucket") is not None:
        out["s3_bucket"] = data["S3Bucket"]
    else:
        out["s3_bucket"] = ""
    if data.get("S3KeyPrefix") is not None:
        out["s3_key_prefix"] = data["S3KeyPrefix"]
    if data.get("InputFormat") is not None:
        import capo_dynamodb.types.bulk_operation_input_format

        out["input_format"] = (
            capo_dynamodb.types.bulk_operation_input_format.deserialize_aws_json_1_0(
                data["InputFormat"]
            )
        )
    else:
        import typing

        out["input_format"] = typing.cast(
            "capo_dynamodb.types.bulk_operation_input_format.BulkOperationInputFormat",
            "",
        )
    if data.get("InputCompressionType") is not None:
        import capo_dynamodb.types.input_compression_type

        out["input_compression_type"] = (
            capo_dynamodb.types.input_compression_type.deserialize_aws_json_1_0(
                data["InputCompressionType"]
            )
        )
    return out
