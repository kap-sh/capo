"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#StartCampaignAssetExportTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_asset_export_task_id
    import capo_partnercentral_marketing.types.campaign_asset_export_task_status


class StartCampaignAssetExportTaskResponse(TypedDict, closed=True):
    id: "capo_partnercentral_marketing.types.campaign_asset_export_task_id.CampaignAssetExportTaskId"
    """The export task identifier."""
    status: "capo_partnercentral_marketing.types.campaign_asset_export_task_status.CampaignAssetExportTaskStatus"
    """The task's state, always IN_PROGRESS at creation."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartCampaignAssetExportTaskResponse) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    import capo_partnercentral_marketing.types.campaign_asset_export_task_status

    out["Status"] = (
        capo_partnercentral_marketing.types.campaign_asset_export_task_status.serialize_cbor(
            value["status"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> StartCampaignAssetExportTaskResponse:
    out: StartCampaignAssetExportTaskResponse = {}  # type: ignore[typeddict-item]
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
    return out
