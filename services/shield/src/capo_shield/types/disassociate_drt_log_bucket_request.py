"""Generated from Smithy shape ``com.amazonaws.shield#DisassociateDRTLogBucketRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_shield.types.log_bucket


class DisassociateDRTLogBucketRequest(TypedDict, closed=True):
    log_bucket: "capo_shield.types.log_bucket.LogBucket"
    """<p>The Amazon S3 bucket that contains the logs that you want to share.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateDRTLogBucketRequest) -> dict:
    out: dict = {}
    out["LogBucket"] = value["log_bucket"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateDRTLogBucketRequest:
    out: DisassociateDRTLogBucketRequest = {}  # type: ignore[typeddict-item]
    if data.get("LogBucket") is not None:
        out["log_bucket"] = data["LogBucket"]
    else:
        out["log_bucket"] = ""
    return out
