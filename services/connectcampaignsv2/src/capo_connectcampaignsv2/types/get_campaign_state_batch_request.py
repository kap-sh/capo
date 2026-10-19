"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#GetCampaignStateBatchRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.campaign_id_list


class GetCampaignStateBatchRequest(TypedDict, closed=True):
    campaign_ids: "capo_connectcampaignsv2.types.campaign_id_list.CampaignIdList"


# --- restJson1 ser/de ---
def serialize_json(value: GetCampaignStateBatchRequest) -> dict:
    out: dict = {}
    import capo_connectcampaignsv2.types.campaign_id_list

    out["campaignIds"] = capo_connectcampaignsv2.types.campaign_id_list.serialize_json(
        value["campaign_ids"]
    )
    return out


def deserialize_json(data: dict) -> GetCampaignStateBatchRequest:
    out: GetCampaignStateBatchRequest = {}  # type: ignore[typeddict-item]
    if data.get("campaignIds") is not None:
        import capo_connectcampaignsv2.types.campaign_id_list

        out["campaign_ids"] = (
            capo_connectcampaignsv2.types.campaign_id_list.deserialize_json(
                data["campaignIds"]
            )
        )
    else:
        out["campaign_ids"] = []
    return out
