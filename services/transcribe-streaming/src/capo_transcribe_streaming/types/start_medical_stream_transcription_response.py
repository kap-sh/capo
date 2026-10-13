"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#StartMedicalStreamTranscriptionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.boolean
    import capo_transcribe_streaming.types.language_code
    import capo_transcribe_streaming.types.media_encoding
    import capo_transcribe_streaming.types.media_sample_rate_hertz
    import capo_transcribe_streaming.types.medical_content_identification_type
    import capo_transcribe_streaming.types.medical_transcript_result_stream
    import capo_transcribe_streaming.types.number_of_channels
    import capo_transcribe_streaming.types.request_id
    import capo_transcribe_streaming.types.session_id
    import capo_transcribe_streaming.types.specialty
    import capo_transcribe_streaming.types.type
    import capo_transcribe_streaming.types.vocabulary_name


class StartMedicalStreamTranscriptionResponse(TypedDict, closed=True):
    request_id: NotRequired["capo_transcribe_streaming.types.request_id.RequestId"]
    """<p>Provides the identifier for your streaming request.</p>"""
    language_code: NotRequired[
        "capo_transcribe_streaming.types.language_code.LanguageCode"
    ]
    """<p>Provides the language code that you specified in your request. This must be <code>en-US</code>.</p>"""
    media_sample_rate_hertz: NotRequired[
        "capo_transcribe_streaming.types.media_sample_rate_hertz.MediaSampleRateHertz"
    ]
    """<p>Provides the sample rate that you specified in your request.</p>"""
    media_encoding: NotRequired[
        "capo_transcribe_streaming.types.media_encoding.MediaEncoding"
    ]
    """<p>Provides the media encoding you specified in your request.</p>"""
    vocabulary_name: NotRequired[
        "capo_transcribe_streaming.types.vocabulary_name.VocabularyName"
    ]
    """<p>Provides the name of the custom vocabulary that you specified in your request.</p>"""
    specialty: NotRequired["capo_transcribe_streaming.types.specialty.Specialty"]
    """<p>Provides the medical specialty that you specified in your request.</p>"""
    type: NotRequired["capo_transcribe_streaming.types.type.Type"]
    """<p>Provides the type of audio you specified in your request.</p>"""
    show_speaker_label: "capo_transcribe_streaming.types.boolean.Boolean"
    """<p>Shows whether speaker partitioning was enabled for your transcription.</p>"""
    session_id: NotRequired["capo_transcribe_streaming.types.session_id.SessionId"]
    """<p>Provides the identifier for your transcription session.</p>"""
    transcript_result_stream: NotRequired[
        "capo_transcribe_streaming.types.medical_transcript_result_stream.MedicalTranscriptResultStream"
    ]
    """<p>Provides detailed information about your streaming session.</p>"""
    enable_channel_identification: "capo_transcribe_streaming.types.boolean.Boolean"
    """<p>Shows whether channel identification was enabled for your transcription.</p>"""
    number_of_channels: NotRequired[
        "capo_transcribe_streaming.types.number_of_channels.NumberOfChannels"
    ]
    """<p>Provides the number of channels that you specified in your request.</p>"""
    content_identification_type: NotRequired[
        "capo_transcribe_streaming.types.medical_content_identification_type.MedicalContentIdentificationType"
    ]
    """<p>Shows whether content identification was enabled for your transcription.</p>"""


def redact_sensitive(value: StartMedicalStreamTranscriptionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "transcript_result_stream" in value:
        out["transcript_result_stream"] = "*** Streaming Data Redacted ***"
    return out
