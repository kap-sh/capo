"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#CampaignSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcampaigns.types.campaign_arn
    import capo_connectcampaigns.types.campaign_id
    import capo_connectcampaigns.types.campaign_name
    import capo_connectcampaigns.types.instance_id


class CampaignSummary(TypedDict, closed=True):
    id: "capo_connectcampaigns.types.campaign_id.CampaignId"
    arn: "capo_connectcampaigns.types.campaign_arn.CampaignArn"
    name: "capo_connectcampaigns.types.campaign_name.CampaignName"
    connect_instance_id: "capo_connectcampaigns.types.instance_id.InstanceId"


# --- restJson1 ser/de ---
def serialize_json(value: CampaignSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["connectInstanceId"] = value["connect_instance_id"]
    return out


def deserialize_json(data: dict) -> CampaignSummary:
    out: CampaignSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("connectInstanceId") is not None:
        out["connect_instance_id"] = data["connectInstanceId"]
    else:
        out["connect_instance_id"] = ""
    return out
