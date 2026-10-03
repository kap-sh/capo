"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ErrorReportLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.bucket
    import capo_iotsitewise.types.string


class ErrorReportLocation(TypedDict, closed=True):
    bucket: "capo_iotsitewise.types.bucket.Bucket"
    """<p>The name of the Amazon S3 bucket to which errors associated with the bulk import job are sent.</p>"""
    prefix: "capo_iotsitewise.types.string.String"
    """<p>Amazon S3 uses the prefix as a folder name to organize data in the bucket. Each Amazon S3 object has a key that is its unique identifier in the bucket. Each object in a bucket has exactly one key. The prefix must end with a forward slash (/). For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html">Organizing objects using prefixes</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorReportLocation) -> dict:
    out: dict = {}
    out["bucket"] = value["bucket"]
    out["prefix"] = value["prefix"]
    return out


def deserialize_json(data: dict) -> ErrorReportLocation:
    out: ErrorReportLocation = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    else:
        raise DeserializationError("ErrorReportLocation.bucket required")
    if data.get("prefix") is not None:
        out["prefix"] = data["prefix"]
    else:
        raise DeserializationError("ErrorReportLocation.prefix required")
    return out
