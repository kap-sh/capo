"""Generated from Smithy shape ``com.amazonaws.endusermessaging#NotifyCodeConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_endusermessaging.types.amazon_resource_name
    import capo_endusermessaging.types.channel_parameters
    import capo_endusermessaging.types.code_configuration_parameters
    import capo_endusermessaging.types.notify_code_configuration_id
    import capo_endusermessaging.types.notify_code_configuration_name


class NotifyCodeConfiguration(TypedDict, closed=True):
    notify_code_configuration_id: "capo_endusermessaging.types.notify_code_configuration_id.NotifyCodeConfigurationId"
    """<p>The unique identifier of the notify code configuration.</p>"""
    notify_code_configuration_arn: (
        "capo_endusermessaging.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The Amazon Resource Name (ARN) of the notify code configuration.</p>"""
    notify_code_configuration_name: "capo_endusermessaging.types.notify_code_configuration_name.NotifyCodeConfigurationName"
    """<p>The name of the notify code configuration.</p>"""
    code_configuration_parameters: NotRequired[
        "capo_endusermessaging.types.code_configuration_parameters.CodeConfigurationParameters"
    ]
    """<p>The passcode policy parameters, including the code type, length, validity period, and maximum number of attempts.</p>"""
    channel_parameters: NotRequired[
        "capo_endusermessaging.types.channel_parameters.ChannelParameters"
    ]
    """<p>The channel-specific parameters used to render and deliver the one-time passcode. A configuration can carry parameters for every channel at once, and the send route selects the matching channel at send time.</p>"""
    deletion_protection_enabled: "bool"
    """<p>Specifies whether deletion protection is enabled. When enabled, the resource cannot be deleted until deletion protection is turned off.</p>"""
    created_at: "datetime.datetime"
    """<p>The time when the resource was created, in Unix epoch time.</p>"""
    updated_at: "datetime.datetime"
    """<p>The time when the resource was last updated, in Unix epoch time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotifyCodeConfiguration) -> dict:
    out: dict = {}
    out["notifyCodeConfigurationId"] = value["notify_code_configuration_id"]
    out["notifyCodeConfigurationArn"] = value["notify_code_configuration_arn"]
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
    out["deletionProtectionEnabled"] = value["deletion_protection_enabled"]
    import capo_endusermessaging.types._prelude.timestamp

    out["createdAt"] = capo_endusermessaging.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_endusermessaging.types._prelude.timestamp

    out["updatedAt"] = capo_endusermessaging.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> NotifyCodeConfiguration:
    out: NotifyCodeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("notifyCodeConfigurationId") is not None:
        out["notify_code_configuration_id"] = data["notifyCodeConfigurationId"]
    else:
        out["notify_code_configuration_id"] = ""
    if data.get("notifyCodeConfigurationArn") is not None:
        out["notify_code_configuration_arn"] = data["notifyCodeConfigurationArn"]
    else:
        out["notify_code_configuration_arn"] = ""
    if data.get("notifyCodeConfigurationName") is not None:
        out["notify_code_configuration_name"] = data["notifyCodeConfigurationName"]
    else:
        out["notify_code_configuration_name"] = ""
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
    else:
        out["deletion_protection_enabled"] = False
    if data.get("createdAt") is not None:
        import capo_endusermessaging.types._prelude.timestamp

        out["created_at"] = (
            capo_endusermessaging.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_endusermessaging.types._prelude.timestamp

        out["updated_at"] = (
            capo_endusermessaging.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out


def redact_sensitive(value: NotifyCodeConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "channel_parameters" in value:
        import capo_endusermessaging.types.channel_parameters

        out["channel_parameters"] = (
            capo_endusermessaging.types.channel_parameters.redact_sensitive(
                value["channel_parameters"]
            )
        )
    return out
