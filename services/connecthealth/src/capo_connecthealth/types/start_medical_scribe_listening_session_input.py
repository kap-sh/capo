"""Generated from Smithy shape ``com.amazonaws.connecthealth#StartMedicalScribeListeningSessionInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.domain_id
    import capo_connecthealth.types.medical_scribe_input_stream
    import capo_connecthealth.types.medical_scribe_language_code
    import capo_connecthealth.types.medical_scribe_media_encoding
    import capo_connecthealth.types.medical_scribe_media_sample_rate_hertz
    import capo_connecthealth.types.scribe_session_id
    import capo_connecthealth.types.subscription_id


class StartMedicalScribeListeningSessionInput(TypedDict, closed=True):
    session_id: "capo_connecthealth.types.scribe_session_id.ScribeSessionId"
    """<p>The Session identifier</p>"""
    domain_id: "capo_connecthealth.types.domain_id.DomainId"
    """<p>The Domain identifier</p>"""
    subscription_id: "capo_connecthealth.types.subscription_id.SubscriptionId"
    """<p>The Subscription identifier</p>"""
    language_code: "capo_connecthealth.types.medical_scribe_language_code.MedicalScribeLanguageCode"
    """<p>The Language Code for the audio in the session</p>"""
    media_sample_rate_hertz: "capo_connecthealth.types.medical_scribe_media_sample_rate_hertz.MedicalScribeMediaSampleRateHertz"
    """<p>The sample rate of the input audio</p>"""
    media_encoding: "capo_connecthealth.types.medical_scribe_media_encoding.MedicalScribeMediaEncoding"
    """<p>The encoding for the input audio</p>"""
    input_stream: NotRequired[
        "capo_connecthealth.types.medical_scribe_input_stream.MedicalScribeInputStream"
    ]
    """<p/>"""


def redact_sensitive(value: StartMedicalScribeListeningSessionInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "input_stream" in value:
        out["input_stream"] = "*** Streaming Data Redacted ***"
    return out
