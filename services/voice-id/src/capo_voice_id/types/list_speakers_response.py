"""Generated from Smithy shape ``com.amazonaws.voiceid#ListSpeakersResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.speaker_summaries
    import capo_voice_id.types.string


class ListSpeakersResponse(TypedDict, closed=True):
    speaker_summaries: NotRequired[
        "capo_voice_id.types.speaker_summaries.SpeakerSummaries"
    ]
    """<p>A list containing details about each speaker in the Amazon Web Services account. </p>"""
    next_token: NotRequired["capo_voice_id.types.string.String"]
    """<p>If <code>NextToken</code> is returned, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListSpeakersResponse) -> dict:
    out: dict = {}
    if "speaker_summaries" in value:
        import capo_voice_id.types.speaker_summaries

        out["SpeakerSummaries"] = (
            capo_voice_id.types.speaker_summaries.serialize_aws_json_1_0(
                value["speaker_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListSpeakersResponse:
    out: ListSpeakersResponse = {}  # type: ignore[typeddict-item]
    if data.get("SpeakerSummaries") is not None:
        import capo_voice_id.types.speaker_summaries

        out["speaker_summaries"] = (
            capo_voice_id.types.speaker_summaries.deserialize_aws_json_1_0(
                data["SpeakerSummaries"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListSpeakersResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "speaker_summaries" in value:
        import capo_voice_id.types.speaker_summaries

        out["speaker_summaries"] = (
            capo_voice_id.types.speaker_summaries.redact_sensitive(
                value["speaker_summaries"]
            )
        )
    return out
