"""Generated from Smithy shape ``com.amazonaws.connectparticipant#GetAuthenticationUrlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectparticipant.types.participant_token
    import capo_connectparticipant.types.redirect_uri
    import capo_connectparticipant.types.session_id


class GetAuthenticationUrlRequest(TypedDict, closed=True):
    session_id: "capo_connectparticipant.types.session_id.SessionId"
    """<p>The sessionId provided in the authenticationInitiated event.</p>"""
    redirect_uri: "capo_connectparticipant.types.redirect_uri.RedirectURI"
    """<p>The URL where the customer will be redirected after Amazon Cognito authorizes the user.</p>"""
    connection_token: "capo_connectparticipant.types.participant_token.ParticipantToken"
    """<p>The authentication token associated with the participant's connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAuthenticationUrlRequest) -> dict:
    out: dict = {}
    out["SessionId"] = value["session_id"]
    out["RedirectUri"] = value["redirect_uri"]
    return out


def deserialize_json(data: dict) -> GetAuthenticationUrlRequest:
    out: GetAuthenticationUrlRequest = {}  # type: ignore[typeddict-item]
    if data.get("SessionId") is not None:
        out["session_id"] = data["SessionId"]
    else:
        out["session_id"] = ""
    if data.get("RedirectUri") is not None:
        out["redirect_uri"] = data["RedirectUri"]
    else:
        out["redirect_uri"] = ""
    return out
