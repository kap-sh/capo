"""Generated from Smithy shape ``com.amazonaws.s3tables#TableBucketLoggingStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.logging_enabled


class TableBucketLoggingStatus(TypedDict, closed=True):
    logging_enabled: NotRequired["capo_s3tables.types.logging_enabled.LoggingEnabled"]
    """<p>Where logs for the table bucket are delivered and how the log objects are named. Must be populated to enable logging.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableBucketLoggingStatus) -> dict:
    out: dict = {}
    if "logging_enabled" in value:
        import capo_s3tables.types.logging_enabled

        out["loggingEnabled"] = capo_s3tables.types.logging_enabled.serialize_json(
            value["logging_enabled"]
        )
    return out


def deserialize_json(data: dict) -> TableBucketLoggingStatus:
    out: TableBucketLoggingStatus = {}  # type: ignore[typeddict-item]
    if data.get("loggingEnabled") is not None:
        import capo_s3tables.types.logging_enabled

        out["logging_enabled"] = capo_s3tables.types.logging_enabled.deserialize_json(
            data["loggingEnabled"]
        )
    return out
