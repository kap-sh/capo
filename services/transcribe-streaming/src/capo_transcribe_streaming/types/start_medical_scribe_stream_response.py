"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#StartMedicalScribeStreamResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.medical_scribe_language_code
    import capo_transcribe_streaming.types.medical_scribe_media_encoding
    import capo_transcribe_streaming.types.medical_scribe_media_sample_rate_hertz
    import capo_transcribe_streaming.types.medical_scribe_result_stream
    import capo_transcribe_streaming.types.request_id
    import capo_transcribe_streaming.types.session_id


class StartMedicalScribeStreamResponse(TypedDict, closed=True):
    session_id: NotRequired["capo_transcribe_streaming.types.session_id.SessionId"]
    """<p>The identifier (in UUID format) for your streaming session.</p> <p>If you already started streaming, this is same ID as the one you specified in your initial <code>StartMedicalScribeStreamRequest</code>. </p>"""
    request_id: NotRequired["capo_transcribe_streaming.types.request_id.RequestId"]
    """<p>The unique identifier for your streaming request. </p>"""
    language_code: NotRequired[
        "capo_transcribe_streaming.types.medical_scribe_language_code.MedicalScribeLanguageCode"
    ]
    """<p>The Language Code that you specified in your request. Same as provided in the <code>StartMedicalScribeStreamRequest</code>. </p>"""
    media_sample_rate_hertz: NotRequired[
        "capo_transcribe_streaming.types.medical_scribe_media_sample_rate_hertz.MedicalScribeMediaSampleRateHertz"
    ]
    """<p>The sample rate (in hertz) that you specified in your request. Same as provided in the <code>StartMedicalScribeStreamRequest</code> </p>"""
    media_encoding: NotRequired[
        "capo_transcribe_streaming.types.medical_scribe_media_encoding.MedicalScribeMediaEncoding"
    ]
    """<p>The Media Encoding you specified in your request. Same as provided in the <code>StartMedicalScribeStreamRequest</code> </p>"""
    result_stream: NotRequired[
        "capo_transcribe_streaming.types.medical_scribe_result_stream.MedicalScribeResultStream"
    ]
    """<p>The result stream where you will receive the output events. </p>"""


def redact_sensitive(value: StartMedicalScribeStreamResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "result_stream" in value:
        out["result_stream"] = "*** Streaming Data Redacted ***"
    return out
