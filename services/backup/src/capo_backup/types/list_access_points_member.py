"""Generated from Smithy shape ``com.amazonaws.backup#ListAccessPointsMember``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_backup.types.access_point_arn
    import capo_backup.types.access_point_metadata_map
    import capo_backup.types.access_point_name
    import capo_backup.types.access_point_status
    import capo_backup.types.backup_vault_arn
    import capo_backup.types.backup_vault_name
    import capo_backup.types.recovery_point_arn
    import capo_backup.types.resource_arn


class ListAccessPointsMember(TypedDict, closed=True):
    access_point_arn: "capo_backup.types.access_point_arn.AccessPointArn"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the backup access point.</p>"""
    access_point_metadata: (
        "capo_backup.types.access_point_metadata_map.AccessPointMetadataMap"
    )
    """<p>Metadata for the backup access point. After the backup access point reaches the <code>AVAILABLE</code> status, this map contains <code>S3AccessPointArn</code> and <code>S3AccessPointAlias</code>, which you use with standard Amazon S3 read APIs to access the backup data. For continuous recovery points, this map also contains <code>AccessPointInTime</code> (in format <code>2021-11-27T03:30:27Z</code>). The access point provides access to the content present in the backup at that specific time.</p>"""
    backup_vault_arn: NotRequired["capo_backup.types.backup_vault_arn.BackupVaultArn"]
    """<p>The Amazon Resource Name (ARN) of the backup vault that contains the recovery point.</p>"""
    backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName"
    """<p>The name of the backup vault that contains the recovery point.</p>"""
    creation_time: "datetime.datetime"
    """<p>The date and time that the backup access point was created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationTime</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    name: "capo_backup.types.access_point_name.AccessPointName"
    """<p>The name of the backup access point.</p>"""
    recovery_point_arn: "capo_backup.types.recovery_point_arn.RecoveryPointArn"
    """<p>The Amazon Resource Name (ARN) of the recovery point that the backup access point provides access to.</p>"""
    resource_arn: "capo_backup.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource that was backed up, such as an Amazon S3 bucket.</p>"""
    resource_type: "str"
    """<p>The type of Amazon Web Services resource associated with the recovery point. For example, <code>S3</code> for Amazon Simple Storage Service.</p>"""
    status: "capo_backup.types.access_point_status.AccessPointStatus"
    """<p>The current status of the backup access point.</p>"""
    status_message: NotRequired["str"]
    """<p>A message that provides additional detail about the status of the backup access point, such as the reason a creation or deletion attempt failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccessPointsMember) -> dict:
    out: dict = {}
    out["AccessPointArn"] = value["access_point_arn"]
    import capo_backup.types.access_point_metadata_map

    out["AccessPointMetadata"] = (
        capo_backup.types.access_point_metadata_map.serialize_json(
            value["access_point_metadata"]
        )
    )
    if "backup_vault_arn" in value:
        out["BackupVaultArn"] = value["backup_vault_arn"]
    out["BackupVaultName"] = value["backup_vault_name"]
    import capo_backup.types._prelude.timestamp

    out["CreationTime"] = capo_backup.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    out["Name"] = value["name"]
    out["RecoveryPointArn"] = value["recovery_point_arn"]
    out["ResourceArn"] = value["resource_arn"]
    out["ResourceType"] = value["resource_type"]
    import capo_backup.types.access_point_status

    out["Status"] = capo_backup.types.access_point_status.serialize_json(
        value["status"]
    )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_json(data: dict) -> ListAccessPointsMember:
    out: ListAccessPointsMember = {}  # type: ignore[typeddict-item]
    if data.get("AccessPointArn") is not None:
        out["access_point_arn"] = data["AccessPointArn"]
    else:
        out["access_point_arn"] = ""
    if data.get("AccessPointMetadata") is not None:
        import capo_backup.types.access_point_metadata_map

        out["access_point_metadata"] = (
            capo_backup.types.access_point_metadata_map.deserialize_json(
                data["AccessPointMetadata"]
            )
        )
    else:
        out["access_point_metadata"] = {}
    if data.get("BackupVaultArn") is not None:
        out["backup_vault_arn"] = data["BackupVaultArn"]
    if data.get("BackupVaultName") is not None:
        out["backup_vault_name"] = data["BackupVaultName"]
    else:
        out["backup_vault_name"] = ""
    if data.get("CreationTime") is not None:
        import capo_backup.types._prelude.timestamp

        out["creation_time"] = capo_backup.types._prelude.timestamp.deserialize_json(
            data["CreationTime"]
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("RecoveryPointArn") is not None:
        out["recovery_point_arn"] = data["RecoveryPointArn"]
    else:
        out["recovery_point_arn"] = ""
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    else:
        out["resource_type"] = ""
    if data.get("Status") is not None:
        import capo_backup.types.access_point_status

        out["status"] = capo_backup.types.access_point_status.deserialize_json(
            data["Status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_backup.types.access_point_status.AccessPointStatus", ""
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    return out


def redact_sensitive(value: ListAccessPointsMember) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "access_point_metadata" in value:
        out["access_point_metadata"] = "*** Sensitive Data Redacted ***"
    return out
