"""Generated from Smithy shape ``com.amazonaws.pinpoint#CustomMessageActivity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.journey_custom_message
    import capo_pinpoint.types.list_of__endpoint_types_element


class CustomMessageActivity(TypedDict, closed=True):
    delivery_uri: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The destination to send the campaign or treatment to. This value can be one of the following:</p> <ul><li><p>The name or Amazon Resource Name (ARN) of an AWS Lambda function to invoke to handle delivery of the campaign or treatment.</p></li> <li><p>The URL for a web application or service that supports HTTPS and can receive the message. The URL has to be a full URL, including the HTTPS protocol.</p></li></ul>"""
    endpoint_types: NotRequired[
        "capo_pinpoint.types.list_of__endpoint_types_element.ListOf__EndpointTypesElement"
    ]
    """<p>The types of endpoints to send the custom message to. Each valid value maps to a type of channel that you can associate with an endpoint by using the ChannelType property of an endpoint.</p>"""
    message_config: NotRequired[
        "capo_pinpoint.types.journey_custom_message.JourneyCustomMessage"
    ]
    """<p>Specifies the message data included in a custom channel message that's sent to participants in a journey.</p>"""
    next_activity: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the next activity to perform, after Amazon Pinpoint calls the AWS Lambda function or web hook.</p>"""
    template_name: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The name of the custom message template to use for the message. If specified, this value must match the name of an existing message template.</p>"""
    template_version: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the version of the message template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the <link linkend="templates-template-name-template-type-versions">Template Versions</link> resource.</p> <p>If you don't specify a value for this property, Amazon Pinpoint uses the <i>active version</i> of the template. The <i>active version</i> is typically the version of a template that's been most recently reviewed and approved for use, depending on your workflow. It isn't necessarily the latest version of a template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomMessageActivity) -> dict:
    out: dict = {}
    if "delivery_uri" in value:
        out["DeliveryUri"] = value["delivery_uri"]
    if "endpoint_types" in value:
        import capo_pinpoint.types.list_of__endpoint_types_element

        out["EndpointTypes"] = (
            capo_pinpoint.types.list_of__endpoint_types_element.serialize_json(
                value["endpoint_types"]
            )
        )
    if "message_config" in value:
        import capo_pinpoint.types.journey_custom_message

        out["MessageConfig"] = (
            capo_pinpoint.types.journey_custom_message.serialize_json(
                value["message_config"]
            )
        )
    if "next_activity" in value:
        out["NextActivity"] = value["next_activity"]
    if "template_name" in value:
        out["TemplateName"] = value["template_name"]
    if "template_version" in value:
        out["TemplateVersion"] = value["template_version"]
    return out


def deserialize_json(data: dict) -> CustomMessageActivity:
    out: CustomMessageActivity = {}  # type: ignore[typeddict-item]
    if data.get("DeliveryUri") is not None:
        out["delivery_uri"] = data["DeliveryUri"]
    if data.get("EndpointTypes") is not None:
        import capo_pinpoint.types.list_of__endpoint_types_element

        out["endpoint_types"] = (
            capo_pinpoint.types.list_of__endpoint_types_element.deserialize_json(
                data["EndpointTypes"]
            )
        )
    if data.get("MessageConfig") is not None:
        import capo_pinpoint.types.journey_custom_message

        out["message_config"] = (
            capo_pinpoint.types.journey_custom_message.deserialize_json(
                data["MessageConfig"]
            )
        )
    if data.get("NextActivity") is not None:
        out["next_activity"] = data["NextActivity"]
    if data.get("TemplateName") is not None:
        out["template_name"] = data["TemplateName"]
    if data.get("TemplateVersion") is not None:
        out["template_version"] = data["TemplateVersion"]
    return out
