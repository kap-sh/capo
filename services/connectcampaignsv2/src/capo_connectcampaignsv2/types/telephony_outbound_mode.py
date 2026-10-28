"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#TelephonyOutboundMode``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcampaignsv2.errors import DeserializationError, SerializationError
from capo_connectcampaignsv2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.agentless_config
    import capo_connectcampaignsv2.types.predictive_config
    import capo_connectcampaignsv2.types.preview_config
    import capo_connectcampaignsv2.types.progressive_config


class TelephonyOutboundModeProgressiveMember(TypedDict, closed=True):
    progressive: "capo_connectcampaignsv2.types.progressive_config.ProgressiveConfig"


class TelephonyOutboundModePredictiveMember(TypedDict, closed=True):
    predictive: "capo_connectcampaignsv2.types.predictive_config.PredictiveConfig"


class TelephonyOutboundModeAgentlessMember(TypedDict, closed=True):
    agentless: "capo_connectcampaignsv2.types.agentless_config.AgentlessConfig"


class TelephonyOutboundModePreviewMember(TypedDict, closed=True):
    preview: "capo_connectcampaignsv2.types.preview_config.PreviewConfig"


TelephonyOutboundMode: TypeAlias = (
    TelephonyOutboundModeProgressiveMember
    | TelephonyOutboundModePredictiveMember
    | TelephonyOutboundModeAgentlessMember
    | TelephonyOutboundModePreviewMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: TelephonyOutboundMode) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"TelephonyOutboundMode: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "progressive" in value:
        import capo_connectcampaignsv2.types.progressive_config

        return {
            "progressive": capo_connectcampaignsv2.types.progressive_config.serialize_json(
                value["progressive"]
            )
        }
    elif "predictive" in value:
        import capo_connectcampaignsv2.types.predictive_config

        return {
            "predictive": capo_connectcampaignsv2.types.predictive_config.serialize_json(
                value["predictive"]
            )
        }
    elif "agentless" in value:
        import capo_connectcampaignsv2.types.agentless_config

        return {
            "agentless": capo_connectcampaignsv2.types.agentless_config.serialize_json(
                value["agentless"]
            )
        }
    elif "preview" in value:
        import capo_connectcampaignsv2.types.preview_config

        return {
            "preview": capo_connectcampaignsv2.types.preview_config.serialize_json(
                value["preview"]
            )
        }
    else:
        raise SerializationError("TelephonyOutboundMode: no variant present")


def deserialize_json(data: dict) -> TelephonyOutboundMode:
    if data.get("progressive") is not None:
        import capo_connectcampaignsv2.types.progressive_config

        return {
            "progressive": capo_connectcampaignsv2.types.progressive_config.deserialize_json(
                data["progressive"]
            )
        }
    elif data.get("predictive") is not None:
        import capo_connectcampaignsv2.types.predictive_config

        return {
            "predictive": capo_connectcampaignsv2.types.predictive_config.deserialize_json(
                data["predictive"]
            )
        }
    elif data.get("agentless") is not None:
        import capo_connectcampaignsv2.types.agentless_config

        return {
            "agentless": capo_connectcampaignsv2.types.agentless_config.deserialize_json(
                data["agentless"]
            )
        }
    elif data.get("preview") is not None:
        import capo_connectcampaignsv2.types.preview_config

        return {
            "preview": capo_connectcampaignsv2.types.preview_config.deserialize_json(
                data["preview"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("TelephonyOutboundMode: no recognized variant key")
