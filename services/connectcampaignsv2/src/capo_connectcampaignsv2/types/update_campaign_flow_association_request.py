"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#UpdateCampaignFlowAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.arn
    import capo_connectcampaignsv2.types.campaign_id


class UpdateCampaignFlowAssociationRequest(TypedDict, closed=True):
    id: "capo_connectcampaignsv2.types.campaign_id.CampaignId"
    connect_campaign_flow_arn: "capo_connectcampaignsv2.types.arn.Arn"


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCampaignFlowAssociationRequest) -> dict:
    out: dict = {}
    out["connectCampaignFlowArn"] = value["connect_campaign_flow_arn"]
    return out


def deserialize_json(data: dict) -> UpdateCampaignFlowAssociationRequest:
    out: UpdateCampaignFlowAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("connectCampaignFlowArn") is not None:
        out["connect_campaign_flow_arn"] = data["connectCampaignFlowArn"]
    else:
        out["connect_campaign_flow_arn"] = ""
    return out
