"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#VoiceProfileSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.arn
    import capo_chime_sdk_voice.types.iso8601_timestamp
    import capo_chime_sdk_voice.types.non_empty_string256


class VoiceProfileSummary(TypedDict, closed=True):
    voice_profile_id: NotRequired[
        "capo_chime_sdk_voice.types.non_empty_string256.NonEmptyString256"
    ]
    """<p>The ID of the voice profile in a voice profile summary.</p>"""
    voice_profile_arn: NotRequired["capo_chime_sdk_voice.types.arn.Arn"]
    """<p>The ARN of the voice profile in a voice profile summary.</p>"""
    voice_profile_domain_id: NotRequired[
        "capo_chime_sdk_voice.types.non_empty_string256.NonEmptyString256"
    ]
    """<p>The ID of the voice profile domain in a voice profile summary.</p>"""
    created_timestamp: NotRequired[
        "capo_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time at which a voice profile summary was created.</p>"""
    updated_timestamp: NotRequired[
        "capo_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time at which a voice profile summary was last updated.</p>"""
    expiration_timestamp: NotRequired[
        "capo_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>Extends the life of the voice profile. You can use <code>UpdateVoiceProfile</code> to refresh an existing voice profile's voice print and extend the life of the summary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VoiceProfileSummary) -> dict:
    out: dict = {}
    if "voice_profile_id" in value:
        out["VoiceProfileId"] = value["voice_profile_id"]
    if "voice_profile_arn" in value:
        out["VoiceProfileArn"] = value["voice_profile_arn"]
    if "voice_profile_domain_id" in value:
        out["VoiceProfileDomainId"] = value["voice_profile_domain_id"]
    if "created_timestamp" in value:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["CreatedTimestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    if "updated_timestamp" in value:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["UpdatedTimestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
                value["updated_timestamp"]
            )
        )
    if "expiration_timestamp" in value:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["ExpirationTimestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
                value["expiration_timestamp"]
            )
        )
    return out


def deserialize_json(data: dict) -> VoiceProfileSummary:
    out: VoiceProfileSummary = {}  # type: ignore[typeddict-item]
    if data.get("VoiceProfileId") is not None:
        out["voice_profile_id"] = data["VoiceProfileId"]
    if data.get("VoiceProfileArn") is not None:
        out["voice_profile_arn"] = data["VoiceProfileArn"]
    if data.get("VoiceProfileDomainId") is not None:
        out["voice_profile_domain_id"] = data["VoiceProfileDomainId"]
    if data.get("CreatedTimestamp") is not None:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["created_timestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if data.get("UpdatedTimestamp") is not None:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["updated_timestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["UpdatedTimestamp"]
            )
        )
    if data.get("ExpirationTimestamp") is not None:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["expiration_timestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["ExpirationTimestamp"]
            )
        )
    return out


def redact_sensitive(value: VoiceProfileSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "voice_profile_arn" in value:
        out["voice_profile_arn"] = "*** Sensitive Data Redacted ***"
    return out
