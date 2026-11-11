"""Generated from Smithy shape ``com.amazonaws.s3tables#PutTableBucketLoggingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3tables.types.table_bucket_arn
    import capo_s3tables.types.table_bucket_logging_status


class PutTableBucketLoggingRequest(TypedDict, closed=True):
    table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the table bucket.</p>"""
    table_bucket_logging_status: (
        "capo_s3tables.types.table_bucket_logging_status.TableBucketLoggingStatus"
    )
    """<p>The logging status to apply to the table bucket. To disable logging, specify an empty <code>tableBucketLoggingStatus</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutTableBucketLoggingRequest) -> dict:
    out: dict = {}
    import capo_s3tables.types.table_bucket_logging_status

    out["tableBucketLoggingStatus"] = (
        capo_s3tables.types.table_bucket_logging_status.serialize_json(
            value["table_bucket_logging_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutTableBucketLoggingRequest:
    out: PutTableBucketLoggingRequest = {}  # type: ignore[typeddict-item]
    if data.get("tableBucketLoggingStatus") is not None:
        import capo_s3tables.types.table_bucket_logging_status

        out["table_bucket_logging_status"] = (
            capo_s3tables.types.table_bucket_logging_status.deserialize_json(
                data["tableBucketLoggingStatus"]
            )
        )
    else:
        raise DeserializationError(
            "PutTableBucketLoggingRequest.table_bucket_logging_status required"
        )
    return out
