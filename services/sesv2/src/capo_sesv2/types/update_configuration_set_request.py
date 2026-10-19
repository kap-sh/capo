"""Generated from Smithy shape ``com.amazonaws.sesv2#UpdateConfigurationSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.configuration_set_name
    import capo_sesv2.types.message_security_options


class UpdateConfigurationSetRequest(TypedDict, closed=True):
    configuration_set_name: (
        "capo_sesv2.types.configuration_set_name.ConfigurationSetName"
    )
    """<p>The name of the configuration set to update.</p>"""
    message_security_options: NotRequired[
        "capo_sesv2.types.message_security_options.MessageSecurityOptions"
    ]
    """<p>The security options that apply to the MIME message itself for messages sent with the configuration set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConfigurationSetRequest) -> dict:
    out: dict = {}
    out["ConfigurationSetName"] = value["configuration_set_name"]
    if "message_security_options" in value:
        import capo_sesv2.types.message_security_options

        out["MessageSecurityOptions"] = (
            capo_sesv2.types.message_security_options.serialize_json(
                value["message_security_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateConfigurationSetRequest:
    out: UpdateConfigurationSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConfigurationSetName") is not None:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    else:
        out["configuration_set_name"] = ""
    if data.get("MessageSecurityOptions") is not None:
        import capo_sesv2.types.message_security_options

        out["message_security_options"] = (
            capo_sesv2.types.message_security_options.deserialize_json(
                data["MessageSecurityOptions"]
            )
        )
    return out
