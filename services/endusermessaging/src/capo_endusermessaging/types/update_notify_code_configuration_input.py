"""Generated from Smithy shape ``com.amazonaws.endusermessaging#UpdateNotifyCodeConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_endusermessaging.types.notify_code_configuration_id_or_arn
    import capo_endusermessaging.types.notify_code_configuration_name
    import capo_endusermessaging.types.update_channel_parameters
    import capo_endusermessaging.types.update_code_configuration_parameters


class UpdateNotifyCodeConfigurationInput(TypedDict, closed=True):
    notify_code_configuration_id: "capo_endusermessaging.types.notify_code_configuration_id_or_arn.NotifyCodeConfigurationIdOrArn"
    """<p>The unique identifier of the notify code configuration. You can specify either the bare ID or the full Amazon Resource Name (ARN).</p>"""
    notify_code_configuration_name: NotRequired[
        "capo_endusermessaging.types.notify_code_configuration_name.NotifyCodeConfigurationName"
    ]
    """<p>The name of the notify code configuration.</p>"""
    code_configuration_parameters: NotRequired[
        "capo_endusermessaging.types.update_code_configuration_parameters.UpdateCodeConfigurationParameters"
    ]
    """<p>The updated passcode policy parameters, including the code type, length, validity period, and maximum number of attempts. When you omit a member, its current value is preserved.</p>"""
    channel_parameters: NotRequired[
        "capo_endusermessaging.types.update_channel_parameters.UpdateChannelParameters"
    ]
    """<p>The updated channel-specific parameters used to render and deliver the one-time passcode. This is a loose, nested update: when you omit a channel, that channel's parameters remain unchanged. Within a supplied channel, an empty string on a string member, or an empty map on the destination-country parameters, clears the currently stored value, and absent members preserve the current value.</p>"""
    deletion_protection_enabled: NotRequired["bool"]
    """<p>Specifies whether deletion protection is enabled. When enabled, the resource cannot be deleted until deletion protection is turned off.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNotifyCodeConfigurationInput) -> dict:
    out: dict = {}
    if "notify_code_configuration_name" in value:
        out["notifyCodeConfigurationName"] = value["notify_code_configuration_name"]
    if "code_configuration_parameters" in value:
        import capo_endusermessaging.types.update_code_configuration_parameters

        out["codeConfigurationParameters"] = (
            capo_endusermessaging.types.update_code_configuration_parameters.serialize_json(
                value["code_configuration_parameters"]
            )
        )
    if "channel_parameters" in value:
        import capo_endusermessaging.types.update_channel_parameters

        out["channelParameters"] = (
            capo_endusermessaging.types.update_channel_parameters.serialize_json(
                value["channel_parameters"]
            )
        )
    if "deletion_protection_enabled" in value:
        out["deletionProtectionEnabled"] = value["deletion_protection_enabled"]
    return out


def deserialize_json(data: dict) -> UpdateNotifyCodeConfigurationInput:
    out: UpdateNotifyCodeConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("notifyCodeConfigurationName") is not None:
        out["notify_code_configuration_name"] = data["notifyCodeConfigurationName"]
    if data.get("codeConfigurationParameters") is not None:
        import capo_endusermessaging.types.update_code_configuration_parameters

        out["code_configuration_parameters"] = (
            capo_endusermessaging.types.update_code_configuration_parameters.deserialize_json(
                data["codeConfigurationParameters"]
            )
        )
    if data.get("channelParameters") is not None:
        import capo_endusermessaging.types.update_channel_parameters

        out["channel_parameters"] = (
            capo_endusermessaging.types.update_channel_parameters.deserialize_json(
                data["channelParameters"]
            )
        )
    if data.get("deletionProtectionEnabled") is not None:
        out["deletion_protection_enabled"] = data["deletionProtectionEnabled"]
    return out
