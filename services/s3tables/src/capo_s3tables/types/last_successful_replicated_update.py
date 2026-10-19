"""Generated from Smithy shape ``com.amazonaws.s3tables#LastSuccessfulReplicatedUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_s3tables.types.metadata_location


class LastSuccessfulReplicatedUpdate(TypedDict, closed=True):
    metadata_location: "capo_s3tables.types.metadata_location.MetadataLocation"
    """<p>The S3 location of the metadata that was successfully replicated.</p>"""
    timestamp: "datetime.datetime"
    """<p>The timestamp when the replication update completed successfully.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LastSuccessfulReplicatedUpdate) -> dict:
    out: dict = {}
    out["metadataLocation"] = value["metadata_location"]
    import capo_s3tables._protocol.serialize

    out["timestamp"] = capo_s3tables._protocol.serialize.fmt_date_time(
        value["timestamp"]
    )
    return out


def deserialize_json(data: dict) -> LastSuccessfulReplicatedUpdate:
    out: LastSuccessfulReplicatedUpdate = {}  # type: ignore[typeddict-item]
    if data.get("metadataLocation") is not None:
        out["metadata_location"] = data["metadataLocation"]
    else:
        out["metadata_location"] = ""
    if data.get("timestamp") is not None:
        import datetime

        out["timestamp"] = datetime.datetime.fromisoformat(
            data["timestamp"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["timestamp"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
