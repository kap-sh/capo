"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#TelephonyChannelSubtypeConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.capacity
    import capo_connectcampaignsv2.types.queue_id
    import capo_connectcampaignsv2.types.telephony_outbound_config
    import capo_connectcampaignsv2.types.telephony_outbound_mode


class TelephonyChannelSubtypeConfig(TypedDict, closed=True):
    capacity: NotRequired["capo_connectcampaignsv2.types.capacity.Capacity"]
    connect_queue_id: NotRequired["capo_connectcampaignsv2.types.queue_id.QueueId"]
    outbound_mode: (
        "capo_connectcampaignsv2.types.telephony_outbound_mode.TelephonyOutboundMode"
    )
    default_outbound_config: "capo_connectcampaignsv2.types.telephony_outbound_config.TelephonyOutboundConfig"


# --- restJson1 ser/de ---
def serialize_json(value: TelephonyChannelSubtypeConfig) -> dict:
    out: dict = {}
    if "capacity" in value:
        out["capacity"] = (
            "NaN"
            if value["capacity"] != value["capacity"]
            else "Infinity"
            if value["capacity"] == float("inf")
            else "-Infinity"
            if value["capacity"] == float("-inf")
            else value["capacity"]
        )
    if "connect_queue_id" in value:
        out["connectQueueId"] = value["connect_queue_id"]
    import capo_connectcampaignsv2.types.telephony_outbound_mode

    out["outboundMode"] = (
        capo_connectcampaignsv2.types.telephony_outbound_mode.serialize_json(
            value["outbound_mode"]
        )
    )
    import capo_connectcampaignsv2.types.telephony_outbound_config

    out["defaultOutboundConfig"] = (
        capo_connectcampaignsv2.types.telephony_outbound_config.serialize_json(
            value["default_outbound_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> TelephonyChannelSubtypeConfig:
    out: TelephonyChannelSubtypeConfig = {}  # type: ignore[typeddict-item]
    if data.get("capacity") is not None:
        out["capacity"] = float(data["capacity"])
    if data.get("connectQueueId") is not None:
        out["connect_queue_id"] = data["connectQueueId"]
    if data.get("outboundMode") is not None:
        import capo_connectcampaignsv2.types.telephony_outbound_mode

        out["outbound_mode"] = (
            capo_connectcampaignsv2.types.telephony_outbound_mode.deserialize_json(
                data["outboundMode"]
            )
        )
    else:
        out["outbound_mode"] = {"$unknown": {"name": ""}}
    if data.get("defaultOutboundConfig") is not None:
        import capo_connectcampaignsv2.types.telephony_outbound_config

        out["default_outbound_config"] = (
            capo_connectcampaignsv2.types.telephony_outbound_config.deserialize_json(
                data["defaultOutboundConfig"]
            )
        )
    else:
        raise DeserializationError(
            "TelephonyChannelSubtypeConfig.default_outbound_config required"
        )
    return out
