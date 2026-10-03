"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#PutSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_runtime_service.types.blob_stream
    import capo_lex_runtime_service.types.dialog_state
    import capo_lex_runtime_service.types.http_content_type
    import capo_lex_runtime_service.types.intent_name
    import capo_lex_runtime_service.types.message_format_type
    import capo_lex_runtime_service.types.sensitive_string
    import capo_lex_runtime_service.types.string
    import capo_lex_runtime_service.types.synthesized_json_active_contexts_string
    import capo_lex_runtime_service.types.synthesized_json_string
    import capo_lex_runtime_service.types.text


class PutSessionResponse(TypedDict, closed=True):
    content_type: NotRequired[
        "capo_lex_runtime_service.types.http_content_type.HttpContentType"
    ]
    """<p>Content type as specified in the <code>Accept</code> HTTP header in the request.</p>"""
    intent_name: NotRequired["capo_lex_runtime_service.types.intent_name.IntentName"]
    """<p>The name of the current intent.</p>"""
    slots: NotRequired[
        "capo_lex_runtime_service.types.synthesized_json_string.SynthesizedJsonString"
    ]
    """<p>Map of zero or more intent slots Amazon Lex detected from the user input during the conversation.</p> <p>Amazon Lex creates a resolution list containing likely values for a slot. The value that it returns is determined by the <code>valueSelectionStrategy</code> selected when the slot type was created or updated. If <code>valueSelectionStrategy</code> is set to <code>ORIGINAL_VALUE</code>, the value provided by the user is returned, if the user value is similar to the slot values. If <code>valueSelectionStrategy</code> is set to <code>TOP_RESOLUTION</code> Amazon Lex returns the first value in the resolution list or, if there is no resolution list, null. If you don't specify a <code>valueSelectionStrategy</code> the default is <code>ORIGINAL_VALUE</code>. </p>"""
    session_attributes: NotRequired[
        "capo_lex_runtime_service.types.synthesized_json_string.SynthesizedJsonString"
    ]
    """<p>Map of key/value pairs representing session-specific context information.</p>"""
    message: NotRequired["capo_lex_runtime_service.types.text.Text"]
    """<p>The next message that should be presented to the user.</p> <p>You can only use this field in the de-DE, en-AU, en-GB, en-US, es-419, es-ES, es-US, fr-CA, fr-FR, and it-IT locales. In all other locales, the <code>message</code> field is null. You should use the <code>encodedMessage</code> field instead.</p>"""
    encoded_message: NotRequired[
        "capo_lex_runtime_service.types.sensitive_string.SensitiveString"
    ]
    """<p>The next message that should be presented to the user.</p> <p>The <code>encodedMessage</code> field is base-64 encoded. You must decode the field before you can use the value.</p>"""
    message_format: NotRequired[
        "capo_lex_runtime_service.types.message_format_type.MessageFormatType"
    ]
    """<p>The format of the response message. One of the following values:</p> <ul> <li> <p> <code>PlainText</code> - The message contains plain UTF-8 text.</p> </li> <li> <p> <code>CustomPayload</code> - The message is a custom format for the client.</p> </li> <li> <p> <code>SSML</code> - The message contains text formatted for voice output.</p> </li> <li> <p> <code>Composite</code> - The message contains an escaped JSON object containing one or more messages from the groups that messages were assigned to when the intent was created.</p> </li> </ul>"""
    dialog_state: NotRequired["capo_lex_runtime_service.types.dialog_state.DialogState"]
    """<p></p> <ul> <li> <p> <code>ConfirmIntent</code> - Amazon Lex is expecting a "yes" or "no" response to confirm the intent before fulfilling an intent.</p> </li> <li> <p> <code>ElicitIntent</code> - Amazon Lex wants to elicit the user's intent.</p> </li> <li> <p> <code>ElicitSlot</code> - Amazon Lex is expecting the value of a slot for the current intent.</p> </li> <li> <p> <code>Failed</code> - Conveys that the conversation with the user has failed. This can happen for various reasons, including the user does not provide an appropriate response to prompts from the service, or if the Lambda function fails to fulfill the intent.</p> </li> <li> <p> <code>Fulfilled</code> - Conveys that the Lambda function has sucessfully fulfilled the intent.</p> </li> <li> <p> <code>ReadyForFulfillment</code> - Conveys that the client has to fulfill the intent.</p> </li> </ul>"""
    slot_to_elicit: NotRequired["capo_lex_runtime_service.types.string.String"]
    """<p>If the <code>dialogState</code> is <code>ElicitSlot</code>, returns the name of the slot for which Amazon Lex is eliciting a value.</p>"""
    audio_stream: "capo_lex_runtime_service.types.blob_stream.BlobStream"
    """<p>The audio version of the message to convey to the user.</p>"""
    session_id: NotRequired["capo_lex_runtime_service.types.string.String"]
    """<p>A unique identifier for the session.</p>"""
    active_contexts: NotRequired[
        "capo_lex_runtime_service.types.synthesized_json_active_contexts_string.SynthesizedJsonActiveContextsString"
    ]
    """<p>A list of active contexts for the session.</p>"""
