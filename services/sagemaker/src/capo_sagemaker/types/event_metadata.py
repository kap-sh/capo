"""Generated from Smithy shape ``com.amazonaws.sagemaker#EventMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_sagemaker.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_metadata
    import capo_sagemaker.types.database_configuration_metadata
    import capo_sagemaker.types.instance_group_metadata
    import capo_sagemaker.types.instance_group_scaling_metadata
    import capo_sagemaker.types.instance_metadata
    import capo_sagemaker.types.slurm_health_metadata


class _EventMetadata_Cluster(TypedDict, closed=True):
    Cluster: "capo_sagemaker.types.cluster_metadata.ClusterMetadata"


class _EventMetadata_InstanceGroup(TypedDict, closed=True):
    InstanceGroup: "capo_sagemaker.types.instance_group_metadata.InstanceGroupMetadata"


class _EventMetadata_InstanceGroupScaling(TypedDict, closed=True):
    InstanceGroupScaling: "capo_sagemaker.types.instance_group_scaling_metadata.InstanceGroupScalingMetadata"


class _EventMetadata_Instance(TypedDict, closed=True):
    Instance: "capo_sagemaker.types.instance_metadata.InstanceMetadata"


class _EventMetadata_DatabaseConfiguration(TypedDict, closed=True):
    DatabaseConfiguration: "capo_sagemaker.types.database_configuration_metadata.DatabaseConfigurationMetadata"


class _EventMetadata_SlurmHealth(TypedDict, closed=True):
    SlurmHealth: "capo_sagemaker.types.slurm_health_metadata.SlurmHealthMetadata"


EventMetadata: TypeAlias = (
    _EventMetadata_Cluster
    | _EventMetadata_InstanceGroup
    | _EventMetadata_InstanceGroupScaling
    | _EventMetadata_Instance
    | _EventMetadata_DatabaseConfiguration
    | _EventMetadata_SlurmHealth
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventMetadata) -> dict:
    if "Cluster" in value:
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
        raise DeserializationError("EventMetadata: no recognized variant key")
