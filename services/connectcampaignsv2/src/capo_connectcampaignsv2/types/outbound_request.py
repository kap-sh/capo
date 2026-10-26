"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#OutboundRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.channel_subtype_parameters
    import capo_connectcampaignsv2.types.client_token
    import capo_connectcampaignsv2.types.time_stamp


class OutboundRequest(TypedDict, closed=True):
    client_token: "capo_connectcampaignsv2.types.client_token.ClientToken"
    expiration_time: "capo_connectcampaignsv2.types.time_stamp.TimeStamp"
    channel_subtype_parameters: "capo_connectcampaignsv2.types.channel_subtype_parameters.ChannelSubtypeParameters"


# --- restJson1 ser/de ---
def serialize_json(value: OutboundRequest) -> dict:
    out: dict = {}
    out["clientToken"] = value["client_token"]
    import capo_connectcampaignsv2.types.time_stamp

    out["expirationTime"] = capo_connectcampaignsv2.types.time_stamp.serialize_json(
        value["expiration_time"]
    )
    import capo_connectcampaignsv2.types.channel_subtype_parameters

    out["channelSubtypeParameters"] = (
        capo_connectcampaignsv2.types.channel_subtype_parameters.serialize_json(
            value["channel_subtype_parameters"]
        )
    )
    return out


def deserialize_json(data: dict) -> OutboundRequest:
    out: OutboundRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        out["client_token"] = ""
    if data.get("expirationTime") is not None:
        import capo_connectcampaignsv2.types.time_stamp

        out["expiration_time"] = (
            capo_connectcampaignsv2.types.time_stamp.deserialize_json(
                data["expirationTime"]
            )
        )
    else:
        import datetime

        out["expiration_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("channelSubtypeParameters") is not None:
        import capo_connectcampaignsv2.types.channel_subtype_parameters

        out["channel_subtype_parameters"] = (
            capo_connectcampaignsv2.types.channel_subtype_parameters.deserialize_json(
                data["channelSubtypeParameters"]
            )
        )
    else:
        out["channel_subtype_parameters"] = {"$unknown": {"name": ""}}
    return out


def redact_sensitive(value: OutboundRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "channel_subtype_parameters" in value:
        import capo_connectcampaignsv2.types.channel_subtype_parameters

        out["channel_subtype_parameters"] = (
            capo_connectcampaignsv2.types.channel_subtype_parameters.redact_sensitive(
                value["channel_subtype_parameters"]
            )
        )
    return out
