"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#WhatsAppChannelSubtypeConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.capacity
    import capo_connectcampaignsv2.types.whats_app_outbound_config
    import capo_connectcampaignsv2.types.whats_app_outbound_mode


class WhatsAppChannelSubtypeConfig(TypedDict, closed=True):
    capacity: NotRequired["capo_connectcampaignsv2.types.capacity.Capacity"]
    outbound_mode: (
        "capo_connectcampaignsv2.types.whats_app_outbound_mode.WhatsAppOutboundMode"
    )
    default_outbound_config: (
        "capo_connectcampaignsv2.types.whats_app_outbound_config.WhatsAppOutboundConfig"
    )


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppChannelSubtypeConfig) -> dict:
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
    import capo_connectcampaignsv2.types.whats_app_outbound_mode

    out["outboundMode"] = (
        capo_connectcampaignsv2.types.whats_app_outbound_mode.serialize_json(
            value["outbound_mode"]
        )
    )
    import capo_connectcampaignsv2.types.whats_app_outbound_config

    out["defaultOutboundConfig"] = (
        capo_connectcampaignsv2.types.whats_app_outbound_config.serialize_json(
            value["default_outbound_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> WhatsAppChannelSubtypeConfig:
    out: WhatsAppChannelSubtypeConfig = {}  # type: ignore[typeddict-item]
    if data.get("capacity") is not None:
        out["capacity"] = float(data["capacity"])
    if data.get("outboundMode") is not None:
        import capo_connectcampaignsv2.types.whats_app_outbound_mode

        out["outbound_mode"] = (
            capo_connectcampaignsv2.types.whats_app_outbound_mode.deserialize_json(
                data["outboundMode"]
            )
        )
    else:
        import capo_connectcampaignsv2.types._unknown

        out["outbound_mode"] = (
            capo_connectcampaignsv2.types._unknown.UnknownUnionMember("")
        )
    if data.get("defaultOutboundConfig") is not None:
        import capo_connectcampaignsv2.types.whats_app_outbound_config

        out["default_outbound_config"] = (
            capo_connectcampaignsv2.types.whats_app_outbound_config.deserialize_json(
                data["defaultOutboundConfig"]
            )
        )
    else:
        raise DeserializationError(
            "WhatsAppChannelSubtypeConfig.default_outbound_config required"
        )
    return out
