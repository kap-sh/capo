"""Generated from Smithy shape ``com.amazonaws.connectparticipant#CreateParticipantConnectionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectparticipant.types.connection_credentials
    import capo_connectparticipant.types.web_rtc_connection
    import capo_connectparticipant.types.websocket


class CreateParticipantConnectionResponse(TypedDict, closed=True):
    websocket: NotRequired["capo_connectparticipant.types.websocket.Websocket"]
    """<p>Creates the participant's websocket connection.</p>"""
    connection_credentials: NotRequired[
        "capo_connectparticipant.types.connection_credentials.ConnectionCredentials"
    ]
    """<p>Creates the participant's connection credentials. The authentication token associated with the participant's connection.</p>"""
    web_rtc_connection: NotRequired[
        "capo_connectparticipant.types.web_rtc_connection.WebRTCConnection"
    ]
    """<p>Creates the participant's WebRTC connection data required for the client application (mobile application or website) to connect to the call. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateParticipantConnectionResponse) -> dict:
    out: dict = {}
    if "websocket" in value:
        import capo_connectparticipant.types.websocket

        out["Websocket"] = capo_connectparticipant.types.websocket.serialize_json(
            value["websocket"]
        )
    if "connection_credentials" in value:
        import capo_connectparticipant.types.connection_credentials

        out["ConnectionCredentials"] = (
            capo_connectparticipant.types.connection_credentials.serialize_json(
                value["connection_credentials"]
            )
        )
    if "web_rtc_connection" in value:
        import capo_connectparticipant.types.web_rtc_connection

        out["WebRTCConnection"] = (
            capo_connectparticipant.types.web_rtc_connection.serialize_json(
                value["web_rtc_connection"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateParticipantConnectionResponse:
    out: CreateParticipantConnectionResponse = {}  # type: ignore[typeddict-item]
    if data.get("Websocket") is not None:
        import capo_connectparticipant.types.websocket

        out["websocket"] = capo_connectparticipant.types.websocket.deserialize_json(
            data["Websocket"]
        )
    if data.get("ConnectionCredentials") is not None:
        import capo_connectparticipant.types.connection_credentials

        out["connection_credentials"] = (
            capo_connectparticipant.types.connection_credentials.deserialize_json(
                data["ConnectionCredentials"]
            )
        )
    if data.get("WebRTCConnection") is not None:
        import capo_connectparticipant.types.web_rtc_connection

        out["web_rtc_connection"] = (
            capo_connectparticipant.types.web_rtc_connection.deserialize_json(
                data["WebRTCConnection"]
            )
        )
    return out


def redact_sensitive(value: CreateParticipantConnectionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "web_rtc_connection" in value:
        import capo_connectparticipant.types.web_rtc_connection

        out["web_rtc_connection"] = (
            capo_connectparticipant.types.web_rtc_connection.redact_sensitive(
                value["web_rtc_connection"]
            )
        )
    return out
