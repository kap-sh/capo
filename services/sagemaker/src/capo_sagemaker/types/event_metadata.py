"""Generated from Smithy shape ``com.amazonaws.sagemaker#EventMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_sagemaker.errors import DeserializationError, SerializationError
from capo_sagemaker.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_metadata
    import capo_sagemaker.types.database_configuration_metadata
    import capo_sagemaker.types.instance_group_metadata
    import capo_sagemaker.types.instance_group_scaling_metadata
    import capo_sagemaker.types.instance_metadata
    import capo_sagemaker.types.slurm_health_metadata


class EventMetadataClusterMember(TypedDict, closed=True):
    Cluster: "capo_sagemaker.types.cluster_metadata.ClusterMetadata"


class EventMetadataInstanceGroupMember(TypedDict, closed=True):
    InstanceGroup: "capo_sagemaker.types.instance_group_metadata.InstanceGroupMetadata"


class EventMetadataInstanceGroupScalingMember(TypedDict, closed=True):
    InstanceGroupScaling: "capo_sagemaker.types.instance_group_scaling_metadata.InstanceGroupScalingMetadata"


class EventMetadataInstanceMember(TypedDict, closed=True):
    Instance: "capo_sagemaker.types.instance_metadata.InstanceMetadata"


class EventMetadataDatabaseConfigurationMember(TypedDict, closed=True):
    DatabaseConfiguration: "capo_sagemaker.types.database_configuration_metadata.DatabaseConfigurationMetadata"


class EventMetadataSlurmHealthMember(TypedDict, closed=True):
    SlurmHealth: "capo_sagemaker.types.slurm_health_metadata.SlurmHealthMetadata"


EventMetadata: TypeAlias = (
    EventMetadataClusterMember
    | EventMetadataInstanceGroupMember
    | EventMetadataInstanceGroupScalingMember
    | EventMetadataInstanceMember
    | EventMetadataDatabaseConfigurationMember
    | EventMetadataSlurmHealthMember
    | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventMetadata) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"EventMetadata: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Cluster" in value:
        import capo_sagemaker.types.cluster_metadata

        return {
            "Cluster": capo_sagemaker.types.cluster_metadata.serialize_aws_json_1_1(
                value["Cluster"]
            )
        }
    elif "InstanceGroup" in value:
        import capo_sagemaker.types.instance_group_metadata

        return {
            "InstanceGroup": capo_sagemaker.types.instance_group_metadata.serialize_aws_json_1_1(
                value["InstanceGroup"]
            )
        }
    elif "InstanceGroupScaling" in value:
        import capo_sagemaker.types.instance_group_scaling_metadata

        return {
            "InstanceGroupScaling": capo_sagemaker.types.instance_group_scaling_metadata.serialize_aws_json_1_1(
                value["InstanceGroupScaling"]
            )
        }
    elif "Instance" in value:
        import capo_sagemaker.types.instance_metadata

        return {
            "Instance": capo_sagemaker.types.instance_metadata.serialize_aws_json_1_1(
                value["Instance"]
            )
        }
    elif "DatabaseConfiguration" in value:
        import capo_sagemaker.types.database_configuration_metadata

        return {
            "DatabaseConfiguration": capo_sagemaker.types.database_configuration_metadata.serialize_aws_json_1_1(
                value["DatabaseConfiguration"]
            )
        }
    elif "SlurmHealth" in value:
        import capo_sagemaker.types.slurm_health_metadata

        return {
            "SlurmHealth": capo_sagemaker.types.slurm_health_metadata.serialize_aws_json_1_1(
                value["SlurmHealth"]
            )
        }
    else:
        raise SerializationError("EventMetadata: no variant present")


def deserialize_aws_json_1_1(data: dict) -> EventMetadata:
    if data.get("Cluster") is not None:
        import capo_sagemaker.types.cluster_metadata

        return {
            "Cluster": capo_sagemaker.types.cluster_metadata.deserialize_aws_json_1_1(
                data["Cluster"]
            )
        }
    elif data.get("InstanceGroup") is not None:
        import capo_sagemaker.types.instance_group_metadata

        return {
            "InstanceGroup": capo_sagemaker.types.instance_group_metadata.deserialize_aws_json_1_1(
                data["InstanceGroup"]
            )
        }
    elif data.get("InstanceGroupScaling") is not None:
        import capo_sagemaker.types.instance_group_scaling_metadata

        return {
            "InstanceGroupScaling": capo_sagemaker.types.instance_group_scaling_metadata.deserialize_aws_json_1_1(
                data["InstanceGroupScaling"]
            )
        }
    elif data.get("Instance") is not None:
        import capo_sagemaker.types.instance_metadata

        return {
            "Instance": capo_sagemaker.types.instance_metadata.deserialize_aws_json_1_1(
                data["Instance"]
            )
        }
    elif data.get("DatabaseConfiguration") is not None:
        import capo_sagemaker.types.database_configuration_metadata

        return {
            "DatabaseConfiguration": capo_sagemaker.types.database_configuration_metadata.deserialize_aws_json_1_1(
                data["DatabaseConfiguration"]
            )
        }
    elif data.get("SlurmHealth") is not None:
        import capo_sagemaker.types.slurm_health_metadata

        return {
            "SlurmHealth": capo_sagemaker.types.slurm_health_metadata.deserialize_aws_json_1_1(
                data["SlurmHealth"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("EventMetadata: no recognized variant key")
