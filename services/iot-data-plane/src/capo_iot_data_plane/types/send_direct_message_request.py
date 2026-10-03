"""Generated from Smithy shape ``com.amazonaws.iotdataplane#SendDirectMessageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_data_plane.types.client_id
    import capo_iot_data_plane.types.confirmation
    import capo_iot_data_plane.types.content_type
    import capo_iot_data_plane.types.correlation_data
    import capo_iot_data_plane.types.payload
    import capo_iot_data_plane.types.payload_format_indicator
    import capo_iot_data_plane.types.response_topic
    import capo_iot_data_plane.types.synthesized_json_user_properties
    import capo_iot_data_plane.types.timeout_in_seconds
    import capo_iot_data_plane.types.topic


class SendDirectMessageRequest(TypedDict, closed=True):
    client_id: "capo_iot_data_plane.types.client_id.ClientId"
    """<p>The unique identifier of the MQTT client to send the message to.</p> <p>Client IDs must not exceed 128 characters and can't start with a dollar sign ($). MQTT client IDs must be URL encoded (percent-encoded) when they contain characters that are not valid in HTTP requests, such as spaces, forward slashes (/), and UTF-8 characters. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/iot-core.html#message-broker-limits">Amazon Web Services IoT Core message broker and protocol limits and quotas</a>.</p>"""
    topic: "capo_iot_data_plane.types.topic.Topic"
    """<p>The topic of the outbound MQTT Publish message to the receiving client. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/iot-core.html#message-broker-limits">Amazon Web Services IoT Core message broker and protocol limits and quotas</a>.</p>"""
    content_type: NotRequired["capo_iot_data_plane.types.content_type.ContentType"]
    """<p>The MQTT5 content type property forwarded to the receiving client (for example, <code>application/json</code>).</p>"""
    response_topic: NotRequired[
        "capo_iot_data_plane.types.response_topic.ResponseTopic"
    ]
    """<p>A UTF-8 encoded string that's used as the topic name for a response message. The response topic describes the topic which the receiver should publish to as part of the request-response flow. The topic must not contain wildcard characters. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/iot-core.html#message-broker-limits">Amazon Web Services IoT Core message broker and protocol limits and quotas</a>.</p>"""
    confirmation: "capo_iot_data_plane.types.confirmation.Confirmation"
    """<p>A Boolean value that specifies whether to wait for delivery confirmation from the receiving client.</p> <p>When set to <code>true</code>, the API delivers the message at QoS 1 and waits for the client to send a delivery confirmation (PUBACK) before returning a successful response. If delivery confirmation is not received within the specified <code>timeout</code> period, the API returns HTTP 504.</p> <p>When set to <code>false</code>, the API delivers the message at QoS 0 and returns after Amazon Web Services IoT Core attempts to deliver the message.</p> <p>Valid values: <code>true</code> | <code>false</code> </p> <p>Default value: <code>false</code> </p>"""
    timeout: "capo_iot_data_plane.types.timeout_in_seconds.TimeoutInSeconds"
    """<p>An integer that represents the maximum time, in seconds, to wait for a delivery confirmation (PUBACK) from the receiving client after the message has been delivered. This parameter is only used when <code>confirmation</code> is set to <code>true</code>. If <code>confirmation</code> is <code>false</code>, this parameter is ignored.</p> <p>The total API response time may be higher than this value due to internal processing. Set your HTTP client timeout to a value greater than this parameter.</p> <p>Valid range: 1 to 15 seconds.</p> <p>Default value: <code>5</code> seconds.</p>"""
    payload: NotRequired["capo_iot_data_plane.types.payload.Payload"]
    """<p>The message body. MQTT accepts text, binary, and empty (null) message payloads.</p>"""
    user_properties: NotRequired[
        "capo_iot_data_plane.types.synthesized_json_user_properties.SynthesizedJsonUserProperties"
    ]
    """<p>A JSON string that contains an array of JSON objects. If you don't use Amazon Web Services SDK or CLI, you must encode the JSON string to base64 format before adding it to the HTTP header. <code>userProperties</code> is an HTTP header value in the API.</p> <p>For MQTT 3.1.1 clients, user properties are silently dropped.</p> <p>The following example <code>userProperties</code> parameter is a JSON string which represents two User Properties. Note that it needs to be base64-encoded:</p> <p> <code>[{"deviceName": "alpha"}, {"deviceCnt": "45"}]</code> </p>"""
    payload_format_indicator: NotRequired[
        "capo_iot_data_plane.types.payload_format_indicator.PayloadFormatIndicator"
    ]
    """<p>An <code>Enum</code> string value that indicates whether the payload is formatted as UTF-8. <code>payloadFormatIndicator</code> is an HTTP header value in the API.</p>"""
    correlation_data: NotRequired[
        "capo_iot_data_plane.types.correlation_data.CorrelationData"
    ]
    """<p>The base64-encoded binary data used by the sender of the request message to identify which request the response message is for when it's received. <code>correlationData</code> is an HTTP header value in the API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendDirectMessageRequest) -> dict:
    out: dict = {}
    if "payload" in value:
        import capo_iot_data_plane.types.payload

        out["payload"] = capo_iot_data_plane.types.payload.serialize_json(
            value["payload"]
        )
    return out


def deserialize_json(data: dict) -> SendDirectMessageRequest:
    out: SendDirectMessageRequest = {}  # type: ignore[typeddict-item]
    if data.get("payload") is not None:
        import capo_iot_data_plane.types.payload

        out["payload"] = capo_iot_data_plane.types.payload.deserialize_json(
            data["payload"]
        )
    return out
