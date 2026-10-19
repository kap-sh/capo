"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#RebootReplicationInstanceMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.boolean_optional
    import capo_database_migration_service.types.string


class RebootReplicationInstanceMessage(TypedDict, closed=True):
    replication_instance_arn: "capo_database_migration_service.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the replication instance.</p>"""
    force_failover: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>If this parameter is <code>true</code>, the reboot is conducted through a Multi-AZ failover. If the instance isn't configured for Multi-AZ, then you can't specify <code>true</code>. ( <code>--force-planned-failover</code> and <code>--force-failover</code> can't both be set to <code>true</code>.)</p>"""
    force_planned_failover: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>If this parameter is <code>true</code>, the reboot is conducted through a planned Multi-AZ failover where resources are released and cleaned up prior to conducting the failover. If the instance isn''t configured for Multi-AZ, then you can't specify <code>true</code>. ( <code>--force-planned-failover</code> and <code>--force-failover</code> can't both be set to <code>true</code>.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RebootReplicationInstanceMessage) -> dict:
    out: dict = {}
    out["ReplicationInstanceArn"] = value["replication_instance_arn"]
    if "force_failover" in value:
        out["ForceFailover"] = value["force_failover"]
    if "force_planned_failover" in value:
        out["ForcePlannedFailover"] = value["force_planned_failover"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RebootReplicationInstanceMessage:
    out: RebootReplicationInstanceMessage = {}  # type: ignore[typeddict-item]
    if data.get("ReplicationInstanceArn") is not None:
        out["replication_instance_arn"] = data["ReplicationInstanceArn"]
    else:
        out["replication_instance_arn"] = ""
    if data.get("ForceFailover") is not None:
        out["force_failover"] = data["ForceFailover"]
    if data.get("ForcePlannedFailover") is not None:
        out["force_planned_failover"] = data["ForcePlannedFailover"]
    return out
