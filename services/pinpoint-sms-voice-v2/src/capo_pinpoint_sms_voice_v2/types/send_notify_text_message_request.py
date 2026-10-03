"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SendNotifyTextMessageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn
    import capo_pinpoint_sms_voice_v2.types.context_map
    import capo_pinpoint_sms_voice_v2.types.notify_configuration_id_or_arn
    import capo_pinpoint_sms_voice_v2.types.notify_template_id
    import capo_pinpoint_sms_voice_v2.types.phone_number
    import capo_pinpoint_sms_voice_v2.types.template_variable_substitution_map
    import capo_pinpoint_sms_voice_v2.types.time_to_live


class SendNotifyTextMessageRequest(TypedDict, closed=True):
    notify_configuration_id: "capo_pinpoint_sms_voice_v2.types.notify_configuration_id_or_arn.NotifyConfigurationIdOrArn"
    """<p>The unique identifier of the notify configuration to use for sending the message. This can be either the NotifyConfigurationId or NotifyConfigurationArn.</p>"""
    destination_phone_number: (
        "capo_pinpoint_sms_voice_v2.types.phone_number.PhoneNumber"
    )
    """<p>The destination phone number in E.164 format.</p>"""
    template_id: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.notify_template_id.NotifyTemplateId"
    ]
    """<p>The unique identifier of the template to use for the message.</p>"""
    template_variables: "capo_pinpoint_sms_voice_v2.types.template_variable_substitution_map.TemplateVariableSubstitutionMap"
    """<p>A map of template variable names and their values. All variable values are passed as strings regardless of the declared variable type. For example, pass <code>INTEGER</code> values as <code>"42"</code> and <code>BOOLEAN</code> values as <code>"true"</code> or <code>"false"</code>.</p>"""
    time_to_live: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.time_to_live.TimeToLive"
    ]
    """<p>How long the text message is valid for, in seconds. By default this is 72 hours.</p>"""
    context: NotRequired["capo_pinpoint_sms_voice_v2.types.context_map.ContextMap"]
    """<p>You can specify custom data in this field. If you do, that data is logged to the event destination.</p>"""
    configuration_set_name: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn.ConfigurationSetNameOrArn"
    ]
    """<p>The name of the configuration set to use. This can be either the ConfigurationSetName or ConfigurationSetArn.</p>"""
    dry_run: "bool"
    """<p>When set to true, the message is checked and validated, but isn't sent to the end recipient.</p>"""
    message_feedback_enabled: NotRequired["bool"]
    """<p>Set to true to enable message feedback for the message. When a user receives the message you need to update the message status using <a>PutMessageFeedback</a>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SendNotifyTextMessageRequest) -> dict:
    out: dict = {}
    out["NotifyConfigurationId"] = value["notify_configuration_id"]
    out["DestinationPhoneNumber"] = value["destination_phone_number"]
    if "template_id" in value:
        out["TemplateId"] = value["template_id"]
    import capo_pinpoint_sms_voice_v2.types.template_variable_substitution_map

    out["TemplateVariables"] = (
        capo_pinpoint_sms_voice_v2.types.template_variable_substitution_map.serialize_aws_json_1_0(
            value["template_variables"]
        )
    )
    if "time_to_live" in value:
        out["TimeToLive"] = value["time_to_live"]
    if "context" in value:
        import capo_pinpoint_sms_voice_v2.types.context_map

        out["Context"] = (
            capo_pinpoint_sms_voice_v2.types.context_map.serialize_aws_json_1_0(
                value["context"]
            )
        )
    if "configuration_set_name" in value:
        out["ConfigurationSetName"] = value["configuration_set_name"]
    out["DryRun"] = value.get("dry_run", False)
    if "message_feedback_enabled" in value:
        out["MessageFeedbackEnabled"] = value["message_feedback_enabled"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SendNotifyTextMessageRequest:
    out: SendNotifyTextMessageRequest = {}  # type: ignore[typeddict-item]
    if data.get("NotifyConfigurationId") is not None:
        out["notify_configuration_id"] = data["NotifyConfigurationId"]
    else:
        raise DeserializationError(
            "SendNotifyTextMessageRequest.notify_configuration_id required"
        )
    if data.get("DestinationPhoneNumber") is not None:
        out["destination_phone_number"] = data["DestinationPhoneNumber"]
    else:
        raise DeserializationError(
            "SendNotifyTextMessageRequest.destination_phone_number required"
        )
    if data.get("TemplateId") is not None:
        out["template_id"] = data["TemplateId"]
    if data.get("TemplateVariables") is not None:
        import capo_pinpoint_sms_voice_v2.types.template_variable_substitution_map

        out["template_variables"] = (
            capo_pinpoint_sms_voice_v2.types.template_variable_substitution_map.deserialize_aws_json_1_0(
                data["TemplateVariables"]
            )
        )
    else:
        raise DeserializationError(
            "SendNotifyTextMessageRequest.template_variables required"
        )
    if data.get("TimeToLive") is not None:
        out["time_to_live"] = data["TimeToLive"]
    if data.get("Context") is not None:
        import capo_pinpoint_sms_voice_v2.types.context_map

        out["context"] = (
            capo_pinpoint_sms_voice_v2.types.context_map.deserialize_aws_json_1_0(
                data["Context"]
            )
        )
    if data.get("ConfigurationSetName") is not None:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    if data.get("DryRun") is not None:
        out["dry_run"] = data["DryRun"]
    else:
        out["dry_run"] = False
    if data.get("MessageFeedbackEnabled") is not None:
        out["message_feedback_enabled"] = data["MessageFeedbackEnabled"]
    return out
