"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#GetCampaignAssetExportTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_asset_export_failure_reason
    import capo_partnercentral_marketing.types.campaign_asset_export_task_id
    import capo_partnercentral_marketing.types.campaign_asset_export_task_status
    import capo_partnercentral_marketing.types.presigned_url
    import capo_partnercentral_marketing.types.timestamp


class GetCampaignAssetExportTaskResponse(TypedDict, closed=True):
    id: "capo_partnercentral_marketing.types.campaign_asset_export_task_id.CampaignAssetExportTaskId"
    """The export task identifier."""
    status: "capo_partnercentral_marketing.types.campaign_asset_export_task_status.CampaignAssetExportTaskStatus"
    """The task's state."""
    created_at: NotRequired["capo_partnercentral_marketing.types.timestamp.Timestamp"]
    """When the task was created."""
    download_url: NotRequired[
        "capo_partnercentral_marketing.types.presigned_url.PresignedUrl"
    ]
    """Presigned GET URL for the ZIP archive. Present only when status is COMPLETED. Freshly minted on each call and short-lived (<=15 minutes)."""
    expires_at: NotRequired["capo_partnercentral_marketing.types.timestamp.Timestamp"]
    """When DownloadUrl expires. Present only when status is COMPLETED."""
    failure_reason: NotRequired[
        "capo_partnercentral_marketing.types.campaign_asset_export_failure_reason.CampaignAssetExportFailureReason"
    ]
    """Why the task failed. Present only when status is FAILED."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetCampaignAssetExportTaskResponse) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    import capo_partnercentral_marketing.types.campaign_asset_export_task_status

    out["Status"] = (
        capo_partnercentral_marketing.types.campaign_asset_export_task_status.serialize_cbor(
            value["status"]
        )
    )
    if "created_at" in value:
        import capo_partnercentral_marketing.types.timestamp

        out["CreatedAt"] = capo_partnercentral_marketing.types.timestamp.serialize_cbor(
            value["created_at"]
        )
    if "download_url" in value:
        out["DownloadUrl"] = value["download_url"]
    if "expires_at" in value:
        import capo_partnercentral_marketing.types.timestamp

        out["ExpiresAt"] = capo_partnercentral_marketing.types.timestamp.serialize_cbor(
            value["expires_at"]
        )
    if "failure_reason" in value:
        import capo_partnercentral_marketing.types.campaign_asset_export_failure_reason

        out["FailureReason"] = (
            capo_partnercentral_marketing.types.campaign_asset_export_failure_reason.serialize_cbor(
                value["failure_reason"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetCampaignAssetExportTaskResponse:
    out: GetCampaignAssetExportTaskResponse = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Status") is not None:
        import capo_partnercentral_marketing.types.campaign_asset_export_task_status

        out["status"] = (
            capo_partnercentral_marketing.types.campaign_asset_export_task_status.deserialize_cbor(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_partnercentral_marketing.types.campaign_asset_export_task_status.CampaignAssetExportTaskStatus",
            "",
        )
    if data.get("CreatedAt") is not None:
        import capo_partnercentral_marketing.types.timestamp

        out["created_at"] = (
            capo_partnercentral_marketing.types.timestamp.deserialize_cbor(
                data["CreatedAt"]
            )
        )
    if data.get("DownloadUrl") is not None:
        out["download_url"] = data["DownloadUrl"]
    if data.get("ExpiresAt") is not None:
        import capo_partnercentral_marketing.types.timestamp

        out["expires_at"] = (
            capo_partnercentral_marketing.types.timestamp.deserialize_cbor(
                data["ExpiresAt"]
            )
        )
    if data.get("FailureReason") is not None:
        import capo_partnercentral_marketing.types.campaign_asset_export_failure_reason

        out["failure_reason"] = (
            capo_partnercentral_marketing.types.campaign_asset_export_failure_reason.deserialize_cbor(
                data["FailureReason"]
            )
        )
    return out
