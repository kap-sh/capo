"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#CreateDbBackupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.db_backup_name
    import capo_timestream_influxdb.types.db_resource_id
    import capo_timestream_influxdb.types.request_tag_map
    import capo_timestream_influxdb.types.retention_days


class CreateDbBackupInput(TypedDict, closed=True):
    name: "capo_timestream_influxdb.types.db_backup_name.DbBackupName"
    """<p>The name of the backup. Must be unique within the account and region.</p>"""
    db_resource_id: "capo_timestream_influxdb.types.db_resource_id.DbResourceId"
    """<p>The id of the DB instance or DB cluster to back up.</p>"""
    retention_days: NotRequired[
        "capo_timestream_influxdb.types.retention_days.RetentionDays"
    ]
    """<p>The number of days to retain the backup. Valid values are 1 to 3650.</p>"""
    tags: NotRequired["capo_timestream_influxdb.types.request_tag_map.RequestTagMap"]
    """<p>A list of key-value pairs to associate with the backup.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateDbBackupInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["dbResourceId"] = value["db_resource_id"]
    if "retention_days" in value:
        out["retentionDays"] = value["retention_days"]
    if "tags" in value:
        import capo_timestream_influxdb.types.request_tag_map

        out["tags"] = (
            capo_timestream_influxdb.types.request_tag_map.serialize_aws_json_1_0(
                value["tags"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateDbBackupInput:
    out: CreateDbBackupInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("dbResourceId") is not None:
        out["db_resource_id"] = data["dbResourceId"]
    else:
        out["db_resource_id"] = ""
    if data.get("retentionDays") is not None:
        out["retention_days"] = data["retentionDays"]
    if data.get("tags") is not None:
        import capo_timestream_influxdb.types.request_tag_map

        out["tags"] = (
            capo_timestream_influxdb.types.request_tag_map.deserialize_aws_json_1_0(
                data["tags"]
            )
        )
    return out
