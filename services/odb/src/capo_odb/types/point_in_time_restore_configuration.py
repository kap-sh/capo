"""Generated from Smithy shape ``com.amazonaws.odb#PointInTimeRestoreConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_odb.types.clone_type
    import capo_odb.types.integer_list
    import capo_odb.types.resource_id_or_arn


class PointInTimeRestoreConfiguration(TypedDict, closed=True):
    source_autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the source Autonomous Database to restore from.</p>"""
    clone_type: "capo_odb.types.clone_type.CloneType"
    """<p>The type of clone to create from the point-in-time restore.</p>"""
    timestamp: NotRequired["datetime.datetime"]
    """<p>The date and time to which to restore the Autonomous Database.</p>"""
    use_latest_available_backup_timestamp: NotRequired["bool"]
    """<p>Indicates whether to use the latest available backup timestamp for the restore.</p>"""
    clone_table_space_list: NotRequired["capo_odb.types.integer_list.IntegerList"]
    """<p>The list of tablespace identifiers to clone from the point-in-time restore.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PointInTimeRestoreConfiguration) -> dict:
    out: dict = {}
    out["sourceAutonomousDatabaseId"] = value["source_autonomous_database_id"]
    import capo_odb.types.clone_type

    out["cloneType"] = capo_odb.types.clone_type.serialize_aws_json_1_0(
        value["clone_type"]
    )
    if "timestamp" in value:
        import capo_odb._protocol.serialize

        out["timestamp"] = capo_odb._protocol.serialize.fmt_date_time(
            value["timestamp"]
        )
    if "use_latest_available_backup_timestamp" in value:
        out["useLatestAvailableBackupTimestamp"] = value[
            "use_latest_available_backup_timestamp"
        ]
    if "clone_table_space_list" in value:
        import capo_odb.types.integer_list

        out["cloneTableSpaceList"] = capo_odb.types.integer_list.serialize_aws_json_1_0(
            value["clone_table_space_list"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> PointInTimeRestoreConfiguration:
    out: PointInTimeRestoreConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("sourceAutonomousDatabaseId") is not None:
        out["source_autonomous_database_id"] = data["sourceAutonomousDatabaseId"]
    else:
        out["source_autonomous_database_id"] = ""
    if data.get("cloneType") is not None:
        import capo_odb.types.clone_type

        out["clone_type"] = capo_odb.types.clone_type.deserialize_aws_json_1_0(
            data["cloneType"]
        )
    else:
        import typing

        out["clone_type"] = typing.cast("capo_odb.types.clone_type.CloneType", "")
    if data.get("timestamp") is not None:
        import datetime

        out["timestamp"] = datetime.datetime.fromisoformat(
            data["timestamp"].replace("Z", "+00:00")
        )
    if data.get("useLatestAvailableBackupTimestamp") is not None:
        out["use_latest_available_backup_timestamp"] = data[
            "useLatestAvailableBackupTimestamp"
        ]
    if data.get("cloneTableSpaceList") is not None:
        import capo_odb.types.integer_list

        out["clone_table_space_list"] = (
            capo_odb.types.integer_list.deserialize_aws_json_1_0(
                data["cloneTableSpaceList"]
            )
        )
    return out
