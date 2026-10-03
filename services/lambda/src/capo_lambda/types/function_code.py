"""Generated from Smithy shape ``com.amazonaws.lambda#FunctionCode``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.blob
    import capo_lambda.types.kms_key_arn
    import capo_lambda.types.s3_bucket
    import capo_lambda.types.s3_key
    import capo_lambda.types.s3_object_storage_mode
    import capo_lambda.types.s3_object_version
    import capo_lambda.types.string


class FunctionCode(TypedDict, closed=True):
    zip_file: NotRequired["capo_lambda.types.blob.Blob"]
    """<p>The base64-encoded contents of the deployment package. Amazon Web Services SDK and CLI clients handle the encoding for you.</p>"""
    s3_bucket: NotRequired["capo_lambda.types.s3_bucket.S3Bucket"]
    """<p>An Amazon S3 bucket in the same Amazon Web Services Region as your function. The bucket can be in a different Amazon Web Services account.</p>"""
    s3_key: NotRequired["capo_lambda.types.s3_key.S3Key"]
    """<p>The Amazon S3 key of the deployment package.</p>"""
    s3_object_version: NotRequired[
        "capo_lambda.types.s3_object_version.S3ObjectVersion"
    ]
    """<p>For versioned objects, the version of the deployment package object to use.</p>"""
    s3_object_storage_mode: NotRequired[
        "capo_lambda.types.s3_object_storage_mode.S3ObjectStorageMode"
    ]
    """<p>Specifies how the deployment package is stored. Valid values:</p> <ul> <li> <p> <code>COPY</code> (default) – Uploads a copy of your deployment package to Lambda.</p> </li> <li> <p> <code>REFERENCE</code> – Lambda references the deployment package from the specified Amazon S3 bucket.</p> </li> </ul>"""
    image_uri: NotRequired["capo_lambda.types.string.String"]
    """<p>URI of a <a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-images.html">container image</a> in the Amazon ECR registry.</p>"""
    source_kms_key_arn: NotRequired["capo_lambda.types.kms_key_arn.KMSKeyArn"]
    """<p>The ARN of the Key Management Service (KMS) customer managed key that's used to encrypt your function's .zip deployment package. If you don't provide a customer managed key, Lambda uses an <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk">Amazon Web Services owned key</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FunctionCode) -> dict:
    out: dict = {}
    if "zip_file" in value:
        import capo_lambda.types.blob

        out["ZipFile"] = capo_lambda.types.blob.serialize_json(value["zip_file"])
    if "s3_bucket" in value:
        out["S3Bucket"] = value["s3_bucket"]
    if "s3_key" in value:
        out["S3Key"] = value["s3_key"]
    if "s3_object_version" in value:
        out["S3ObjectVersion"] = value["s3_object_version"]
    if "s3_object_storage_mode" in value:
        import capo_lambda.types.s3_object_storage_mode

        out["S3ObjectStorageMode"] = (
            capo_lambda.types.s3_object_storage_mode.serialize_json(
                value["s3_object_storage_mode"]
            )
        )
    if "image_uri" in value:
        out["ImageUri"] = value["image_uri"]
    if "source_kms_key_arn" in value:
        out["SourceKMSKeyArn"] = value["source_kms_key_arn"]
    return out


def deserialize_json(data: dict) -> FunctionCode:
    out: FunctionCode = {}  # type: ignore[typeddict-item]
    if data.get("ZipFile") is not None:
        import capo_lambda.types.blob

        out["zip_file"] = capo_lambda.types.blob.deserialize_json(data["ZipFile"])
    if data.get("S3Bucket") is not None:
        out["s3_bucket"] = data["S3Bucket"]
    if data.get("S3Key") is not None:
        out["s3_key"] = data["S3Key"]
    if data.get("S3ObjectVersion") is not None:
        out["s3_object_version"] = data["S3ObjectVersion"]
    if data.get("S3ObjectStorageMode") is not None:
        import capo_lambda.types.s3_object_storage_mode

        out["s3_object_storage_mode"] = (
            capo_lambda.types.s3_object_storage_mode.deserialize_json(
                data["S3ObjectStorageMode"]
            )
        )
    if data.get("ImageUri") is not None:
        out["image_uri"] = data["ImageUri"]
    if data.get("SourceKMSKeyArn") is not None:
        out["source_kms_key_arn"] = data["SourceKMSKeyArn"]
    return out
