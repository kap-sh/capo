"""Generated from Smithy shape ``com.amazonaws.polly#StartSpeechSynthesisStreamInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_polly.types.engine
    import capo_polly.types.language_code
    import capo_polly.types.lexicon_name_list
    import capo_polly.types.output_format
    import capo_polly.types.sample_rate
    import capo_polly.types.start_speech_synthesis_stream_action_stream
    import capo_polly.types.voice_id


class StartSpeechSynthesisStreamInput(TypedDict, closed=True):
    engine: "capo_polly.types.engine.Engine"
    """<p>Specifies the engine for Amazon Polly to use when processing input text for speech synthesis. Currently, only the <code>generative</code> engine is supported. If you specify a voice that the selected engine doesn't support, Amazon Polly returns an error.</p>"""
    language_code: NotRequired["capo_polly.types.language_code.LanguageCode"]
    """<p>An optional parameter that sets the language code for the speech synthesis request. Specify this parameter only when using a bilingual voice. If a bilingual voice is used and no language code is specified, Amazon Polly uses the default language of the bilingual voice.</p>"""
    lexicon_names: NotRequired["capo_polly.types.lexicon_name_list.LexiconNameList"]
    """<p>The names of one or more pronunciation lexicons for the service to apply during synthesis. Amazon Polly applies lexicons only when the lexicon language matches the voice language.</p>"""
    output_format: "capo_polly.types.output_format.OutputFormat"
    """<p>The audio format for the synthesized speech. Currently, Amazon Polly does not support JSON speech marks.</p>"""
    sample_rate: NotRequired["capo_polly.types.sample_rate.SampleRate"]
    """<p>The audio frequency, specified in Hz.</p>"""
    voice_id: "capo_polly.types.voice_id.VoiceId"
    """<p>The voice to use in synthesis. To get a list of available voice IDs, use the <a href="https://docs.aws.amazon.com/polly/latest/API/API_DescribeVoices.html">DescribeVoices</a> operation.</p>"""
    action_stream: NotRequired[
        "capo_polly.types.start_speech_synthesis_stream_action_stream.StartSpeechSynthesisStreamActionStream"
    ]
    """<p>The input event stream that contains text events and stream control events.</p>"""
