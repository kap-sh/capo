"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#PostTextResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_runtime_service.types.active_contexts_list
    import capo_lex_runtime_service.types.bot_version
    import capo_lex_runtime_service.types.dialog_state
    import capo_lex_runtime_service.types.intent_confidence
    import capo_lex_runtime_service.types.intent_list
    import capo_lex_runtime_service.types.intent_name
    import capo_lex_runtime_service.types.message_format_type
    import capo_lex_runtime_service.types.response_card
    import capo_lex_runtime_service.types.sentiment_response
    import capo_lex_runtime_service.types.string
    import capo_lex_runtime_service.types.string_map
    import capo_lex_runtime_service.types.text


class PostTextResponse(TypedDict, closed=True):
    intent_name: NotRequired["capo_lex_runtime_service.types.intent_name.IntentName"]
    """<p>The current user intent that Amazon Lex is aware of.</p>"""
    nlu_intent_confidence: NotRequired[
        "capo_lex_runtime_service.types.intent_confidence.IntentConfidence"
    ]
    """<p>Provides a score that indicates how confident Amazon Lex is that the returned intent is the one that matches the user's intent. The score is between 0.0 and 1.0. For more information, see <a href="https://docs.aws.amazon.com/lex/latest/dg/confidence-scores.html">Confidence Scores</a>.</p> <p>The score is a relative score, not an absolute score. The score may change based on improvements to Amazon Lex.</p>"""
    alternative_intents: NotRequired[
        "capo_lex_runtime_service.types.intent_list.IntentList"
    ]
    """<p>One to four alternative intents that may be applicable to the user's intent.</p> <p>Each alternative includes a score that indicates how confident Amazon Lex is that the intent matches the user's intent. The intents are sorted by the confidence score.</p>"""
    slots: NotRequired["capo_lex_runtime_service.types.string_map.StringMap"]
    """<p> The intent slots that Amazon Lex detected from the user input in the conversation. </p> <p>Amazon Lex creates a resolution list containing likely values for a slot. The value that it returns is determined by the <code>valueSelectionStrategy</code> selected when the slot type was created or updated. If <code>valueSelectionStrategy</code> is set to <code>ORIGINAL_VALUE</code>, the value provided by the user is returned, if the user value is similar to the slot values. If <code>valueSelectionStrategy</code> is set to <code>TOP_RESOLUTION</code> Amazon Lex returns the first value in the resolution list or, if there is no resolution list, null. If you don't specify a <code>valueSelectionStrategy</code>, the default is <code>ORIGINAL_VALUE</code>.</p>"""
    session_attributes: NotRequired[
        "capo_lex_runtime_service.types.string_map.StringMap"
    ]
    """<p>A map of key-value pairs representing the session-specific context information.</p>"""
    message: NotRequired["capo_lex_runtime_service.types.text.Text"]
    """<p>The message to convey to the user. The message can come from the bot's configuration or from a Lambda function.</p> <p>If the intent is not configured with a Lambda function, or if the Lambda function returned <code>Delegate</code> as the <code>dialogAction.type</code> its response, Amazon Lex decides on the next course of action and selects an appropriate message from the bot's configuration based on the current interaction context. For example, if Amazon Lex isn't able to understand user input, it uses a clarification prompt message.</p> <p>When you create an intent you can assign messages to groups. When messages are assigned to groups Amazon Lex returns one message from each group in the response. The message field is an escaped JSON string containing the messages. For more information about the structure of the JSON string returned, see <a>msg-prompts-formats</a>.</p> <p>If the Lambda function returns a message, Amazon Lex passes it to the client in its response.</p>"""
    sentiment_response: NotRequired[
        "capo_lex_runtime_service.types.sentiment_response.SentimentResponse"
    ]
    """<p>The sentiment expressed in and utterance.</p> <p>When the bot is configured to send utterances to Amazon Comprehend for sentiment analysis, this field contains the result of the analysis.</p>"""
    message_format: NotRequired[
        "capo_lex_runtime_service.types.message_format_type.MessageFormatType"
    ]
    """<p>The format of the response message. One of the following values:</p> <ul> <li> <p> <code>PlainText</code> - The message contains plain UTF-8 text.</p> </li> <li> <p> <code>CustomPayload</code> - The message is a custom format defined by the Lambda function.</p> </li> <li> <p> <code>SSML</code> - The message contains text formatted for voice output.</p> </li> <li> <p> <code>Composite</code> - The message contains an escaped JSON object containing one or more messages from the groups that messages were assigned to when the intent was created.</p> </li> </ul>"""
    dialog_state: NotRequired["capo_lex_runtime_service.types.dialog_state.DialogState"]
    """<p> Identifies the current state of the user interaction. Amazon Lex returns one of the following values as <code>dialogState</code>. The client can optionally use this information to customize the user interface. </p> <ul> <li> <p> <code>ElicitIntent</code> - Amazon Lex wants to elicit user intent. </p> <p>For example, a user might utter an intent ("I want to order a pizza"). If Amazon Lex cannot infer the user intent from this utterance, it will return this dialogState.</p> </li> <li> <p> <code>ConfirmIntent</code> - Amazon Lex is expecting a "yes" or "no" response. </p> <p> For example, Amazon Lex wants user confirmation before fulfilling an intent. </p> <p>Instead of a simple "yes" or "no," a user might respond with additional information. For example, "yes, but make it thick crust pizza" or "no, I want to order a drink". Amazon Lex can process such additional information (in these examples, update the crust type slot value, or change intent from OrderPizza to OrderDrink).</p> </li> <li> <p> <code>ElicitSlot</code> - Amazon Lex is expecting a slot value for the current intent. </p> <p>For example, suppose that in the response Amazon Lex sends this message: "What size pizza would you like?". A user might reply with the slot value (e.g., "medium"). The user might also provide additional information in the response (e.g., "medium thick crust pizza"). Amazon Lex can process such additional information appropriately. </p> </li> <li> <p> <code>Fulfilled</code> - Conveys that the Lambda function configured for the intent has successfully fulfilled the intent. </p> </li> <li> <p> <code>ReadyForFulfillment</code> - Conveys that the client has to fulfill the intent. </p> </li> <li> <p> <code>Failed</code> - Conveys that the conversation with the user failed. </p> <p> This can happen for various reasons including that the user did not provide an appropriate response to prompts from the service (you can configure how many times Amazon Lex can prompt a user for specific information), or the Lambda function failed to fulfill the intent. </p> </li> </ul>"""
    slot_to_elicit: NotRequired["capo_lex_runtime_service.types.string.String"]
    """<p>If the <code>dialogState</code> value is <code>ElicitSlot</code>, returns the name of the slot for which Amazon Lex is eliciting a value. </p>"""
    response_card: NotRequired[
        "capo_lex_runtime_service.types.response_card.ResponseCard"
    ]
    """<p>Represents the options that the user has to respond to the current prompt. Response Card can come from the bot configuration (in the Amazon Lex console, choose the settings button next to a slot) or from a code hook (Lambda function). </p>"""
    session_id: NotRequired["capo_lex_runtime_service.types.string.String"]
    """<p>A unique identifier for the session.</p>"""
    bot_version: NotRequired["capo_lex_runtime_service.types.bot_version.BotVersion"]
    """<p>The version of the bot that responded to the conversation. You can use this information to help determine if one version of a bot is performing better than another version.</p>"""
    active_contexts: NotRequired[
        "capo_lex_runtime_service.types.active_contexts_list.ActiveContextsList"
    ]
    """<p>A list of active contexts for the session. A context can be set when an intent is fulfilled or by calling the <code>PostContent</code>, <code>PostText</code>, or <code>PutSession</code> operation.</p> <p>You can use a context to control the intents that can follow up an intent, or to modify the operation of your application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PostTextResponse) -> dict:
    out: dict = {}
    if "intent_name" in value:
        out["intentName"] = value["intent_name"]
    if "nlu_intent_confidence" in value:
        import capo_lex_runtime_service.types.intent_confidence

        out["nluIntentConfidence"] = (
            capo_lex_runtime_service.types.intent_confidence.serialize_json(
                value["nlu_intent_confidence"]
            )
        )
    if "alternative_intents" in value:
        import capo_lex_runtime_service.types.intent_list

        out["alternativeIntents"] = (
            capo_lex_runtime_service.types.intent_list.serialize_json(
                value["alternative_intents"]
            )
        )
    if "slots" in value:
        import capo_lex_runtime_service.types.string_map

        out["slots"] = capo_lex_runtime_service.types.string_map.serialize_json(
            value["slots"]
        )
    if "session_attributes" in value:
        import capo_lex_runtime_service.types.string_map

        out["sessionAttributes"] = (
            capo_lex_runtime_service.types.string_map.serialize_json(
                value["session_attributes"]
            )
        )
    if "message" in value:
        out["message"] = value["message"]
    if "sentiment_response" in value:
        import capo_lex_runtime_service.types.sentiment_response

        out["sentimentResponse"] = (
            capo_lex_runtime_service.types.sentiment_response.serialize_json(
                value["sentiment_response"]
            )
        )
    if "message_format" in value:
        import capo_lex_runtime_service.types.message_format_type

        out["messageFormat"] = (
            capo_lex_runtime_service.types.message_format_type.serialize_json(
                value["message_format"]
            )
        )
    if "dialog_state" in value:
        import capo_lex_runtime_service.types.dialog_state

        out["dialogState"] = capo_lex_runtime_service.types.dialog_state.serialize_json(
            value["dialog_state"]
        )
    if "slot_to_elicit" in value:
        out["slotToElicit"] = value["slot_to_elicit"]
    if "response_card" in value:
        import capo_lex_runtime_service.types.response_card

        out["responseCard"] = (
            capo_lex_runtime_service.types.response_card.serialize_json(
                value["response_card"]
            )
        )
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "active_contexts" in value:
        import capo_lex_runtime_service.types.active_contexts_list

        out["activeContexts"] = (
            capo_lex_runtime_service.types.active_contexts_list.serialize_json(
                value["active_contexts"]
            )
        )
    return out


def deserialize_json(data: dict) -> PostTextResponse:
    out: PostTextResponse = {}  # type: ignore[typeddict-item]
    if data.get("intentName") is not None:
        out["intent_name"] = data["intentName"]
    if data.get("nluIntentConfidence") is not None:
        import capo_lex_runtime_service.types.intent_confidence

        out["nlu_intent_confidence"] = (
            capo_lex_runtime_service.types.intent_confidence.deserialize_json(
                data["nluIntentConfidence"]
            )
        )
    if data.get("alternativeIntents") is not None:
        import capo_lex_runtime_service.types.intent_list

        out["alternative_intents"] = (
            capo_lex_runtime_service.types.intent_list.deserialize_json(
                data["alternativeIntents"]
            )
        )
    if data.get("slots") is not None:
        import capo_lex_runtime_service.types.string_map

        out["slots"] = capo_lex_runtime_service.types.string_map.deserialize_json(
            data["slots"]
        )
    if data.get("sessionAttributes") is not None:
        import capo_lex_runtime_service.types.string_map

        out["session_attributes"] = (
            capo_lex_runtime_service.types.string_map.deserialize_json(
                data["sessionAttributes"]
            )
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("sentimentResponse") is not None:
        import capo_lex_runtime_service.types.sentiment_response

        out["sentiment_response"] = (
            capo_lex_runtime_service.types.sentiment_response.deserialize_json(
                data["sentimentResponse"]
            )
        )
    if data.get("messageFormat") is not None:
        import capo_lex_runtime_service.types.message_format_type

        out["message_format"] = (
            capo_lex_runtime_service.types.message_format_type.deserialize_json(
                data["messageFormat"]
            )
        )
    if data.get("dialogState") is not None:
        import capo_lex_runtime_service.types.dialog_state

        out["dialog_state"] = (
            capo_lex_runtime_service.types.dialog_state.deserialize_json(
                data["dialogState"]
            )
        )
    if data.get("slotToElicit") is not None:
        out["slot_to_elicit"] = data["slotToElicit"]
    if data.get("responseCard") is not None:
        import capo_lex_runtime_service.types.response_card

        out["response_card"] = (
            capo_lex_runtime_service.types.response_card.deserialize_json(
                data["responseCard"]
            )
        )
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    if data.get("botVersion") is not None:
        out["bot_version"] = data["botVersion"]
    if data.get("activeContexts") is not None:
        import capo_lex_runtime_service.types.active_contexts_list

        out["active_contexts"] = (
            capo_lex_runtime_service.types.active_contexts_list.deserialize_json(
                data["activeContexts"]
            )
        )
    return out
