"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTableBucketLoggingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3tables.types.table_bucket_logging_status


class GetTableBucketLoggingResponse(TypedDict, closed=True):
    table_bucket_logging_status: (
        "capo_s3tables.types.table_bucket_logging_status.TableBucketLoggingStatus"
    )
    """<p>The logging status of the table bucket. If logging is disabled, <code>loggingEnabled</code> is absent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableBucketLoggingResponse) -> dict:
    out: dict = {}
    import capo_s3tables.types.table_bucket_logging_status

    out["tableBucketLoggingStatus"] = (
        capo_s3tables.types.table_bucket_logging_status.serialize_json(
            value["table_bucket_logging_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetTableBucketLoggingResponse:
    out: GetTableBucketLoggingResponse = {}  # type: ignore[typeddict-item]
    if data.get("tableBucketLoggingStatus") is not None:
        import capo_s3tables.types.table_bucket_logging_status

        out["table_bucket_logging_status"] = (
            capo_s3tables.types.table_bucket_logging_status.deserialize_json(
                data["tableBucketLoggingStatus"]
            )
        )
    else:
        raise DeserializationError(
            "GetTableBucketLoggingResponse.table_bucket_logging_status required"
        )
    return out
