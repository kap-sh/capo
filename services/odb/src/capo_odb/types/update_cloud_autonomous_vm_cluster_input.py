"""Generated from Smithy shape ``com.amazonaws.odb#UpdateCloudAutonomousVmClusterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.license_model
    import capo_odb.types.maintenance_window
    import capo_odb.types.resource_display_name
    import capo_odb.types.resource_id


class UpdateCloudAutonomousVmClusterInput(TypedDict, closed=True):
    cloud_autonomous_vm_cluster_id: "capo_odb.types.resource_id.ResourceId"
    """<p>The unique identifier of the Autonomous VM cluster to update.</p>"""
    autonomous_data_storage_size_in_t_bs: NotRequired["float"]
    """<p>The data storage size to allocate for Autonomous Databases in the Autonomous VM cluster, in terabytes (TB).</p>"""
    cpu_core_count_per_node: NotRequired["int"]
    """<p>The number of CPU cores to enable per node in the Autonomous VM cluster. If you don't specify a value, the existing number of CPU cores per node is retained.</p>"""
    description: NotRequired["str"]
    """<p>A user-provided description of the Autonomous VM cluster.</p>"""
    display_name: NotRequired[
        "capo_odb.types.resource_display_name.ResourceDisplayName"
    ]
    """<p>A new user-friendly name for the Autonomous VM cluster.</p>"""
    license_model: NotRequired["capo_odb.types.license_model.LicenseModel"]
    """<p>The Oracle license model to apply to the Autonomous VM cluster.</p>"""
    maintenance_window: NotRequired[
        "capo_odb.types.maintenance_window.MaintenanceWindow"
    ]
    """<p>The scheduling details for the maintenance window. Patching and system updates take place during the maintenance window.</p>"""
    total_container_databases: NotRequired["int"]
    """<p>The total number of Autonomous Container Databases that can be created in the Autonomous VM cluster.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateCloudAutonomousVmClusterInput) -> dict:
    out: dict = {}
    out["cloudAutonomousVmClusterId"] = value["cloud_autonomous_vm_cluster_id"]
    if "autonomous_data_storage_size_in_t_bs" in value:
        out["autonomousDataStorageSizeInTBs"] = (
            "NaN"
            if value["autonomous_data_storage_size_in_t_bs"]
            != value["autonomous_data_storage_size_in_t_bs"]
            else "Infinity"
            if value["autonomous_data_storage_size_in_t_bs"] == float("inf")
            else "-Infinity"
            if value["autonomous_data_storage_size_in_t_bs"] == float("-inf")
            else value["autonomous_data_storage_size_in_t_bs"]
        )
    if "cpu_core_count_per_node" in value:
        out["cpuCoreCountPerNode"] = value["cpu_core_count_per_node"]
    if "description" in value:
        out["description"] = value["description"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "license_model" in value:
        import capo_odb.types.license_model

        out["licenseModel"] = capo_odb.types.license_model.serialize_aws_json_1_0(
            value["license_model"]
        )
    if "maintenance_window" in value:
        import capo_odb.types.maintenance_window

        out["maintenanceWindow"] = (
            capo_odb.types.maintenance_window.serialize_aws_json_1_0(
                value["maintenance_window"]
            )
        )
    if "total_container_databases" in value:
        out["totalContainerDatabases"] = value["total_container_databases"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateCloudAutonomousVmClusterInput:
    out: UpdateCloudAutonomousVmClusterInput = {}  # type: ignore[typeddict-item]
    if data.get("cloudAutonomousVmClusterId") is not None:
        out["cloud_autonomous_vm_cluster_id"] = data["cloudAutonomousVmClusterId"]
    else:
        out["cloud_autonomous_vm_cluster_id"] = ""
    if data.get("autonomousDataStorageSizeInTBs") is not None:
        out["autonomous_data_storage_size_in_t_bs"] = float(
            data["autonomousDataStorageSizeInTBs"]
        )
    if data.get("cpuCoreCountPerNode") is not None:
        out["cpu_core_count_per_node"] = data["cpuCoreCountPerNode"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("licenseModel") is not None:
        import capo_odb.types.license_model

        out["license_model"] = capo_odb.types.license_model.deserialize_aws_json_1_0(
            data["licenseModel"]
        )
    if data.get("maintenanceWindow") is not None:
        import capo_odb.types.maintenance_window

        out["maintenance_window"] = (
            capo_odb.types.maintenance_window.deserialize_aws_json_1_0(
                data["maintenanceWindow"]
            )
        )
    if data.get("totalContainerDatabases") is not None:
        out["total_container_databases"] = data["totalContainerDatabases"]
    return out
