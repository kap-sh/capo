"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#Backup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.backup_arn
    import capo_cloudhsm_v2.types.backup_id
    import capo_cloudhsm_v2.types.backup_state
    import capo_cloudhsm_v2.types.boolean
    import capo_cloudhsm_v2.types.cluster_id
    import capo_cloudhsm_v2.types.cluster_mode
    import capo_cloudhsm_v2.types.hsm_type
    import capo_cloudhsm_v2.types.region
    import capo_cloudhsm_v2.types.tag_list
    import capo_cloudhsm_v2.types.timestamp


class Backup(TypedDict, closed=True):
    backup_id: "capo_cloudhsm_v2.types.backup_id.BackupId"
    """<p>The identifier (ID) of the backup.</p>"""
    backup_arn: NotRequired["capo_cloudhsm_v2.types.backup_arn.BackupArn"]
    """<p>The Amazon Resource Name (ARN) of the backup.</p>"""
    backup_state: NotRequired["capo_cloudhsm_v2.types.backup_state.BackupState"]
    """<p>The state of the backup.</p>"""
    cluster_id: NotRequired["capo_cloudhsm_v2.types.cluster_id.ClusterId"]
    """<p>The identifier (ID) of the cluster that was backed up.</p>"""
    create_timestamp: NotRequired["capo_cloudhsm_v2.types.timestamp.Timestamp"]
    """<p>The date and time when the backup was created.</p>"""
    copy_timestamp: NotRequired["capo_cloudhsm_v2.types.timestamp.Timestamp"]
    """<p>The date and time when the backup was copied from a source backup.</p>"""
    never_expires: NotRequired["capo_cloudhsm_v2.types.boolean.Boolean"]
    """<p>Specifies whether the service should exempt a backup from the retention policy for the cluster. <code>True</code> exempts a backup from the retention policy. <code>False</code> means the service applies the backup retention policy defined at the cluster.</p>"""
    source_region: NotRequired["capo_cloudhsm_v2.types.region.Region"]
    """<p>The AWS Region that contains the source backup from which the new backup was copied.</p>"""
    source_backup: NotRequired["capo_cloudhsm_v2.types.backup_id.BackupId"]
    """<p>The identifier (ID) of the source backup from which the new backup was copied.</p>"""
    source_cluster: NotRequired["capo_cloudhsm_v2.types.cluster_id.ClusterId"]
    """<p>The identifier (ID) of the cluster containing the source backup from which the new backup was copied.</p>"""
    delete_timestamp: NotRequired["capo_cloudhsm_v2.types.timestamp.Timestamp"]
    """<p>The date and time when the backup will be permanently deleted.</p>"""
    tag_list: NotRequired["capo_cloudhsm_v2.types.tag_list.TagList"]
    """<p>The list of tags for the backup.</p>"""
    hsm_type: NotRequired["capo_cloudhsm_v2.types.hsm_type.HsmType"]
    """<p>The HSM type used to create the backup.</p>"""
    mode: NotRequired["capo_cloudhsm_v2.types.cluster_mode.ClusterMode"]
    """<p>The mode of the cluster that was backed up.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Backup) -> dict:
    out: dict = {}
    out["BackupId"] = value["backup_id"]
    if "backup_arn" in value:
        out["BackupArn"] = value["backup_arn"]
    if "backup_state" in value:
        import capo_cloudhsm_v2.types.backup_state

        out["BackupState"] = capo_cloudhsm_v2.types.backup_state.serialize_aws_json_1_1(
            value["backup_state"]
        )
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    if "create_timestamp" in value:
        import capo_cloudhsm_v2.types.timestamp

        out["CreateTimestamp"] = (
            capo_cloudhsm_v2.types.timestamp.serialize_aws_json_1_1(
                value["create_timestamp"]
            )
        )
    if "copy_timestamp" in value:
        import capo_cloudhsm_v2.types.timestamp

        out["CopyTimestamp"] = capo_cloudhsm_v2.types.timestamp.serialize_aws_json_1_1(
            value["copy_timestamp"]
        )
    if "never_expires" in value:
        out["NeverExpires"] = value["never_expires"]
    if "source_region" in value:
        out["SourceRegion"] = value["source_region"]
    if "source_backup" in value:
        out["SourceBackup"] = value["source_backup"]
    if "source_cluster" in value:
        out["SourceCluster"] = value["source_cluster"]
    if "delete_timestamp" in value:
        import capo_cloudhsm_v2.types.timestamp

        out["DeleteTimestamp"] = (
            capo_cloudhsm_v2.types.timestamp.serialize_aws_json_1_1(
                value["delete_timestamp"]
            )
        )
    if "tag_list" in value:
        import capo_cloudhsm_v2.types.tag_list

        out["TagList"] = capo_cloudhsm_v2.types.tag_list.serialize_aws_json_1_1(
            value["tag_list"]
        )
    if "hsm_type" in value:
        out["HsmType"] = value["hsm_type"]
    if "mode" in value:
        import capo_cloudhsm_v2.types.cluster_mode

        out["Mode"] = capo_cloudhsm_v2.types.cluster_mode.serialize_aws_json_1_1(
            value["mode"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Backup:
    out: Backup = {}  # type: ignore[typeddict-item]
    if data.get("BackupId") is not None:
        out["backup_id"] = data["BackupId"]
    else:
        out["backup_id"] = ""
    if data.get("BackupArn") is not None:
        out["backup_arn"] = data["BackupArn"]
    if data.get("BackupState") is not None:
        import capo_cloudhsm_v2.types.backup_state

        out["backup_state"] = (
            capo_cloudhsm_v2.types.backup_state.deserialize_aws_json_1_1(
                data["BackupState"]
            )
        )
    if data.get("ClusterId") is not None:
        out["cluster_id"] = data["ClusterId"]
    if data.get("CreateTimestamp") is not None:
        import capo_cloudhsm_v2.types.timestamp

        out["create_timestamp"] = (
            capo_cloudhsm_v2.types.timestamp.deserialize_aws_json_1_1(
                data["CreateTimestamp"]
            )
        )
    if data.get("CopyTimestamp") is not None:
        import capo_cloudhsm_v2.types.timestamp

        out["copy_timestamp"] = (
            capo_cloudhsm_v2.types.timestamp.deserialize_aws_json_1_1(
                data["CopyTimestamp"]
            )
        )
    if data.get("NeverExpires") is not None:
        out["never_expires"] = data["NeverExpires"]
    if data.get("SourceRegion") is not None:
        out["source_region"] = data["SourceRegion"]
    if data.get("SourceBackup") is not None:
        out["source_backup"] = data["SourceBackup"]
    if data.get("SourceCluster") is not None:
        out["source_cluster"] = data["SourceCluster"]
    if data.get("DeleteTimestamp") is not None:
        import capo_cloudhsm_v2.types.timestamp

        out["delete_timestamp"] = (
            capo_cloudhsm_v2.types.timestamp.deserialize_aws_json_1_1(
                data["DeleteTimestamp"]
            )
        )
    if data.get("TagList") is not None:
        import capo_cloudhsm_v2.types.tag_list

        out["tag_list"] = capo_cloudhsm_v2.types.tag_list.deserialize_aws_json_1_1(
            data["TagList"]
        )
    if data.get("HsmType") is not None:
        out["hsm_type"] = data["HsmType"]
    if data.get("Mode") is not None:
        import capo_cloudhsm_v2.types.cluster_mode

        out["mode"] = capo_cloudhsm_v2.types.cluster_mode.deserialize_aws_json_1_1(
            data["Mode"]
        )
    return out
