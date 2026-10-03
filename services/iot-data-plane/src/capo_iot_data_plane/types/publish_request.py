"""Generated from Smithy shape ``com.amazonaws.iotdataplane#PublishRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_data_plane.types.content_type
    import capo_iot_data_plane.types.correlation_data
    import capo_iot_data_plane.types.message_expiry
    import capo_iot_data_plane.types.payload
    import capo_iot_data_plane.types.payload_format_indicator
    import capo_iot_data_plane.types.qos
    import capo_iot_data_plane.types.response_topic
    import capo_iot_data_plane.types.retain
    import capo_iot_data_plane.types.synthesized_json_user_properties
    import capo_iot_data_plane.types.topic


class PublishRequest(TypedDict, closed=True):
    topic: "capo_iot_data_plane.types.topic.Topic"
    """<p>The name of the MQTT topic.</p>"""
    qos: "capo_iot_data_plane.types.qos.Qos"
    """<p>The Quality of Service (QoS) level. The default QoS level is 0.</p>"""
    retain: "capo_iot_data_plane.types.retain.Retain"
    """<p>A Boolean value that determines whether to set the RETAIN flag when the message is published.</p> <p>Setting the RETAIN flag causes the message to be retained and sent to new subscribers to the topic.</p> <p>Valid values: <code>true</code> | <code>false</code> </p> <p>Default value: <code>false</code> </p>"""
    payload: NotRequired["capo_iot_data_plane.types.payload.Payload"]
    """<p>The message body. MQTT accepts text, binary, and empty (null) message payloads.</p> <p>Publishing an empty (null) payload with <b>retain</b> = <code>true</code> deletes the retained message identified by <b>topic</b> from Amazon Web Services IoT Core.</p>"""
    user_properties: NotRequired[
        "capo_iot_data_plane.types.synthesized_json_user_properties.SynthesizedJsonUserProperties"
    ]
    """<p>A JSON string that contains an array of JSON objects. If you don’t use Amazon Web Services SDK or CLI, you must encode the JSON string to base64 format before adding it to the HTTP header. <code>userProperties</code> is an HTTP header value in the API.</p> <p>The following example <code>userProperties</code> parameter is a JSON string which represents two User Properties. Note that it needs to be base64-encoded:</p> <p> <code>[{"deviceName": "alpha"}, {"deviceCnt": "45"}]</code> </p>"""
    payload_format_indicator: NotRequired[
        "capo_iot_data_plane.types.payload_format_indicator.PayloadFormatIndicator"
    ]
    """<p>An <code>Enum</code> string value that indicates whether the payload is formatted as UTF-8. <code>payloadFormatIndicator</code> is an HTTP header value in the API.</p>"""
    content_type: NotRequired["capo_iot_data_plane.types.content_type.ContentType"]
    """<p>A UTF-8 encoded string that describes the content of the publishing message.</p>"""
    response_topic: NotRequired[
        "capo_iot_data_plane.types.response_topic.ResponseTopic"
    ]
    """<p>A UTF-8 encoded string that's used as the topic name for a response message. The response topic is used to describe the topic which the receiver should publish to as part of the request-response flow. The topic must not contain wildcard characters.</p>"""
    correlation_data: NotRequired[
        "capo_iot_data_plane.types.correlation_data.CorrelationData"
    ]
    """<p>The base64-encoded binary data used by the sender of the request message to identify which request the response message is for when it's received. <code>correlationData</code> is an HTTP header value in the API.</p>"""
    message_expiry: "capo_iot_data_plane.types.message_expiry.MessageExpiry"
    """<p>A user-defined integer value that represents the message expiry interval in seconds. If absent, the message doesn't expire. For more information about the limits of <code>messageExpiry</code>, see <a href="https://docs.aws.amazon.com/general/latest/gr/iot-core.html#message-broker-limits">Amazon Web Services IoT Core message broker and protocol limits and quotas </a> from the Amazon Web Services Reference Guide.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PublishRequest) -> dict:
    out: dict = {}
    if "payload" in value:
        import capo_iot_data_plane.types.payload

        out["payload"] = capo_iot_data_plane.types.payload.serialize_json(
            value["payload"]
        )
    return out


def deserialize_json(data: dict) -> PublishRequest:
    out: PublishRequest = {}  # type: ignore[typeddict-item]
    if data.get("payload") is not None:
        import capo_iot_data_plane.types.payload

        out["payload"] = capo_iot_data_plane.types.payload.deserialize_json(
            data["payload"]
        )
    return out
