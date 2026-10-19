"""Generated from Smithy shape ``com.amazonaws.odb#ExadbVmClusterSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_odb.types.cluster_name
    import capo_odb.types.data_collection_options
    import capo_odb.types.exadata_iorm_config
    import capo_odb.types.exadb_vm_cluster_storage_details
    import capo_odb.types.grid_image_type
    import capo_odb.types.hostname
    import capo_odb.types.iam_role_list
    import capo_odb.types.license_model
    import capo_odb.types.resource_arn
    import capo_odb.types.resource_display_name
    import capo_odb.types.resource_id_or_arn
    import capo_odb.types.resource_status
    import capo_odb.types.shape_attribute
    import capo_odb.types.string_list


class ExadbVmClusterSummary(TypedDict, closed=True):
    exadb_vm_cluster_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the Exascale VM cluster.</p>"""
    cluster_name: NotRequired["capo_odb.types.cluster_name.ClusterName"]
    """<p>The name of the Grid Infrastructure (GI) cluster.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the Exascale VM cluster was created.</p>"""
    data_collection_options: NotRequired[
        "capo_odb.types.data_collection_options.DataCollectionOptions"
    ]
    """<p>The set of diagnostic collection options enabled for the Exascale VM cluster.</p>"""
    display_name: NotRequired[
        "capo_odb.types.resource_display_name.ResourceDisplayName"
    ]
    """<p>The user-friendly name for the Exascale VM cluster.</p>"""
    domain: NotRequired["str"]
    """<p>The domain of the Exascale VM cluster.</p>"""
    enabled_ecpu_count: NotRequired["int"]
    """<p>The number of elastic compute processing units (ECPUs) enabled on the Exascale VM cluster.</p>"""
    exadb_vm_cluster_arn: NotRequired["capo_odb.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the Exascale VM cluster.</p>"""
    exascale_db_storage_vault_arn: NotRequired[
        "capo_odb.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Exascale storage vault associated with this Exascale VM cluster.</p>"""
    exascale_db_storage_vault_id: NotRequired[
        "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    ]
    """<p>The unique identifier of the Exascale storage vault associated with this Exascale VM cluster.</p>"""
    gi_version: NotRequired["str"]
    """<p>The software version of the Oracle Grid Infrastructure (GI) for the Exascale VM cluster.</p>"""
    grid_image_id: NotRequired["str"]
    """<p>The Grid Infrastructure software image ID for the Exascale VM cluster.</p>"""
    grid_image_type: NotRequired["capo_odb.types.grid_image_type.GridImageType"]
    """<p>The type of Grid Infrastructure image for the Exascale VM cluster.</p>"""
    hostname: NotRequired["capo_odb.types.hostname.Hostname"]
    """<p>The host name for the Exascale VM cluster.</p>"""
    iam_roles: NotRequired["capo_odb.types.iam_role_list.IamRoleList"]
    """<p>The Amazon Web Services Identity and Access Management (IAM) service roles associated with the Exascale VM cluster.</p>"""
    iorm_config_cache: NotRequired[
        "capo_odb.types.exadata_iorm_config.ExadataIormConfig"
    ]
    """<p>The I/O Resource Management (IORM) configuration cache details for the Exascale VM cluster.</p>"""
    last_update_history_entry_id: NotRequired["str"]
    """<p>The Oracle Cloud ID (OCID) of the last maintenance update history entry.</p>"""
    license_model: NotRequired["capo_odb.types.license_model.LicenseModel"]
    """<p>The Oracle license model applied to the Exascale VM cluster.</p>"""
    listener_port: NotRequired["int"]
    """<p>The port number configured for the listener on the Exascale VM cluster.</p>"""
    memory_size_in_g_bs: NotRequired["int"]
    """<p>The amount of memory, in gigabytes (GB), that's allocated for the Exascale VM cluster.</p>"""
    node_count: NotRequired["int"]
    """<p>The number of nodes in the Exascale VM cluster.</p>"""
    ocid: NotRequired["str"]
    """<p>The OCID of the Exascale VM cluster.</p>"""
    oci_resource_anchor_name: NotRequired["str"]
    """<p>The name of the OCI resource anchor for the Exascale VM cluster.</p>"""
    oci_url: NotRequired["str"]
    """<p>The HTTPS link to the Exascale VM cluster in Oracle Cloud Infrastructure (OCI).</p>"""
    odb_network_arn: NotRequired["capo_odb.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the ODB network associated with this Exascale VM cluster.</p>"""
    odb_network_id: NotRequired["capo_odb.types.resource_id_or_arn.ResourceIdOrArn"]
    """<p>The unique identifier of the ODB network for the Exascale VM cluster.</p>"""
    percent_progress: NotRequired["float"]
    """<p>The amount of progress made on the current operation on the Exascale VM cluster, expressed as a percentage.</p>"""
    scan_dns_name: NotRequired["str"]
    """<p>The fully qualified domain name (FQDN) of the DNS record for the Single Client Access Name (SCAN) IP addresses that are associated with the Exascale VM cluster.</p>"""
    scan_dns_record_id: NotRequired["str"]
    """<p>The OCID of the DNS record for the SCAN IP addresses that are associated with the Exascale VM cluster.</p>"""
    scan_ip_ids: NotRequired["capo_odb.types.string_list.StringList"]
    """<p>The OCID of the SCAN IP addresses that are associated with the Exascale VM cluster.</p>"""
    scan_listener_port_tcp: NotRequired["int"]
    """<p>The port number for TCP connections to the Single Client Access Name (SCAN) listener for the Exascale VM cluster.</p>"""
    scan_listener_port_tcp_ssl: NotRequired["int"]
    """<p>The port number for TCP connections with SSL to the Single Client Access Name (SCAN) listener for the Exascale VM cluster.</p>"""
    shape: NotRequired["str"]
    """<p>The hardware model name of the Exadata infrastructure that's running the Exascale VM cluster.</p>"""
    shape_attribute: NotRequired["capo_odb.types.shape_attribute.ShapeAttribute"]
    """<p>The shape attribute for the Exascale VM cluster.</p>"""
    snapshot_file_system_storage: NotRequired[
        "capo_odb.types.exadb_vm_cluster_storage_details.ExadbVmClusterStorageDetails"
    ]
    """<p>The snapshot file system storage details for the Exascale VM cluster.</p>"""
    ssh_public_keys: NotRequired["capo_odb.types.string_list.StringList"]
    """<p>The public key portion of one or more key pairs used for SSH access to the Exascale VM cluster.</p>"""
    status: NotRequired["capo_odb.types.resource_status.ResourceStatus"]
    """<p>The current status of the Exascale VM cluster.</p>"""
    status_reason: NotRequired["str"]
    """<p>Additional information about the status of the Exascale VM cluster.</p>"""
    system_version: NotRequired["str"]
    """<p>The operating system version of the image chosen for the Exascale VM cluster.</p>"""
    time_zone: NotRequired["str"]
    """<p>The time zone of the Exascale VM cluster.</p>"""
    total_ecpu_count: NotRequired["int"]
    """<p>The total number of ECPUs for the Exascale VM cluster.</p>"""
    total_file_system_storage: NotRequired[
        "capo_odb.types.exadb_vm_cluster_storage_details.ExadbVmClusterStorageDetails"
    ]
    """<p>The total file system storage details for the Exascale VM cluster.</p>"""
    vip_ids: NotRequired["capo_odb.types.string_list.StringList"]
    """<p>The virtual IP (VIP) addresses associated with the Exascale VM cluster. One VIP address is assigned per node to support failover. If a node fails, its VIP is reassigned to another active node in the cluster.</p>"""
    vm_file_system_storage: NotRequired[
        "capo_odb.types.exadb_vm_cluster_storage_details.ExadbVmClusterStorageDetails"
    ]
    """<p>The VM file system storage details for the Exascale VM cluster.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExadbVmClusterSummary) -> dict:
    out: dict = {}
    out["exadbVmClusterId"] = value["exadb_vm_cluster_id"]
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    if "created_at" in value:
        import capo_odb._protocol.serialize

        out["createdAt"] = capo_odb._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "data_collection_options" in value:
        import capo_odb.types.data_collection_options

        out["dataCollectionOptions"] = (
            capo_odb.types.data_collection_options.serialize_aws_json_1_0(
                value["data_collection_options"]
            )
        )
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "domain" in value:
        out["domain"] = value["domain"]
    if "enabled_ecpu_count" in value:
        out["enabledEcpuCount"] = value["enabled_ecpu_count"]
    if "exadb_vm_cluster_arn" in value:
        out["exadbVmClusterArn"] = value["exadb_vm_cluster_arn"]
    if "exascale_db_storage_vault_arn" in value:
        out["exascaleDbStorageVaultArn"] = value["exascale_db_storage_vault_arn"]
    if "exascale_db_storage_vault_id" in value:
        out["exascaleDbStorageVaultId"] = value["exascale_db_storage_vault_id"]
    if "gi_version" in value:
        out["giVersion"] = value["gi_version"]
    if "grid_image_id" in value:
        out["gridImageId"] = value["grid_image_id"]
    if "grid_image_type" in value:
        import capo_odb.types.grid_image_type

        out["gridImageType"] = capo_odb.types.grid_image_type.serialize_aws_json_1_0(
            value["grid_image_type"]
        )
    if "hostname" in value:
        out["hostname"] = value["hostname"]
    if "iam_roles" in value:
        import capo_odb.types.iam_role_list

        out["iamRoles"] = capo_odb.types.iam_role_list.serialize_aws_json_1_0(
            value["iam_roles"]
        )
    if "iorm_config_cache" in value:
        import capo_odb.types.exadata_iorm_config

        out["iormConfigCache"] = (
            capo_odb.types.exadata_iorm_config.serialize_aws_json_1_0(
                value["iorm_config_cache"]
            )
        )
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
    if "odb_network_arn" in value:
        out["odbNetworkArn"] = value["odb_network_arn"]
    if "odb_network_id" in value:
        out["odbNetworkId"] = value["odb_network_id"]
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
    if "scan_dns_name" in value:
        out["scanDnsName"] = value["scan_dns_name"]
    if "scan_dns_record_id" in value:
        out["scanDnsRecordId"] = value["scan_dns_record_id"]
    if "scan_ip_ids" in value:
        import capo_odb.types.string_list

        out["scanIpIds"] = capo_odb.types.string_list.serialize_aws_json_1_0(
            value["scan_ip_ids"]
        )
    if "scan_listener_port_tcp" in value:
        out["scanListenerPortTcp"] = value["scan_listener_port_tcp"]
    if "scan_listener_port_tcp_ssl" in value:
        out["scanListenerPortTcpSsl"] = value["scan_listener_port_tcp_ssl"]
    if "shape" in value:
        out["shape"] = value["shape"]
    if "shape_attribute" in value:
        import capo_odb.types.shape_attribute

        out["shapeAttribute"] = capo_odb.types.shape_attribute.serialize_aws_json_1_0(
            value["shape_attribute"]
        )
    if "snapshot_file_system_storage" in value:
        import capo_odb.types.exadb_vm_cluster_storage_details

        out["snapshotFileSystemStorage"] = (
            capo_odb.types.exadb_vm_cluster_storage_details.serialize_aws_json_1_0(
                value["snapshot_file_system_storage"]
            )
        )
    if "ssh_public_keys" in value:
        import capo_odb.types.string_list

        out["sshPublicKeys"] = capo_odb.types.string_list.serialize_aws_json_1_0(
            value["ssh_public_keys"]
        )
    if "status" in value:
        import capo_odb.types.resource_status

        out["status"] = capo_odb.types.resource_status.serialize_aws_json_1_0(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "system_version" in value:
        out["systemVersion"] = value["system_version"]
    if "time_zone" in value:
        out["timeZone"] = value["time_zone"]
    if "total_ecpu_count" in value:
        out["totalEcpuCount"] = value["total_ecpu_count"]
    if "total_file_system_storage" in value:
        import capo_odb.types.exadb_vm_cluster_storage_details

        out["totalFileSystemStorage"] = (
            capo_odb.types.exadb_vm_cluster_storage_details.serialize_aws_json_1_0(
                value["total_file_system_storage"]
            )
        )
    if "vip_ids" in value:
        import capo_odb.types.string_list

        out["vipIds"] = capo_odb.types.string_list.serialize_aws_json_1_0(
            value["vip_ids"]
        )
    if "vm_file_system_storage" in value:
        import capo_odb.types.exadb_vm_cluster_storage_details

        out["vmFileSystemStorage"] = (
            capo_odb.types.exadb_vm_cluster_storage_details.serialize_aws_json_1_0(
                value["vm_file_system_storage"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ExadbVmClusterSummary:
    out: ExadbVmClusterSummary = {}  # type: ignore[typeddict-item]
    if data.get("exadbVmClusterId") is not None:
        out["exadb_vm_cluster_id"] = data["exadbVmClusterId"]
    else:
        out["exadb_vm_cluster_id"] = ""
    if data.get("clusterName") is not None:
        out["cluster_name"] = data["clusterName"]
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("dataCollectionOptions") is not None:
        import capo_odb.types.data_collection_options

        out["data_collection_options"] = (
            capo_odb.types.data_collection_options.deserialize_aws_json_1_0(
                data["dataCollectionOptions"]
            )
        )
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("domain") is not None:
        out["domain"] = data["domain"]
    if data.get("enabledEcpuCount") is not None:
        out["enabled_ecpu_count"] = data["enabledEcpuCount"]
    if data.get("exadbVmClusterArn") is not None:
        out["exadb_vm_cluster_arn"] = data["exadbVmClusterArn"]
    if data.get("exascaleDbStorageVaultArn") is not None:
        out["exascale_db_storage_vault_arn"] = data["exascaleDbStorageVaultArn"]
    if data.get("exascaleDbStorageVaultId") is not None:
        out["exascale_db_storage_vault_id"] = data["exascaleDbStorageVaultId"]
    if data.get("giVersion") is not None:
        out["gi_version"] = data["giVersion"]
    if data.get("gridImageId") is not None:
        out["grid_image_id"] = data["gridImageId"]
    if data.get("gridImageType") is not None:
        import capo_odb.types.grid_image_type

        out["grid_image_type"] = (
            capo_odb.types.grid_image_type.deserialize_aws_json_1_0(
                data["gridImageType"]
            )
        )
    if data.get("hostname") is not None:
        out["hostname"] = data["hostname"]
    if data.get("iamRoles") is not None:
        import capo_odb.types.iam_role_list

        out["iam_roles"] = capo_odb.types.iam_role_list.deserialize_aws_json_1_0(
            data["iamRoles"]
        )
    if data.get("iormConfigCache") is not None:
        import capo_odb.types.exadata_iorm_config

        out["iorm_config_cache"] = (
            capo_odb.types.exadata_iorm_config.deserialize_aws_json_1_0(
                data["iormConfigCache"]
            )
        )
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
    if data.get("odbNetworkArn") is not None:
        out["odb_network_arn"] = data["odbNetworkArn"]
    if data.get("odbNetworkId") is not None:
        out["odb_network_id"] = data["odbNetworkId"]
    if data.get("percentProgress") is not None:
        out["percent_progress"] = float(data["percentProgress"])
    if data.get("scanDnsName") is not None:
        out["scan_dns_name"] = data["scanDnsName"]
    if data.get("scanDnsRecordId") is not None:
        out["scan_dns_record_id"] = data["scanDnsRecordId"]
    if data.get("scanIpIds") is not None:
        import capo_odb.types.string_list

        out["scan_ip_ids"] = capo_odb.types.string_list.deserialize_aws_json_1_0(
            data["scanIpIds"]
        )
    if data.get("scanListenerPortTcp") is not None:
        out["scan_listener_port_tcp"] = data["scanListenerPortTcp"]
    if data.get("scanListenerPortTcpSsl") is not None:
        out["scan_listener_port_tcp_ssl"] = data["scanListenerPortTcpSsl"]
    if data.get("shape") is not None:
        out["shape"] = data["shape"]
    if data.get("shapeAttribute") is not None:
        import capo_odb.types.shape_attribute

        out["shape_attribute"] = (
            capo_odb.types.shape_attribute.deserialize_aws_json_1_0(
                data["shapeAttribute"]
            )
        )
    if data.get("snapshotFileSystemStorage") is not None:
        import capo_odb.types.exadb_vm_cluster_storage_details

        out["snapshot_file_system_storage"] = (
            capo_odb.types.exadb_vm_cluster_storage_details.deserialize_aws_json_1_0(
                data["snapshotFileSystemStorage"]
            )
        )
    if data.get("sshPublicKeys") is not None:
        import capo_odb.types.string_list

        out["ssh_public_keys"] = capo_odb.types.string_list.deserialize_aws_json_1_0(
            data["sshPublicKeys"]
        )
    if data.get("status") is not None:
        import capo_odb.types.resource_status

        out["status"] = capo_odb.types.resource_status.deserialize_aws_json_1_0(
            data["status"]
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("systemVersion") is not None:
        out["system_version"] = data["systemVersion"]
    if data.get("timeZone") is not None:
        out["time_zone"] = data["timeZone"]
    if data.get("totalEcpuCount") is not None:
        out["total_ecpu_count"] = data["totalEcpuCount"]
    if data.get("totalFileSystemStorage") is not None:
        import capo_odb.types.exadb_vm_cluster_storage_details

        out["total_file_system_storage"] = (
            capo_odb.types.exadb_vm_cluster_storage_details.deserialize_aws_json_1_0(
                data["totalFileSystemStorage"]
            )
        )
    if data.get("vipIds") is not None:
        import capo_odb.types.string_list

        out["vip_ids"] = capo_odb.types.string_list.deserialize_aws_json_1_0(
            data["vipIds"]
        )
    if data.get("vmFileSystemStorage") is not None:
        import capo_odb.types.exadb_vm_cluster_storage_details

        out["vm_file_system_storage"] = (
            capo_odb.types.exadb_vm_cluster_storage_details.deserialize_aws_json_1_0(
                data["vmFileSystemStorage"]
            )
        )
    return out
