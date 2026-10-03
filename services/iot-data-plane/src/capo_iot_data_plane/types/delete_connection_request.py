"""Generated from Smithy shape ``com.amazonaws.iotdataplane#DeleteConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_data_plane.types.clean_session
    import capo_iot_data_plane.types.client_id
    import capo_iot_data_plane.types.prevent_will_message


class DeleteConnectionRequest(TypedDict, closed=True):
    client_id: "capo_iot_data_plane.types.client_id.ClientId"
    """<p>The unique identifier of the MQTT client to disconnect. The client ID can't start with a dollar sign ($).</p> <p>MQTT client IDs must be URL encoded (percent-encoded) when they contain characters that are not valid in HTTP requests, such as spaces, forward slashes (/), and UTF-8 characters.</p>"""
    clean_session: "capo_iot_data_plane.types.clean_session.CleanSession"
    """<p>Specifies whether to remove the client's persistent session state when disconnecting. Set to <code>TRUE</code> to delete all session information, including subscriptions and queued messages. Set to <code>FALSE</code> to preserve the session state for <a href="https://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html#mqtt-persistent-sessions">persistent sessions</a>. For clean sessions this parameter will be ignored. By default, this is set to <code>FALSE</code> (preserves the session state).</p>"""
    prevent_will_message: (
        "capo_iot_data_plane.types.prevent_will_message.PreventWillMessage"
    )
    """<p>Controls if Amazon Web Services IoT Core publishes the client's Last Will and Testament (LWT) message upon disconnection. Set to <code>TRUE</code> to prevent publishing the LWT message. Set to <code>FALSE</code> to ensure that LWT is published. By default, this is set to <code>FALSE</code> (LWT message is published).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConnectionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConnectionRequest:
    out: DeleteConnectionRequest = {}  # type: ignore[typeddict-item]
    return out
