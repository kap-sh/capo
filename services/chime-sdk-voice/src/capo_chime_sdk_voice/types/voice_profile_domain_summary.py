"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#VoiceProfileDomainSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.arn
    import capo_chime_sdk_voice.types.iso8601_timestamp
    import capo_chime_sdk_voice.types.non_empty_string256
    import capo_chime_sdk_voice.types.voice_profile_domain_description
    import capo_chime_sdk_voice.types.voice_profile_domain_name


class VoiceProfileDomainSummary(TypedDict, closed=True):
    voice_profile_domain_id: NotRequired[
        "capo_chime_sdk_voice.types.non_empty_string256.NonEmptyString256"
    ]
    """<p>The ID of the voice profile domain summary.</p>"""
    voice_profile_domain_arn: NotRequired["capo_chime_sdk_voice.types.arn.Arn"]
    """<p>The ARN of a voice profile in a voice profile domain summary.</p>"""
    name: NotRequired[
        "capo_chime_sdk_voice.types.voice_profile_domain_name.VoiceProfileDomainName"
    ]
    """<p>The name of the voice profile domain summary.</p>"""
    description: NotRequired[
        "capo_chime_sdk_voice.types.voice_profile_domain_description.VoiceProfileDomainDescription"
    ]
    """<p>Describes the voice profile domain summary.</p>"""
    created_timestamp: NotRequired[
        "capo_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time at which the voice profile domain summary was created.</p>"""
    updated_timestamp: NotRequired[
        "capo_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time at which the voice profile domain summary was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VoiceProfileDomainSummary) -> dict:
    out: dict = {}
    if "voice_profile_domain_id" in value:
        out["VoiceProfileDomainId"] = value["voice_profile_domain_id"]
    if "voice_profile_domain_arn" in value:
        out["VoiceProfileDomainArn"] = value["voice_profile_domain_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
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
    return out


def deserialize_json(data: dict) -> VoiceProfileDomainSummary:
    out: VoiceProfileDomainSummary = {}  # type: ignore[typeddict-item]
    if data.get("VoiceProfileDomainId") is not None:
        out["voice_profile_domain_id"] = data["VoiceProfileDomainId"]
    if data.get("VoiceProfileDomainArn") is not None:
        out["voice_profile_domain_arn"] = data["VoiceProfileDomainArn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
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
    return out


def redact_sensitive(value: VoiceProfileDomainSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "voice_profile_domain_arn" in value:
        out["voice_profile_domain_arn"] = "*** Sensitive Data Redacted ***"
    return out
