"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#PutHubConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.hub_token_timer_expiry_setting_in_seconds


class PutHubConfigurationRequest(TypedDict, closed=True):
    hub_token_timer_expiry_setting_in_seconds: "capo_iot_managed_integrations.types.hub_token_timer_expiry_setting_in_seconds.HubTokenTimerExpirySettingInSeconds"
    """<p>A user-defined integer value that represents the hub token timer expiry setting in seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutHubConfigurationRequest) -> dict:
    out: dict = {}
    out["HubTokenTimerExpirySettingInSeconds"] = value[
        "hub_token_timer_expiry_setting_in_seconds"
    ]
    return out


def deserialize_json(data: dict) -> PutHubConfigurationRequest:
    out: PutHubConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("HubTokenTimerExpirySettingInSeconds") is not None:
        out["hub_token_timer_expiry_setting_in_seconds"] = data[
            "HubTokenTimerExpirySettingInSeconds"
        ]
    else:
        out["hub_token_timer_expiry_setting_in_seconds"] = 0
    return out
