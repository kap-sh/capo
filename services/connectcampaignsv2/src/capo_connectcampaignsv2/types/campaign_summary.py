"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#CampaignSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.arn
    import capo_connectcampaignsv2.types.campaign_arn
    import capo_connectcampaignsv2.types.campaign_id
    import capo_connectcampaignsv2.types.campaign_name
    import capo_connectcampaignsv2.types.channel_subtype_list
    import capo_connectcampaignsv2.types.entry_limits_config
    import capo_connectcampaignsv2.types.external_campaign_type
    import capo_connectcampaignsv2.types.instance_id
    import capo_connectcampaignsv2.types.schedule


class CampaignSummary(TypedDict, closed=True):
    id: "capo_connectcampaignsv2.types.campaign_id.CampaignId"
    arn: "capo_connectcampaignsv2.types.campaign_arn.CampaignArn"
    name: "capo_connectcampaignsv2.types.campaign_name.CampaignName"
    connect_instance_id: "capo_connectcampaignsv2.types.instance_id.InstanceId"
    channel_subtypes: (
        "capo_connectcampaignsv2.types.channel_subtype_list.ChannelSubtypeList"
    )
    type: NotRequired[
        "capo_connectcampaignsv2.types.external_campaign_type.ExternalCampaignType"
    ]
    schedule: NotRequired["capo_connectcampaignsv2.types.schedule.Schedule"]
    entry_limits_config: NotRequired[
        "capo_connectcampaignsv2.types.entry_limits_config.EntryLimitsConfig"
    ]
    connect_campaign_flow_arn: NotRequired["capo_connectcampaignsv2.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: CampaignSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["connectInstanceId"] = value["connect_instance_id"]
    import capo_connectcampaignsv2.types.channel_subtype_list

    out["channelSubtypes"] = (
        capo_connectcampaignsv2.types.channel_subtype_list.serialize_json(
            value["channel_subtypes"]
        )
    )
    if "type" in value:
        out["type"] = value["type"]
    if "schedule" in value:
        import capo_connectcampaignsv2.types.schedule

        out["schedule"] = capo_connectcampaignsv2.types.schedule.serialize_json(
            value["schedule"]
        )
    if "entry_limits_config" in value:
        import capo_connectcampaignsv2.types.entry_limits_config

        out["entryLimitsConfig"] = (
            capo_connectcampaignsv2.types.entry_limits_config.serialize_json(
                value["entry_limits_config"]
            )
        )
    if "connect_campaign_flow_arn" in value:
        out["connectCampaignFlowArn"] = value["connect_campaign_flow_arn"]
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
    if data.get("channelSubtypes") is not None:
        import capo_connectcampaignsv2.types.channel_subtype_list

        out["channel_subtypes"] = (
            capo_connectcampaignsv2.types.channel_subtype_list.deserialize_json(
                data["channelSubtypes"]
            )
        )
    else:
        out["channel_subtypes"] = []
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("schedule") is not None:
        import capo_connectcampaignsv2.types.schedule

        out["schedule"] = capo_connectcampaignsv2.types.schedule.deserialize_json(
            data["schedule"]
        )
    if data.get("entryLimitsConfig") is not None:
        import capo_connectcampaignsv2.types.entry_limits_config

        out["entry_limits_config"] = (
            capo_connectcampaignsv2.types.entry_limits_config.deserialize_json(
                data["entryLimitsConfig"]
            )
        )
    if data.get("connectCampaignFlowArn") is not None:
        out["connect_campaign_flow_arn"] = data["connectCampaignFlowArn"]
    return out
