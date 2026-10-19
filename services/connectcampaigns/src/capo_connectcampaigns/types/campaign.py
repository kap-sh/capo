"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#Campaign``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connectcampaigns.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcampaigns.types.campaign_arn
    import capo_connectcampaigns.types.campaign_id
    import capo_connectcampaigns.types.campaign_name
    import capo_connectcampaigns.types.dialer_config
    import capo_connectcampaigns.types.instance_id
    import capo_connectcampaigns.types.outbound_call_config
    import capo_connectcampaigns.types.tag_map


class Campaign(TypedDict, closed=True):
    id: "capo_connectcampaigns.types.campaign_id.CampaignId"
    arn: "capo_connectcampaigns.types.campaign_arn.CampaignArn"
    name: "capo_connectcampaigns.types.campaign_name.CampaignName"
    connect_instance_id: "capo_connectcampaigns.types.instance_id.InstanceId"
    dialer_config: "capo_connectcampaigns.types.dialer_config.DialerConfig"
    outbound_call_config: (
        "capo_connectcampaigns.types.outbound_call_config.OutboundCallConfig"
    )
    tags: NotRequired["capo_connectcampaigns.types.tag_map.TagMap"]


# --- restJson1 ser/de ---
def serialize_json(value: Campaign) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["connectInstanceId"] = value["connect_instance_id"]
    import capo_connectcampaigns.types.dialer_config

    out["dialerConfig"] = capo_connectcampaigns.types.dialer_config.serialize_json(
        value["dialer_config"]
    )
    import capo_connectcampaigns.types.outbound_call_config

    out["outboundCallConfig"] = (
        capo_connectcampaigns.types.outbound_call_config.serialize_json(
            value["outbound_call_config"]
        )
    )
    if "tags" in value:
        import capo_connectcampaigns.types.tag_map

        out["tags"] = capo_connectcampaigns.types.tag_map.serialize_json(value["tags"])
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
    if data.get("dialerConfig") is not None:
        import capo_connectcampaigns.types.dialer_config

        out["dialer_config"] = (
            capo_connectcampaigns.types.dialer_config.deserialize_json(
                data["dialerConfig"]
            )
        )
    else:
        import capo_connectcampaigns.types._unknown

        out["dialer_config"] = capo_connectcampaigns.types._unknown.UnknownUnionMember(
            ""
        )
    if data.get("outboundCallConfig") is not None:
        import capo_connectcampaigns.types.outbound_call_config

        out["outbound_call_config"] = (
            capo_connectcampaigns.types.outbound_call_config.deserialize_json(
                data["outboundCallConfig"]
            )
        )
    else:
        raise DeserializationError("Campaign.outbound_call_config required")
    if data.get("tags") is not None:
        import capo_connectcampaigns.types.tag_map

        out["tags"] = capo_connectcampaigns.types.tag_map.deserialize_json(data["tags"])
    return out
