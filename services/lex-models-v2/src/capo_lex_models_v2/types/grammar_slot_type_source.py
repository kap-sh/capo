"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#GrammarSlotTypeSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.kms_key_arn
    import capo_lex_models_v2.types.s3_bucket_name
    import capo_lex_models_v2.types.s3_object_path


class GrammarSlotTypeSource(TypedDict, closed=True):
    s3_bucket_name: "capo_lex_models_v2.types.s3_bucket_name.S3BucketName"
    """<p>The name of the Amazon S3 bucket that contains the grammar source.</p>"""
    s3_object_key: "capo_lex_models_v2.types.s3_object_path.S3ObjectPath"
    """<p>The path to the grammar in the Amazon S3 bucket.</p>"""
    kms_key_arn: NotRequired["capo_lex_models_v2.types.kms_key_arn.KmsKeyArn"]
    """<p>The KMS key required to decrypt the contents of the grammar, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GrammarSlotTypeSource) -> dict:
    out: dict = {}
    out["s3BucketName"] = value["s3_bucket_name"]
    out["s3ObjectKey"] = value["s3_object_key"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> GrammarSlotTypeSource:
    out: GrammarSlotTypeSource = {}  # type: ignore[typeddict-item]
    if data.get("s3BucketName") is not None:
        out["s3_bucket_name"] = data["s3BucketName"]
    else:
        out["s3_bucket_name"] = ""
    if data.get("s3ObjectKey") is not None:
        out["s3_object_key"] = data["s3ObjectKey"]
    else:
        out["s3_object_key"] = ""
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
