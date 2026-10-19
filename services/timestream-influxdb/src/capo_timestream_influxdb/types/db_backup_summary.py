"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#DbBackupSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_timestream_influxdb.types.arn
    import capo_timestream_influxdb.types.date
    import capo_timestream_influxdb.types.db_backup_id
    import capo_timestream_influxdb.types.db_backup_name
    import capo_timestream_influxdb.types.db_backup_status
    import capo_timestream_influxdb.types.db_backup_type
    import capo_timestream_influxdb.types.db_resource_id
    import capo_timestream_influxdb.types.engine_type
    import capo_timestream_influxdb.types.kms_key_id
    import capo_timestream_influxdb.types.resource_deployment_type


class DbBackupSummary(TypedDict, closed=True):
    id: "capo_timestream_influxdb.types.db_backup_id.DbBackupId"
    """<p>Service-generated unique identifier of the backup.</p>"""
    name: NotRequired["capo_timestream_influxdb.types.db_backup_name.DbBackupName"]
    """<p>The customer-provided name of the backup.</p>"""
    arn: "capo_timestream_influxdb.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the backup.</p>"""
    status: NotRequired[
        "capo_timestream_influxdb.types.db_backup_status.DbBackupStatus"
    ]
    """<p>The status of the backup. Valid values are IN_PROGRESS, COMPLETED, FAILED, DELETING, and DELETED.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The time when the backup was created.</p>"""
    expires_after: NotRequired["capo_timestream_influxdb.types.date.Date"]
    """<p>The date after which the backup will be automatically deleted.</p>"""
    db_resource_id: NotRequired[
        "capo_timestream_influxdb.types.db_resource_id.DbResourceId"
    ]
    """<p>The identifier of the DB resource that the backup was created from.</p>"""
    type: NotRequired["capo_timestream_influxdb.types.db_backup_type.DbBackupType"]
    """<p>The type of backup. Valid values are HOURLY, DAILY, WEEKLY, MONTHLY, CUSTOM_SCHEDULE, ON_DEMAND, and CONTINUOUS.</p>"""
    engine_type: NotRequired["capo_timestream_influxdb.types.engine_type.EngineType"]
    """<p>The engine type of the resource that the backup was created from.</p>"""
    deployment_type: NotRequired[
        "capo_timestream_influxdb.types.resource_deployment_type.ResourceDeploymentType"
    ]
    """<p>The deployment type of the resource that the backup was created from.</p>"""
    kms_key_id: NotRequired["capo_timestream_influxdb.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Web Services KMS key ARN used for encryption of the resource at the time of backup.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DbBackupSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    out["arn"] = value["arn"]
    if "status" in value:
        import capo_timestream_influxdb.types.db_backup_status

        out["status"] = (
            capo_timestream_influxdb.types.db_backup_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "created_at" in value:
        import capo_timestream_influxdb._protocol.serialize

        out["createdAt"] = capo_timestream_influxdb._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "expires_after" in value:
        out["expiresAfter"] = value["expires_after"]
    if "db_resource_id" in value:
        out["dbResourceId"] = value["db_resource_id"]
    if "type" in value:
        import capo_timestream_influxdb.types.db_backup_type

        out["type"] = (
            capo_timestream_influxdb.types.db_backup_type.serialize_aws_json_1_0(
                value["type"]
            )
        )
    if "engine_type" in value:
        import capo_timestream_influxdb.types.engine_type

        out["engineType"] = (
            capo_timestream_influxdb.types.engine_type.serialize_aws_json_1_0(
                value["engine_type"]
            )
        )
    if "deployment_type" in value:
        import capo_timestream_influxdb.types.resource_deployment_type

        out["deploymentType"] = (
            capo_timestream_influxdb.types.resource_deployment_type.serialize_aws_json_1_0(
                value["deployment_type"]
            )
        )
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DbBackupSummary:
    out: DbBackupSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("status") is not None:
        import capo_timestream_influxdb.types.db_backup_status

        out["status"] = (
            capo_timestream_influxdb.types.db_backup_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("expiresAfter") is not None:
        out["expires_after"] = data["expiresAfter"]
    if data.get("dbResourceId") is not None:
        out["db_resource_id"] = data["dbResourceId"]
    if data.get("type") is not None:
        import capo_timestream_influxdb.types.db_backup_type

        out["type"] = (
            capo_timestream_influxdb.types.db_backup_type.deserialize_aws_json_1_0(
                data["type"]
            )
        )
    if data.get("engineType") is not None:
        import capo_timestream_influxdb.types.engine_type

        out["engine_type"] = (
            capo_timestream_influxdb.types.engine_type.deserialize_aws_json_1_0(
                data["engineType"]
            )
        )
    if data.get("deploymentType") is not None:
        import capo_timestream_influxdb.types.resource_deployment_type

        out["deployment_type"] = (
            capo_timestream_influxdb.types.resource_deployment_type.deserialize_aws_json_1_0(
                data["deploymentType"]
            )
        )
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    return out
