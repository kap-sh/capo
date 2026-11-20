"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#GetCampaignTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_template_id
    import capo_partnercentral_marketing.types.catalog


class GetCampaignTemplateRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_marketing.types.catalog.Catalog"
    """The catalog (AWS or Sandbox)."""
    identifier: (
        "capo_partnercentral_marketing.types.campaign_template_id.CampaignTemplateId"
    )
    """The campaign template's id. A campaign template has no ARN (DG-084)."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetCampaignTemplateRequest) -> dict:
    out: dict = {}
    import capo_partnercentral_marketing.types.catalog

    out["Catalog"] = capo_partnercentral_marketing.types.catalog.serialize_cbor(
        value["catalog"]
    )
    out["Identifier"] = value["identifier"]
    return out


def deserialize_cbor(data: dict) -> GetCampaignTemplateRequest:
    out: GetCampaignTemplateRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    return out
