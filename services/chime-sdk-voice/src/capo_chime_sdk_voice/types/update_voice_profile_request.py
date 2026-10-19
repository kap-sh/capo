"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#UpdateVoiceProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.non_empty_string256


class UpdateVoiceProfileRequest(TypedDict, closed=True):
    voice_profile_id: "capo_chime_sdk_voice.types.non_empty_string256.NonEmptyString256"
    """<p>The profile ID.</p>"""
    speaker_search_task_id: (
        "capo_chime_sdk_voice.types.non_empty_string256.NonEmptyString256"
    )
    """<p>The ID of the speaker search task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateVoiceProfileRequest) -> dict:
    out: dict = {}
    out["SpeakerSearchTaskId"] = value["speaker_search_task_id"]
    return out


def deserialize_json(data: dict) -> UpdateVoiceProfileRequest:
    out: UpdateVoiceProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("SpeakerSearchTaskId") is not None:
        out["speaker_search_task_id"] = data["SpeakerSearchTaskId"]
    else:
        out["speaker_search_task_id"] = ""
    return out
