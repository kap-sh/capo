"""Generated from Smithy shape ``com.amazonaws.voiceid#DeleteSpeakerRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.domain_id
    import capo_voice_id.types.speaker_id


class DeleteSpeakerRequest(TypedDict, closed=True):
    domain_id: "capo_voice_id.types.domain_id.DomainId"
    """<p>The identifier of the domain that contains the speaker.</p>"""
    speaker_id: "capo_voice_id.types.speaker_id.SpeakerId"
    """<p>The identifier of the speaker you want to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteSpeakerRequest) -> dict:
    out: dict = {}
    out["DomainId"] = value["domain_id"]
    out["SpeakerId"] = value["speaker_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteSpeakerRequest:
    out: DeleteSpeakerRequest = {}  # type: ignore[typeddict-item]
    if data.get("DomainId") is not None:
        out["domain_id"] = data["DomainId"]
    else:
        out["domain_id"] = ""
    if data.get("SpeakerId") is not None:
        out["speaker_id"] = data["SpeakerId"]
    else:
        out["speaker_id"] = ""
    return out


def redact_sensitive(value: DeleteSpeakerRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "speaker_id" in value:
        out["speaker_id"] = "*** Sensitive Data Redacted ***"
    return out
