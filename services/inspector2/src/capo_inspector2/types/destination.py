"""Generated from Smithy shape ``com.amazonaws.inspector2#Destination``."""

from typing_extensions import NotRequired, TypedDict


class Destination(TypedDict, closed=True):
    bucket_name: "str"
    """<p>The name of the Amazon S3 bucket to export findings to.</p>"""
    key_prefix: NotRequired["str"]
    """<p>The prefix that the findings will be written under.</p>"""
    kms_key_arn: "str"
    """<p>The ARN of the KMS key used to encrypt data when exporting findings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Destination) -> dict:
    out: dict = {}
    out["bucketName"] = value["bucket_name"]
    if "key_prefix" in value:
        out["keyPrefix"] = value["key_prefix"]
    out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> Destination:
    out: Destination = {}  # type: ignore[typeddict-item]
    if data.get("bucketName") is not None:
        out["bucket_name"] = data["bucketName"]
    else:
        out["bucket_name"] = ""
    if data.get("keyPrefix") is not None:
        out["key_prefix"] = data["keyPrefix"]
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    else:
        out["kms_key_arn"] = ""
    return out
