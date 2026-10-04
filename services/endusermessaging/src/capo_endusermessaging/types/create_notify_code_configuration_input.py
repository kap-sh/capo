"""Generated from Smithy shape ``com.amazonaws.endusermessaging#CreateNotifyCodeConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_endusermessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_endusermessaging.types.channel_parameters
    import capo_endusermessaging.types.client_token
    import capo_endusermessaging.types.code_configuration_parameters
    import capo_endusermessaging.types.notify_code_configuration_name
    import capo_endusermessaging.types.tag_list


class CreateNotifyCodeConfigurationInput(TypedDict, closed=True):
    notify_code_configuration_name: "capo_endusermessaging.types.notify_code_configuration_name.NotifyCodeConfigurationName"
    """<p>The name of the notify code configuration.</p>"""
    code_configuration_parameters: NotRequired[
        "capo_endusermessaging.types.code_configuration_parameters.CodeConfigurationParameters"
    ]
    """<p>The passcode policy parameters, including the code type, length, validity period, and maximum number of attempts. Each member is optional. When you omit a member, no value is applied at create time and the default is applied when a passcode is sent.</p>"""
    channel_parameters: NotRequired[
        "capo_endusermessaging.types.channel_parameters.ChannelParameters"
    ]
    """<p>The channel-specific parameters used to render and deliver the one-time passcode. Provide parameters for any subset of channels. Each member configures one delivery route, and the route that is selected at send time uses the matching channel.</p>"""
    deletion_protection_enabled: NotRequired["bool"]
    """<p>Specifies whether deletion protection is enabled. When enabled, the resource cannot be deleted until deletion protection is turned off.</p>"""
    client_token: NotRequired["capo_endusermessaging.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you do not specify a client token, the AWS SDK automatically generates one.</p>"""
    tags: NotRequired["capo_endusermessaging.types.tag_list.TagList"]
    """<p>An array of key and value pair tags that are associated with the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNotifyCodeConfigurationInput) -> dict:
    out: dict = {}
    out["notifyCodeConfigurationName"] = value["notify_code_configuration_name"]
    if "code_configuration_parameters" in value:
        import capo_endusermessaging.types.code_configuration_parameters

        out["codeConfigurationParameters"] = (
            capo_endusermessaging.types.code_configuration_parameters.serialize_json(
                value["code_configuration_parameters"]
            )
        )
    if "channel_parameters" in value:
        import capo_endusermessaging.types.channel_parameters

        out["channelParameters"] = (
            capo_endusermessaging.types.channel_parameters.serialize_json(
                value["channel_parameters"]
            )
        )
    if "deletion_protection_enabled" in value:
        out["deletionProtectionEnabled"] = value["deletion_protection_enabled"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_endusermessaging.types.tag_list

        out["tags"] = capo_endusermessaging.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateNotifyCodeConfigurationInput:
    out: CreateNotifyCodeConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("notifyCodeConfigurationName") is not None:
        out["notify_code_configuration_name"] = data["notifyCodeConfigurationName"]
    else:
        raise DeserializationError(
            "CreateNotifyCodeConfigurationInput.notify_code_configuration_name required"
        )
    if data.get("codeConfigurationParameters") is not None:
        import capo_endusermessaging.types.code_configuration_parameters

        out["code_configuration_parameters"] = (
            capo_endusermessaging.types.code_configuration_parameters.deserialize_json(
                data["codeConfigurationParameters"]
            )
        )
    if data.get("channelParameters") is not None:
        import capo_endusermessaging.types.channel_parameters

        out["channel_parameters"] = (
            capo_endusermessaging.types.channel_parameters.deserialize_json(
                data["channelParameters"]
            )
        )
    if data.get("deletionProtectionEnabled") is not None:
        out["deletion_protection_enabled"] = data["deletionProtectionEnabled"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_endusermessaging.types.tag_list

        out["tags"] = capo_endusermessaging.types.tag_list.deserialize_json(
            data["tags"]
        )
    return out
