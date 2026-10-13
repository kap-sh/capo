"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#RecognizeUtteranceResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.blob_stream
    import capo_lex_runtime_v2.types.non_empty_string
    import capo_lex_runtime_v2.types.session_id


class RecognizeUtteranceResponse(TypedDict, closed=True):
    input_mode: NotRequired["capo_lex_runtime_v2.types.non_empty_string.NonEmptyString"]
    """<p>Indicates whether the input mode to the operation was text, speech, or from a touch-tone keypad. </p>"""
    content_type: NotRequired[
        "capo_lex_runtime_v2.types.non_empty_string.NonEmptyString"
    ]
    """<p>Content type as specified in the <code>responseContentType</code> in the request.</p>"""
    messages: NotRequired["capo_lex_runtime_v2.types.non_empty_string.NonEmptyString"]
    """<p>A list of messages that were last sent to the user. The messages are ordered based on the order that you returned the messages from your Lambda function or the order that the messages are defined in the bot.</p> <p>The <code>messages</code> field is compressed with gzip and then base64 encoded. Before you can use the contents of the field, you must decode and decompress the contents. See the example for a simple function to decode and decompress the contents.</p>"""
    interpretations: NotRequired[
        "capo_lex_runtime_v2.types.non_empty_string.NonEmptyString"
    ]
    """<p>A list of intents that Amazon Lex V2 determined might satisfy the user's utterance.</p> <p>Each interpretation includes the intent, a score that indicates how confident Amazon Lex V2 is that the interpretation is the correct one, and an optional sentiment response that indicates the sentiment expressed in the utterance.</p> <p>The <code>interpretations</code> field is compressed with gzip and then base64 encoded. Before you can use the contents of the field, you must decode and decompress the contents. See the example for a simple function to decode and decompress the contents.</p>"""
    session_state: NotRequired[
        "capo_lex_runtime_v2.types.non_empty_string.NonEmptyString"
    ]
    """<p>Represents the current state of the dialog between the user and the bot.</p> <p>Use this to determine the progress of the conversation and what the next action might be.</p> <p>The <code>sessionState</code> field is compressed with gzip and then base64 encoded. Before you can use the contents of the field, you must decode and decompress the contents. See the example for a simple function to decode and decompress the contents.</p>"""
    request_attributes: NotRequired[
        "capo_lex_runtime_v2.types.non_empty_string.NonEmptyString"
    ]
    """<p>The attributes sent in the request.</p> <p>The <code>requestAttributes</code> field is compressed with gzip and then base64 encoded. Before you can use the contents of the field, you must decode and decompress the contents.</p>"""
    session_id: NotRequired["capo_lex_runtime_v2.types.session_id.SessionId"]
    """<p>The identifier of the session in use.</p>"""
    input_transcript: NotRequired[
        "capo_lex_runtime_v2.types.non_empty_string.NonEmptyString"
    ]
    """<p>The text used to process the request.</p> <p>If the input was an audio stream, the <code>inputTranscript</code> field contains the text extracted from the audio stream. This is the text that is actually processed to recognize intents and slot values. You can use this information to determine if Amazon Lex V2 is correctly processing the audio that you send.</p> <p>The <code>inputTranscript</code> field is compressed with gzip and then base64 encoded. Before you can use the contents of the field, you must decode and decompress the contents. See the example for a simple function to decode and decompress the contents.</p>"""
    audio_stream: "capo_lex_runtime_v2.types.blob_stream.BlobStream"
    """<p>The prompt or statement to send to the user. This is based on the bot configuration and context. For example, if Amazon Lex V2 did not understand the user intent, it sends the <code>clarificationPrompt</code> configured for the bot. If the intent requires confirmation before taking the fulfillment action, it sends the <code>confirmationPrompt</code>. Another example: Suppose that the Lambda function successfully fulfilled the intent, and sent a message to convey to the user. Then Amazon Lex V2 sends that message in the response.</p>"""
    recognized_bot_member: NotRequired[
        "capo_lex_runtime_v2.types.non_empty_string.NonEmptyString"
    ]
    """<p>The bot member that recognized the utterance.</p>"""


def redact_sensitive(value: RecognizeUtteranceResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "audio_stream" in value:
        out["audio_stream"] = "*** Streaming Data Redacted ***"
    return out
