"""Generated from Smithy shape ``com.amazonaws.odb#CloudAutonomousVmClusterSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_odb.types.compute_model
    import capo_odb.types.iam_role_list
    import capo_odb.types.license_model
    import capo_odb.types.maintenance_window
    import capo_odb.types.resource_arn
    import capo_odb.types.resource_display_name
    import capo_odb.types.resource_id
    import capo_odb.types.resource_id_or_arn
    import capo_odb.types.resource_status
    import capo_odb.types.string_list


class CloudAutonomousVmClusterSummary(TypedDict, closed=True):
    cloud_autonomous_vm_cluster_id: "capo_odb.types.resource_id.ResourceId"
    """<p>The unique identifier of the Autonomous VM cluster.</p>"""
    cloud_autonomous_vm_cluster_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) for the Autonomous VM cluster.</p>"""
    odb_network_id: NotRequired["capo_odb.types.resource_id_or_arn.ResourceIdOrArn"]
    """<p>The unique identifier of the ODB network associated with this Autonomous VM cluster.</p>"""
    odb_network_arn: NotRequired["capo_odb.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the ODB network associated with this Autonomous VM cluster.</p>"""
    oci_resource_anchor_name: NotRequired["str"]
    """<p>The name of the OCI resource anchor associated with this Autonomous VM cluster.</p>"""
    percent_progress: NotRequired["float"]
    """<p>The progress of the current operation on the Autonomous VM cluster, as a percentage.</p>"""
    display_name: NotRequired[
        "capo_odb.types.resource_display_name.ResourceDisplayName"
    ]
    """<p>The user-friendly name for the Autonomous VM cluster.</p>"""
    status: NotRequired["capo_odb.types.resource_status.ResourceStatus"]
    """<p>The current status of the Autonomous VM cluster.</p>"""
    status_reason: NotRequired["str"]
    """<p>Additional information about the current status of the Autonomous VM cluster, if applicable.</p>"""
    cloud_exadata_infrastructure_id: NotRequired[
        "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    ]
    """<p>The unique identifier of the Exadata infrastructure containing this Autonomous VM cluster.</p>"""
    cloud_exadata_infrastructure_arn: NotRequired[
        "capo_odb.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Exadata infrastructure containing this Autonomous VM cluster.</p>"""
    autonomous_data_storage_percentage: NotRequired["float"]
    """<p>The percentage of data storage currently in use for Autonomous Databases in the Autonomous VM cluster.</p>"""
    autonomous_data_storage_size_in_t_bs: NotRequired["float"]
    """<p>The total data storage allocated for Autonomous Databases in the Autonomous VM cluster, in TB.</p>"""
    available_autonomous_data_storage_size_in_t_bs: NotRequired["float"]
    """<p>The available data storage for Autonomous Databases in the Autonomous VM cluster, in TB.</p>"""
    available_container_databases: NotRequired["int"]
    """<p>The number of Autonomous Container Databases that you can create with the currently available storage.</p>"""
    available_cpus: NotRequired["float"]
    """<p>The number of CPU cores available for allocation to Autonomous Databases.</p>"""
    compute_model: NotRequired["capo_odb.types.compute_model.ComputeModel"]
    """<p>The compute model of the Autonomous VM cluster: ECPU or OCPU.</p>"""
    cpu_core_count: NotRequired["int"]
    """<p>The total number of CPU cores in the Autonomous VM cluster.</p>"""
    cpu_core_count_per_node: NotRequired["int"]
    """<p>The number of CPU cores per node in the Autonomous VM cluster.</p>"""
    cpu_percentage: NotRequired["float"]
    """<p>The percentage of total CPU cores currently in use in the Autonomous VM cluster.</p>"""
    data_storage_size_in_g_bs: NotRequired["float"]
    """<p>The total data storage allocated to the Autonomous VM cluster, in GB.</p>"""
    data_storage_size_in_t_bs: NotRequired["float"]
    """<p>The total data storage allocated to the Autonomous VM cluster, in TB.</p>"""
    db_node_storage_size_in_g_bs: NotRequired["int"]
    """<p>The local node storage allocated to the Autonomous VM cluster, in GB.</p>"""
    db_servers: NotRequired["capo_odb.types.string_list.StringList"]
    """<p>The list of database servers associated with the Autonomous VM cluster.</p>"""
    description: NotRequired["str"]
    """<p>The user-provided description of the Autonomous VM cluster.</p>"""
    domain: NotRequired["str"]
    """<p>The domain name for the Autonomous VM cluster.</p>"""
    exadata_storage_in_t_bs_lowest_scaled_value: NotRequired["float"]
    """<p>The lowest value to which Exadata storage can be scaled down, in TB.</p>"""
    hostname: NotRequired["str"]
    """<p>The host name for the Autonomous VM cluster.</p>"""
    ocid: NotRequired["str"]
    """<p>The Oracle Cloud Identifier (OCID) of the Autonomous VM cluster.</p>"""
    oci_url: NotRequired["str"]
    """<p>The URL for accessing the OCI console page for this Autonomous VM cluster.</p>"""
    is_mtls_enabled_vm_cluster: NotRequired["bool"]
    """<p>Indicates if mutual TLS (mTLS) authentication is enabled for the Autonomous VM cluster.</p>"""
    license_model: NotRequired["capo_odb.types.license_model.LicenseModel"]
    """<p>The Oracle license model that applies to the Autonomous VM cluster.</p>"""
    maintenance_window: NotRequired[
        "capo_odb.types.maintenance_window.MaintenanceWindow"
    ]
    """<p>The scheduling details for the maintenance window. Patching and system updates take place during the maintenance window.</p>"""
    max_acds_lowest_scaled_value: NotRequired["int"]
    """<p>The lowest value to which you can scale down the maximum number of Autonomous CDBs.</p>"""
    memory_per_oracle_compute_unit_in_g_bs: NotRequired["int"]
    """<p>The amount of memory allocated per Oracle Compute Unit (OCU), in GB.</p>"""
    memory_size_in_g_bs: NotRequired["int"]
    """<p>The total amount of memory allocated to the Autonomous VM cluster, in GB.</p>"""
    node_count: NotRequired["int"]
    """<p>The number of database server nodes in the Autonomous VM cluster.</p>"""
    non_provisionable_autonomous_container_databases: NotRequired["int"]
    """<p>The number of Autonomous CDBs that can't be provisioned because of resource constraints.</p>"""
    provisionable_autonomous_container_databases: NotRequired["int"]
    """<p>The number of Autonomous CDBs that you can provision in the Autonomous VM cluster.</p>"""
    provisioned_autonomous_container_databases: NotRequired["int"]
    """<p>The number of Autonomous Container Databases currently provisioned in the Autonomous VM cluster.</p>"""
    provisioned_cpus: NotRequired["float"]
    """<p>The number of CPUs currently provisioned in the Autonomous VM cluster.</p>"""
    reclaimable_cpus: NotRequired["float"]
    """<p>The number of CPUs that can be reclaimed from terminated or scaled-down Autonomous Databases.</p>"""
    reserved_cpus: NotRequired["float"]
    """<p>The number of CPUs reserved for system operations and redundancy.</p>"""
    scan_listener_port_non_tls: NotRequired["int"]
    """<p>The SCAN listener port for non-TLS (TCP) protocol.</p>"""
    scan_listener_port_tls: NotRequired["int"]
    """<p>The SCAN listener port for TLS (TCP) protocol.</p>"""
    shape: NotRequired["str"]
    """<p>The shape of the Exadata infrastructure for the Autonomous VM cluster.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the Autonomous VM cluster was created.</p>"""
    time_database_ssl_certificate_expires: NotRequired["datetime.datetime"]
    """<p>The expiration date and time of the database SSL certificate.</p>"""
    time_ords_certificate_expires: NotRequired["datetime.datetime"]
    """<p>The expiration date and time of the Oracle REST Data Services (ORDS) certificate.</p>"""
    time_zone: NotRequired["str"]
    """<p>The time zone of the Autonomous VM cluster.</p>"""
    total_container_databases: NotRequired["int"]
    """<p>The total number of Autonomous Container Databases that can be created in the Autonomous VM cluster.</p>"""
    iam_roles: NotRequired["capo_odb.types.iam_role_list.IamRoleList"]
    """<p>The Amazon Web Services Identity and Access Management (IAM) service roles associated with the Autonomous VM cluster in the summary information.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CloudAutonomousVmClusterSummary) -> dict:
    out: dict = {}
    out["cloudAutonomousVmClusterId"] = value["cloud_autonomous_vm_cluster_id"]
    if "cloud_autonomous_vm_cluster_arn" in value:
        out["cloudAutonomousVmClusterArn"] = value["cloud_autonomous_vm_cluster_arn"]
    if "odb_network_id" in value:
        out["odbNetworkId"] = value["odb_network_id"]
    if "odb_network_arn" in value:
        out["odbNetworkArn"] = value["odb_network_arn"]
    if "oci_resource_anchor_name" in value:
        out["ociResourceAnchorName"] = value["oci_resource_anchor_name"]
    if "percent_progress" in value:
        out["percentProgress"] = (
            "NaN"
            if value["percent_progress"] != value["percent_progress"]
            else "Infinity"
            if value["percent_progress"] == float("inf")
            else "-Infinity"
            if value["percent_progress"] == float("-inf")
            else value["percent_progress"]
        )
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "status" in value:
        import capo_odb.types.resource_status

        out["status"] = capo_odb.types.resource_status.serialize_aws_json_1_0(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "cloud_exadata_infrastructure_id" in value:
        out["cloudExadataInfrastructureId"] = value["cloud_exadata_infrastructure_id"]
    if "cloud_exadata_infrastructure_arn" in value:
        out["cloudExadataInfrastructureArn"] = value["cloud_exadata_infrastructure_arn"]
    if "autonomous_data_storage_percentage" in value:
        out["autonomousDataStoragePercentage"] = (
            "NaN"
            if value["autonomous_data_storage_percentage"]
            != value["autonomous_data_storage_percentage"]
            else "Infinity"
            if value["autonomous_data_storage_percentage"] == float("inf")
            else "-Infinity"
            if value["autonomous_data_storage_percentage"] == float("-inf")
            else value["autonomous_data_storage_percentage"]
        )
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
    if "available_autonomous_data_storage_size_in_t_bs" in value:
        out["availableAutonomousDataStorageSizeInTBs"] = (
            "NaN"
            if value["available_autonomous_data_storage_size_in_t_bs"]
            != value["available_autonomous_data_storage_size_in_t_bs"]
            else "Infinity"
            if value["available_autonomous_data_storage_size_in_t_bs"] == float("inf")
            else "-Infinity"
            if value["available_autonomous_data_storage_size_in_t_bs"] == float("-inf")
            else value["available_autonomous_data_storage_size_in_t_bs"]
        )
    if "available_container_databases" in value:
        out["availableContainerDatabases"] = value["available_container_databases"]
    if "available_cpus" in value:
        out["availableCpus"] = (
            "NaN"
            if value["available_cpus"] != value["available_cpus"]
            else "Infinity"
            if value["available_cpus"] == float("inf")
            else "-Infinity"
            if value["available_cpus"] == float("-inf")
            else value["available_cpus"]
        )
    if "compute_model" in value:
        import capo_odb.types.compute_model

        out["computeModel"] = capo_odb.types.compute_model.serialize_aws_json_1_0(
            value["compute_model"]
        )
    if "cpu_core_count" in value:
        out["cpuCoreCount"] = value["cpu_core_count"]
    if "cpu_core_count_per_node" in value:
        out["cpuCoreCountPerNode"] = value["cpu_core_count_per_node"]
    if "cpu_percentage" in value:
        out["cpuPercentage"] = (
            "NaN"
            if value["cpu_percentage"] != value["cpu_percentage"]
            else "Infinity"
            if value["cpu_percentage"] == float("inf")
            else "-Infinity"
            if value["cpu_percentage"] == float("-inf")
            else value["cpu_percentage"]
        )
    if "data_storage_size_in_g_bs" in value:
        out["dataStorageSizeInGBs"] = (
            "NaN"
            if value["data_storage_size_in_g_bs"] != value["data_storage_size_in_g_bs"]
            else "Infinity"
            if value["data_storage_size_in_g_bs"] == float("inf")
            else "-Infinity"
            if value["data_storage_size_in_g_bs"] == float("-inf")
            else value["data_storage_size_in_g_bs"]
        )
    if "data_storage_size_in_t_bs" in value:
        out["dataStorageSizeInTBs"] = (
            "NaN"
            if value["data_storage_size_in_t_bs"] != value["data_storage_size_in_t_bs"]
            else "Infinity"
            if value["data_storage_size_in_t_bs"] == float("inf")
            else "-Infinity"
            if value["data_storage_size_in_t_bs"] == float("-inf")
            else value["data_storage_size_in_t_bs"]
        )
    if "db_node_storage_size_in_g_bs" in value:
        out["dbNodeStorageSizeInGBs"] = value["db_node_storage_size_in_g_bs"]
    if "db_servers" in value:
        import capo_odb.types.string_list

        out["dbServers"] = capo_odb.types.string_list.serialize_aws_json_1_0(
            value["db_servers"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "domain" in value:
        out["domain"] = value["domain"]
    if "exadata_storage_in_t_bs_lowest_scaled_value" in value:
        out["exadataStorageInTBsLowestScaledValue"] = (
            "NaN"
            if value["exadata_storage_in_t_bs_lowest_scaled_value"]
            != value["exadata_storage_in_t_bs_lowest_scaled_value"]
            else "Infinity"
            if value["exadata_storage_in_t_bs_lowest_scaled_value"] == float("inf")
            else "-Infinity"
            if value["exadata_storage_in_t_bs_lowest_scaled_value"] == float("-inf")
            else value["exadata_storage_in_t_bs_lowest_scaled_value"]
        )
    if "hostname" in value:
        out["hostname"] = value["hostname"]
    if "ocid" in value:
        out["ocid"] = value["ocid"]
    if "oci_url" in value:
        out["ociUrl"] = value["oci_url"]
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
    if "max_acds_lowest_scaled_value" in value:
        out["maxAcdsLowestScaledValue"] = value["max_acds_lowest_scaled_value"]
    if "memory_per_oracle_compute_unit_in_g_bs" in value:
        out["memoryPerOracleComputeUnitInGBs"] = value[
            "memory_per_oracle_compute_unit_in_g_bs"
        ]
    if "memory_size_in_g_bs" in value:
        out["memorySizeInGBs"] = value["memory_size_in_g_bs"]
    if "node_count" in value:
        out["nodeCount"] = value["node_count"]
    if "non_provisionable_autonomous_container_databases" in value:
        out["nonProvisionableAutonomousContainerDatabases"] = value[
            "non_provisionable_autonomous_container_databases"
        ]
    if "provisionable_autonomous_container_databases" in value:
        out["provisionableAutonomousContainerDatabases"] = value[
            "provisionable_autonomous_container_databases"
        ]
    if "provisioned_autonomous_container_databases" in value:
        out["provisionedAutonomousContainerDatabases"] = value[
            "provisioned_autonomous_container_databases"
        ]
    if "provisioned_cpus" in value:
        out["provisionedCpus"] = (
            "NaN"
            if value["provisioned_cpus"] != value["provisioned_cpus"]
            else "Infinity"
            if value["provisioned_cpus"] == float("inf")
            else "-Infinity"
            if value["provisioned_cpus"] == float("-inf")
            else value["provisioned_cpus"]
        )
    if "reclaimable_cpus" in value:
        out["reclaimableCpus"] = (
            "NaN"
            if value["reclaimable_cpus"] != value["reclaimable_cpus"]
            else "Infinity"
            if value["reclaimable_cpus"] == float("inf")
            else "-Infinity"
            if value["reclaimable_cpus"] == float("-inf")
            else value["reclaimable_cpus"]
        )
    if "reserved_cpus" in value:
        out["reservedCpus"] = (
            "NaN"
            if value["reserved_cpus"] != value["reserved_cpus"]
            else "Infinity"
            if value["reserved_cpus"] == float("inf")
            else "-Infinity"
            if value["reserved_cpus"] == float("-inf")
            else value["reserved_cpus"]
        )
    if "scan_listener_port_non_tls" in value:
        out["scanListenerPortNonTls"] = value["scan_listener_port_non_tls"]
    if "scan_listener_port_tls" in value:
        out["scanListenerPortTls"] = value["scan_listener_port_tls"]
    if "shape" in value:
        out["shape"] = value["shape"]
    if "created_at" in value:
        import capo_odb._protocol.serialize

        out["createdAt"] = capo_odb._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "time_database_ssl_certificate_expires" in value:
        import capo_odb._protocol.serialize

        out["timeDatabaseSslCertificateExpires"] = (
            capo_odb._protocol.serialize.fmt_date_time(
                value["time_database_ssl_certificate_expires"]
            )
        )
    if "time_ords_certificate_expires" in value:
        import capo_odb._protocol.serialize

        out["timeOrdsCertificateExpires"] = capo_odb._protocol.serialize.fmt_date_time(
            value["time_ords_certificate_expires"]
        )
    if "time_zone" in value:
        out["timeZone"] = value["time_zone"]
    if "total_container_databases" in value:
        out["totalContainerDatabases"] = value["total_container_databases"]
    if "iam_roles" in value:
        import capo_odb.types.iam_role_list

        out["iamRoles"] = capo_odb.types.iam_role_list.serialize_aws_json_1_0(
            value["iam_roles"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CloudAutonomousVmClusterSummary:
    out: CloudAutonomousVmClusterSummary = {}  # type: ignore[typeddict-item]
    if data.get("cloudAutonomousVmClusterId") is not None:
        out["cloud_autonomous_vm_cluster_id"] = data["cloudAutonomousVmClusterId"]
    else:
        out["cloud_autonomous_vm_cluster_id"] = ""
    if data.get("cloudAutonomousVmClusterArn") is not None:
        out["cloud_autonomous_vm_cluster_arn"] = data["cloudAutonomousVmClusterArn"]
    if data.get("odbNetworkId") is not None:
        out["odb_network_id"] = data["odbNetworkId"]
    if data.get("odbNetworkArn") is not None:
        out["odb_network_arn"] = data["odbNetworkArn"]
    if data.get("ociResourceAnchorName") is not None:
        out["oci_resource_anchor_name"] = data["ociResourceAnchorName"]
    if data.get("percentProgress") is not None:
        out["percent_progress"] = float(data["percentProgress"])
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("status") is not None:
        import capo_odb.types.resource_status

        out["status"] = capo_odb.types.resource_status.deserialize_aws_json_1_0(
            data["status"]
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("cloudExadataInfrastructureId") is not None:
        out["cloud_exadata_infrastructure_id"] = data["cloudExadataInfrastructureId"]
    if data.get("cloudExadataInfrastructureArn") is not None:
        out["cloud_exadata_infrastructure_arn"] = data["cloudExadataInfrastructureArn"]
    if data.get("autonomousDataStoragePercentage") is not None:
        out["autonomous_data_storage_percentage"] = float(
            data["autonomousDataStoragePercentage"]
        )
    if data.get("autonomousDataStorageSizeInTBs") is not None:
        out["autonomous_data_storage_size_in_t_bs"] = float(
            data["autonomousDataStorageSizeInTBs"]
        )
    if data.get("availableAutonomousDataStorageSizeInTBs") is not None:
        out["available_autonomous_data_storage_size_in_t_bs"] = float(
            data["availableAutonomousDataStorageSizeInTBs"]
        )
    if data.get("availableContainerDatabases") is not None:
        out["available_container_databases"] = data["availableContainerDatabases"]
    if data.get("availableCpus") is not None:
        out["available_cpus"] = float(data["availableCpus"])
    if data.get("computeModel") is not None:
        import capo_odb.types.compute_model

        out["compute_model"] = capo_odb.types.compute_model.deserialize_aws_json_1_0(
            data["computeModel"]
        )
    if data.get("cpuCoreCount") is not None:
        out["cpu_core_count"] = data["cpuCoreCount"]
    if data.get("cpuCoreCountPerNode") is not None:
        out["cpu_core_count_per_node"] = data["cpuCoreCountPerNode"]
    if data.get("cpuPercentage") is not None:
        out["cpu_percentage"] = float(data["cpuPercentage"])
    if data.get("dataStorageSizeInGBs") is not None:
        out["data_storage_size_in_g_bs"] = float(data["dataStorageSizeInGBs"])
    if data.get("dataStorageSizeInTBs") is not None:
        out["data_storage_size_in_t_bs"] = float(data["dataStorageSizeInTBs"])
    if data.get("dbNodeStorageSizeInGBs") is not None:
        out["db_node_storage_size_in_g_bs"] = data["dbNodeStorageSizeInGBs"]
    if data.get("dbServers") is not None:
        import capo_odb.types.string_list

        out["db_servers"] = capo_odb.types.string_list.deserialize_aws_json_1_0(
            data["dbServers"]
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("domain") is not None:
        out["domain"] = data["domain"]
    if data.get("exadataStorageInTBsLowestScaledValue") is not None:
        out["exadata_storage_in_t_bs_lowest_scaled_value"] = float(
            data["exadataStorageInTBsLowestScaledValue"]
        )
    if data.get("hostname") is not None:
        out["hostname"] = data["hostname"]
    if data.get("ocid") is not None:
        out["ocid"] = data["ocid"]
    if data.get("ociUrl") is not None:
        out["oci_url"] = data["ociUrl"]
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
    if data.get("maxAcdsLowestScaledValue") is not None:
        out["max_acds_lowest_scaled_value"] = data["maxAcdsLowestScaledValue"]
    if data.get("memoryPerOracleComputeUnitInGBs") is not None:
        out["memory_per_oracle_compute_unit_in_g_bs"] = data[
            "memoryPerOracleComputeUnitInGBs"
        ]
    if data.get("memorySizeInGBs") is not None:
        out["memory_size_in_g_bs"] = data["memorySizeInGBs"]
    if data.get("nodeCount") is not None:
        out["node_count"] = data["nodeCount"]
    if data.get("nonProvisionableAutonomousContainerDatabases") is not None:
        out["non_provisionable_autonomous_container_databases"] = data[
            "nonProvisionableAutonomousContainerDatabases"
        ]
    if data.get("provisionableAutonomousContainerDatabases") is not None:
        out["provisionable_autonomous_container_databases"] = data[
            "provisionableAutonomousContainerDatabases"
        ]
    if data.get("provisionedAutonomousContainerDatabases") is not None:
        out["provisioned_autonomous_container_databases"] = data[
            "provisionedAutonomousContainerDatabases"
        ]
    if data.get("provisionedCpus") is not None:
        out["provisioned_cpus"] = float(data["provisionedCpus"])
    if data.get("reclaimableCpus") is not None:
        out["reclaimable_cpus"] = float(data["reclaimableCpus"])
    if data.get("reservedCpus") is not None:
        out["reserved_cpus"] = float(data["reservedCpus"])
    if data.get("scanListenerPortNonTls") is not None:
        out["scan_listener_port_non_tls"] = data["scanListenerPortNonTls"]
    if data.get("scanListenerPortTls") is not None:
        out["scan_listener_port_tls"] = data["scanListenerPortTls"]
    if data.get("shape") is not None:
        out["shape"] = data["shape"]
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("timeDatabaseSslCertificateExpires") is not None:
        import datetime

        out["time_database_ssl_certificate_expires"] = datetime.datetime.fromisoformat(
            data["timeDatabaseSslCertificateExpires"].replace("Z", "+00:00")
        )
    if data.get("timeOrdsCertificateExpires") is not None:
        import datetime

        out["time_ords_certificate_expires"] = datetime.datetime.fromisoformat(
            data["timeOrdsCertificateExpires"].replace("Z", "+00:00")
        )
    if data.get("timeZone") is not None:
        out["time_zone"] = data["timeZone"]
    if data.get("totalContainerDatabases") is not None:
        out["total_container_databases"] = data["totalContainerDatabases"]
    if data.get("iamRoles") is not None:
        import capo_odb.types.iam_role_list

        out["iam_roles"] = capo_odb.types.iam_role_list.deserialize_aws_json_1_0(
            data["iamRoles"]
        )
    return out
