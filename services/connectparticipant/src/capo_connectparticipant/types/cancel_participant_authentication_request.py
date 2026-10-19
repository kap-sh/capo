"""Generated from Smithy shape ``com.amazonaws.connectparticipant#CancelParticipantAuthenticationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectparticipant.types.participant_token
    import capo_connectparticipant.types.session_id


class CancelParticipantAuthenticationRequest(TypedDict, closed=True):
    session_id: "capo_connectparticipant.types.session_id.SessionId"
    """<p>The <code>sessionId</code> provided in the <code>authenticationInitiated</code> event.</p>"""
    connection_token: "capo_connectparticipant.types.participant_token.ParticipantToken"
    """<p>The authentication token associated with the participant's connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelParticipantAuthenticationRequest) -> dict:
    out: dict = {}
    out["SessionId"] = value["session_id"]
    return out


def deserialize_json(data: dict) -> CancelParticipantAuthenticationRequest:
    out: CancelParticipantAuthenticationRequest = {}  # type: ignore[typeddict-item]
    if data.get("SessionId") is not None:
        out["session_id"] = data["SessionId"]
    else:
        out["session_id"] = ""
    return out
