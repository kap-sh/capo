"""Generated from Smithy shape ``com.amazonaws.dynamodb#BackupDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.backup_arn
    import capo_dynamodb.types.backup_creation_date_time
    import capo_dynamodb.types.backup_name
    import capo_dynamodb.types.backup_size_bytes
    import capo_dynamodb.types.backup_status
    import capo_dynamodb.types.backup_type
    import capo_dynamodb.types.date


class BackupDetails(TypedDict, closed=True):
    backup_arn: "capo_dynamodb.types.backup_arn.BackupArn"
    """<p>ARN associated with the backup.</p>"""
    backup_name: "capo_dynamodb.types.backup_name.BackupName"
    """<p>Name of the requested backup.</p>"""
    backup_size_bytes: NotRequired[
        "capo_dynamodb.types.backup_size_bytes.BackupSizeBytes"
    ]
    """<p>Size of the backup in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.</p>"""
    backup_status: "capo_dynamodb.types.backup_status.BackupStatus"
    """<p>Backup can be in one of the following states: CREATING, ACTIVE, DELETED. </p>"""
    backup_type: "capo_dynamodb.types.backup_type.BackupType"
    """<p>BackupType:</p> <ul> <li> <p> <code>USER</code> - You create and manage these using the on-demand backup feature.</p> </li> <li> <p> <code>SYSTEM</code> - If you delete a table with point-in-time recovery enabled, a <code>SYSTEM</code> backup is automatically created and is retained for 35 days (at no additional cost). System backups allow you to restore the deleted table to the state it was in just before the point of deletion. </p> </li> <li> <p> <code>AWS_BACKUP</code> - On-demand backup created by you from Backup service.</p> </li> </ul>"""
    backup_creation_date_time: (
        "capo_dynamodb.types.backup_creation_date_time.BackupCreationDateTime"
    )
    """<p>Time at which the backup was created. This is the request time of the backup. </p>"""
    backup_expiry_date_time: NotRequired["capo_dynamodb.types.date.Date"]
    """<p>Time at which the automatic on-demand backup created by DynamoDB will expire. This <code>SYSTEM</code> on-demand backup expires automatically 35 days after its creation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BackupDetails) -> dict:
    out: dict = {}
    out["BackupArn"] = value["backup_arn"]
    out["BackupName"] = value["backup_name"]
    if "backup_size_bytes" in value:
        out["BackupSizeBytes"] = value["backup_size_bytes"]
    import capo_dynamodb.types.backup_status

    out["BackupStatus"] = capo_dynamodb.types.backup_status.serialize_aws_json_1_0(
        value["backup_status"]
    )
    import capo_dynamodb.types.backup_type

    out["BackupType"] = capo_dynamodb.types.backup_type.serialize_aws_json_1_0(
        value["backup_type"]
    )
    import capo_dynamodb.types.backup_creation_date_time

    out["BackupCreationDateTime"] = (
        capo_dynamodb.types.backup_creation_date_time.serialize_aws_json_1_0(
            value["backup_creation_date_time"]
        )
    )
    if "backup_expiry_date_time" in value:
        import capo_dynamodb.types.date

        out["BackupExpiryDateTime"] = capo_dynamodb.types.date.serialize_aws_json_1_0(
            value["backup_expiry_date_time"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BackupDetails:
    out: BackupDetails = {}  # type: ignore[typeddict-item]
    if data.get("BackupArn") is not None:
        out["backup_arn"] = data["BackupArn"]
    else:
        out["backup_arn"] = ""
    if data.get("BackupName") is not None:
        out["backup_name"] = data["BackupName"]
    else:
        out["backup_name"] = ""
    if data.get("BackupSizeBytes") is not None:
        out["backup_size_bytes"] = data["BackupSizeBytes"]
    if data.get("BackupStatus") is not None:
        import capo_dynamodb.types.backup_status

        out["backup_status"] = (
            capo_dynamodb.types.backup_status.deserialize_aws_json_1_0(
                data["BackupStatus"]
            )
        )
    else:
        import typing

        out["backup_status"] = typing.cast(
            "capo_dynamodb.types.backup_status.BackupStatus", ""
        )
    if data.get("BackupType") is not None:
        import capo_dynamodb.types.backup_type

        out["backup_type"] = capo_dynamodb.types.backup_type.deserialize_aws_json_1_0(
            data["BackupType"]
        )
    else:
        import typing

        out["backup_type"] = typing.cast(
            "capo_dynamodb.types.backup_type.BackupType", ""
        )
    if data.get("BackupCreationDateTime") is not None:
        import capo_dynamodb.types.backup_creation_date_time

        out["backup_creation_date_time"] = (
            capo_dynamodb.types.backup_creation_date_time.deserialize_aws_json_1_0(
                data["BackupCreationDateTime"]
            )
        )
    else:
        import datetime

        out["backup_creation_date_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("BackupExpiryDateTime") is not None:
        import capo_dynamodb.types.date

        out["backup_expiry_date_time"] = (
            capo_dynamodb.types.date.deserialize_aws_json_1_0(
                data["BackupExpiryDateTime"]
            )
        )
    return out
