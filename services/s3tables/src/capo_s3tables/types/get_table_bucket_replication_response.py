"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTableBucketReplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3tables.types.table_bucket_replication_configuration
    import capo_s3tables.types.version_token


class GetTableBucketReplicationResponse(TypedDict, closed=True):
    version_token: "capo_s3tables.types.version_token.VersionToken"
    """<p>A version token that represents the current state of the replication configuration. Use this token when updating the configuration to ensure consistency.</p>"""
    configuration: "capo_s3tables.types.table_bucket_replication_configuration.TableBucketReplicationConfiguration"
    """<p>The replication configuration for the table bucket, including the IAM role and replication rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableBucketReplicationResponse) -> dict:
    out: dict = {}
    out["versionToken"] = value["version_token"]
    import capo_s3tables.types.table_bucket_replication_configuration

    out["configuration"] = (
        capo_s3tables.types.table_bucket_replication_configuration.serialize_json(
            value["configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetTableBucketReplicationResponse:
    out: GetTableBucketReplicationResponse = {}  # type: ignore[typeddict-item]
    if data.get("versionToken") is not None:
        out["version_token"] = data["versionToken"]
    else:
        out["version_token"] = ""
    if data.get("configuration") is not None:
        import capo_s3tables.types.table_bucket_replication_configuration

        out["configuration"] = (
            capo_s3tables.types.table_bucket_replication_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError(
            "GetTableBucketReplicationResponse.configuration required"
        )
    return out
