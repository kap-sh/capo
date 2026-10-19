"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#DialerConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcampaigns.errors import DeserializationError, SerializationError
from capo_connectcampaigns.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connectcampaigns.types.agentless_dialer_config
    import capo_connectcampaigns.types.predictive_dialer_config
    import capo_connectcampaigns.types.progressive_dialer_config


class _DialerConfig_progressiveDialerConfig(TypedDict, closed=True):
    progressiveDialerConfig: (
        "capo_connectcampaigns.types.progressive_dialer_config.ProgressiveDialerConfig"
    )


class _DialerConfig_predictiveDialerConfig(TypedDict, closed=True):
    predictiveDialerConfig: (
        "capo_connectcampaigns.types.predictive_dialer_config.PredictiveDialerConfig"
    )


class _DialerConfig_agentlessDialerConfig(TypedDict, closed=True):
    agentlessDialerConfig: (
        "capo_connectcampaigns.types.agentless_dialer_config.AgentlessDialerConfig"
    )


DialerConfig: TypeAlias = (
    _DialerConfig_progressiveDialerConfig
    | _DialerConfig_predictiveDialerConfig
    | _DialerConfig_agentlessDialerConfig
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: DialerConfig) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"DialerConfig: cannot serialize unknown variant {value.name!r}"
        )
    elif "progressiveDialerConfig" in value:
        import capo_connectcampaigns.types.progressive_dialer_config

        return {
            "progressiveDialerConfig": capo_connectcampaigns.types.progressive_dialer_config.serialize_json(
                value["progressiveDialerConfig"]
            )
        }
    elif "predictiveDialerConfig" in value:
        import capo_connectcampaigns.types.predictive_dialer_config

        return {
            "predictiveDialerConfig": capo_connectcampaigns.types.predictive_dialer_config.serialize_json(
                value["predictiveDialerConfig"]
            )
        }
    elif "agentlessDialerConfig" in value:
        import capo_connectcampaigns.types.agentless_dialer_config

        return {
            "agentlessDialerConfig": capo_connectcampaigns.types.agentless_dialer_config.serialize_json(
                value["agentlessDialerConfig"]
            )
        }
    else:
        raise SerializationError("DialerConfig: no variant present")


def deserialize_json(data: dict) -> DialerConfig:
    if data.get("progressiveDialerConfig") is not None:
        import capo_connectcampaigns.types.progressive_dialer_config

        return {
            "progressiveDialerConfig": capo_connectcampaigns.types.progressive_dialer_config.deserialize_json(
                data["progressiveDialerConfig"]
            )
        }
    elif data.get("predictiveDialerConfig") is not None:
        import capo_connectcampaigns.types.predictive_dialer_config

        return {
            "predictiveDialerConfig": capo_connectcampaigns.types.predictive_dialer_config.deserialize_json(
                data["predictiveDialerConfig"]
            )
        }
    elif data.get("agentlessDialerConfig") is not None:
        import capo_connectcampaigns.types.agentless_dialer_config

        return {
            "agentlessDialerConfig": capo_connectcampaigns.types.agentless_dialer_config.deserialize_json(
                data["agentlessDialerConfig"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("DialerConfig: no recognized variant key")
