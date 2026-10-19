"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTableReplicationStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.replication_destination_statuses
    import capo_s3tables.types.table_arn


class GetTableReplicationStatusResponse(TypedDict, closed=True):
    source_table_arn: "capo_s3tables.types.table_arn.TableARN"
    """<p>The Amazon Resource Name (ARN) of the source table being replicated.</p>"""
    destinations: "capo_s3tables.types.replication_destination_statuses.ReplicationDestinationStatuses"
    """<p>An array of status information for each replication destination, including the current state, last successful update, and any error messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableReplicationStatusResponse) -> dict:
    out: dict = {}
    out["sourceTableArn"] = value["source_table_arn"]
    import capo_s3tables.types.replication_destination_statuses

    out["destinations"] = (
        capo_s3tables.types.replication_destination_statuses.serialize_json(
            value["destinations"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetTableReplicationStatusResponse:
    out: GetTableReplicationStatusResponse = {}  # type: ignore[typeddict-item]
    if data.get("sourceTableArn") is not None:
        out["source_table_arn"] = data["sourceTableArn"]
    else:
        out["source_table_arn"] = ""
    if data.get("destinations") is not None:
        import capo_s3tables.types.replication_destination_statuses

        out["destinations"] = (
            capo_s3tables.types.replication_destination_statuses.deserialize_json(
                data["destinations"]
            )
        )
    else:
        out["destinations"] = []
    return out
