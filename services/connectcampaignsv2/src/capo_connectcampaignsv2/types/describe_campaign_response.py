"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#DescribeCampaignResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.campaign


class DescribeCampaignResponse(TypedDict, closed=True):
    campaign: NotRequired["capo_connectcampaignsv2.types.campaign.Campaign"]


# --- restJson1 ser/de ---
def serialize_json(value: DescribeCampaignResponse) -> dict:
    out: dict = {}
    if "campaign" in value:
        import capo_connectcampaignsv2.types.campaign

        out["campaign"] = capo_connectcampaignsv2.types.campaign.serialize_json(
            value["campaign"]
        )
    return out


def deserialize_json(data: dict) -> DescribeCampaignResponse:
    out: DescribeCampaignResponse = {}  # type: ignore[typeddict-item]
    if data.get("campaign") is not None:
        import capo_connectcampaignsv2.types.campaign

        out["campaign"] = capo_connectcampaignsv2.types.campaign.deserialize_json(
            data["campaign"]
        )
    return out


def redact_sensitive(value: DescribeCampaignResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "campaign" in value:
        import capo_connectcampaignsv2.types.campaign

        out["campaign"] = capo_connectcampaignsv2.types.campaign.redact_sensitive(
            value["campaign"]
        )
    return out
