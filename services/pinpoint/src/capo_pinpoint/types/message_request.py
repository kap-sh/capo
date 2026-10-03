"""Generated from Smithy shape ``com.amazonaws.pinpoint#MessageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.direct_message_configuration
    import capo_pinpoint.types.map_of__string
    import capo_pinpoint.types.map_of_address_configuration
    import capo_pinpoint.types.map_of_endpoint_send_configuration
    import capo_pinpoint.types.template_configuration


class MessageRequest(TypedDict, closed=True):
    addresses: NotRequired[
        "capo_pinpoint.types.map_of_address_configuration.MapOfAddressConfiguration"
    ]
    """<p>A map of key-value pairs, where each key is an address and each value is an <a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-messages.html#apps-application-id-messages-model-addressconfiguration">AddressConfiguration</a> object. An address can be a push notification token, a phone number, or an email address. You can use an <a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-messages.html#apps-application-id-messages-model-addressconfiguration">AddressConfiguration</a> object to tailor the message for an address by specifying settings such as content overrides and message variables.</p>"""
    context: NotRequired["capo_pinpoint.types.map_of__string.MapOf__string"]
    """<p>A map of custom attributes to attach to the message. For a push notification, this payload is added to the data.pinpoint object. For an email or text message, this payload is added to email/SMS delivery receipt event attributes.</p>"""
    endpoints: NotRequired[
        "capo_pinpoint.types.map_of_endpoint_send_configuration.MapOfEndpointSendConfiguration"
    ]
    """<p>A map of key-value pairs, where each key is an endpoint ID and each value is an <a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-messages.html#apps-application-id-messages-model-endpointsendconfiguration">EndpointSendConfiguration</a> object. You can use an <a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-messages.html#apps-application-id-messages-model-endpointsendconfiguration">EndpointSendConfiguration</a> object to tailor the message for an endpoint by specifying settings such as content overrides and message variables.</p>"""
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


# --- restJson1 ser/de ---
def serialize_json(value: MessageRequest) -> dict:
    out: dict = {}
    if "addresses" in value:
        import capo_pinpoint.types.map_of_address_configuration

        out["Addresses"] = (
            capo_pinpoint.types.map_of_address_configuration.serialize_json(
                value["addresses"]
            )
        )
    if "context" in value:
        import capo_pinpoint.types.map_of__string

        out["Context"] = capo_pinpoint.types.map_of__string.serialize_json(
            value["context"]
        )
    if "endpoints" in value:
        import capo_pinpoint.types.map_of_endpoint_send_configuration

        out["Endpoints"] = (
            capo_pinpoint.types.map_of_endpoint_send_configuration.serialize_json(
                value["endpoints"]
            )
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
    return out


def deserialize_json(data: dict) -> MessageRequest:
    out: MessageRequest = {}  # type: ignore[typeddict-item]
    if data.get("Addresses") is not None:
        import capo_pinpoint.types.map_of_address_configuration

        out["addresses"] = (
            capo_pinpoint.types.map_of_address_configuration.deserialize_json(
                data["Addresses"]
            )
        )
    if data.get("Context") is not None:
        import capo_pinpoint.types.map_of__string

        out["context"] = capo_pinpoint.types.map_of__string.deserialize_json(
            data["Context"]
        )
    if data.get("Endpoints") is not None:
        import capo_pinpoint.types.map_of_endpoint_send_configuration

        out["endpoints"] = (
            capo_pinpoint.types.map_of_endpoint_send_configuration.deserialize_json(
                data["Endpoints"]
            )
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
    return out
