"""Generated from Smithy shape ``com.amazonaws.voiceid#Speaker``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.customer_speaker_id
    import capo_voice_id.types.domain_id
    import capo_voice_id.types.generated_speaker_id
    import capo_voice_id.types.speaker_status
    import capo_voice_id.types.timestamp


class Speaker(TypedDict, closed=True):
    domain_id: NotRequired["capo_voice_id.types.domain_id.DomainId"]
    """<p>The identifier of the domain that contains the speaker.</p>"""
    customer_speaker_id: NotRequired[
        "capo_voice_id.types.customer_speaker_id.CustomerSpeakerId"
    ]
    """<p>The client-provided identifier for the speaker.</p>"""
    generated_speaker_id: NotRequired[
        "capo_voice_id.types.generated_speaker_id.GeneratedSpeakerId"
    ]
    """<p>The service-generated identifier for the speaker.</p>"""
    status: NotRequired["capo_voice_id.types.speaker_status.SpeakerStatus"]
    """<p>The current status of the speaker.</p>"""
    created_at: NotRequired["capo_voice_id.types.timestamp.Timestamp"]
    """<p>A timestamp of when the speaker was created. </p>"""
    updated_at: NotRequired["capo_voice_id.types.timestamp.Timestamp"]
    """<p>A timestamp of the speaker's last update.</p>"""
    last_accessed_at: NotRequired["capo_voice_id.types.timestamp.Timestamp"]
    """<p>The timestamp of when the speaker was last accessed for enrollment, re-enrollment or a successful authentication. This timestamp is accurate to one hour.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Speaker) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["DomainId"] = value["domain_id"]
    if "customer_speaker_id" in value:
        out["CustomerSpeakerId"] = value["customer_speaker_id"]
    if "generated_speaker_id" in value:
        out["GeneratedSpeakerId"] = value["generated_speaker_id"]
    if "status" in value:
        out["Status"] = value["status"]
    if "created_at" in value:
        import capo_voice_id.types.timestamp

        out["CreatedAt"] = capo_voice_id.types.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_voice_id.types.timestamp

        out["UpdatedAt"] = capo_voice_id.types.timestamp.serialize_aws_json_1_0(
            value["updated_at"]
        )
    if "last_accessed_at" in value:
        import capo_voice_id.types.timestamp

        out["LastAccessedAt"] = capo_voice_id.types.timestamp.serialize_aws_json_1_0(
            value["last_accessed_at"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Speaker:
    out: Speaker = {}  # type: ignore[typeddict-item]
    if data.get("DomainId") is not None:
        out["domain_id"] = data["DomainId"]
    if data.get("CustomerSpeakerId") is not None:
        out["customer_speaker_id"] = data["CustomerSpeakerId"]
    if data.get("GeneratedSpeakerId") is not None:
        out["generated_speaker_id"] = data["GeneratedSpeakerId"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("CreatedAt") is not None:
        import capo_voice_id.types.timestamp

        out["created_at"] = capo_voice_id.types.timestamp.deserialize_aws_json_1_0(
            data["CreatedAt"]
        )
    if data.get("UpdatedAt") is not None:
        import capo_voice_id.types.timestamp

        out["updated_at"] = capo_voice_id.types.timestamp.deserialize_aws_json_1_0(
            data["UpdatedAt"]
        )
    if data.get("LastAccessedAt") is not None:
        import capo_voice_id.types.timestamp

        out["last_accessed_at"] = (
            capo_voice_id.types.timestamp.deserialize_aws_json_1_0(
                data["LastAccessedAt"]
            )
        )
    return out


def redact_sensitive(value: Speaker) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "customer_speaker_id" in value:
        out["customer_speaker_id"] = "*** Sensitive Data Redacted ***"
    return out
