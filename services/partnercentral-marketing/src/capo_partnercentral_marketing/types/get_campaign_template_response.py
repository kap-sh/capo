"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#GetCampaignTemplateResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_partnercentral_marketing.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_template


class GetCampaignTemplateResponse(TypedDict, closed=True):
    campaign_template: (
        "capo_partnercentral_marketing.types.campaign_template.CampaignTemplate"
    )
    """The campaign template, including its asset templates."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetCampaignTemplateResponse) -> dict:
    out: dict = {}
    import capo_partnercentral_marketing.types.campaign_template

    out["CampaignTemplate"] = (
        capo_partnercentral_marketing.types.campaign_template.serialize_cbor(
            value["campaign_template"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> GetCampaignTemplateResponse:
    out: GetCampaignTemplateResponse = {}  # type: ignore[typeddict-item]
    if data.get("CampaignTemplate") is not None:
        import capo_partnercentral_marketing.types.campaign_template

        out["campaign_template"] = (
            capo_partnercentral_marketing.types.campaign_template.deserialize_cbor(
                data["CampaignTemplate"]
            )
        )
    else:
        raise DeserializationError(
            "GetCampaignTemplateResponse.campaign_template required"
        )
    return out


def redact_sensitive(value: GetCampaignTemplateResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "campaign_template" in value:
        import capo_partnercentral_marketing.types.campaign_template

        out["campaign_template"] = (
            capo_partnercentral_marketing.types.campaign_template.redact_sensitive(
                value["campaign_template"]
            )
        )
    return out
