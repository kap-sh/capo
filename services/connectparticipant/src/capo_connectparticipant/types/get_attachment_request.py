"""Generated from Smithy shape ``com.amazonaws.connectparticipant#GetAttachmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectparticipant.types.artifact_id
    import capo_connectparticipant.types.participant_token
    import capo_connectparticipant.types.url_expiry_in_seconds


class GetAttachmentRequest(TypedDict, closed=True):
    attachment_id: "capo_connectparticipant.types.artifact_id.ArtifactId"
    """<p>A unique identifier for the attachment.</p>"""
    connection_token: "capo_connectparticipant.types.participant_token.ParticipantToken"
    """<p>The authentication token associated with the participant's connection.</p>"""
    url_expiry_in_seconds: NotRequired[
        "capo_connectparticipant.types.url_expiry_in_seconds.URLExpiryInSeconds"
    ]
    """<p>The expiration time of the URL in ISO timestamp. It's specified in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For example, 2019-11-08T02:41:28.172Z.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAttachmentRequest) -> dict:
    out: dict = {}
    out["AttachmentId"] = value["attachment_id"]
    if "url_expiry_in_seconds" in value:
        out["UrlExpiryInSeconds"] = value["url_expiry_in_seconds"]
    return out


def deserialize_json(data: dict) -> GetAttachmentRequest:
    out: GetAttachmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("AttachmentId") is not None:
        out["attachment_id"] = data["AttachmentId"]
    else:
        out["attachment_id"] = ""
    if data.get("UrlExpiryInSeconds") is not None:
        out["url_expiry_in_seconds"] = data["UrlExpiryInSeconds"]
    return out
