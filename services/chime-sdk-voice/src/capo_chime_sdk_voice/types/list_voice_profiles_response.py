"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ListVoiceProfilesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.string
    import capo_chime_sdk_voice.types.voice_profile_summary_list


class ListVoiceProfilesResponse(TypedDict, closed=True):
    voice_profiles: NotRequired[
        "capo_chime_sdk_voice.types.voice_profile_summary_list.VoiceProfileSummaryList"
    ]
    """<p>The list of voice profiles.</p>"""
    next_token: NotRequired["capo_chime_sdk_voice.types.string.String"]
    """<p>The token used to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVoiceProfilesResponse) -> dict:
    out: dict = {}
    if "voice_profiles" in value:
        import capo_chime_sdk_voice.types.voice_profile_summary_list

        out["VoiceProfiles"] = (
            capo_chime_sdk_voice.types.voice_profile_summary_list.serialize_json(
                value["voice_profiles"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListVoiceProfilesResponse:
    out: ListVoiceProfilesResponse = {}  # type: ignore[typeddict-item]
    if data.get("VoiceProfiles") is not None:
        import capo_chime_sdk_voice.types.voice_profile_summary_list

        out["voice_profiles"] = (
            capo_chime_sdk_voice.types.voice_profile_summary_list.deserialize_json(
                data["VoiceProfiles"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListVoiceProfilesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "voice_profiles" in value:
        import capo_chime_sdk_voice.types.voice_profile_summary_list

        out["voice_profiles"] = (
            capo_chime_sdk_voice.types.voice_profile_summary_list.redact_sensitive(
                value["voice_profiles"]
            )
        )
    return out
