"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#BatchCreateCampaignAssetEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.identifier


class BatchCreateCampaignAssetEntry(TypedDict, closed=True):
    source_asset_template_identifier: (
        "capo_partnercentral_marketing.types.identifier.Identifier"
    )
    """The asset template to instantiate, as returned by GetCampaignTemplate in CampaignTemplate.AssetTemplates[].id. Must belong to the campaign's own campaign template. An asset's editable field schema is copied from this blueprint at creation and pinned, so an asset without one could be neither validated on update nor made live. Also this entry's request identifier: it MUST be unique across the request's entries, since a campaign holds at most one asset per blueprint (I-15) and two entries naming the same blueprint could not both succeed."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BatchCreateCampaignAssetEntry) -> dict:
    out: dict = {}
    out["SourceAssetTemplateIdentifier"] = value["source_asset_template_identifier"]
    return out


def deserialize_cbor(data: dict) -> BatchCreateCampaignAssetEntry:
    out: BatchCreateCampaignAssetEntry = {}  # type: ignore[typeddict-item]
    if data.get("SourceAssetTemplateIdentifier") is not None:
        out["source_asset_template_identifier"] = data["SourceAssetTemplateIdentifier"]
    else:
        out["source_asset_template_identifier"] = ""
    return out
