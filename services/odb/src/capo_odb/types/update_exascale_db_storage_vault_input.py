"""Generated from Smithy shape ``com.amazonaws.odb#UpdateExascaleDbStorageVaultInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.resource_display_name
    import capo_odb.types.resource_id_or_arn


class UpdateExascaleDbStorageVaultInput(TypedDict, closed=True):
    exascale_db_storage_vault_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the Exascale storage vault to update.</p>"""
    additional_flash_cache_in_percent: NotRequired["int"]
    """<p>The additional flash cache percentage for the Exascale storage vault.</p>"""
    autoscale_limit_in_g_bs: NotRequired["int"]
    """<p>The autoscale limit in gigabytes (GB) for the Exascale storage vault.</p>"""
    description: NotRequired["str"]
    """<p>A new description for the Exascale storage vault.</p>"""
    display_name: NotRequired[
        "capo_odb.types.resource_display_name.ResourceDisplayName"
    ]
    """<p>A new user-friendly name for the Exascale storage vault.</p>"""
    high_capacity_database_storage_total_size_in_g_bs: NotRequired["int"]
    """<p>The total size of the high-capacity database storage, in gigabytes (GB), for the Exascale storage vault.</p>"""
    is_autoscale_enabled: NotRequired["bool"]
    """<p>Specifies whether autoscaling is enabled for the Exascale storage vault.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateExascaleDbStorageVaultInput) -> dict:
    out: dict = {}
    out["exascaleDbStorageVaultId"] = value["exascale_db_storage_vault_id"]
    if "additional_flash_cache_in_percent" in value:
        out["additionalFlashCacheInPercent"] = value[
            "additional_flash_cache_in_percent"
        ]
    if "autoscale_limit_in_g_bs" in value:
        out["autoscaleLimitInGBs"] = value["autoscale_limit_in_g_bs"]
    if "description" in value:
        out["description"] = value["description"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "high_capacity_database_storage_total_size_in_g_bs" in value:
        out["highCapacityDatabaseStorageTotalSizeInGBs"] = value[
            "high_capacity_database_storage_total_size_in_g_bs"
        ]
    if "is_autoscale_enabled" in value:
        out["isAutoscaleEnabled"] = value["is_autoscale_enabled"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateExascaleDbStorageVaultInput:
    out: UpdateExascaleDbStorageVaultInput = {}  # type: ignore[typeddict-item]
    if data.get("exascaleDbStorageVaultId") is not None:
        out["exascale_db_storage_vault_id"] = data["exascaleDbStorageVaultId"]
    else:
        out["exascale_db_storage_vault_id"] = ""
    if data.get("additionalFlashCacheInPercent") is not None:
        out["additional_flash_cache_in_percent"] = data["additionalFlashCacheInPercent"]
    if data.get("autoscaleLimitInGBs") is not None:
        out["autoscale_limit_in_g_bs"] = data["autoscaleLimitInGBs"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("highCapacityDatabaseStorageTotalSizeInGBs") is not None:
        out["high_capacity_database_storage_total_size_in_g_bs"] = data[
            "highCapacityDatabaseStorageTotalSizeInGBs"
        ]
    if data.get("isAutoscaleEnabled") is not None:
        out["is_autoscale_enabled"] = data["isAutoscaleEnabled"]
    return out
