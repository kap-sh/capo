"""Generated from Smithy shape ``com.amazonaws.voiceid#DescribeSpeakerResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.speaker


class DescribeSpeakerResponse(TypedDict, closed=True):
    speaker: NotRequired["capo_voice_id.types.speaker.Speaker"]
    """<p>Information about the specified speaker.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeSpeakerResponse) -> dict:
    out: dict = {}
    if "speaker" in value:
        import capo_voice_id.types.speaker

        out["Speaker"] = capo_voice_id.types.speaker.serialize_aws_json_1_0(
            value["speaker"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeSpeakerResponse:
    out: DescribeSpeakerResponse = {}  # type: ignore[typeddict-item]
    if data.get("Speaker") is not None:
        import capo_voice_id.types.speaker

        out["speaker"] = capo_voice_id.types.speaker.deserialize_aws_json_1_0(
            data["Speaker"]
        )
    return out


def redact_sensitive(value: DescribeSpeakerResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "speaker" in value:
        import capo_voice_id.types.speaker

        out["speaker"] = capo_voice_id.types.speaker.redact_sensitive(value["speaker"])
    return out
