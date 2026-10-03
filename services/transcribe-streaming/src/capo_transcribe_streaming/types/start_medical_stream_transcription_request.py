"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#StartMedicalStreamTranscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.audio_stream
    import capo_transcribe_streaming.types.boolean
    import capo_transcribe_streaming.types.language_code
    import capo_transcribe_streaming.types.media_encoding
    import capo_transcribe_streaming.types.media_sample_rate_hertz
    import capo_transcribe_streaming.types.medical_content_identification_type
    import capo_transcribe_streaming.types.number_of_channels
    import capo_transcribe_streaming.types.session_id
    import capo_transcribe_streaming.types.specialty
    import capo_transcribe_streaming.types.type
    import capo_transcribe_streaming.types.vocabulary_name


class StartMedicalStreamTranscriptionRequest(TypedDict, closed=True):
    language_code: "capo_transcribe_streaming.types.language_code.LanguageCode"
    """<p>Specify the language code that represents the language spoken in your audio.</p> <important> <p>Amazon Transcribe Medical only supports US English (<code>en-US</code>).</p> </important>"""
    media_sample_rate_hertz: (
        "capo_transcribe_streaming.types.media_sample_rate_hertz.MediaSampleRateHertz"
    )
    """<p>The sample rate of the input audio (in hertz). Amazon Transcribe Medical supports a range from 16,000 Hz to 48,000 Hz. Note that the sample rate you specify must match that of your audio.</p>"""
    media_encoding: "capo_transcribe_streaming.types.media_encoding.MediaEncoding"
    """<p>Specify the encoding used for the input audio. Supported formats are:</p> <ul> <li> <p>FLAC</p> </li> <li> <p>OPUS-encoded audio in an Ogg container</p> </li> <li> <p>PCM (only signed 16-bit little-endian audio formats, which does not include WAV)</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/how-input.html#how-input-audio">Media formats</a>.</p>"""
    vocabulary_name: NotRequired[
        "capo_transcribe_streaming.types.vocabulary_name.VocabularyName"
    ]
    """<p>Specify the name of the custom vocabulary that you want to use when processing your transcription. Note that vocabulary names are case sensitive.</p>"""
    specialty: "capo_transcribe_streaming.types.specialty.Specialty"
    """<p>Specify the medical specialty contained in your audio.</p>"""
    type: "capo_transcribe_streaming.types.type.Type"
    """<p>Specify the type of input audio. For example, choose <code>DICTATION</code> for a provider dictating patient notes and <code>CONVERSATION</code> for a dialogue between a patient and a medical professional.</p>"""
    show_speaker_label: "capo_transcribe_streaming.types.boolean.Boolean"
    """<p>Enables speaker partitioning (diarization) in your transcription output. Speaker partitioning labels the speech from individual speakers in your media file.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/diarization.html">Partitioning speakers (diarization)</a>.</p>"""
    session_id: NotRequired["capo_transcribe_streaming.types.session_id.SessionId"]
    """<p>Specify a name for your transcription session. If you don't include this parameter in your request, Amazon Transcribe Medical generates an ID and returns it in the response.</p>"""
    audio_stream: "capo_transcribe_streaming.types.audio_stream.AudioStream"
    enable_channel_identification: "capo_transcribe_streaming.types.boolean.Boolean"
    """<p>Enables channel identification in multi-channel audio.</p> <p>Channel identification transcribes the audio on each channel independently, then appends the output for each channel into one transcript.</p> <p>If you have multi-channel audio and do not enable channel identification, your audio is transcribed in a continuous manner and your transcript is not separated by channel.</p> <p>If you include <code>EnableChannelIdentification</code> in your request, you must also include <code>NumberOfChannels</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/channel-id.html">Transcribing multi-channel audio</a>.</p>"""
    number_of_channels: NotRequired[
        "capo_transcribe_streaming.types.number_of_channels.NumberOfChannels"
    ]
    """<p>Specify the number of channels in your audio stream. This value must be <code>2</code>, as only two channels are supported. If your audio doesn't contain multiple channels, do not include this parameter in your request.</p> <p>If you include <code>NumberOfChannels</code> in your request, you must also include <code>EnableChannelIdentification</code>.</p>"""
    content_identification_type: NotRequired[
        "capo_transcribe_streaming.types.medical_content_identification_type.MedicalContentIdentificationType"
    ]
    """<p>Labels all personal health information (PHI) identified in your transcript.</p> <p>Content identification is performed at the segment level; PHI is flagged upon complete transcription of an audio segment.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/phi-id.html">Identifying personal health information (PHI) in a transcription</a>.</p>"""
