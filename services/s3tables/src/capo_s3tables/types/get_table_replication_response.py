"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTableReplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3tables.types.table_replication_configuration


class GetTableReplicationResponse(TypedDict, closed=True):
    version_token: "str"
    """<p>A version token that represents the current state of the table's replication configuration. Use this token when updating the configuration to ensure consistency.</p>"""
    configuration: "capo_s3tables.types.table_replication_configuration.TableReplicationConfiguration"
    """<p>The replication configuration for the table, including the IAM role and replication rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableReplicationResponse) -> dict:
    out: dict = {}
    out["versionToken"] = value["version_token"]
    import capo_s3tables.types.table_replication_configuration

    out["configuration"] = (
        capo_s3tables.types.table_replication_configuration.serialize_json(
            value["configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetTableReplicationResponse:
    out: GetTableReplicationResponse = {}  # type: ignore[typeddict-item]
    if data.get("versionToken") is not None:
        out["version_token"] = data["versionToken"]
    else:
        out["version_token"] = ""
    if data.get("configuration") is not None:
        import capo_s3tables.types.table_replication_configuration

        out["configuration"] = (
            capo_s3tables.types.table_replication_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError("GetTableReplicationResponse.configuration required")
    return out
