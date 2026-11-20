"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#BatchCreateCampaignAssetResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_asset_id
    import capo_partnercentral_marketing.types.campaign_asset_layout
    import capo_partnercentral_marketing.types.identifier


class BatchCreateCampaignAssetResult(TypedDict, closed=True):
    source_asset_template_id: (
        "capo_partnercentral_marketing.types.identifier.Identifier"
    )
    """The entry's request identifier."""
    id: "capo_partnercentral_marketing.types.campaign_asset_id.CampaignAssetId"
    """The asset's identifier, derived from (CampaignId, SourceAssetTemplateId) rather than minted, so the same entry always resolves to the same id."""
    layout: NotRequired[
        "capo_partnercentral_marketing.types.campaign_asset_layout.CampaignAssetLayout"
    ]
    """For a multi-layout blueprint, the asset's layout options, so a client can render the first layout picker without reading each asset back. Nothing is selected at creation. Absent for a single-layout blueprint."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BatchCreateCampaignAssetResult) -> dict:
    out: dict = {}
    out["SourceAssetTemplateId"] = value["source_asset_template_id"]
    out["Id"] = value["id"]
    if "layout" in value:
        import capo_partnercentral_marketing.types.campaign_asset_layout

        out["Layout"] = (
            capo_partnercentral_marketing.types.campaign_asset_layout.serialize_cbor(
                value["layout"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> BatchCreateCampaignAssetResult:
    out: BatchCreateCampaignAssetResult = {}  # type: ignore[typeddict-item]
    if data.get("SourceAssetTemplateId") is not None:
        out["source_asset_template_id"] = data["SourceAssetTemplateId"]
    else:
        out["source_asset_template_id"] = ""
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Layout") is not None:
        import capo_partnercentral_marketing.types.campaign_asset_layout

        out["layout"] = (
            capo_partnercentral_marketing.types.campaign_asset_layout.deserialize_cbor(
                data["Layout"]
            )
        )
    return out
