"""Generated from Smithy shape ``com.amazonaws.pinpoint#SendUsersMessageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.direct_message_configuration
    import capo_pinpoint.types.map_of__string
    import capo_pinpoint.types.map_of_endpoint_send_configuration
    import capo_pinpoint.types.template_configuration


class SendUsersMessageRequest(TypedDict, closed=True):
    context: NotRequired["capo_pinpoint.types.map_of__string.MapOf__string"]
    """<p>A map of custom attribute-value pairs. For a push notification, Amazon Pinpoint adds these attributes to the data.pinpoint object in the body of the notification payload. Amazon Pinpoint also provides these attributes in the events that it generates for users-messages deliveries.</p>"""
    message_configuration: NotRequired[
        "capo_pinpoint.types.direct_message_configuration.DirectMessageConfiguration"
    ]
    """<p>The settings and content for the default message and any default messages that you defined for specific channels.</p>"""
    template_configuration: NotRequired[
        "capo_pinpoint.types.template_configuration.TemplateConfiguration"
    ]
    """<p>The message template to use for the message.</p>"""
    trace_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for tracing the message. This identifier is visible to message recipients.</p>"""
    users: NotRequired[
        "capo_pinpoint.types.map_of_endpoint_send_configuration.MapOfEndpointSendConfiguration"
    ]
    """<p>A map that associates user IDs with <a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-messages.html#apps-application-id-messages-model-endpointsendconfiguration">EndpointSendConfiguration</a> objects. You can use an <a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-messages.html#apps-application-id-messages-model-endpointsendconfiguration">EndpointSendConfiguration</a> object to tailor the message for a user by specifying settings such as content overrides and message variables.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendUsersMessageRequest) -> dict:
    out: dict = {}
    if "context" in value:
        import capo_pinpoint.types.map_of__string

        out["Context"] = capo_pinpoint.types.map_of__string.serialize_json(
            value["context"]
        )
    if "message_configuration" in value:
        import capo_pinpoint.types.direct_message_configuration

        out["MessageConfiguration"] = (
            capo_pinpoint.types.direct_message_configuration.serialize_json(
                value["message_configuration"]
            )
        )
    if "template_configuration" in value:
        import capo_pinpoint.types.template_configuration

        out["TemplateConfiguration"] = (
            capo_pinpoint.types.template_configuration.serialize_json(
                value["template_configuration"]
            )
        )
    if "trace_id" in value:
        out["TraceId"] = value["trace_id"]
    if "users" in value:
        import capo_pinpoint.types.map_of_endpoint_send_configuration

        out["Users"] = (
            capo_pinpoint.types.map_of_endpoint_send_configuration.serialize_json(
                value["users"]
            )
        )
    return out


def deserialize_json(data: dict) -> SendUsersMessageRequest:
    out: SendUsersMessageRequest = {}  # type: ignore[typeddict-item]
    if data.get("Context") is not None:
        import capo_pinpoint.types.map_of__string

        out["context"] = capo_pinpoint.types.map_of__string.deserialize_json(
            data["Context"]
        )
    if data.get("MessageConfiguration") is not None:
        import capo_pinpoint.types.direct_message_configuration

        out["message_configuration"] = (
            capo_pinpoint.types.direct_message_configuration.deserialize_json(
                data["MessageConfiguration"]
            )
        )
    if data.get("TemplateConfiguration") is not None:
        import capo_pinpoint.types.template_configuration

        out["template_configuration"] = (
            capo_pinpoint.types.template_configuration.deserialize_json(
                data["TemplateConfiguration"]
            )
        )
    if data.get("TraceId") is not None:
        out["trace_id"] = data["TraceId"]
    if data.get("Users") is not None:
        import capo_pinpoint.types.map_of_endpoint_send_configuration

        out["users"] = (
            capo_pinpoint.types.map_of_endpoint_send_configuration.deserialize_json(
                data["Users"]
            )
        )
    return out
