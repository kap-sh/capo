"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#GetCampaignAssetActivationTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_identifier
    import capo_partnercentral_marketing.types.catalog


class GetCampaignAssetActivationTaskRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_marketing.types.catalog.Catalog"
    """The catalog (AWS or Sandbox)."""
    campaign_identifier: (
        "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier"
    )
    """The campaign whose current task to read. This addresses the task, and also authorizes the call."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetCampaignAssetActivationTaskRequest) -> dict:
    out: dict = {}
    import capo_partnercentral_marketing.types.catalog

    out["Catalog"] = capo_partnercentral_marketing.types.catalog.serialize_cbor(
        value["catalog"]
    )
    out["CampaignIdentifier"] = value["campaign_identifier"]
    return out


def deserialize_cbor(data: dict) -> GetCampaignAssetActivationTaskRequest:
    out: GetCampaignAssetActivationTaskRequest = {}  # type: ignore[typeddict-item]
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
    return out
