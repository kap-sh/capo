"""Generated from Smithy shape ``com.amazonaws.pipes#S3LogDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.s3_output_format
    import capo_pipes.types.string


class S3LogDestination(TypedDict, closed=True):
    bucket_name: NotRequired["capo_pipes.types.string.String"]
    """<p>The name of the Amazon S3 bucket to which EventBridge delivers the log records for the pipe.</p>"""
    prefix: NotRequired["capo_pipes.types.string.String"]
    """<p>The prefix text with which to begin Amazon S3 log object names.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html">Organizing objects using prefixes</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p>"""
    bucket_owner: NotRequired["capo_pipes.types.string.String"]
    """<p>The Amazon Web Services account that owns the Amazon S3 bucket to which EventBridge delivers the log records for the pipe.</p>"""
    output_format: NotRequired["capo_pipes.types.s3_output_format.S3OutputFormat"]
    """<p>The format EventBridge uses for the log records.</p> <p>EventBridge currently only supports <code>json</code> formatting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3LogDestination) -> dict:
    out: dict = {}
    if "bucket_name" in value:
        out["BucketName"] = value["bucket_name"]
    if "prefix" in value:
        out["Prefix"] = value["prefix"]
    if "bucket_owner" in value:
        out["BucketOwner"] = value["bucket_owner"]
    if "output_format" in value:
        out["OutputFormat"] = value["output_format"]
    return out


def deserialize_json(data: dict) -> S3LogDestination:
    out: S3LogDestination = {}  # type: ignore[typeddict-item]
    if data.get("BucketName") is not None:
        out["bucket_name"] = data["BucketName"]
    if data.get("Prefix") is not None:
        out["prefix"] = data["Prefix"]
    if data.get("BucketOwner") is not None:
        out["bucket_owner"] = data["BucketOwner"]
    if data.get("OutputFormat") is not None:
        out["output_format"] = data["OutputFormat"]
    return out
