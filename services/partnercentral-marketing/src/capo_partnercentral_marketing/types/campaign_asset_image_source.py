"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignAssetImageSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_asset_id
    import capo_partnercentral_marketing.types.campaign_identifier
    import capo_partnercentral_marketing.types.template_field_id


class CampaignAssetImageSource(TypedDict, closed=True):
    campaign_identifier: (
        "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier"
    )
    """The source campaign's id or ARN."""
    campaign_asset_identifier: (
        "capo_partnercentral_marketing.types.campaign_asset_id.CampaignAssetId"
    )
    """The source asset's id."""
    field_id: "capo_partnercentral_marketing.types.template_field_id.TemplateFieldId"
    """The source image field."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignAssetImageSource) -> dict:
    out: dict = {}
    out["CampaignIdentifier"] = value["campaign_identifier"]
    out["CampaignAssetIdentifier"] = value["campaign_asset_identifier"]
    out["FieldId"] = value["field_id"]
    return out


def deserialize_cbor(data: dict) -> CampaignAssetImageSource:
    out: CampaignAssetImageSource = {}  # type: ignore[typeddict-item]
    if data.get("CampaignIdentifier") is not None:
        out["campaign_identifier"] = data["CampaignIdentifier"]
    else:
        out["campaign_identifier"] = ""
    if data.get("CampaignAssetIdentifier") is not None:
        out["campaign_asset_identifier"] = data["CampaignAssetIdentifier"]
    else:
        out["campaign_asset_identifier"] = ""
    if data.get("FieldId") is not None:
        out["field_id"] = data["FieldId"]
    else:
        out["field_id"] = ""
    return out
