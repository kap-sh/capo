"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#GetCampaignResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_partnercentral_marketing.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign


class GetCampaignResponse(TypedDict, closed=True):
    campaign: "capo_partnercentral_marketing.types.campaign.Campaign"
    """The campaign."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetCampaignResponse) -> dict:
    out: dict = {}
    import capo_partnercentral_marketing.types.campaign

    out["Campaign"] = capo_partnercentral_marketing.types.campaign.serialize_cbor(
        value["campaign"]
    )
    return out


def deserialize_cbor(data: dict) -> GetCampaignResponse:
    out: GetCampaignResponse = {}  # type: ignore[typeddict-item]
    if data.get("Campaign") is not None:
        import capo_partnercentral_marketing.types.campaign

        out["campaign"] = capo_partnercentral_marketing.types.campaign.deserialize_cbor(
            data["Campaign"]
        )
    else:
        raise DeserializationError("GetCampaignResponse.campaign required")
    return out


def redact_sensitive(value: GetCampaignResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "campaign" in value:
        import capo_partnercentral_marketing.types.campaign

        out["campaign"] = capo_partnercentral_marketing.types.campaign.redact_sensitive(
            value["campaign"]
        )
    return out
