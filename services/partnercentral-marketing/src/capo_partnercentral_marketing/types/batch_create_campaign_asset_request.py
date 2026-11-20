"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#BatchCreateCampaignAssetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.batch_create_campaign_asset_entries
    import capo_partnercentral_marketing.types.campaign_identifier
    import capo_partnercentral_marketing.types.catalog


class BatchCreateCampaignAssetRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_marketing.types.catalog.Catalog"
    """The catalog (AWS or Sandbox)."""
    campaign_identifier: (
        "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier"
    )
    """The campaign identifier."""
    entries: "capo_partnercentral_marketing.types.batch_create_campaign_asset_entries.BatchCreateCampaignAssetEntries"
    """The blueprints to instantiate, one entry each."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BatchCreateCampaignAssetRequest) -> dict:
    out: dict = {}
    import capo_partnercentral_marketing.types.catalog

    out["Catalog"] = capo_partnercentral_marketing.types.catalog.serialize_cbor(
        value["catalog"]
    )
    out["CampaignIdentifier"] = value["campaign_identifier"]
    import capo_partnercentral_marketing.types.batch_create_campaign_asset_entries

    out["Entries"] = (
        capo_partnercentral_marketing.types.batch_create_campaign_asset_entries.serialize_cbor(
            value["entries"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> BatchCreateCampaignAssetRequest:
    out: BatchCreateCampaignAssetRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("Entries") is not None:
        import capo_partnercentral_marketing.types.batch_create_campaign_asset_entries

        out["entries"] = (
            capo_partnercentral_marketing.types.batch_create_campaign_asset_entries.deserialize_cbor(
                data["Entries"]
            )
        )
    else:
        out["entries"] = []
    return out
