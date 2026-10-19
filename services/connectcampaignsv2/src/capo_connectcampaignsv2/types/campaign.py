"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#Campaign``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.arn
    import capo_connectcampaignsv2.types.campaign_arn
    import capo_connectcampaignsv2.types.campaign_id
    import capo_connectcampaignsv2.types.campaign_name
    import capo_connectcampaignsv2.types.channel_subtype_config
    import capo_connectcampaignsv2.types.communication_limits_config
    import capo_connectcampaignsv2.types.communication_time_config
    import capo_connectcampaignsv2.types.entry_limits_config
    import capo_connectcampaignsv2.types.external_campaign_type
    import capo_connectcampaignsv2.types.instance_id
    import capo_connectcampaignsv2.types.schedule
    import capo_connectcampaignsv2.types.source
    import capo_connectcampaignsv2.types.tag_map


class Campaign(TypedDict, closed=True):
    id: "capo_connectcampaignsv2.types.campaign_id.CampaignId"
    arn: "capo_connectcampaignsv2.types.campaign_arn.CampaignArn"
    name: "capo_connectcampaignsv2.types.campaign_name.CampaignName"
    connect_instance_id: "capo_connectcampaignsv2.types.instance_id.InstanceId"
    channel_subtype_config: NotRequired[
        "capo_connectcampaignsv2.types.channel_subtype_config.ChannelSubtypeConfig"
    ]
    type: NotRequired[
        "capo_connectcampaignsv2.types.external_campaign_type.ExternalCampaignType"
    ]
    source: NotRequired["capo_connectcampaignsv2.types.source.Source"]
    connect_campaign_flow_arn: NotRequired["capo_connectcampaignsv2.types.arn.Arn"]
    schedule: NotRequired["capo_connectcampaignsv2.types.schedule.Schedule"]
    entry_limits_config: NotRequired[
        "capo_connectcampaignsv2.types.entry_limits_config.EntryLimitsConfig"
    ]
    communication_time_config: NotRequired[
        "capo_connectcampaignsv2.types.communication_time_config.CommunicationTimeConfig"
    ]
    communication_limits_override: NotRequired[
        "capo_connectcampaignsv2.types.communication_limits_config.CommunicationLimitsConfig"
    ]
    tags: NotRequired["capo_connectcampaignsv2.types.tag_map.TagMap"]


# --- restJson1 ser/de ---
def serialize_json(value: Campaign) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["connectInstanceId"] = value["connect_instance_id"]
    if "channel_subtype_config" in value:
        import capo_connectcampaignsv2.types.channel_subtype_config

        out["channelSubtypeConfig"] = (
            capo_connectcampaignsv2.types.channel_subtype_config.serialize_json(
                value["channel_subtype_config"]
            )
        )
    if "type" in value:
        out["type"] = value["type"]
    if "source" in value:
        import capo_connectcampaignsv2.types.source

        out["source"] = capo_connectcampaignsv2.types.source.serialize_json(
            value["source"]
        )
    if "connect_campaign_flow_arn" in value:
        out["connectCampaignFlowArn"] = value["connect_campaign_flow_arn"]
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
    if "communication_time_config" in value:
        import capo_connectcampaignsv2.types.communication_time_config

        out["communicationTimeConfig"] = (
            capo_connectcampaignsv2.types.communication_time_config.serialize_json(
                value["communication_time_config"]
            )
        )
    if "communication_limits_override" in value:
        import capo_connectcampaignsv2.types.communication_limits_config

        out["communicationLimitsOverride"] = (
            capo_connectcampaignsv2.types.communication_limits_config.serialize_json(
                value["communication_limits_override"]
            )
        )
    if "tags" in value:
        import capo_connectcampaignsv2.types.tag_map

        out["tags"] = capo_connectcampaignsv2.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> Campaign:
    out: Campaign = {}  # type: ignore[typeddict-item]
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
    if data.get("channelSubtypeConfig") is not None:
        import capo_connectcampaignsv2.types.channel_subtype_config

        out["channel_subtype_config"] = (
            capo_connectcampaignsv2.types.channel_subtype_config.deserialize_json(
                data["channelSubtypeConfig"]
            )
        )
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("source") is not None:
        import capo_connectcampaignsv2.types.source

        out["source"] = capo_connectcampaignsv2.types.source.deserialize_json(
            data["source"]
        )
    if data.get("connectCampaignFlowArn") is not None:
        out["connect_campaign_flow_arn"] = data["connectCampaignFlowArn"]
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
    if data.get("communicationTimeConfig") is not None:
        import capo_connectcampaignsv2.types.communication_time_config

        out["communication_time_config"] = (
            capo_connectcampaignsv2.types.communication_time_config.deserialize_json(
                data["communicationTimeConfig"]
            )
        )
    if data.get("communicationLimitsOverride") is not None:
        import capo_connectcampaignsv2.types.communication_limits_config

        out["communication_limits_override"] = (
            capo_connectcampaignsv2.types.communication_limits_config.deserialize_json(
                data["communicationLimitsOverride"]
            )
        )
    if data.get("tags") is not None:
        import capo_connectcampaignsv2.types.tag_map

        out["tags"] = capo_connectcampaignsv2.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out


def redact_sensitive(value: Campaign) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "channel_subtype_config" in value:
        import capo_connectcampaignsv2.types.channel_subtype_config

        out["channel_subtype_config"] = (
            capo_connectcampaignsv2.types.channel_subtype_config.redact_sensitive(
                value["channel_subtype_config"]
            )
        )
    return out
