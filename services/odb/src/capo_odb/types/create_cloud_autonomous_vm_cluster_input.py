"""Generated from Smithy shape ``com.amazonaws.odb#CreateCloudAutonomousVmClusterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.general_input_string
    import capo_odb.types.license_model
    import capo_odb.types.maintenance_window
    import capo_odb.types.request_tag_map
    import capo_odb.types.resource_display_name
    import capo_odb.types.resource_id_or_arn
    import capo_odb.types.string_list


class CreateCloudAutonomousVmClusterInput(TypedDict, closed=True):
    cloud_exadata_infrastructure_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the Exadata infrastructure where the VM cluster will be created.</p>"""
    odb_network_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the ODB network to be used for the VM cluster.</p>"""
    display_name: "capo_odb.types.resource_display_name.ResourceDisplayName"
    """<p>The display name for the Autonomous VM cluster. The name does not need to be unique.</p>"""
    client_token: NotRequired["capo_odb.types.general_input_string.GeneralInputString"]
    """<p>A client-provided token to ensure idempotency of the request.</p>"""
    autonomous_data_storage_size_in_t_bs: "float"
    """<p>The data disk group size to be allocated for Autonomous Databases, in terabytes (TB).</p>"""
    cpu_core_count_per_node: "int"
    """<p>The number of CPU cores to be enabled per VM cluster node.</p>"""
    db_servers: NotRequired["capo_odb.types.string_list.StringList"]
    """<p>The list of database servers to be used for the Autonomous VM cluster.</p>"""
    description: NotRequired["str"]
    """<p>A user-provided description of the Autonomous VM cluster.</p>"""
    is_mtls_enabled_vm_cluster: NotRequired["bool"]
    """<p>Specifies whether to enable mutual TLS (mTLS) authentication for the Autonomous VM cluster.</p>"""
    license_model: NotRequired["capo_odb.types.license_model.LicenseModel"]
    """<p>The Oracle license model to apply to the Autonomous VM cluster.</p>"""
    maintenance_window: NotRequired[
        "capo_odb.types.maintenance_window.MaintenanceWindow"
    ]
    """<p>The scheduling details for the maintenance window. Patching and system updates take place during the maintenance window.</p>"""
    memory_per_oracle_compute_unit_in_g_bs: "int"
    """<p>The amount of memory to be allocated per OCPU, in GB.</p>"""
    scan_listener_port_non_tls: NotRequired["int"]
    """<p>The SCAN listener port for non-TLS (TCP) protocol.</p>"""
    scan_listener_port_tls: NotRequired["int"]
    """<p>The SCAN listener port for TLS (TCP) protocol.</p>"""
    tags: NotRequired["capo_odb.types.request_tag_map.RequestTagMap"]
    """<p>Free-form tags for this resource. Each tag is a key-value pair with no predefined name, type, or namespace.</p>"""
    time_zone: NotRequired["str"]
    """<p>The time zone to use for the Autonomous VM cluster.</p>"""
    total_container_databases: "int"
    """<p>The total number of Autonomous CDBs that you can create in the Autonomous VM cluster.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateCloudAutonomousVmClusterInput) -> dict:
    out: dict = {}
    out["cloudExadataInfrastructureId"] = value["cloud_exadata_infrastructure_id"]
    out["odbNetworkId"] = value["odb_network_id"]
    out["displayName"] = value["display_name"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
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
    out["cpuCoreCountPerNode"] = value["cpu_core_count_per_node"]
    if "db_servers" in value:
        import capo_odb.types.string_list

        out["dbServers"] = capo_odb.types.string_list.serialize_aws_json_1_0(
            value["db_servers"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "is_mtls_enabled_vm_cluster" in value:
        out["isMtlsEnabledVmCluster"] = value["is_mtls_enabled_vm_cluster"]
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
    out["memoryPerOracleComputeUnitInGBs"] = value[
        "memory_per_oracle_compute_unit_in_g_bs"
    ]
    if "scan_listener_port_non_tls" in value:
        out["scanListenerPortNonTls"] = value["scan_listener_port_non_tls"]
    if "scan_listener_port_tls" in value:
        out["scanListenerPortTls"] = value["scan_listener_port_tls"]
    if "tags" in value:
        import capo_odb.types.request_tag_map

        out["tags"] = capo_odb.types.request_tag_map.serialize_aws_json_1_0(
            value["tags"]
        )
    if "time_zone" in value:
        out["timeZone"] = value["time_zone"]
    out["totalContainerDatabases"] = value["total_container_databases"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateCloudAutonomousVmClusterInput:
    out: CreateCloudAutonomousVmClusterInput = {}  # type: ignore[typeddict-item]
    if data.get("cloudExadataInfrastructureId") is not None:
        out["cloud_exadata_infrastructure_id"] = data["cloudExadataInfrastructureId"]
    else:
        out["cloud_exadata_infrastructure_id"] = ""
    if data.get("odbNetworkId") is not None:
        out["odb_network_id"] = data["odbNetworkId"]
    else:
        out["odb_network_id"] = ""
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        out["display_name"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("autonomousDataStorageSizeInTBs") is not None:
        out["autonomous_data_storage_size_in_t_bs"] = float(
            data["autonomousDataStorageSizeInTBs"]
        )
    else:
        out["autonomous_data_storage_size_in_t_bs"] = 0.0
    if data.get("cpuCoreCountPerNode") is not None:
        out["cpu_core_count_per_node"] = data["cpuCoreCountPerNode"]
    else:
        out["cpu_core_count_per_node"] = 0
    if data.get("dbServers") is not None:
        import capo_odb.types.string_list

        out["db_servers"] = capo_odb.types.string_list.deserialize_aws_json_1_0(
            data["dbServers"]
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("isMtlsEnabledVmCluster") is not None:
        out["is_mtls_enabled_vm_cluster"] = data["isMtlsEnabledVmCluster"]
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
    if data.get("memoryPerOracleComputeUnitInGBs") is not None:
        out["memory_per_oracle_compute_unit_in_g_bs"] = data[
            "memoryPerOracleComputeUnitInGBs"
        ]
    else:
        out["memory_per_oracle_compute_unit_in_g_bs"] = 0
    if data.get("scanListenerPortNonTls") is not None:
        out["scan_listener_port_non_tls"] = data["scanListenerPortNonTls"]
    if data.get("scanListenerPortTls") is not None:
        out["scan_listener_port_tls"] = data["scanListenerPortTls"]
    if data.get("tags") is not None:
        import capo_odb.types.request_tag_map

        out["tags"] = capo_odb.types.request_tag_map.deserialize_aws_json_1_0(
            data["tags"]
        )
    if data.get("timeZone") is not None:
        out["time_zone"] = data["timeZone"]
    if data.get("totalContainerDatabases") is not None:
        out["total_container_databases"] = data["totalContainerDatabases"]
    else:
        out["total_container_databases"] = 0
    return out
