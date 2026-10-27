"""Generated from Smithy shape ``com.amazonaws.odb#CreateExascaleDbStorageVaultInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.general_input_string
    import capo_odb.types.request_tag_map
    import capo_odb.types.resource_display_name
    import capo_odb.types.resource_id_or_arn


class CreateExascaleDbStorageVaultInput(TypedDict, closed=True):
    display_name: "capo_odb.types.resource_display_name.ResourceDisplayName"
    """<p>A user-friendly name for the Exascale storage vault.</p>"""
    high_capacity_database_storage_total_size_in_g_bs: "int"
    """<p>The total size of the high-capacity database storage, in gigabytes (GB), for the Exascale storage vault.</p>"""
    additional_flash_cache_in_percent: NotRequired["int"]
    """<p>The additional flash cache percentage for the Exascale storage vault.</p>"""
    autoscale_limit_in_g_bs: NotRequired["int"]
    """<p>The autoscale limit in gigabytes (GB) for the Exascale storage vault.</p>"""
    cloud_exadata_infrastructure_id: NotRequired[
        "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    ]
    """<p>The unique identifier or Amazon Resource Name (ARN) of the Exadata infrastructure on which to create the Exascale storage vault. Specify this value to create the Exascale storage vault on dedicated Exadata infrastructure that has Exascale storage configured. If you specify <code>availabilityZone</code> or <code>availabilityZoneId</code>, the value must match the Availability Zone of the Exadata infrastructure. If you specify neither, the service uses the Availability Zone of the Exadata infrastructure.</p>"""
    availability_zone_id: NotRequired["str"]
    """<p>The Availability Zone ID for the Exascale storage vault.</p>"""
    availability_zone: NotRequired["str"]
    """<p>The Availability Zone for the Exascale storage vault.</p>"""
    description: NotRequired["str"]
    """<p>A description of the Exascale storage vault.</p>"""
    is_autoscale_enabled: NotRequired["bool"]
    """<p>Specifies whether autoscaling is enabled for the Exascale storage vault.</p>"""
    tags: NotRequired["capo_odb.types.request_tag_map.RequestTagMap"]
    """<p>The list of resource tags to apply to the Exascale storage vault.</p>"""
    time_zone: NotRequired["str"]
    """<p>The time zone for the Exascale storage vault.</p>"""
    client_token: NotRequired["capo_odb.types.general_input_string.GeneralInputString"]
    """<p>A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If you submit the same request twice with the same client token, the service ignores the second request and returns the result of the first. If you don't specify a client token, the AWS SDK automatically generates one. The client token is valid for up to 24 hours after it's first used.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateExascaleDbStorageVaultInput) -> dict:
    out: dict = {}
    out["displayName"] = value["display_name"]
    out["highCapacityDatabaseStorageTotalSizeInGBs"] = value[
        "high_capacity_database_storage_total_size_in_g_bs"
    ]
    if "additional_flash_cache_in_percent" in value:
        out["additionalFlashCacheInPercent"] = value[
            "additional_flash_cache_in_percent"
        ]
    if "autoscale_limit_in_g_bs" in value:
        out["autoscaleLimitInGBs"] = value["autoscale_limit_in_g_bs"]
    if "cloud_exadata_infrastructure_id" in value:
        out["cloudExadataInfrastructureId"] = value["cloud_exadata_infrastructure_id"]
    if "availability_zone_id" in value:
        out["availabilityZoneId"] = value["availability_zone_id"]
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "description" in value:
        out["description"] = value["description"]
    if "is_autoscale_enabled" in value:
        out["isAutoscaleEnabled"] = value["is_autoscale_enabled"]
    if "tags" in value:
        import capo_odb.types.request_tag_map

        out["tags"] = capo_odb.types.request_tag_map.serialize_aws_json_1_0(
            value["tags"]
        )
    if "time_zone" in value:
        out["timeZone"] = value["time_zone"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateExascaleDbStorageVaultInput:
    out: CreateExascaleDbStorageVaultInput = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        out["display_name"] = ""
    if data.get("highCapacityDatabaseStorageTotalSizeInGBs") is not None:
        out["high_capacity_database_storage_total_size_in_g_bs"] = data[
            "highCapacityDatabaseStorageTotalSizeInGBs"
        ]
    else:
        out["high_capacity_database_storage_total_size_in_g_bs"] = 0
    if data.get("additionalFlashCacheInPercent") is not None:
        out["additional_flash_cache_in_percent"] = data["additionalFlashCacheInPercent"]
    if data.get("autoscaleLimitInGBs") is not None:
        out["autoscale_limit_in_g_bs"] = data["autoscaleLimitInGBs"]
    if data.get("cloudExadataInfrastructureId") is not None:
        out["cloud_exadata_infrastructure_id"] = data["cloudExadataInfrastructureId"]
    if data.get("availabilityZoneId") is not None:
        out["availability_zone_id"] = data["availabilityZoneId"]
    if data.get("availabilityZone") is not None:
        out["availability_zone"] = data["availabilityZone"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("isAutoscaleEnabled") is not None:
        out["is_autoscale_enabled"] = data["isAutoscaleEnabled"]
    if data.get("tags") is not None:
        import capo_odb.types.request_tag_map

        out["tags"] = capo_odb.types.request_tag_map.deserialize_aws_json_1_0(
            data["tags"]
        )
    if data.get("timeZone") is not None:
        out["time_zone"] = data["timeZone"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
