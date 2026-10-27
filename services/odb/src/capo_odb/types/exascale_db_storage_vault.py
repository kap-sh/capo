"""Generated from Smithy shape ``com.amazonaws.odb#ExascaleDbStorageVault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_odb.types.exascale_db_storage_details
    import capo_odb.types.exascale_db_storage_vault_type
    import capo_odb.types.resource_arn
    import capo_odb.types.resource_arn_list
    import capo_odb.types.resource_id
    import capo_odb.types.resource_id_list
    import capo_odb.types.resource_id_or_arn
    import capo_odb.types.resource_status
    import capo_odb.types.shape_attribute_list


class ExascaleDbStorageVault(TypedDict, closed=True):
    exascale_db_storage_vault_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the Exascale storage vault.</p>"""
    additional_flash_cache_in_percent: NotRequired["int"]
    """<p>The additional flash cache percentage for the Exascale storage vault.</p>"""
    attached_shape_attributes: NotRequired[
        "capo_odb.types.shape_attribute_list.ShapeAttributeList"
    ]
    """<p>The list of shape attributes attached to the Exascale storage vault.</p>"""
    autoscale_limit_in_g_bs: NotRequired["int"]
    """<p>The autoscale limit in gigabytes (GB) for the Exascale storage vault.</p>"""
    availability_zone: NotRequired["str"]
    """<p>The Availability Zone for the Exascale storage vault.</p>"""
    availability_zone_id: NotRequired["str"]
    """<p>The Availability Zone ID for the Exascale storage vault.</p>"""
    cloud_exadata_infrastructure_arn: NotRequired[
        "capo_odb.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Exadata infrastructure that hosts the Exascale storage vault. This value is present only for vaults on dedicated Exadata infrastructure.</p>"""
    cloud_exadata_infrastructure_id: NotRequired[
        "capo_odb.types.resource_id.ResourceId"
    ]
    """<p>The unique identifier of the Exadata infrastructure that hosts the Exascale storage vault. This value is present only for vaults on dedicated Exadata infrastructure.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the Exascale storage vault was created.</p>"""
    description: NotRequired["str"]
    """<p>The description of the Exascale storage vault.</p>"""
    display_name: NotRequired["str"]
    """<p>The user-friendly name for the Exascale storage vault.</p>"""
    vm_cluster_arns: NotRequired["capo_odb.types.resource_arn_list.ResourceArnList"]
    """<p>The list of Amazon Resource Names (ARNs) of the VM clusters associated with this Exascale storage vault.</p>"""
    vm_cluster_count: NotRequired["int"]
    """<p>The number of VM clusters associated with this Exascale storage vault.</p>"""
    vm_cluster_ids: NotRequired["capo_odb.types.resource_id_list.ResourceIdList"]
    """<p>The list of unique identifiers of the VM clusters associated with this Exascale storage vault.</p>"""
    exascale_db_storage_vault_arn: NotRequired[
        "capo_odb.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Exascale storage vault.</p>"""
    high_capacity_database_storage: NotRequired[
        "capo_odb.types.exascale_db_storage_details.ExascaleDbStorageDetails"
    ]
    """<p>The high-capacity database storage details for the Exascale storage vault.</p>"""
    is_autoscale_enabled: NotRequired["bool"]
    """<p>Specifies whether autoscaling is enabled for the Exascale storage vault.</p>"""
    ocid: NotRequired["str"]
    """<p>The OCID of the Exascale storage vault.</p>"""
    oci_resource_anchor_name: NotRequired["str"]
    """<p>The name of the OCI resource anchor for the Exascale storage vault.</p>"""
    oci_url: NotRequired["str"]
    """<p>The HTTPS link to the Exascale storage vault in Oracle Cloud Infrastructure (OCI).</p>"""
    percent_progress: NotRequired["float"]
    """<p>The amount of progress made on the current operation on the Exascale storage vault, expressed as a percentage.</p>"""
    status: NotRequired["capo_odb.types.resource_status.ResourceStatus"]
    """<p>The current status of the Exascale storage vault.</p>"""
    status_reason: NotRequired["str"]
    """<p>Additional information about the status of the Exascale storage vault.</p>"""
    time_zone: NotRequired["str"]
    """<p>The time zone of the Exascale storage vault.</p>"""
    vault_type: NotRequired[
        "capo_odb.types.exascale_db_storage_vault_type.ExascaleDbStorageVaultType"
    ]
    """<p>The type of infrastructure that hosts the Exascale storage vault.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExascaleDbStorageVault) -> dict:
    out: dict = {}
    out["exascaleDbStorageVaultId"] = value["exascale_db_storage_vault_id"]
    if "additional_flash_cache_in_percent" in value:
        out["additionalFlashCacheInPercent"] = value[
            "additional_flash_cache_in_percent"
        ]
    if "attached_shape_attributes" in value:
        import capo_odb.types.shape_attribute_list

        out["attachedShapeAttributes"] = (
            capo_odb.types.shape_attribute_list.serialize_aws_json_1_0(
                value["attached_shape_attributes"]
            )
        )
    if "autoscale_limit_in_g_bs" in value:
        out["autoscaleLimitInGBs"] = value["autoscale_limit_in_g_bs"]
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "availability_zone_id" in value:
        out["availabilityZoneId"] = value["availability_zone_id"]
    if "cloud_exadata_infrastructure_arn" in value:
        out["cloudExadataInfrastructureArn"] = value["cloud_exadata_infrastructure_arn"]
    if "cloud_exadata_infrastructure_id" in value:
        out["cloudExadataInfrastructureId"] = value["cloud_exadata_infrastructure_id"]
    if "created_at" in value:
        import capo_odb._protocol.serialize

        out["createdAt"] = capo_odb._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "vm_cluster_arns" in value:
        import capo_odb.types.resource_arn_list

        out["vmClusterArns"] = capo_odb.types.resource_arn_list.serialize_aws_json_1_0(
            value["vm_cluster_arns"]
        )
    if "vm_cluster_count" in value:
        out["vmClusterCount"] = value["vm_cluster_count"]
    if "vm_cluster_ids" in value:
        import capo_odb.types.resource_id_list

        out["vmClusterIds"] = capo_odb.types.resource_id_list.serialize_aws_json_1_0(
            value["vm_cluster_ids"]
        )
    if "exascale_db_storage_vault_arn" in value:
        out["exascaleDbStorageVaultArn"] = value["exascale_db_storage_vault_arn"]
    if "high_capacity_database_storage" in value:
        import capo_odb.types.exascale_db_storage_details

        out["highCapacityDatabaseStorage"] = (
            capo_odb.types.exascale_db_storage_details.serialize_aws_json_1_0(
                value["high_capacity_database_storage"]
            )
        )
    if "is_autoscale_enabled" in value:
        out["isAutoscaleEnabled"] = value["is_autoscale_enabled"]
    if "ocid" in value:
        out["ocid"] = value["ocid"]
    if "oci_resource_anchor_name" in value:
        out["ociResourceAnchorName"] = value["oci_resource_anchor_name"]
    if "oci_url" in value:
        out["ociUrl"] = value["oci_url"]
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
    if "status" in value:
        import capo_odb.types.resource_status

        out["status"] = capo_odb.types.resource_status.serialize_aws_json_1_0(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "time_zone" in value:
        out["timeZone"] = value["time_zone"]
    if "vault_type" in value:
        import capo_odb.types.exascale_db_storage_vault_type

        out["vaultType"] = (
            capo_odb.types.exascale_db_storage_vault_type.serialize_aws_json_1_0(
                value["vault_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ExascaleDbStorageVault:
    out: ExascaleDbStorageVault = {}  # type: ignore[typeddict-item]
    if data.get("exascaleDbStorageVaultId") is not None:
        out["exascale_db_storage_vault_id"] = data["exascaleDbStorageVaultId"]
    else:
        out["exascale_db_storage_vault_id"] = ""
    if data.get("additionalFlashCacheInPercent") is not None:
        out["additional_flash_cache_in_percent"] = data["additionalFlashCacheInPercent"]
    if data.get("attachedShapeAttributes") is not None:
        import capo_odb.types.shape_attribute_list

        out["attached_shape_attributes"] = (
            capo_odb.types.shape_attribute_list.deserialize_aws_json_1_0(
                data["attachedShapeAttributes"]
            )
        )
    if data.get("autoscaleLimitInGBs") is not None:
        out["autoscale_limit_in_g_bs"] = data["autoscaleLimitInGBs"]
    if data.get("availabilityZone") is not None:
        out["availability_zone"] = data["availabilityZone"]
    if data.get("availabilityZoneId") is not None:
        out["availability_zone_id"] = data["availabilityZoneId"]
    if data.get("cloudExadataInfrastructureArn") is not None:
        out["cloud_exadata_infrastructure_arn"] = data["cloudExadataInfrastructureArn"]
    if data.get("cloudExadataInfrastructureId") is not None:
        out["cloud_exadata_infrastructure_id"] = data["cloudExadataInfrastructureId"]
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("vmClusterArns") is not None:
        import capo_odb.types.resource_arn_list

        out["vm_cluster_arns"] = (
            capo_odb.types.resource_arn_list.deserialize_aws_json_1_0(
                data["vmClusterArns"]
            )
        )
    if data.get("vmClusterCount") is not None:
        out["vm_cluster_count"] = data["vmClusterCount"]
    if data.get("vmClusterIds") is not None:
        import capo_odb.types.resource_id_list

        out["vm_cluster_ids"] = (
            capo_odb.types.resource_id_list.deserialize_aws_json_1_0(
                data["vmClusterIds"]
            )
        )
    if data.get("exascaleDbStorageVaultArn") is not None:
        out["exascale_db_storage_vault_arn"] = data["exascaleDbStorageVaultArn"]
    if data.get("highCapacityDatabaseStorage") is not None:
        import capo_odb.types.exascale_db_storage_details

        out["high_capacity_database_storage"] = (
            capo_odb.types.exascale_db_storage_details.deserialize_aws_json_1_0(
                data["highCapacityDatabaseStorage"]
            )
        )
    if data.get("isAutoscaleEnabled") is not None:
        out["is_autoscale_enabled"] = data["isAutoscaleEnabled"]
    if data.get("ocid") is not None:
        out["ocid"] = data["ocid"]
    if data.get("ociResourceAnchorName") is not None:
        out["oci_resource_anchor_name"] = data["ociResourceAnchorName"]
    if data.get("ociUrl") is not None:
        out["oci_url"] = data["ociUrl"]
    if data.get("percentProgress") is not None:
        out["percent_progress"] = float(data["percentProgress"])
    if data.get("status") is not None:
        import capo_odb.types.resource_status

        out["status"] = capo_odb.types.resource_status.deserialize_aws_json_1_0(
            data["status"]
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("timeZone") is not None:
        out["time_zone"] = data["timeZone"]
    if data.get("vaultType") is not None:
        import capo_odb.types.exascale_db_storage_vault_type

        out["vault_type"] = (
            capo_odb.types.exascale_db_storage_vault_type.deserialize_aws_json_1_0(
                data["vaultType"]
            )
        )
    return out
