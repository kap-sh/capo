"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#PutSessionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.blob_stream
    import capo_lex_runtime_v2.types.non_empty_string
    import capo_lex_runtime_v2.types.session_id


class PutSessionResponse(TypedDict, closed=True):
    content_type: NotRequired[
        "capo_lex_runtime_v2.types.non_empty_string.NonEmptyString"
    ]
    """<p>The type of response. Same as the type specified in the <code>responseContentType</code> field in the request.</p>"""
    messages: NotRequired["capo_lex_runtime_v2.types.non_empty_string.NonEmptyString"]
    """<p>A list of messages that were last sent to the user. The messages are ordered based on how you return the messages from you Lambda function or the order that the messages are defined in the bot.</p>"""
    session_state: NotRequired[
        "capo_lex_runtime_v2.types.non_empty_string.NonEmptyString"
    ]
    """<p>A base-64-encoded gzipped field that represents the current state of the dialog between the user and the bot. Use this to determine the progress of the conversation and what the next action may be.</p>"""
    request_attributes: NotRequired[
        "capo_lex_runtime_v2.types.non_empty_string.NonEmptyString"
    ]
    """<p>A base-64-encoded gzipped field that provides request-specific information passed between the client application and Amazon Lex V2. These are the same as the <code>requestAttribute</code> parameter in the call to the <code>PutSession</code> operation.</p>"""
    session_id: NotRequired["capo_lex_runtime_v2.types.session_id.SessionId"]
    """<p>The identifier of the session that received the data.</p>"""
    audio_stream: "capo_lex_runtime_v2.types.blob_stream.BlobStream"
    """<p>If the requested content type was audio, the audio version of the message to convey to the user.</p>"""


def redact_sensitive(value: PutSessionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "audio_stream" in value:
        out["audio_stream"] = "*** Streaming Data Redacted ***"
    return out
