"""Generated from Smithy shape ``com.amazonaws.kinesis#S3StorageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.bucket_arn
    import capo_kinesis.types.expected_bucket_owner
    import capo_kinesis.types.s3_compression_type
    import capo_kinesis.types.s3_output_key_template
    import capo_kinesis.types.s3_storage_class


class S3StorageConfiguration(TypedDict, closed=True):
    bucket_arn: "capo_kinesis.types.bucket_arn.BucketARN"
    """<p>The Amazon Resource Name (ARN) of the destination Amazon S3 bucket.</p>"""
    expected_bucket_owner: (
        "capo_kinesis.types.expected_bucket_owner.ExpectedBucketOwner"
    )
    """<p>The Amazon Web Services account ID of the expected owner of the destination bucket. This value helps prevent delivery to an unintended bucket if ownership changes.</p>"""
    output_key_template: NotRequired[
        "capo_kinesis.types.s3_output_key_template.S3OutputKeyTemplate"
    ]
    """<p>The template used to construct the Amazon S3 object key for delivered objects. If not specified, a default template is used.</p>"""
    storage_class: NotRequired["capo_kinesis.types.s3_storage_class.S3StorageClass"]
    """<p>The Amazon S3 storage class for delivered objects. Valid values:</p> <ul> <li> <p> <code>STANDARD</code> - The default storage class, for frequently accessed data.</p> </li> <li> <p> <code>INTELLIGENT_TIERING</code> - Automatically moves objects to the most cost-effective access tier based on usage patterns.</p> </li> <li> <p> <code>GLACIER_IR</code> - Low-cost storage for rarely accessed data that requires millisecond retrieval.</p> </li> </ul>"""
    compression_type: "capo_kinesis.types.s3_compression_type.S3CompressionType"
    """<p>The compression applied to delivered objects. Valid values:</p> <ul> <li> <p> <code>NONE</code> - No compression.</p> </li> <li> <p> <code>GZIP</code> - gzip compression.</p> </li> <li> <p> <code>ZSTD</code> - Zstandard compression.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3StorageConfiguration) -> dict:
    out: dict = {}
    out["BucketARN"] = value["bucket_arn"]
    out["ExpectedBucketOwner"] = value["expected_bucket_owner"]
    if "output_key_template" in value:
        out["OutputKeyTemplate"] = value["output_key_template"]
    if "storage_class" in value:
        import capo_kinesis.types.s3_storage_class

        out["StorageClass"] = (
            capo_kinesis.types.s3_storage_class.serialize_aws_json_1_1(
                value["storage_class"]
            )
        )
    import capo_kinesis.types.s3_compression_type

    out["CompressionType"] = (
        capo_kinesis.types.s3_compression_type.serialize_aws_json_1_1(
            value["compression_type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> S3StorageConfiguration:
    out: S3StorageConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("BucketARN") is not None:
        out["bucket_arn"] = data["BucketARN"]
    else:
        out["bucket_arn"] = ""
    if data.get("ExpectedBucketOwner") is not None:
        out["expected_bucket_owner"] = data["ExpectedBucketOwner"]
    else:
        out["expected_bucket_owner"] = ""
    if data.get("OutputKeyTemplate") is not None:
        out["output_key_template"] = data["OutputKeyTemplate"]
    if data.get("StorageClass") is not None:
        import capo_kinesis.types.s3_storage_class

        out["storage_class"] = (
            capo_kinesis.types.s3_storage_class.deserialize_aws_json_1_1(
                data["StorageClass"]
            )
        )
    if data.get("CompressionType") is not None:
        import capo_kinesis.types.s3_compression_type

        out["compression_type"] = (
            capo_kinesis.types.s3_compression_type.deserialize_aws_json_1_1(
                data["CompressionType"]
            )
        )
    else:
        import typing

        out["compression_type"] = typing.cast(
            "capo_kinesis.types.s3_compression_type.S3CompressionType", ""
        )
    return out
