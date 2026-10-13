"""Generated from Smithy shape ``com.amazonaws.odb#CloudExadataInfrastructure``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_odb.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_odb.types.compute_model
    import capo_odb.types.customer_contacts
    import capo_odb.types.maintenance_window
    import capo_odb.types.resource_id_or_arn
    import capo_odb.types.resource_status


class CloudExadataInfrastructure(TypedDict, closed=True):
    cloud_exadata_infrastructure_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier for the Exadata infrastructure.</p>"""
    display_name: NotRequired["str"]
    """<p>The user-friendly name for the Exadata infrastructure.</p>"""
    status: NotRequired["capo_odb.types.resource_status.ResourceStatus"]
    """<p>The current status of the Exadata infrastructure.</p>"""
    status_reason: NotRequired["str"]
    """<p>Additional information about the status of the Exadata infrastructure.</p>"""
    cloud_exadata_infrastructure_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) for the Exadata infrastructure.</p>"""
    activated_storage_count: NotRequired["int"]
    """<p>The number of storage servers requested for the Exadata infrastructure.</p>"""
    additional_storage_count: NotRequired["int"]
    """<p>The number of storage servers requested for the Exadata infrastructure.</p>"""
    available_storage_size_in_g_bs: NotRequired["int"]
    """<p>The amount of available storage, in gigabytes (GB), for the Exadata infrastructure.</p>"""
    availability_zone: NotRequired["str"]
    """<p>The name of the Availability Zone (AZ) where the Exadata infrastructure is located.</p>"""
    availability_zone_id: NotRequired["str"]
    """<p>The AZ ID of the AZ where the Exadata infrastructure is located.</p>"""
    compute_count: NotRequired["int"]
    """<p>The number of database servers for the Exadata infrastructure.</p>"""
    cpu_count: NotRequired["int"]
    """<p>The total number of CPU cores that are allocated to the Exadata infrastructure.</p>"""
    customer_contacts_to_send_to_oci: NotRequired[
        "capo_odb.types.customer_contacts.CustomerContacts"
    ]
    """<p>The email addresses of contacts to receive notification from Oracle about maintenance updates for the Exadata infrastructure.</p>"""
    data_storage_size_in_t_bs: NotRequired["float"]
    """<p>The size of the Exadata infrastructure's data disk group, in terabytes (TB).</p>"""
    db_node_storage_size_in_g_bs: NotRequired["int"]
    """<p>The size of the Exadata infrastructure's local node storage, in gigabytes (GB).</p>"""
    db_server_version: NotRequired["str"]
    """<p>The software version of the database servers (dom0) in the Exadata infrastructure.</p>"""
    last_maintenance_run_id: NotRequired["str"]
    """<p>The Oracle Cloud Identifier (OCID) of the last maintenance run for the Exadata infrastructure.</p>"""
    maintenance_window: NotRequired[
        "capo_odb.types.maintenance_window.MaintenanceWindow"
    ]
    """<p>The scheduling details for the maintenance window. Patching and system updates take place during the maintenance window.</p>"""
    max_cpu_count: NotRequired["int"]
    """<p>The total number of CPU cores available on the Exadata infrastructure.</p>"""
    max_data_storage_in_t_bs: NotRequired["float"]
    """<p>The total amount of data disk group storage, in terabytes (TB), that's available on the Exadata infrastructure.</p>"""
    max_db_node_storage_size_in_g_bs: NotRequired["int"]
    """<p>The total amount of local node storage, in gigabytes (GB), that's available on the Exadata infrastructure.</p>"""
    max_memory_in_g_bs: NotRequired["int"]
    """<p>The total amount of memory, in gigabytes (GB), that's available on the Exadata infrastructure.</p>"""
    memory_size_in_g_bs: NotRequired["int"]
    """<p>The amount of memory, in gigabytes (GB), that's allocated on the Exadata infrastructure.</p>"""
    monthly_db_server_version: NotRequired["str"]
    """<p>The monthly software version of the database servers installed on the Exadata infrastructure.</p>"""
    monthly_storage_server_version: NotRequired["str"]
    """<p>The monthly software version of the storage servers installed on the Exadata infrastructure.</p>"""
    next_maintenance_run_id: NotRequired["str"]
    """<p>The OCID of the next maintenance run for the Exadata infrastructure.</p>"""
    oci_resource_anchor_name: NotRequired["str"]
    """<p>The name of the OCI resource anchor for the Exadata infrastructure.</p>"""
    oci_url: NotRequired["str"]
    """<p>The HTTPS link to the Exadata infrastructure in OCI.</p>"""
    ocid: NotRequired["str"]
    """<p>The OCID of the Exadata infrastructure.</p>"""
    shape: NotRequired["str"]
    """<p>The model name of the Exadata infrastructure.</p>"""
    storage_count: NotRequired["int"]
    """<p>The number of storage servers that are activated for the Exadata infrastructure.</p>"""
    storage_server_version: NotRequired["str"]
    """<p>The software version of the storage servers on the Exadata infrastructure.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the Exadata infrastructure was created.</p>"""
    total_storage_size_in_g_bs: NotRequired["int"]
    """<p>The total amount of storage, in gigabytes (GB), on the the Exadata infrastructure.</p>"""
    percent_progress: NotRequired["float"]
    """<p>The amount of progress made on the current operation on the Exadata infrastructure, expressed as a percentage.</p>"""
    database_server_type: NotRequired["str"]
    """<p>The database server model type of the Exadata infrastructure. For the list of valid model names, use the <code>ListDbSystemShapes</code> operation.</p>"""
    storage_server_type: NotRequired["str"]
    """<p>The storage server model type of the Exadata infrastructure. For the list of valid model names, use the <code>ListDbSystemShapes</code> operation.</p>"""
    compute_model: NotRequired["capo_odb.types.compute_model.ComputeModel"]
    """<p>The OCI model compute model used when you create or clone an instance: ECPU or OCPU. An ECPU is an abstracted measure of compute resources. ECPUs are based on the number of cores elastically allocated from a pool of compute and storage servers. An OCPU is a legacy physical measure of compute resources. OCPUs are based on the physical core of a processor with hyper-threading enabled. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CloudExadataInfrastructure) -> dict:
    out: dict = {}
    out["cloudExadataInfrastructureId"] = value["cloud_exadata_infrastructure_id"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "status" in value:
        import capo_odb.types.resource_status

        out["status"] = capo_odb.types.resource_status.serialize_aws_json_1_0(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "cloud_exadata_infrastructure_arn" in value:
        out["cloudExadataInfrastructureArn"] = value["cloud_exadata_infrastructure_arn"]
    if "activated_storage_count" in value:
        out["activatedStorageCount"] = value["activated_storage_count"]
    if "additional_storage_count" in value:
        out["additionalStorageCount"] = value["additional_storage_count"]
    if "available_storage_size_in_g_bs" in value:
        out["availableStorageSizeInGBs"] = value["available_storage_size_in_g_bs"]
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "availability_zone_id" in value:
        out["availabilityZoneId"] = value["availability_zone_id"]
    if "compute_count" in value:
        out["computeCount"] = value["compute_count"]
    if "cpu_count" in value:
        out["cpuCount"] = value["cpu_count"]
    if "customer_contacts_to_send_to_oci" in value:
        import capo_odb.types.customer_contacts

        out["customerContactsToSendToOCI"] = (
            capo_odb.types.customer_contacts.serialize_aws_json_1_0(
                value["customer_contacts_to_send_to_oci"]
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
    if "db_server_version" in value:
        out["dbServerVersion"] = value["db_server_version"]
    if "last_maintenance_run_id" in value:
        out["lastMaintenanceRunId"] = value["last_maintenance_run_id"]
    if "maintenance_window" in value:
        import capo_odb.types.maintenance_window

        out["maintenanceWindow"] = (
            capo_odb.types.maintenance_window.serialize_aws_json_1_0(
                value["maintenance_window"]
            )
        )
    if "max_cpu_count" in value:
        out["maxCpuCount"] = value["max_cpu_count"]
    if "max_data_storage_in_t_bs" in value:
        out["maxDataStorageInTBs"] = (
            "NaN"
            if value["max_data_storage_in_t_bs"] != value["max_data_storage_in_t_bs"]
            else "Infinity"
            if value["max_data_storage_in_t_bs"] == float("inf")
            else "-Infinity"
            if value["max_data_storage_in_t_bs"] == float("-inf")
            else value["max_data_storage_in_t_bs"]
        )
    if "max_db_node_storage_size_in_g_bs" in value:
        out["maxDbNodeStorageSizeInGBs"] = value["max_db_node_storage_size_in_g_bs"]
    if "max_memory_in_g_bs" in value:
        out["maxMemoryInGBs"] = value["max_memory_in_g_bs"]
    if "memory_size_in_g_bs" in value:
        out["memorySizeInGBs"] = value["memory_size_in_g_bs"]
    if "monthly_db_server_version" in value:
        out["monthlyDbServerVersion"] = value["monthly_db_server_version"]
    if "monthly_storage_server_version" in value:
        out["monthlyStorageServerVersion"] = value["monthly_storage_server_version"]
    if "next_maintenance_run_id" in value:
        out["nextMaintenanceRunId"] = value["next_maintenance_run_id"]
    if "oci_resource_anchor_name" in value:
        out["ociResourceAnchorName"] = value["oci_resource_anchor_name"]
    if "oci_url" in value:
        out["ociUrl"] = value["oci_url"]
    if "ocid" in value:
        out["ocid"] = value["ocid"]
    if "shape" in value:
        out["shape"] = value["shape"]
    if "storage_count" in value:
        out["storageCount"] = value["storage_count"]
    if "storage_server_version" in value:
        out["storageServerVersion"] = value["storage_server_version"]
    if "created_at" in value:
        import capo_odb._protocol.serialize

        out["createdAt"] = capo_odb._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "total_storage_size_in_g_bs" in value:
        out["totalStorageSizeInGBs"] = value["total_storage_size_in_g_bs"]
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
    if "database_server_type" in value:
        out["databaseServerType"] = value["database_server_type"]
    if "storage_server_type" in value:
        out["storageServerType"] = value["storage_server_type"]
    if "compute_model" in value:
        import capo_odb.types.compute_model

        out["computeModel"] = capo_odb.types.compute_model.serialize_aws_json_1_0(
            value["compute_model"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CloudExadataInfrastructure:
    out: CloudExadataInfrastructure = {}  # type: ignore[typeddict-item]
    if data.get("cloudExadataInfrastructureId") is not None:
        out["cloud_exadata_infrastructure_id"] = data["cloudExadataInfrastructureId"]
    else:
        raise DeserializationError(
            "CloudExadataInfrastructure.cloud_exadata_infrastructure_id required"
        )
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("status") is not None:
        import capo_odb.types.resource_status

        out["status"] = capo_odb.types.resource_status.deserialize_aws_json_1_0(
            data["status"]
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("cloudExadataInfrastructureArn") is not None:
        out["cloud_exadata_infrastructure_arn"] = data["cloudExadataInfrastructureArn"]
    if data.get("activatedStorageCount") is not None:
        out["activated_storage_count"] = data["activatedStorageCount"]
    if data.get("additionalStorageCount") is not None:
        out["additional_storage_count"] = data["additionalStorageCount"]
    if data.get("availableStorageSizeInGBs") is not None:
        out["available_storage_size_in_g_bs"] = data["availableStorageSizeInGBs"]
    if data.get("availabilityZone") is not None:
        out["availability_zone"] = data["availabilityZone"]
    if data.get("availabilityZoneId") is not None:
        out["availability_zone_id"] = data["availabilityZoneId"]
    if data.get("computeCount") is not None:
        out["compute_count"] = data["computeCount"]
    if data.get("cpuCount") is not None:
        out["cpu_count"] = data["cpuCount"]
    if data.get("customerContactsToSendToOCI") is not None:
        import capo_odb.types.customer_contacts

        out["customer_contacts_to_send_to_oci"] = (
            capo_odb.types.customer_contacts.deserialize_aws_json_1_0(
                data["customerContactsToSendToOCI"]
            )
        )
    if data.get("dataStorageSizeInTBs") is not None:
        out["data_storage_size_in_t_bs"] = float(data["dataStorageSizeInTBs"])
    if data.get("dbNodeStorageSizeInGBs") is not None:
        out["db_node_storage_size_in_g_bs"] = data["dbNodeStorageSizeInGBs"]
    if data.get("dbServerVersion") is not None:
        out["db_server_version"] = data["dbServerVersion"]
    if data.get("lastMaintenanceRunId") is not None:
        out["last_maintenance_run_id"] = data["lastMaintenanceRunId"]
    if data.get("maintenanceWindow") is not None:
        import capo_odb.types.maintenance_window

        out["maintenance_window"] = (
            capo_odb.types.maintenance_window.deserialize_aws_json_1_0(
                data["maintenanceWindow"]
            )
        )
    if data.get("maxCpuCount") is not None:
        out["max_cpu_count"] = data["maxCpuCount"]
    if data.get("maxDataStorageInTBs") is not None:
        out["max_data_storage_in_t_bs"] = float(data["maxDataStorageInTBs"])
    if data.get("maxDbNodeStorageSizeInGBs") is not None:
        out["max_db_node_storage_size_in_g_bs"] = data["maxDbNodeStorageSizeInGBs"]
    if data.get("maxMemoryInGBs") is not None:
        out["max_memory_in_g_bs"] = data["maxMemoryInGBs"]
    if data.get("memorySizeInGBs") is not None:
        out["memory_size_in_g_bs"] = data["memorySizeInGBs"]
    if data.get("monthlyDbServerVersion") is not None:
        out["monthly_db_server_version"] = data["monthlyDbServerVersion"]
    if data.get("monthlyStorageServerVersion") is not None:
        out["monthly_storage_server_version"] = data["monthlyStorageServerVersion"]
    if data.get("nextMaintenanceRunId") is not None:
        out["next_maintenance_run_id"] = data["nextMaintenanceRunId"]
    if data.get("ociResourceAnchorName") is not None:
        out["oci_resource_anchor_name"] = data["ociResourceAnchorName"]
    if data.get("ociUrl") is not None:
        out["oci_url"] = data["ociUrl"]
    if data.get("ocid") is not None:
        out["ocid"] = data["ocid"]
    if data.get("shape") is not None:
        out["shape"] = data["shape"]
    if data.get("storageCount") is not None:
        out["storage_count"] = data["storageCount"]
    if data.get("storageServerVersion") is not None:
        out["storage_server_version"] = data["storageServerVersion"]
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("totalStorageSizeInGBs") is not None:
        out["total_storage_size_in_g_bs"] = data["totalStorageSizeInGBs"]
    if data.get("percentProgress") is not None:
        out["percent_progress"] = float(data["percentProgress"])
    if data.get("databaseServerType") is not None:
        out["database_server_type"] = data["databaseServerType"]
    if data.get("storageServerType") is not None:
        out["storage_server_type"] = data["storageServerType"]
    if data.get("computeModel") is not None:
        import capo_odb.types.compute_model

        out["compute_model"] = capo_odb.types.compute_model.deserialize_aws_json_1_0(
            data["computeModel"]
        )
    return out


def redact_sensitive(value: CloudExadataInfrastructure) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "customer_contacts_to_send_to_oci" in value:
        import capo_odb.types.customer_contacts

        out["customer_contacts_to_send_to_oci"] = (
            capo_odb.types.customer_contacts.redact_sensitive(
                value["customer_contacts_to_send_to_oci"]
            )
        )
    return out
