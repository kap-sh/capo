"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#RecognizeUtteranceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.blob_stream
    import capo_lex_runtime_v2.types.bot_alias_identifier
    import capo_lex_runtime_v2.types.bot_identifier
    import capo_lex_runtime_v2.types.locale_id
    import capo_lex_runtime_v2.types.non_empty_string
    import capo_lex_runtime_v2.types.sensitive_non_empty_string
    import capo_lex_runtime_v2.types.session_id


class RecognizeUtteranceRequest(TypedDict, closed=True):
    bot_id: "capo_lex_runtime_v2.types.bot_identifier.BotIdentifier"
    """<p>The identifier of the bot that should receive the request.</p>"""
    bot_alias_id: "capo_lex_runtime_v2.types.bot_alias_identifier.BotAliasIdentifier"
    """<p>The alias identifier in use for the bot that should receive the request.</p>"""
    locale_id: "capo_lex_runtime_v2.types.locale_id.LocaleId"
    """<p>The locale where the session is in use.</p>"""
    session_id: "capo_lex_runtime_v2.types.session_id.SessionId"
    """<p>The identifier of the session in use.</p>"""
    session_state: NotRequired[
        "capo_lex_runtime_v2.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>Sets the state of the session with the user. You can use this to set the current intent, attributes, context, and dialog action. Use the dialog action to determine the next step that Amazon Lex V2 should use in the conversation with the user.</p> <p>The <code>sessionState</code> field must be compressed using gzip and then base64 encoded before sending to Amazon Lex V2.</p>"""
    request_attributes: NotRequired[
        "capo_lex_runtime_v2.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>Request-specific information passed between the client application and Amazon Lex V2 </p> <p>The namespace <code>x-amz-lex:</code> is reserved for special attributes. Don't create any request attributes for prefix <code>x-amz-lex:</code>.</p> <p>The <code>requestAttributes</code> field must be compressed using gzip and then base64 encoded before sending to Amazon Lex V2.</p>"""
    request_content_type: "capo_lex_runtime_v2.types.non_empty_string.NonEmptyString"
    """<p>Indicates the format for audio input or that the content is text. The header must start with one of the following prefixes:</p> <ul> <li> <p>PCM format, audio data must be in little-endian byte order.</p> <ul> <li> <p>audio/l16; rate=16000; channels=1</p> </li> <li> <p>audio/x-l16; sample-rate=16000; channel-count=1</p> </li> <li> <p>audio/lpcm; sample-rate=8000; sample-size-bits=16; channel-count=1; is-big-endian=false</p> </li> </ul> </li> <li> <p>Opus format</p> <ul> <li> <p>audio/x-cbr-opus-with-preamble;preamble-size=0;bit-rate=256000;frame-size-milliseconds=4</p> </li> </ul> </li> <li> <p>Text format</p> <ul> <li> <p>text/plain; charset=utf-8</p> </li> </ul> </li> </ul>"""
    response_content_type: NotRequired[
        "capo_lex_runtime_v2.types.non_empty_string.NonEmptyString"
    ]
    """<p>The message that Amazon Lex V2 returns in the response can be either text or speech based on the <code>responseContentType</code> value.</p> <ul> <li> <p>If the value is <code>text/plain;charset=utf-8</code>, Amazon Lex V2 returns text in the response.</p> </li> <li> <p>If the value begins with <code>audio/</code>, Amazon Lex V2 returns speech in the response. Amazon Lex V2 uses Amazon Polly to generate the speech using the configuration that you specified in the <code>responseContentType</code> parameter. For example, if you specify <code>audio/mpeg</code> as the value, Amazon Lex V2 returns speech in the MPEG format.</p> </li> <li> <p>If the value is <code>audio/pcm</code>, the speech returned is <code>audio/pcm</code> at 16 KHz in 16-bit, little-endian format.</p> </li> <li> <p>The following are the accepted values:</p> <ul> <li> <p>audio/mpeg</p> </li> <li> <p>audio/ogg</p> </li> <li> <p>audio/pcm (16 KHz)</p> </li> <li> <p>audio/* (defaults to mpeg)</p> </li> <li> <p>text/plain; charset=utf-8</p> </li> </ul> </li> </ul>"""
    input_stream: NotRequired["capo_lex_runtime_v2.types.blob_stream.BlobStream"]
    """<p>User input in PCM or Opus audio format or text format as described in the <code>requestContentType</code> parameter.</p>"""


def redact_sensitive(value: RecognizeUtteranceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "session_state" in value:
        out["session_state"] = "*** Sensitive Data Redacted ***"
    if "request_attributes" in value:
        out["request_attributes"] = "*** Sensitive Data Redacted ***"
    if "input_stream" in value:
        out["input_stream"] = "*** Streaming Data Redacted ***"
    return out
