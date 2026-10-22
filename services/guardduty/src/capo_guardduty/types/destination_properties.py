"""Generated from Smithy shape ``com.amazonaws.guardduty#DestinationProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.account_id
    import capo_guardduty.types.string


class DestinationProperties(TypedDict, closed=True):
    destination_arn: NotRequired["capo_guardduty.types.string.String"]
    """<p>The ARN of the resource to publish to.</p> <p>To specify an S3 bucket folder use the following format: <code>arn:aws:s3:::DOC-EXAMPLE-BUCKET/myFolder/</code> </p>"""
    kms_key_arn: NotRequired["capo_guardduty.types.string.String"]
    """<p>The ARN of the KMS key to use for encryption.</p>"""
    expected_bucket_owner: NotRequired["capo_guardduty.types.account_id.AccountId"]
    """<p>The 12-digit Amazon Web Services account ID of the account that owns the Amazon S3 bucket specified in the <code>DestinationArn</code> parameter.</p> <p>When you provide this value, GuardDuty verifies that the specified account owns the bucket before it exports findings. If the account ID doesn't match the actual owner of the bucket, GuardDuty doesn't export findings to that bucket. This helps prevent GuardDuty from exporting your findings to a bucket that a different Amazon Web Services account owns (for example, if the original bucket was deleted and its name was later claimed by another account). If you don't specify this value, GuardDuty doesn't perform this verification. GuardDuty strongly recommends that you provide the expected bucket owner when possible.</p> <p>When you update a publishing destination, omitting this field leaves the currently stored value unchanged. This field appears in the response only if it was provided when the publishing destination was created or updated.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_exportfindings.html#guardduty-exportfindings-expected-bucket-owner">Verifying the Amazon S3 bucket owner</a> in the <i>Amazon GuardDuty User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DestinationProperties) -> dict:
    out: dict = {}
    if "destination_arn" in value:
        out["destinationArn"] = value["destination_arn"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "expected_bucket_owner" in value:
        out["expectedBucketOwner"] = value["expected_bucket_owner"]
    return out


def deserialize_json(data: dict) -> DestinationProperties:
    out: DestinationProperties = {}  # type: ignore[typeddict-item]
    if data.get("destinationArn") is not None:
        out["destination_arn"] = data["destinationArn"]
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("expectedBucketOwner") is not None:
        out["expected_bucket_owner"] = data["expectedBucketOwner"]
    return out
