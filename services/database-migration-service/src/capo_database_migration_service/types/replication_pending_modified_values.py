"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ReplicationPendingModifiedValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.boolean_optional
    import capo_database_migration_service.types.integer_optional
    import capo_database_migration_service.types.replication_instance_class
    import capo_database_migration_service.types.string


class ReplicationPendingModifiedValues(TypedDict, closed=True):
    replication_instance_class: NotRequired[
        "capo_database_migration_service.types.replication_instance_class.ReplicationInstanceClass"
    ]
    """<p>The compute and memory capacity of the replication instance as defined for the specified replication instance class.</p> <p>For more information on the settings and capacities for the available replication instance classes, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html#CHAP_ReplicationInstance.InDepth"> Selecting the right DMS replication instance for your migration</a>. </p>"""
    allocated_storage: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The amount of storage (in gigabytes) that is allocated for the replication instance.</p>"""
    multi_az: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p> Specifies whether the replication instance is a Multi-AZ deployment. You can't set the <code>AvailabilityZone</code> parameter if the Multi-AZ parameter is set to <code>true</code>. </p>"""
    engine_version: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The engine version number of the replication instance.</p>"""
    network_type: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The type of IP address protocol used by a replication instance, such as IPv4 only or Dual-stack that supports both IPv4 and IPv6 addressing. IPv6 only is not yet supported.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationPendingModifiedValues) -> dict:
    out: dict = {}
    if "replication_instance_class" in value:
        out["ReplicationInstanceClass"] = value["replication_instance_class"]
    if "allocated_storage" in value:
        out["AllocatedStorage"] = value["allocated_storage"]
    if "multi_az" in value:
        out["MultiAZ"] = value["multi_az"]
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    if "network_type" in value:
        out["NetworkType"] = value["network_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReplicationPendingModifiedValues:
    out: ReplicationPendingModifiedValues = {}  # type: ignore[typeddict-item]
    if data.get("ReplicationInstanceClass") is not None:
        out["replication_instance_class"] = data["ReplicationInstanceClass"]
    if data.get("AllocatedStorage") is not None:
        out["allocated_storage"] = data["AllocatedStorage"]
    if data.get("MultiAZ") is not None:
        out["multi_az"] = data["MultiAZ"]
    if data.get("EngineVersion") is not None:
        out["engine_version"] = data["EngineVersion"]
    if data.get("NetworkType") is not None:
        out["network_type"] = data["NetworkType"]
    return out
