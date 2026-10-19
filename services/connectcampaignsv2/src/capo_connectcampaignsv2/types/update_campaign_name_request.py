"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#UpdateCampaignNameRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.campaign_id
    import capo_connectcampaignsv2.types.campaign_name


class UpdateCampaignNameRequest(TypedDict, closed=True):
    id: "capo_connectcampaignsv2.types.campaign_id.CampaignId"
    name: "capo_connectcampaignsv2.types.campaign_name.CampaignName"


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCampaignNameRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateCampaignNameRequest:
    out: UpdateCampaignNameRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
