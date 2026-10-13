"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#RedundantIngestCredential``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.participant_id
    import capo_ivs_realtime.types.stream_key


class RedundantIngestCredential(TypedDict, closed=True):
    participant_id: NotRequired["capo_ivs_realtime.types.participant_id.ParticipantId"]
    """<p>ID of the participant within the stage.</p>"""
    stream_key: NotRequired["capo_ivs_realtime.types.stream_key.StreamKey"]
    """<p>Ingest-key value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedundantIngestCredential) -> dict:
    out: dict = {}
    if "participant_id" in value:
        out["participantId"] = value["participant_id"]
    if "stream_key" in value:
        out["streamKey"] = value["stream_key"]
    return out


def deserialize_json(data: dict) -> RedundantIngestCredential:
    out: RedundantIngestCredential = {}  # type: ignore[typeddict-item]
    if data.get("participantId") is not None:
        out["participant_id"] = data["participantId"]
    if data.get("streamKey") is not None:
        out["stream_key"] = data["streamKey"]
    return out


def redact_sensitive(value: RedundantIngestCredential) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "stream_key" in value:
        out["stream_key"] = "*** Sensitive Data Redacted ***"
    return out
