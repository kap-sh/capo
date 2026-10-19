"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestSetStorageLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.kms_key_arn
    import capo_lex_models_v2.types.s3_bucket_name
    import capo_lex_models_v2.types.s3_object_path


class TestSetStorageLocation(TypedDict, closed=True):
    s3_bucket_name: "capo_lex_models_v2.types.s3_bucket_name.S3BucketName"
    """<p>The name of the Amazon S3 bucket in which the test set is stored.</p>"""
    s3_path: "capo_lex_models_v2.types.s3_object_path.S3ObjectPath"
    """<p>The path inside the Amazon S3 bucket where the test set is stored.</p>"""
    kms_key_arn: NotRequired["capo_lex_models_v2.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of an Amazon Web Services Key Management Service (KMS) key for encrypting the test set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestSetStorageLocation) -> dict:
    out: dict = {}
    out["s3BucketName"] = value["s3_bucket_name"]
    out["s3Path"] = value["s3_path"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> TestSetStorageLocation:
    out: TestSetStorageLocation = {}  # type: ignore[typeddict-item]
    if data.get("s3BucketName") is not None:
        out["s3_bucket_name"] = data["s3BucketName"]
    else:
        out["s3_bucket_name"] = ""
    if data.get("s3Path") is not None:
        out["s3_path"] = data["s3Path"]
    else:
        out["s3_path"] = ""
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
