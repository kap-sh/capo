"""Generated from Smithy shape ``com.amazonaws.voiceid#AuthenticationResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.authentication_configuration
    import capo_voice_id.types.authentication_decision
    import capo_voice_id.types.customer_speaker_id
    import capo_voice_id.types.generated_speaker_id
    import capo_voice_id.types.score
    import capo_voice_id.types.timestamp
    import capo_voice_id.types.unique_id_large


class AuthenticationResult(TypedDict, closed=True):
    authentication_result_id: NotRequired[
        "capo_voice_id.types.unique_id_large.UniqueIdLarge"
    ]
    """<p>The unique identifier for this authentication result. Because there can be multiple authentications for a given session, this field helps to identify if the returned result is from a previous streaming activity or a new result. Note that in absence of any new streaming activity, <code>AcceptanceThreshold</code> changes, or <code>SpeakerId</code> changes, Voice ID always returns cached Authentication Result for this API.</p>"""
    audio_aggregation_started_at: NotRequired["capo_voice_id.types.timestamp.Timestamp"]
    """<p>A timestamp of when audio aggregation started for this authentication result.</p>"""
    audio_aggregation_ended_at: NotRequired["capo_voice_id.types.timestamp.Timestamp"]
    """<p>A timestamp of when audio aggregation ended for this authentication result.</p>"""
    customer_speaker_id: NotRequired[
        "capo_voice_id.types.customer_speaker_id.CustomerSpeakerId"
    ]
    """<p>The client-provided identifier for the speaker whose authentication result is produced. Only present if a <code>SpeakerId</code> is provided for the session.</p>"""
    generated_speaker_id: NotRequired[
        "capo_voice_id.types.generated_speaker_id.GeneratedSpeakerId"
    ]
    """<p>The service-generated identifier for the speaker whose authentication result is produced.</p>"""
    decision: NotRequired[
        "capo_voice_id.types.authentication_decision.AuthenticationDecision"
    ]
    """<p>The authentication decision produced by Voice ID, processed against the current session state and streamed audio of the speaker.</p>"""
    score: NotRequired["capo_voice_id.types.score.Score"]
    """<p>The authentication score for the speaker whose authentication result is produced. This value is only present if the authentication decision is either <code>ACCEPT</code> or <code>REJECT</code>.</p>"""
    configuration: NotRequired[
        "capo_voice_id.types.authentication_configuration.AuthenticationConfiguration"
    ]
    """<p>The <code>AuthenticationConfiguration</code> used to generate this authentication result.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AuthenticationResult) -> dict:
    out: dict = {}
    if "authentication_result_id" in value:
        out["AuthenticationResultId"] = value["authentication_result_id"]
    if "audio_aggregation_started_at" in value:
        import capo_voice_id.types.timestamp

        out["AudioAggregationStartedAt"] = (
            capo_voice_id.types.timestamp.serialize_aws_json_1_0(
                value["audio_aggregation_started_at"]
            )
        )
    if "audio_aggregation_ended_at" in value:
        import capo_voice_id.types.timestamp

        out["AudioAggregationEndedAt"] = (
            capo_voice_id.types.timestamp.serialize_aws_json_1_0(
                value["audio_aggregation_ended_at"]
            )
        )
    if "customer_speaker_id" in value:
        out["CustomerSpeakerId"] = value["customer_speaker_id"]
    if "generated_speaker_id" in value:
        out["GeneratedSpeakerId"] = value["generated_speaker_id"]
    if "decision" in value:
        out["Decision"] = value["decision"]
    if "score" in value:
        out["Score"] = value["score"]
    if "configuration" in value:
        import capo_voice_id.types.authentication_configuration

        out["Configuration"] = (
            capo_voice_id.types.authentication_configuration.serialize_aws_json_1_0(
                value["configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AuthenticationResult:
    out: AuthenticationResult = {}  # type: ignore[typeddict-item]
    if data.get("AuthenticationResultId") is not None:
        out["authentication_result_id"] = data["AuthenticationResultId"]
    if data.get("AudioAggregationStartedAt") is not None:
        import capo_voice_id.types.timestamp

        out["audio_aggregation_started_at"] = (
            capo_voice_id.types.timestamp.deserialize_aws_json_1_0(
                data["AudioAggregationStartedAt"]
            )
        )
    if data.get("AudioAggregationEndedAt") is not None:
        import capo_voice_id.types.timestamp

        out["audio_aggregation_ended_at"] = (
            capo_voice_id.types.timestamp.deserialize_aws_json_1_0(
                data["AudioAggregationEndedAt"]
            )
        )
    if data.get("CustomerSpeakerId") is not None:
        out["customer_speaker_id"] = data["CustomerSpeakerId"]
    if data.get("GeneratedSpeakerId") is not None:
        out["generated_speaker_id"] = data["GeneratedSpeakerId"]
    if data.get("Decision") is not None:
        out["decision"] = data["Decision"]
    if data.get("Score") is not None:
        out["score"] = data["Score"]
    if data.get("Configuration") is not None:
        import capo_voice_id.types.authentication_configuration

        out["configuration"] = (
            capo_voice_id.types.authentication_configuration.deserialize_aws_json_1_0(
                data["Configuration"]
            )
        )
    return out


def redact_sensitive(value: AuthenticationResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "customer_speaker_id" in value:
        out["customer_speaker_id"] = "*** Sensitive Data Redacted ***"
    return out
