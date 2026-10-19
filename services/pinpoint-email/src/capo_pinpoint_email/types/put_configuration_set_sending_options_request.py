"""Generated from Smithy shape ``com.amazonaws.pinpointemail#PutConfigurationSetSendingOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_email.types.configuration_set_name
    import capo_pinpoint_email.types.enabled


class PutConfigurationSetSendingOptionsRequest(TypedDict, closed=True):
    configuration_set_name: (
        "capo_pinpoint_email.types.configuration_set_name.ConfigurationSetName"
    )
    """<p>The name of the configuration set that you want to enable or disable email sending for.</p>"""
    sending_enabled: NotRequired["capo_pinpoint_email.types.enabled.Enabled"]
    """<p>If <code>true</code>, email sending is enabled for the configuration set. If <code>false</code>, email sending is disabled for the configuration set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutConfigurationSetSendingOptionsRequest) -> dict:
    out: dict = {}
    if "sending_enabled" in value:
        out["SendingEnabled"] = value["sending_enabled"]
    return out


def deserialize_json(data: dict) -> PutConfigurationSetSendingOptionsRequest:
    out: PutConfigurationSetSendingOptionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("SendingEnabled") is not None:
        out["sending_enabled"] = data["SendingEnabled"]
    return out
