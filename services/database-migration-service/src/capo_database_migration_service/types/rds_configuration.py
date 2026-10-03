"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#RdsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.double_optional
    import capo_database_migration_service.types.integer_optional
    import capo_database_migration_service.types.string


class RdsConfiguration(TypedDict, closed=True):
    engine_edition: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>Describes the recommended target Amazon RDS engine edition.</p>"""
    instance_type: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>Describes the recommended target Amazon RDS instance type.</p>"""
    instance_vcpu: NotRequired[
        "capo_database_migration_service.types.double_optional.DoubleOptional"
    ]
    """<p>Describes the number of virtual CPUs (vCPU) on the recommended Amazon RDS DB instance that meets your requirements.</p>"""
    instance_memory: NotRequired[
        "capo_database_migration_service.types.double_optional.DoubleOptional"
    ]
    """<p>Describes the memory on the recommended Amazon RDS DB instance that meets your requirements.</p>"""
    storage_type: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>Describes the storage type of the recommended Amazon RDS DB instance that meets your requirements.</p> <p>Amazon RDS provides three storage types: General Purpose SSD (also known as gp2 and gp3), Provisioned IOPS SSD (also known as io1), and magnetic (also known as standard).</p>"""
    storage_size: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>Describes the storage size of the recommended Amazon RDS DB instance that meets your requirements.</p>"""
    storage_iops: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>Describes the number of I/O operations completed each second (IOPS) on the recommended Amazon RDS DB instance that meets your requirements.</p>"""
    deployment_option: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>Describes the deployment option for the recommended Amazon RDS DB instance. The deployment options include Multi-AZ and Single-AZ deployments. Valid values include <code>"MULTI_AZ"</code> and <code>"SINGLE_AZ"</code>.</p>"""
    engine_version: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>Describes the recommended target Amazon RDS engine version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RdsConfiguration) -> dict:
    out: dict = {}
    if "engine_edition" in value:
        out["EngineEdition"] = value["engine_edition"]
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    if "instance_vcpu" in value:
        out["InstanceVcpu"] = (
            "NaN"
            if value["instance_vcpu"] != value["instance_vcpu"]
            else "Infinity"
            if value["instance_vcpu"] == float("inf")
            else "-Infinity"
            if value["instance_vcpu"] == float("-inf")
            else value["instance_vcpu"]
        )
    if "instance_memory" in value:
        out["InstanceMemory"] = (
            "NaN"
            if value["instance_memory"] != value["instance_memory"]
            else "Infinity"
            if value["instance_memory"] == float("inf")
            else "-Infinity"
            if value["instance_memory"] == float("-inf")
            else value["instance_memory"]
        )
    if "storage_type" in value:
        out["StorageType"] = value["storage_type"]
    if "storage_size" in value:
        out["StorageSize"] = value["storage_size"]
    if "storage_iops" in value:
        out["StorageIops"] = value["storage_iops"]
    if "deployment_option" in value:
        out["DeploymentOption"] = value["deployment_option"]
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RdsConfiguration:
    out: RdsConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("EngineEdition") is not None:
        out["engine_edition"] = data["EngineEdition"]
    if data.get("InstanceType") is not None:
        out["instance_type"] = data["InstanceType"]
    if data.get("InstanceVcpu") is not None:
        out["instance_vcpu"] = float(data["InstanceVcpu"])
    if data.get("InstanceMemory") is not None:
        out["instance_memory"] = float(data["InstanceMemory"])
    if data.get("StorageType") is not None:
        out["storage_type"] = data["StorageType"]
    if data.get("StorageSize") is not None:
        out["storage_size"] = data["StorageSize"]
    if data.get("StorageIops") is not None:
        out["storage_iops"] = data["StorageIops"]
    if data.get("DeploymentOption") is not None:
        out["deployment_option"] = data["DeploymentOption"]
    if data.get("EngineVersion") is not None:
        out["engine_version"] = data["EngineVersion"]
    return out
