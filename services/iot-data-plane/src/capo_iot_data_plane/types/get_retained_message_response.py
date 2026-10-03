"""Generated from Smithy shape ``com.amazonaws.iotdataplane#GetRetainedMessageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_data_plane.types.payload
    import capo_iot_data_plane.types.qos
    import capo_iot_data_plane.types.timestamp
    import capo_iot_data_plane.types.topic
    import capo_iot_data_plane.types.user_properties_blob


class GetRetainedMessageResponse(TypedDict, closed=True):
    topic: NotRequired["capo_iot_data_plane.types.topic.Topic"]
    """<p>The topic name to which the retained message was published.</p>"""
    payload: NotRequired["capo_iot_data_plane.types.payload.Payload"]
    """<p>The Base64-encoded message payload of the retained message body.</p>"""
    qos: "capo_iot_data_plane.types.qos.Qos"
    """<p>The quality of service (QoS) level used to publish the retained message.</p>"""
    last_modified_time: "capo_iot_data_plane.types.timestamp.Timestamp"
    """<p>The Epoch date and time, in milliseconds, when the retained message was stored by IoT.</p>"""
    user_properties: NotRequired[
        "capo_iot_data_plane.types.user_properties_blob.UserPropertiesBlob"
    ]
    """<p>A base64-encoded JSON string that includes an array of JSON objects, or null if the retained message doesn't include any user properties.</p> <p>The following example <code>userProperties</code> parameter is a JSON string that represents two user properties. Note that it will be base64-encoded:</p> <p> <code>[{"deviceName": "alpha"}, {"deviceCnt": "45"}]</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRetainedMessageResponse) -> dict:
    out: dict = {}
    if "topic" in value:
        out["topic"] = value["topic"]
    if "payload" in value:
        import capo_iot_data_plane.types.payload

        out["payload"] = capo_iot_data_plane.types.payload.serialize_json(
            value["payload"]
        )
    out["qos"] = value.get("qos", 0)
    out["lastModifiedTime"] = value.get("last_modified_time", 0)
    if "user_properties" in value:
        import capo_iot_data_plane.types.user_properties_blob

        out["userProperties"] = (
            capo_iot_data_plane.types.user_properties_blob.serialize_json(
                value["user_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetRetainedMessageResponse:
    out: GetRetainedMessageResponse = {}  # type: ignore[typeddict-item]
    if data.get("topic") is not None:
        out["topic"] = data["topic"]
    if data.get("payload") is not None:
        import capo_iot_data_plane.types.payload

        out["payload"] = capo_iot_data_plane.types.payload.deserialize_json(
            data["payload"]
        )
    if data.get("qos") is not None:
        out["qos"] = data["qos"]
    else:
        out["qos"] = 0
    if data.get("lastModifiedTime") is not None:
        out["last_modified_time"] = data["lastModifiedTime"]
    else:
        out["last_modified_time"] = 0
    if data.get("userProperties") is not None:
        import capo_iot_data_plane.types.user_properties_blob

        out["user_properties"] = (
            capo_iot_data_plane.types.user_properties_blob.deserialize_json(
                data["userProperties"]
            )
        )
    return out
