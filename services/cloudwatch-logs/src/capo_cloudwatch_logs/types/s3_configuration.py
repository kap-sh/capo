"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#S3Configuration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.account_id
    import capo_cloudwatch_logs.types.kms_key_id
    import capo_cloudwatch_logs.types.role_arn
    import capo_cloudwatch_logs.types.s3_uri


class S3Configuration(TypedDict, closed=True):
    destination_identifier: "capo_cloudwatch_logs.types.s3_uri.S3Uri"
    """<p>The Amazon S3 URI where query results are delivered. Must be a valid S3 URI format.</p>"""
    role_arn: "capo_cloudwatch_logs.types.role_arn.RoleArn"
    """<p>The ARN of the IAM role that grants permissions to write query results to the specified Amazon S3 destination.</p>"""
    owner_account_id: NotRequired["capo_cloudwatch_logs.types.account_id.AccountId"]
    """<p>The Amazon Web Services accountId for the bucket owning account.</p>"""
    kms_key_id: NotRequired["capo_cloudwatch_logs.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Resource Name (ARN) of the KMS encryption key. Must belong to the same Amazon Web Services Region as the destination Amazon S3 bucket.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3Configuration) -> dict:
    out: dict = {}
    out["destinationIdentifier"] = value["destination_identifier"]
    out["roleArn"] = value["role_arn"]
    if "owner_account_id" in value:
        out["ownerAccountId"] = value["owner_account_id"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3Configuration:
    out: S3Configuration = {}  # type: ignore[typeddict-item]
    if data.get("destinationIdentifier") is not None:
        out["destination_identifier"] = data["destinationIdentifier"]
    else:
        out["destination_identifier"] = ""
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("ownerAccountId") is not None:
        out["owner_account_id"] = data["ownerAccountId"]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    return out
