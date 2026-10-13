"""Generated from Smithy shape ``com.amazonaws.connecthealth#StartMedicalScribeListeningSessionOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.domain_id
    import capo_connecthealth.types.medical_scribe_language_code
    import capo_connecthealth.types.medical_scribe_media_encoding
    import capo_connecthealth.types.medical_scribe_media_sample_rate_hertz
    import capo_connecthealth.types.medical_scribe_output_stream
    import capo_connecthealth.types.request_id
    import capo_connecthealth.types.scribe_session_id
    import capo_connecthealth.types.subscription_id


class StartMedicalScribeListeningSessionOutput(TypedDict, closed=True):
    session_id: NotRequired[
        "capo_connecthealth.types.scribe_session_id.ScribeSessionId"
    ]
    """<p>The Session identifier</p>"""
    domain_id: NotRequired["capo_connecthealth.types.domain_id.DomainId"]
    """<p>The Domain identifier</p>"""
    subscription_id: NotRequired[
        "capo_connecthealth.types.subscription_id.SubscriptionId"
    ]
    """<p>The Subscription identifier</p>"""
    request_id: NotRequired["capo_connecthealth.types.request_id.RequestId"]
    """<p>The Request identifier</p>"""
    language_code: NotRequired[
        "capo_connecthealth.types.medical_scribe_language_code.MedicalScribeLanguageCode"
    ]
    """<p>The Language Code for the audio in the session</p>"""
    media_sample_rate_hertz: NotRequired[
        "capo_connecthealth.types.medical_scribe_media_sample_rate_hertz.MedicalScribeMediaSampleRateHertz"
    ]
    """<p>The sample rate of the input audio</p>"""
    media_encoding: NotRequired[
        "capo_connecthealth.types.medical_scribe_media_encoding.MedicalScribeMediaEncoding"
    ]
    """<p>The encoding for the input audio</p>"""
    response_stream: NotRequired[
        "capo_connecthealth.types.medical_scribe_output_stream.MedicalScribeOutputStream"
    ]
    """<p>The output stream containing transcript events</p>"""


def redact_sensitive(value: StartMedicalScribeListeningSessionOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "response_stream" in value:
        out["response_stream"] = "*** Streaming Data Redacted ***"
    return out
