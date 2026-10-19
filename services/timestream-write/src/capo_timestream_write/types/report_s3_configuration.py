"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#ReportS3Configuration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_write.types.s3_bucket_name
    import capo_timestream_write.types.s3_encryption_option
    import capo_timestream_write.types.s3_object_key_prefix
    import capo_timestream_write.types.string_value2048


class ReportS3Configuration(TypedDict, closed=True):
    bucket_name: "capo_timestream_write.types.s3_bucket_name.S3BucketName"
    """<p></p>"""
    object_key_prefix: NotRequired[
        "capo_timestream_write.types.s3_object_key_prefix.S3ObjectKeyPrefix"
    ]
    """<p></p>"""
    encryption_option: NotRequired[
        "capo_timestream_write.types.s3_encryption_option.S3EncryptionOption"
    ]
    """<p></p>"""
    kms_key_id: NotRequired[
        "capo_timestream_write.types.string_value2048.StringValue2048"
    ]
    """<p></p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReportS3Configuration) -> dict:
    out: dict = {}
    out["BucketName"] = value["bucket_name"]
    if "object_key_prefix" in value:
        out["ObjectKeyPrefix"] = value["object_key_prefix"]
    if "encryption_option" in value:
        import capo_timestream_write.types.s3_encryption_option

        out["EncryptionOption"] = (
            capo_timestream_write.types.s3_encryption_option.serialize_aws_json_1_0(
                value["encryption_option"]
            )
        )
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ReportS3Configuration:
    out: ReportS3Configuration = {}  # type: ignore[typeddict-item]
    if data.get("BucketName") is not None:
        out["bucket_name"] = data["BucketName"]
    else:
        out["bucket_name"] = ""
    if data.get("ObjectKeyPrefix") is not None:
        out["object_key_prefix"] = data["ObjectKeyPrefix"]
    if data.get("EncryptionOption") is not None:
        import capo_timestream_write.types.s3_encryption_option

        out["encryption_option"] = (
            capo_timestream_write.types.s3_encryption_option.deserialize_aws_json_1_0(
                data["EncryptionOption"]
            )
        )
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    return out
