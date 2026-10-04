"""Generated from Smithy shape ``com.amazonaws.endusermessaging#SendNotifyCodeVerificationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_endusermessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_endusermessaging.types.channel_parameters
    import capo_endusermessaging.types.code_configuration_parameters
    import capo_endusermessaging.types.configuration_set_name
    import capo_endusermessaging.types.context_map
    import capo_endusermessaging.types.destination_identity
    import capo_endusermessaging.types.notify_channel
    import capo_endusermessaging.types.notify_code_configuration_id_or_arn
    import capo_endusermessaging.types.origination_identity
    import capo_endusermessaging.types.reference_id


class SendNotifyCodeVerificationInput(TypedDict, closed=True):
    channel: "capo_endusermessaging.types.notify_channel.NotifyChannel"
    """<p>The channel used to deliver the one-time passcode to the recipient.</p>"""
    destination_identity: (
        "capo_endusermessaging.types.destination_identity.DestinationIdentity"
    )
    """<p>The recipient identifier. For the TEXT and VOICE channels, specify an E.164 phone number. For the WhatsApp channel, specify a WhatsApp address.</p>"""
    origination_identity: (
        "capo_endusermessaging.types.origination_identity.OriginationIdentity"
    )
    """<p>The identity used to send the message, such as a phone number, sender ID, or pool that is owned by your account.</p>"""
    notify_code_configuration: NotRequired[
        "capo_endusermessaging.types.notify_code_configuration_id_or_arn.NotifyCodeConfigurationIdOrArn"
    ]
    """<p>The identifier or Amazon Resource Name (ARN) of the notify code configuration that supplies the passcode policy and template defaults. When you do not specify a configuration, you must supply the template in the request.</p>"""
    override_channel_parameters: NotRequired[
        "capo_endusermessaging.types.channel_parameters.ChannelParameters"
    ]
    """<p>The channel-specific parameters used to render and deliver the one-time passcode for this request. The route that is derived from the channel and the origination identity selects the matching channel. When you do not specify channel parameters, the service uses the parameters from the referenced notify code configuration.</p>"""
    override_code_configuration_parameters: NotRequired[
        "capo_endusermessaging.types.code_configuration_parameters.CodeConfigurationParameters"
    ]
    """<p>The per-send overrides for the passcode policy parameters, including the code type, length, validity period, and maximum number of attempts. These values override the values from the referenced notify code configuration. When you do not specify a value, the value from the configuration is used, and if neither is set, the service default applies.</p>"""
    configuration_set_name: NotRequired[
        "capo_endusermessaging.types.configuration_set_name.ConfigurationSetName"
    ]
    """<p>The name of the configuration set used to control how delivery events for the message are handled.</p>"""
    context: NotRequired["capo_endusermessaging.types.context_map.ContextMap"]
    """<p>A map of custom key and value pairs that are propagated to the delivery events for this verification.</p>"""
    reference_id: NotRequired["capo_endusermessaging.types.reference_id.ReferenceId"]
    """<p>A caller-supplied reference identifier that binds a send request to a later validate request. Specify the same value in both requests.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendNotifyCodeVerificationInput) -> dict:
    out: dict = {}
    import capo_endusermessaging.types.notify_channel

    out["channel"] = capo_endusermessaging.types.notify_channel.serialize_json(
        value["channel"]
    )
    out["destinationIdentity"] = value["destination_identity"]
    out["originationIdentity"] = value["origination_identity"]
    if "notify_code_configuration" in value:
        out["notifyCodeConfiguration"] = value["notify_code_configuration"]
    if "override_channel_parameters" in value:
        import capo_endusermessaging.types.channel_parameters

        out["overrideChannelParameters"] = (
            capo_endusermessaging.types.channel_parameters.serialize_json(
                value["override_channel_parameters"]
            )
        )
    if "override_code_configuration_parameters" in value:
        import capo_endusermessaging.types.code_configuration_parameters

        out["overrideCodeConfigurationParameters"] = (
            capo_endusermessaging.types.code_configuration_parameters.serialize_json(
                value["override_code_configuration_parameters"]
            )
        )
    if "configuration_set_name" in value:
        out["configurationSetName"] = value["configuration_set_name"]
    if "context" in value:
        import capo_endusermessaging.types.context_map

        out["context"] = capo_endusermessaging.types.context_map.serialize_json(
            value["context"]
        )
    if "reference_id" in value:
        out["referenceId"] = value["reference_id"]
    return out


def deserialize_json(data: dict) -> SendNotifyCodeVerificationInput:
    out: SendNotifyCodeVerificationInput = {}  # type: ignore[typeddict-item]
    if data.get("channel") is not None:
        import capo_endusermessaging.types.notify_channel

        out["channel"] = capo_endusermessaging.types.notify_channel.deserialize_json(
            data["channel"]
        )
    else:
        raise DeserializationError("SendNotifyCodeVerificationInput.channel required")
    if data.get("destinationIdentity") is not None:
        out["destination_identity"] = data["destinationIdentity"]
    else:
        raise DeserializationError(
            "SendNotifyCodeVerificationInput.destination_identity required"
        )
    if data.get("originationIdentity") is not None:
        out["origination_identity"] = data["originationIdentity"]
    else:
        raise DeserializationError(
            "SendNotifyCodeVerificationInput.origination_identity required"
        )
    if data.get("notifyCodeConfiguration") is not None:
        out["notify_code_configuration"] = data["notifyCodeConfiguration"]
    if data.get("overrideChannelParameters") is not None:
        import capo_endusermessaging.types.channel_parameters

        out["override_channel_parameters"] = (
            capo_endusermessaging.types.channel_parameters.deserialize_json(
                data["overrideChannelParameters"]
            )
        )
    if data.get("overrideCodeConfigurationParameters") is not None:
        import capo_endusermessaging.types.code_configuration_parameters

        out["override_code_configuration_parameters"] = (
            capo_endusermessaging.types.code_configuration_parameters.deserialize_json(
                data["overrideCodeConfigurationParameters"]
            )
        )
    if data.get("configurationSetName") is not None:
        out["configuration_set_name"] = data["configurationSetName"]
    if data.get("context") is not None:
        import capo_endusermessaging.types.context_map

        out["context"] = capo_endusermessaging.types.context_map.deserialize_json(
            data["context"]
        )
    if data.get("referenceId") is not None:
        out["reference_id"] = data["referenceId"]
    return out
