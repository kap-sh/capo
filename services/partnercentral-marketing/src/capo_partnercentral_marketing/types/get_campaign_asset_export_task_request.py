"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#GetCampaignAssetExportTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_asset_export_task_id
    import capo_partnercentral_marketing.types.campaign_identifier
    import capo_partnercentral_marketing.types.catalog


class GetCampaignAssetExportTaskRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_marketing.types.catalog.Catalog"
    """The catalog (AWS or Sandbox)."""
    campaign_identifier: (
        "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier"
    )
    """The campaign that owns the export task. Accepts the campaign id or ARN. Required so the read is authorized on campaign/{CampaignId}; the task must belong to this campaign or the request resolves to not-found."""
    campaign_asset_export_task_identifier: "capo_partnercentral_marketing.types.campaign_asset_export_task_id.CampaignAssetExportTaskId"
    """The export task to retrieve: the `Id` StartCampaignAssetExportTask returned (`etsk-…`). An id only. An export task has no ARN: none is returned, recorded or authorized on (the read authorizes on its campaign), so there is no ARN to accept (DG-063 D-35)."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetCampaignAssetExportTaskRequest) -> dict:
    out: dict = {}
    import capo_partnercentral_marketing.types.catalog

    out["Catalog"] = capo_partnercentral_marketing.types.catalog.serialize_cbor(
        value["catalog"]
    )
    out["CampaignIdentifier"] = value["campaign_identifier"]
    out["CampaignAssetExportTaskIdentifier"] = value[
        "campaign_asset_export_task_identifier"
    ]
    return out


def deserialize_cbor(data: dict) -> GetCampaignAssetExportTaskRequest:
    out: GetCampaignAssetExportTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        import capo_partnercentral_marketing.types.catalog

        out["catalog"] = capo_partnercentral_marketing.types.catalog.deserialize_cbor(
            data["Catalog"]
        )
    else:
        import typing

        out["catalog"] = typing.cast(
            "capo_partnercentral_marketing.types.catalog.Catalog", ""
        )
    if data.get("CampaignIdentifier") is not None:
        out["campaign_identifier"] = data["CampaignIdentifier"]
    else:
        out["campaign_identifier"] = ""
    if data.get("CampaignAssetExportTaskIdentifier") is not None:
        out["campaign_asset_export_task_identifier"] = data[
            "CampaignAssetExportTaskIdentifier"
        ]
    else:
        out["campaign_asset_export_task_identifier"] = ""
    return out
