"""Generated from Smithy shape ``com.amazonaws.odb#CloudVmCluster``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_odb.types.compute_model
    import capo_odb.types.data_collection_options
    import capo_odb.types.disk_redundancy
    import capo_odb.types.exadata_iorm_config
    import capo_odb.types.file_system_configuration_details_list
    import capo_odb.types.iam_role_list
    import capo_odb.types.license_model
    import capo_odb.types.resource_arn
    import capo_odb.types.resource_id
    import capo_odb.types.resource_id_or_arn
    import capo_odb.types.resource_status
    import capo_odb.types.sensitive_string_list
    import capo_odb.types.storage_management_type
    import capo_odb.types.string_list
    import capo_odb.types.vm_storage_type


class CloudVmCluster(TypedDict, closed=True):
    cloud_vm_cluster_id: "capo_odb.types.resource_id.ResourceId"
    """<p>The unique identifier of the VM cluster.</p>"""
    display_name: NotRequired["str"]
    """<p>The user-friendly name for the VM cluster.</p>"""
    status: NotRequired["capo_odb.types.resource_status.ResourceStatus"]
    """<p>The current status of the VM cluster.</p>"""
    status_reason: NotRequired["str"]
    """<p>Additional information about the status of the VM cluster.</p>"""
    cloud_vm_cluster_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the VM cluster.</p>"""
    cloud_exadata_infrastructure_id: NotRequired["str"]
    """<p>The unique identifier of the Exadata infrastructure that this VM cluster belongs to.</p>"""
    cloud_exadata_infrastructure_arn: NotRequired[
        "capo_odb.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Exadata infrastructure that this VM cluster belongs to.</p>"""
    exascale_db_storage_vault_id: NotRequired["capo_odb.types.resource_id.ResourceId"]
    """<p>The unique identifier of the Exascale storage vault that the VM cluster uses. This value is present only for VM clusters that use an Exascale storage vault.</p>"""
    exascale_db_storage_vault_arn: NotRequired[
        "capo_odb.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Exascale storage vault that the VM cluster uses. This value is present only for VM clusters that use an Exascale storage vault.</p>"""
    storage_management_type: NotRequired[
        "capo_odb.types.storage_management_type.StorageManagementType"
    ]
    """<p>The type of storage management for the VM cluster. A value of <code>ASM</code> indicates Oracle Automatic Storage Management, and <code>EXASCALE</code> indicates Exascale storage.</p>"""
    vm_file_system_storage_type: NotRequired[
        "capo_odb.types.vm_storage_type.VmStorageType"
    ]
    """<p>The type of storage that the VM cluster uses for its VM file systems.</p>"""
    vm_backup_storage_type: NotRequired["capo_odb.types.vm_storage_type.VmStorageType"]
    """<p>The type of storage that the VM cluster uses for VM backups.</p>"""
    file_system_configuration_details: NotRequired[
        "capo_odb.types.file_system_configuration_details_list.FileSystemConfigurationDetailsList"
    ]
    """<p>The list of file system configurations for the VM cluster.</p>"""
    cluster_name: NotRequired["str"]
    """<p>The name of the Grid Infrastructure (GI) cluster.</p>"""
    cpu_core_count: NotRequired["int"]
    """<p>The number of CPU cores enabled on the VM cluster.</p>"""
    data_collection_options: NotRequired[
        "capo_odb.types.data_collection_options.DataCollectionOptions"
    ]
    """<p>The set of diagnostic collection options enabled for the VM cluster.</p>"""
    data_storage_size_in_t_bs: NotRequired["float"]
    """<p>The size of the data disk group, in terabytes (TB), that's allocated for the VM cluster.</p>"""
    db_node_storage_size_in_g_bs: NotRequired["int"]
    """<p>The amount of local node storage, in gigabytes (GB), that's allocated for the VM cluster.</p>"""
    db_servers: NotRequired["capo_odb.types.string_list.StringList"]
    """<p>The list of database servers for the VM cluster.</p>"""
    disk_redundancy: NotRequired["capo_odb.types.disk_redundancy.DiskRedundancy"]
    """<p>The type of redundancy configured for the VM cluster. <code>NORMAL</code> is 2-way redundancy. <code>HIGH</code> is 3-way redundancy.</p>"""
    gi_version: NotRequired["str"]
    """<p>The software version of the Oracle Grid Infrastructure (GI) for the VM cluster.</p>"""
    hostname: NotRequired["str"]
    """<p>The host name for the VM cluster.</p>"""
    iorm_config_cache: NotRequired[
        "capo_odb.types.exadata_iorm_config.ExadataIormConfig"
    ]
    """<p>The ExadataIormConfig cache details for the VM cluster.</p>"""
    is_local_backup_enabled: NotRequired["bool"]
    """<p>Indicates whether database backups to local Exadata storage is enabled for the VM cluster.</p>"""
    is_sparse_diskgroup_enabled: NotRequired["bool"]
    """<p>Indicates whether the VM cluster is configured with a sparse disk group.</p>"""
    last_update_history_entry_id: NotRequired["str"]
    """<p>The Oracle Cloud ID (OCID) of the last maintenance update history entry.</p>"""
    license_model: NotRequired["capo_odb.types.license_model.LicenseModel"]
    """<p>The Oracle license model applied to the VM cluster.</p>"""
    listener_port: NotRequired["int"]
    """<p>The port number configured for the listener on the VM cluster.</p>"""
    memory_size_in_g_bs: NotRequired["int"]
    """<p>The amount of memory, in gigabytes (GB), that's allocated for the VM cluster.</p>"""
    node_count: NotRequired["int"]
    """<p>The number of nodes in the VM cluster.</p>"""
    ocid: NotRequired["str"]
    """<p>The OCID of the VM cluster.</p>"""
    oci_resource_anchor_name: NotRequired["str"]
    """<p>The name of the OCI resource anchor for the VM cluster.</p>"""
    oci_url: NotRequired["str"]
    """<p>The HTTPS link to the VM cluster in OCI.</p>"""
    domain: NotRequired["str"]
    """<p>The domain of the VM cluster.</p>"""
    scan_dns_name: NotRequired["str"]
    """<p>The fully qualified domain name (FQDN) of the DNS record for the Single Client Access Name (SCAN) IP addresses that are associated with the VM cluster.</p>"""
    scan_dns_record_id: NotRequired["str"]
    """<p>The OCID of the DNS record for the SCAN IP addresses that are associated with the VM cluster.</p>"""
    scan_ip_ids: NotRequired["capo_odb.types.string_list.StringList"]
    """<p>The OCID of the SCAN IP addresses that are associated with the VM cluster.</p>"""
    shape: NotRequired["str"]
    """<p>The hardware model name of the Exadata infrastructure that's running the VM cluster.</p>"""
    ssh_public_keys: NotRequired[
        "capo_odb.types.sensitive_string_list.SensitiveStringList"
    ]
    """<p>The public key portion of one or more key pairs used for SSH access to the VM cluster.</p>"""
    storage_size_in_g_bs: NotRequired["int"]
    """<p>The amount of local node storage, in gigabytes (GB), that's allocated to the VM cluster.</p>"""
    system_version: NotRequired["str"]
    """<p>The operating system version of the image chosen for the VM cluster.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the VM cluster was created.</p>"""
    time_zone: NotRequired["str"]
    """<p>The time zone of the VM cluster.</p>"""
    vip_ids: NotRequired["capo_odb.types.string_list.StringList"]
    """<p>The virtual IP (VIP) addresses that are associated with the VM cluster. Oracle's Cluster Ready Services (CRS) creates and maintains one VIP address for each node in the VM cluster to enable failover. If one node fails, the VIP is reassigned to another active node in the cluster.</p>"""
    odb_network_id: NotRequired["capo_odb.types.resource_id_or_arn.ResourceIdOrArn"]
    """<p>The unique identifier of the ODB network for the VM cluster.</p>"""
    odb_network_arn: NotRequired["capo_odb.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the ODB network associated with this VM cluster.</p>"""
    percent_progress: NotRequired["float"]
    """<p>The amount of progress made on the current operation on the VM cluster, expressed as a percentage.</p>"""
    compute_model: NotRequired["capo_odb.types.compute_model.ComputeModel"]
    """<p>The OCI model compute model used when you create or clone an instance: ECPU or OCPU. An ECPU is an abstracted measure of compute resources. ECPUs are based on the number of cores elastically allocated from a pool of compute and storage servers. An OCPU is a legacy physical measure of compute resources. OCPUs are based on the physical core of a processor with hyper-threading enabled. </p>"""
    iam_roles: NotRequired["capo_odb.types.iam_role_list.IamRoleList"]
    """<p>The Amazon Web Services Identity and Access Management (IAM) service roles associated with the VM cluster.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CloudVmCluster) -> dict:
    out: dict = {}
    out["cloudVmClusterId"] = value["cloud_vm_cluster_id"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "status" in value:
        import capo_odb.types.resource_status

        out["status"] = capo_odb.types.resource_status.serialize_aws_json_1_0(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "cloud_vm_cluster_arn" in value:
        out["cloudVmClusterArn"] = value["cloud_vm_cluster_arn"]
    if "cloud_exadata_infrastructure_id" in value:
        out["cloudExadataInfrastructureId"] = value["cloud_exadata_infrastructure_id"]
    if "cloud_exadata_infrastructure_arn" in value:
        out["cloudExadataInfrastructureArn"] = value["cloud_exadata_infrastructure_arn"]
    if "exascale_db_storage_vault_id" in value:
        out["exascaleDbStorageVaultId"] = value["exascale_db_storage_vault_id"]
    if "exascale_db_storage_vault_arn" in value:
        out["exascaleDbStorageVaultArn"] = value["exascale_db_storage_vault_arn"]
    if "storage_management_type" in value:
        import capo_odb.types.storage_management_type

        out["storageManagementType"] = (
            capo_odb.types.storage_management_type.serialize_aws_json_1_0(
                value["storage_management_type"]
            )
        )
    if "vm_file_system_storage_type" in value:
        import capo_odb.types.vm_storage_type

        out["vmFileSystemStorageType"] = (
            capo_odb.types.vm_storage_type.serialize_aws_json_1_0(
                value["vm_file_system_storage_type"]
            )
        )
    if "vm_backup_storage_type" in value:
        import capo_odb.types.vm_storage_type

        out["vmBackupStorageType"] = (
            capo_odb.types.vm_storage_type.serialize_aws_json_1_0(
                value["vm_backup_storage_type"]
            )
        )
    if "file_system_configuration_details" in value:
        import capo_odb.types.file_system_configuration_details_list

        out["fileSystemConfigurationDetails"] = (
            capo_odb.types.file_system_configuration_details_list.serialize_aws_json_1_0(
                value["file_system_configuration_details"]
            )
        )
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    if "cpu_core_count" in value:
        out["cpuCoreCount"] = value["cpu_core_count"]
    if "data_collection_options" in value:
        import capo_odb.types.data_collection_options

        out["dataCollectionOptions"] = (
            capo_odb.types.data_collection_options.serialize_aws_json_1_0(
                value["data_collection_options"]
            )
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
    if "disk_redundancy" in value:
        import capo_odb.types.disk_redundancy

        out["diskRedundancy"] = capo_odb.types.disk_redundancy.serialize_aws_json_1_0(
            value["disk_redundancy"]
        )
    if "gi_version" in value:
        out["giVersion"] = value["gi_version"]
    if "hostname" in value:
        out["hostname"] = value["hostname"]
    if "iorm_config_cache" in value:
        import capo_odb.types.exadata_iorm_config

        out["iormConfigCache"] = (
            capo_odb.types.exadata_iorm_config.serialize_aws_json_1_0(
                value["iorm_config_cache"]
            )
        )
    if "is_local_backup_enabled" in value:
        out["isLocalBackupEnabled"] = value["is_local_backup_enabled"]
    if "is_sparse_diskgroup_enabled" in value:
        out["isSparseDiskgroupEnabled"] = value["is_sparse_diskgroup_enabled"]
    if "last_update_history_entry_id" in value:
        out["lastUpdateHistoryEntryId"] = value["last_update_history_entry_id"]
    if "license_model" in value:
        import capo_odb.types.license_model

        out["licenseModel"] = capo_odb.types.license_model.serialize_aws_json_1_0(
            value["license_model"]
        )
    if "listener_port" in value:
        out["listenerPort"] = value["listener_port"]
    if "memory_size_in_g_bs" in value:
        out["memorySizeInGBs"] = value["memory_size_in_g_bs"]
    if "node_count" in value:
        out["nodeCount"] = value["node_count"]
    if "ocid" in value:
        out["ocid"] = value["ocid"]
    if "oci_resource_anchor_name" in value:
        out["ociResourceAnchorName"] = value["oci_resource_anchor_name"]
    if "oci_url" in value:
        out["ociUrl"] = value["oci_url"]
    if "domain" in value:
        out["domain"] = value["domain"]
    if "scan_dns_name" in value:
        out["scanDnsName"] = value["scan_dns_name"]
    if "scan_dns_record_id" in value:
        out["scanDnsRecordId"] = value["scan_dns_record_id"]
    if "scan_ip_ids" in value:
        import capo_odb.types.string_list

        out["scanIpIds"] = capo_odb.types.string_list.serialize_aws_json_1_0(
            value["scan_ip_ids"]
        )
    if "shape" in value:
        out["shape"] = value["shape"]
    if "ssh_public_keys" in value:
        import capo_odb.types.sensitive_string_list

        out["sshPublicKeys"] = (
            capo_odb.types.sensitive_string_list.serialize_aws_json_1_0(
                value["ssh_public_keys"]
            )
        )
    if "storage_size_in_g_bs" in value:
        out["storageSizeInGBs"] = value["storage_size_in_g_bs"]
    if "system_version" in value:
        out["systemVersion"] = value["system_version"]
    if "created_at" in value:
        import capo_odb._protocol.serialize

        out["createdAt"] = capo_odb._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "time_zone" in value:
        out["timeZone"] = value["time_zone"]
    if "vip_ids" in value:
        import capo_odb.types.string_list

        out["vipIds"] = capo_odb.types.string_list.serialize_aws_json_1_0(
            value["vip_ids"]
        )
    if "odb_network_id" in value:
        out["odbNetworkId"] = value["odb_network_id"]
    if "odb_network_arn" in value:
        out["odbNetworkArn"] = value["odb_network_arn"]
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
    if "compute_model" in value:
        import capo_odb.types.compute_model

        out["computeModel"] = capo_odb.types.compute_model.serialize_aws_json_1_0(
            value["compute_model"]
        )
    if "iam_roles" in value:
        import capo_odb.types.iam_role_list

        out["iamRoles"] = capo_odb.types.iam_role_list.serialize_aws_json_1_0(
            value["iam_roles"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CloudVmCluster:
    out: CloudVmCluster = {}  # type: ignore[typeddict-item]
    if data.get("cloudVmClusterId") is not None:
        out["cloud_vm_cluster_id"] = data["cloudVmClusterId"]
    else:
        out["cloud_vm_cluster_id"] = ""
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("status") is not None:
        import capo_odb.types.resource_status

        out["status"] = capo_odb.types.resource_status.deserialize_aws_json_1_0(
            data["status"]
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("cloudVmClusterArn") is not None:
        out["cloud_vm_cluster_arn"] = data["cloudVmClusterArn"]
    if data.get("cloudExadataInfrastructureId") is not None:
        out["cloud_exadata_infrastructure_id"] = data["cloudExadataInfrastructureId"]
    if data.get("cloudExadataInfrastructureArn") is not None:
        out["cloud_exadata_infrastructure_arn"] = data["cloudExadataInfrastructureArn"]
    if data.get("exascaleDbStorageVaultId") is not None:
        out["exascale_db_storage_vault_id"] = data["exascaleDbStorageVaultId"]
    if data.get("exascaleDbStorageVaultArn") is not None:
        out["exascale_db_storage_vault_arn"] = data["exascaleDbStorageVaultArn"]
    if data.get("storageManagementType") is not None:
        import capo_odb.types.storage_management_type

        out["storage_management_type"] = (
            capo_odb.types.storage_management_type.deserialize_aws_json_1_0(
                data["storageManagementType"]
            )
        )
    if data.get("vmFileSystemStorageType") is not None:
        import capo_odb.types.vm_storage_type

        out["vm_file_system_storage_type"] = (
            capo_odb.types.vm_storage_type.deserialize_aws_json_1_0(
                data["vmFileSystemStorageType"]
            )
        )
    if data.get("vmBackupStorageType") is not None:
        import capo_odb.types.vm_storage_type

        out["vm_backup_storage_type"] = (
            capo_odb.types.vm_storage_type.deserialize_aws_json_1_0(
                data["vmBackupStorageType"]
            )
        )
    if data.get("fileSystemConfigurationDetails") is not None:
        import capo_odb.types.file_system_configuration_details_list

        out["file_system_configuration_details"] = (
            capo_odb.types.file_system_configuration_details_list.deserialize_aws_json_1_0(
                data["fileSystemConfigurationDetails"]
            )
        )
    if data.get("clusterName") is not None:
        out["cluster_name"] = data["clusterName"]
    if data.get("cpuCoreCount") is not None:
        out["cpu_core_count"] = data["cpuCoreCount"]
    if data.get("dataCollectionOptions") is not None:
        import capo_odb.types.data_collection_options

        out["data_collection_options"] = (
            capo_odb.types.data_collection_options.deserialize_aws_json_1_0(
                data["dataCollectionOptions"]
            )
        )
    if data.get("dataStorageSizeInTBs") is not None:
        out["data_storage_size_in_t_bs"] = float(data["dataStorageSizeInTBs"])
    if data.get("dbNodeStorageSizeInGBs") is not None:
        out["db_node_storage_size_in_g_bs"] = data["dbNodeStorageSizeInGBs"]
    if data.get("dbServers") is not None:
        import capo_odb.types.string_list

        out["db_servers"] = capo_odb.types.string_list.deserialize_aws_json_1_0(
            data["dbServers"]
        )
    if data.get("diskRedundancy") is not None:
        import capo_odb.types.disk_redundancy

        out["disk_redundancy"] = (
            capo_odb.types.disk_redundancy.deserialize_aws_json_1_0(
                data["diskRedundancy"]
            )
        )
    if data.get("giVersion") is not None:
        out["gi_version"] = data["giVersion"]
    if data.get("hostname") is not None:
        out["hostname"] = data["hostname"]
    if data.get("iormConfigCache") is not None:
        import capo_odb.types.exadata_iorm_config

        out["iorm_config_cache"] = (
            capo_odb.types.exadata_iorm_config.deserialize_aws_json_1_0(
                data["iormConfigCache"]
            )
        )
    if data.get("isLocalBackupEnabled") is not None:
        out["is_local_backup_enabled"] = data["isLocalBackupEnabled"]
    if data.get("isSparseDiskgroupEnabled") is not None:
        out["is_sparse_diskgroup_enabled"] = data["isSparseDiskgroupEnabled"]
    if data.get("lastUpdateHistoryEntryId") is not None:
        out["last_update_history_entry_id"] = data["lastUpdateHistoryEntryId"]
    if data.get("licenseModel") is not None:
        import capo_odb.types.license_model

        out["license_model"] = capo_odb.types.license_model.deserialize_aws_json_1_0(
            data["licenseModel"]
        )
    if data.get("listenerPort") is not None:
        out["listener_port"] = data["listenerPort"]
    if data.get("memorySizeInGBs") is not None:
        out["memory_size_in_g_bs"] = data["memorySizeInGBs"]
    if data.get("nodeCount") is not None:
        out["node_count"] = data["nodeCount"]
    if data.get("ocid") is not None:
        out["ocid"] = data["ocid"]
    if data.get("ociResourceAnchorName") is not None:
        out["oci_resource_anchor_name"] = data["ociResourceAnchorName"]
    if data.get("ociUrl") is not None:
        out["oci_url"] = data["ociUrl"]
    if data.get("domain") is not None:
        out["domain"] = data["domain"]
    if data.get("scanDnsName") is not None:
        out["scan_dns_name"] = data["scanDnsName"]
    if data.get("scanDnsRecordId") is not None:
        out["scan_dns_record_id"] = data["scanDnsRecordId"]
    if data.get("scanIpIds") is not None:
        import capo_odb.types.string_list

        out["scan_ip_ids"] = capo_odb.types.string_list.deserialize_aws_json_1_0(
            data["scanIpIds"]
        )
    if data.get("shape") is not None:
        out["shape"] = data["shape"]
    if data.get("sshPublicKeys") is not None:
        import capo_odb.types.sensitive_string_list

        out["ssh_public_keys"] = (
            capo_odb.types.sensitive_string_list.deserialize_aws_json_1_0(
                data["sshPublicKeys"]
            )
        )
    if data.get("storageSizeInGBs") is not None:
        out["storage_size_in_g_bs"] = data["storageSizeInGBs"]
    if data.get("systemVersion") is not None:
        out["system_version"] = data["systemVersion"]
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("timeZone") is not None:
        out["time_zone"] = data["timeZone"]
    if data.get("vipIds") is not None:
        import capo_odb.types.string_list

        out["vip_ids"] = capo_odb.types.string_list.deserialize_aws_json_1_0(
            data["vipIds"]
        )
    if data.get("odbNetworkId") is not None:
        out["odb_network_id"] = data["odbNetworkId"]
    if data.get("odbNetworkArn") is not None:
        out["odb_network_arn"] = data["odbNetworkArn"]
    if data.get("percentProgress") is not None:
        out["percent_progress"] = float(data["percentProgress"])
    if data.get("computeModel") is not None:
        import capo_odb.types.compute_model

        out["compute_model"] = capo_odb.types.compute_model.deserialize_aws_json_1_0(
            data["computeModel"]
        )
    if data.get("iamRoles") is not None:
        import capo_odb.types.iam_role_list

        out["iam_roles"] = capo_odb.types.iam_role_list.deserialize_aws_json_1_0(
            data["iamRoles"]
        )
    return out


def redact_sensitive(value: CloudVmCluster) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ssh_public_keys" in value:
        import capo_odb.types.sensitive_string_list

        out["ssh_public_keys"] = capo_odb.types.sensitive_string_list.redact_sensitive(
            value["ssh_public_keys"]
        )
    return out
