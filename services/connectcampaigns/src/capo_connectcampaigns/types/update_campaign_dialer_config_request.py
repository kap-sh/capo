"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#UpdateCampaignDialerConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcampaigns.types.campaign_id
    import capo_connectcampaigns.types.dialer_config


class UpdateCampaignDialerConfigRequest(TypedDict, closed=True):
    id: "capo_connectcampaigns.types.campaign_id.CampaignId"
    dialer_config: "capo_connectcampaigns.types.dialer_config.DialerConfig"


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCampaignDialerConfigRequest) -> dict:
    out: dict = {}
    import capo_connectcampaigns.types.dialer_config

    out["dialerConfig"] = capo_connectcampaigns.types.dialer_config.serialize_json(
        value["dialer_config"]
    )
    return out


def deserialize_json(data: dict) -> UpdateCampaignDialerConfigRequest:
    out: UpdateCampaignDialerConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("dialerConfig") is not None:
        import capo_connectcampaigns.types.dialer_config

        out["dialer_config"] = (
            capo_connectcampaigns.types.dialer_config.deserialize_json(
                data["dialerConfig"]
            )
        )
    else:
        out["dialer_config"] = {"$unknown": {"name": ""}}
    return out
