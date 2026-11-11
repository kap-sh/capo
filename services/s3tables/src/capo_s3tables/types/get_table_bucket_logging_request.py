"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTableBucketLoggingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.table_bucket_arn


class GetTableBucketLoggingRequest(TypedDict, closed=True):
    table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the table bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableBucketLoggingRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTableBucketLoggingRequest:
    out: GetTableBucketLoggingRequest = {}  # type: ignore[typeddict-item]
    return out
