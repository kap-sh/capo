"""Generated from Smithy shape ``com.amazonaws.iot#MqttHeaders``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.content_type
    import capo_iot.types.correlation_data
    import capo_iot.types.message_expiry
    import capo_iot.types.payload_format_indicator
    import capo_iot.types.response_topic
    import capo_iot.types.user_properties


class MqttHeaders(TypedDict, closed=True):
    payload_format_indicator: NotRequired[
        "capo_iot.types.payload_format_indicator.PayloadFormatIndicator"
    ]
    """<p>An <code>Enum</code> string value that indicates whether the payload is formatted as UTF-8.</p> <p>Valid values are <code>UNSPECIFIED_BYTES</code> and <code>UTF8_DATA</code>.</p> <p>For more information, see <a href="https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html#_Toc3901111"> Payload Format Indicator</a> from the MQTT Version 5.0 specification.</p> <p>Supports <a href="https://docs.aws.amazon.com/iot/latest/developerguide/iot-substitution-templates.html">substitution templates</a>.</p>"""
    content_type: NotRequired["capo_iot.types.content_type.ContentType"]
    """<p>A UTF-8 encoded string that describes the content of the publishing message.</p> <p>For more information, see <a href="https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html#_Toc3901118"> Content Type</a> from the MQTT Version 5.0 specification.</p> <p>Supports <a href="https://docs.aws.amazon.com/iot/latest/developerguide/iot-substitution-templates.html">substitution templates</a>.</p>"""
    response_topic: NotRequired["capo_iot.types.response_topic.ResponseTopic"]
    """<p>A UTF-8 encoded string that's used as the topic name for a response message. The response topic is used to describe the topic which the receiver should publish to as part of the request-response flow. The topic must not contain wildcard characters.</p> <p>For more information, see <a href="https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html#_Toc3901114"> Response Topic</a> from the MQTT Version 5.0 specification.</p> <p>Supports <a href="https://docs.aws.amazon.com/iot/latest/developerguide/iot-substitution-templates.html">substitution templates</a>.</p>"""
    correlation_data: NotRequired["capo_iot.types.correlation_data.CorrelationData"]
    """<p>The base64-encoded binary data used by the sender of the request message to identify which request the response message is for when it's received.</p> <p>For more information, see <a href="https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html#_Toc3901115"> Correlation Data</a> from the MQTT Version 5.0 specification.</p> <note> <p> This binary data must be based64-encoded. </p> </note> <p>Supports <a href="https://docs.aws.amazon.com/iot/latest/developerguide/iot-substitution-templates.html">substitution templates</a>.</p>"""
    message_expiry: NotRequired["capo_iot.types.message_expiry.MessageExpiry"]
    """<p>A user-defined integer value that will persist a message at the message broker for a specified amount of time to ensure that the message will expire if it's no longer relevant to the subscriber. The value of <code>messageExpiry</code> represents the number of seconds before it expires. For more information about the limits of <code>messageExpiry</code>, see <a href="https://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html">Amazon Web Services IoT Core message broker and protocol limits and quotas </a> from the Amazon Web Services Reference Guide.</p> <p>Supports <a href="https://docs.aws.amazon.com/iot/latest/developerguide/iot-substitution-templates.html">substitution templates</a>.</p>"""
    user_properties: NotRequired["capo_iot.types.user_properties.UserProperties"]
    """<p>An array of key-value pairs that you define in the MQTT5 header.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MqttHeaders) -> dict:
    out: dict = {}
    if "payload_format_indicator" in value:
        out["payloadFormatIndicator"] = value["payload_format_indicator"]
    if "content_type" in value:
        out["contentType"] = value["content_type"]
    if "response_topic" in value:
        out["responseTopic"] = value["response_topic"]
    if "correlation_data" in value:
        out["correlationData"] = value["correlation_data"]
    if "message_expiry" in value:
        out["messageExpiry"] = value["message_expiry"]
    if "user_properties" in value:
        import capo_iot.types.user_properties

        out["userProperties"] = capo_iot.types.user_properties.serialize_json(
            value["user_properties"]
        )
    return out


def deserialize_json(data: dict) -> MqttHeaders:
    out: MqttHeaders = {}  # type: ignore[typeddict-item]
    if data.get("payloadFormatIndicator") is not None:
        out["payload_format_indicator"] = data["payloadFormatIndicator"]
    if data.get("contentType") is not None:
        out["content_type"] = data["contentType"]
    if data.get("responseTopic") is not None:
        out["response_topic"] = data["responseTopic"]
    if data.get("correlationData") is not None:
        out["correlation_data"] = data["correlationData"]
    if data.get("messageExpiry") is not None:
        out["message_expiry"] = data["messageExpiry"]
    if data.get("userProperties") is not None:
        import capo_iot.types.user_properties

        out["user_properties"] = capo_iot.types.user_properties.deserialize_json(
            data["userProperties"]
        )
    return out
