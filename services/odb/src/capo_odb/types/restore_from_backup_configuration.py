"""Generated from Smithy shape ``com.amazonaws.odb#RestoreFromBackupConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.clone_type
    import capo_odb.types.integer_list
    import capo_odb.types.resource_id_or_arn


class RestoreFromBackupConfiguration(TypedDict, closed=True):
    autonomous_database_backup_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the Autonomous Database backup to restore from.</p>"""
    clone_type: "capo_odb.types.clone_type.CloneType"
    """<p>The type of clone to create from the backup.</p>"""
    clone_table_space_list: NotRequired["capo_odb.types.integer_list.IntegerList"]
    """<p>The list of tablespace identifiers to clone from the backup.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RestoreFromBackupConfiguration) -> dict:
    out: dict = {}
    out["autonomousDatabaseBackupId"] = value["autonomous_database_backup_id"]
    import capo_odb.types.clone_type

    out["cloneType"] = capo_odb.types.clone_type.serialize_aws_json_1_0(
        value["clone_type"]
    )
    if "clone_table_space_list" in value:
        import capo_odb.types.integer_list

        out["cloneTableSpaceList"] = capo_odb.types.integer_list.serialize_aws_json_1_0(
            value["clone_table_space_list"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RestoreFromBackupConfiguration:
    out: RestoreFromBackupConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("autonomousDatabaseBackupId") is not None:
        out["autonomous_database_backup_id"] = data["autonomousDatabaseBackupId"]
    else:
        out["autonomous_database_backup_id"] = ""
    if data.get("cloneType") is not None:
        import capo_odb.types.clone_type

        out["clone_type"] = capo_odb.types.clone_type.deserialize_aws_json_1_0(
            data["cloneType"]
        )
    else:
        import typing

        out["clone_type"] = typing.cast("capo_odb.types.clone_type.CloneType", "")
    if data.get("cloneTableSpaceList") is not None:
        import capo_odb.types.integer_list

        out["clone_table_space_list"] = (
            capo_odb.types.integer_list.deserialize_aws_json_1_0(
                data["cloneTableSpaceList"]
            )
        )
    return out
