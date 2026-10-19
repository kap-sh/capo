"""Generated from Smithy shape ``com.amazonaws.qapps#SessionSharingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.session_sharing_accept_responses
    import capo_qapps.types.session_sharing_enabled
    import capo_qapps.types.session_sharing_reveal_cards


class SessionSharingConfiguration(TypedDict, closed=True):
    enabled: "capo_qapps.types.session_sharing_enabled.SessionSharingEnabled"
    """<p>Indicates whether an Q App session is shareable with other users.</p>"""
    accept_responses: NotRequired[
        "capo_qapps.types.session_sharing_accept_responses.SessionSharingAcceptResponses"
    ]
    """<p>Indicates whether an Q App session can accept responses from users.</p>"""
    reveal_cards: NotRequired[
        "capo_qapps.types.session_sharing_reveal_cards.SessionSharingRevealCards"
    ]
    """<p>Indicates whether collected responses for an Q App session are revealed for all users.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionSharingConfiguration) -> dict:
    out: dict = {}
    out["enabled"] = value["enabled"]
    if "accept_responses" in value:
        out["acceptResponses"] = value["accept_responses"]
    if "reveal_cards" in value:
        out["revealCards"] = value["reveal_cards"]
    return out


def deserialize_json(data: dict) -> SessionSharingConfiguration:
    out: SessionSharingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    if data.get("acceptResponses") is not None:
        out["accept_responses"] = data["acceptResponses"]
    if data.get("revealCards") is not None:
        out["reveal_cards"] = data["revealCards"]
    return out
