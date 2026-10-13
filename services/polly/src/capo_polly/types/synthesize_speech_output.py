"""Generated from Smithy shape ``com.amazonaws.polly#SynthesizeSpeechOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_polly.types.audio_stream
    import capo_polly.types.content_type
    import capo_polly.types.request_characters


class SynthesizeSpeechOutput(TypedDict, closed=True):
    audio_stream: "capo_polly.types.audio_stream.AudioStream"
    """<p> Stream containing the synthesized speech. </p>"""
    content_type: NotRequired["capo_polly.types.content_type.ContentType"]
    """<p> Specifies the type audio stream. This should reflect the <code>OutputFormat</code> parameter in your request. </p> <ul> <li> <p> If you request <code>mp3</code> as the <code>OutputFormat</code>, the <code>ContentType</code> returned is audio/mpeg. </p> </li> <li> <p> If you request <code>ogg_vorbis</code> as the <code>OutputFormat</code>, the <code>ContentType</code> returned is audio/ogg. </p> </li> <li> <p> If you request <code>ogg_opus</code> as the <code>OutputFormat</code>, the <code>ContentType</code> returned is audio/ogg. </p> </li> <li> <p> If you request <code>pcm</code> as the <code>OutputFormat</code>, the <code>ContentType</code> returned is audio/pcm in a signed 16-bit, 1 channel (mono), little-endian format. </p> </li> <li> <p> If you request <code>mu-law</code> as the <code>OutputFormat</code>, the <code>ContentType</code> returned is audio/mulaw. </p> </li> <li> <p> If you request <code>a-law</code> as the <code>OutputFormat</code>, the <code>ContentType</code> returned is audio/alaw. </p> </li> <li> <p>If you request <code>json</code> as the <code>OutputFormat</code>, the <code>ContentType</code> returned is application/x-json-stream.</p> </li> </ul> <p> </p>"""
    request_characters: "capo_polly.types.request_characters.RequestCharacters"
    """<p>Number of characters synthesized.</p>"""


def redact_sensitive(value: SynthesizeSpeechOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "audio_stream" in value:
        out["audio_stream"] = "*** Streaming Data Redacted ***"
    return out
