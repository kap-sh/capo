"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#PutBotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_model_building_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.boolean
    import capo_lex_model_building_service.types.bot_name
    import capo_lex_model_building_service.types.confidence_threshold
    import capo_lex_model_building_service.types.description
    import capo_lex_model_building_service.types.intent_list
    import capo_lex_model_building_service.types.locale
    import capo_lex_model_building_service.types.process_behavior
    import capo_lex_model_building_service.types.prompt
    import capo_lex_model_building_service.types.session_ttl
    import capo_lex_model_building_service.types.statement
    import capo_lex_model_building_service.types.string
    import capo_lex_model_building_service.types.tag_list


class PutBotRequest(TypedDict, closed=True):
    name: "capo_lex_model_building_service.types.bot_name.BotName"
    """<p>The name of the bot. The name is <i>not</i> case sensitive. </p>"""
    description: NotRequired[
        "capo_lex_model_building_service.types.description.Description"
    ]
    """<p>A description of the bot.</p>"""
    intents: NotRequired["capo_lex_model_building_service.types.intent_list.IntentList"]
    """<p>An array of <code>Intent</code> objects. Each intent represents a command that a user can express. For example, a pizza ordering bot might support an OrderPizza intent. For more information, see <a>how-it-works</a>.</p>"""
    enable_model_improvements: NotRequired[
        "capo_lex_model_building_service.types.boolean.Boolean"
    ]
    """<p>Set to <code>true</code> to enable access to natural language understanding improvements. </p> <p>When you set the <code>enableModelImprovements</code> parameter to <code>true</code> you can use the <code>nluIntentConfidenceThreshold</code> parameter to configure confidence scores. For more information, see <a href="https://docs.aws.amazon.com/lex/latest/dg/confidence-scores.html">Confidence Scores</a>.</p> <p>You can only set the <code>enableModelImprovements</code> parameter in certain Regions. If you set the parameter to <code>true</code>, your bot has access to accuracy improvements.</p> <p>The Regions where you can set the <code>enableModelImprovements</code> parameter to <code>true</code> are:</p> <ul> <li> <p>US East (N. Virginia) (us-east-1)</p> </li> <li> <p>US West (Oregon) (us-west-2)</p> </li> <li> <p>Asia Pacific (Sydney) (ap-southeast-2)</p> </li> <li> <p>EU (Ireland) (eu-west-1)</p> </li> </ul> <p>In other Regions, the <code>enableModelImprovements</code> parameter is set to <code>true</code> by default. In these Regions setting the parameter to <code>false</code> throws a <code>ValidationException</code> exception.</p>"""
    nlu_intent_confidence_threshold: NotRequired[
        "capo_lex_model_building_service.types.confidence_threshold.ConfidenceThreshold"
    ]
    """<p>Determines the threshold where Amazon Lex will insert the <code>AMAZON.FallbackIntent</code>, <code>AMAZON.KendraSearchIntent</code>, or both when returning alternative intents in a <a href="https://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostContent.html">PostContent</a> or <a href="https://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html">PostText</a> response. <code>AMAZON.FallbackIntent</code> and <code>AMAZON.KendraSearchIntent</code> are only inserted if they are configured for the bot.</p> <p>You must set the <code>enableModelImprovements</code> parameter to <code>true</code> to use confidence scores in the following regions.</p> <ul> <li> <p>US East (N. Virginia) (us-east-1)</p> </li> <li> <p>US West (Oregon) (us-west-2)</p> </li> <li> <p>Asia Pacific (Sydney) (ap-southeast-2)</p> </li> <li> <p>EU (Ireland) (eu-west-1)</p> </li> </ul> <p>In other Regions, the <code>enableModelImprovements</code> parameter is set to <code>true</code> by default.</p> <p>For example, suppose a bot is configured with the confidence threshold of 0.80 and the <code>AMAZON.FallbackIntent</code>. Amazon Lex returns three alternative intents with the following confidence scores: IntentA (0.70), IntentB (0.60), IntentC (0.50). The response from the <code>PostText</code> operation would be:</p> <ul> <li> <p>AMAZON.FallbackIntent</p> </li> <li> <p>IntentA</p> </li> <li> <p>IntentB</p> </li> <li> <p>IntentC</p> </li> </ul>"""
    clarification_prompt: NotRequired[
        "capo_lex_model_building_service.types.prompt.Prompt"
    ]
    """<p>When Amazon Lex doesn't understand the user's intent, it uses this message to get clarification. To specify how many times Amazon Lex should repeat the clarification prompt, use the <code>maxAttempts</code> field. If Amazon Lex still doesn't understand, it sends the message in the <code>abortStatement</code> field. </p> <p>When you create a clarification prompt, make sure that it suggests the correct response from the user. for example, for a bot that orders pizza and drinks, you might create this clarification prompt: "What would you like to do? You can say 'Order a pizza' or 'Order a drink.'"</p> <p>If you have defined a fallback intent, it will be invoked if the clarification prompt is repeated the number of times defined in the <code>maxAttempts</code> field. For more information, see <a href="https://docs.aws.amazon.com/lex/latest/dg/built-in-intent-fallback.html"> AMAZON.FallbackIntent</a>.</p> <p>If you don't define a clarification prompt, at runtime Amazon Lex will return a 400 Bad Request exception in three cases: </p> <ul> <li> <p>Follow-up prompt - When the user responds to a follow-up prompt but does not provide an intent. For example, in response to a follow-up prompt that says "Would you like anything else today?" the user says "Yes." Amazon Lex will return a 400 Bad Request exception because it does not have a clarification prompt to send to the user to get an intent.</p> </li> <li> <p>Lambda function - When using a Lambda function, you return an <code>ElicitIntent</code> dialog type. Since Amazon Lex does not have a clarification prompt to get an intent from the user, it returns a 400 Bad Request exception.</p> </li> <li> <p>PutSession operation - When using the <code>PutSession</code> operation, you send an <code>ElicitIntent</code> dialog type. Since Amazon Lex does not have a clarification prompt to get an intent from the user, it returns a 400 Bad Request exception.</p> </li> </ul>"""
    abort_statement: NotRequired[
        "capo_lex_model_building_service.types.statement.Statement"
    ]
    """<p>When Amazon Lex can't understand the user's input in context, it tries to elicit the information a few times. After that, Amazon Lex sends the message defined in <code>abortStatement</code> to the user, and then cancels the conversation. To set the number of retries, use the <code>valueElicitationPrompt</code> field for the slot type. </p> <p>For example, in a pizza ordering bot, Amazon Lex might ask a user "What type of crust would you like?" If the user's response is not one of the expected responses (for example, "thin crust, "deep dish," etc.), Amazon Lex tries to elicit a correct response a few more times. </p> <p>For example, in a pizza ordering application, <code>OrderPizza</code> might be one of the intents. This intent might require the <code>CrustType</code> slot. You specify the <code>valueElicitationPrompt</code> field when you create the <code>CrustType</code> slot.</p> <p>If you have defined a fallback intent the cancel statement will not be sent to the user, the fallback intent is used instead. For more information, see <a href="https://docs.aws.amazon.com/lex/latest/dg/built-in-intent-fallback.html"> AMAZON.FallbackIntent</a>.</p>"""
    idle_session_ttl_in_seconds: NotRequired[
        "capo_lex_model_building_service.types.session_ttl.SessionTTL"
    ]
    """<p>The maximum time in seconds that Amazon Lex retains the data gathered in a conversation.</p> <p>A user interaction session remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Lex deletes any data provided before the timeout.</p> <p>For example, suppose that a user chooses the OrderPizza intent, but gets sidetracked halfway through placing an order. If the user doesn't complete the order within the specified time, Amazon Lex discards the slot information that it gathered, and the user must start over.</p> <p>If you don't include the <code>idleSessionTTLInSeconds</code> element in a <code>PutBot</code> operation request, Amazon Lex uses the default value. This is also true if the request replaces an existing bot.</p> <p>The default is 300 seconds (5 minutes).</p>"""
    voice_id: NotRequired["capo_lex_model_building_service.types.string.String"]
    """<p>The Amazon Polly voice ID that you want Amazon Lex to use for voice interactions with the user. The locale configured for the voice must match the locale of the bot. For more information, see <a href="https://docs.aws.amazon.com/polly/latest/dg/voicelist.html">Voices in Amazon Polly</a> in the <i>Amazon Polly Developer Guide</i>.</p>"""
    checksum: NotRequired["capo_lex_model_building_service.types.string.String"]
    """<p>Identifies a specific revision of the <code>$LATEST</code> version.</p> <p>When you create a new bot, leave the <code>checksum</code> field blank. If you specify a checksum you get a <code>BadRequestException</code> exception.</p> <p>When you want to update a bot, set the <code>checksum</code> field to the checksum of the most recent revision of the <code>$LATEST</code> version. If you don't specify the <code> checksum</code> field, or if the checksum does not match the <code>$LATEST</code> version, you get a <code>PreconditionFailedException</code> exception.</p>"""
    process_behavior: NotRequired[
        "capo_lex_model_building_service.types.process_behavior.ProcessBehavior"
    ]
    """<p>If you set the <code>processBehavior</code> element to <code>BUILD</code>, Amazon Lex builds the bot so that it can be run. If you set the element to <code>SAVE</code> Amazon Lex saves the bot, but doesn't build it. </p> <p>If you don't specify this value, the default value is <code>BUILD</code>.</p>"""
    locale: "capo_lex_model_building_service.types.locale.Locale"
    """<p> Specifies the target locale for the bot. Any intent used in the bot must be compatible with the locale of the bot. </p> <p>The default is <code>en-US</code>.</p>"""
    child_directed: "capo_lex_model_building_service.types.boolean.Boolean"
    """<p>For each Amazon Lex bot created with the Amazon Lex Model Building Service, you must specify whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to the Children's Online Privacy Protection Act (COPPA) by specifying <code>true</code> or <code>false</code> in the <code>childDirected</code> field. By specifying <code>true</code> in the <code>childDirected</code> field, you confirm that your use of Amazon Lex <b>is</b> related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. By specifying <code>false</code> in the <code>childDirected</code> field, you confirm that your use of Amazon Lex <b>is not</b> related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. You may not specify a default value for the <code>childDirected</code> field that does not accurately reflect whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA.</p> <p>If your use of Amazon Lex relates to a website, program, or other application that is directed in whole or in part, to children under age 13, you must obtain any required verifiable parental consent under COPPA. For information regarding the use of Amazon Lex in connection with websites, programs, or other applications that are directed or targeted, in whole or in part, to children under age 13, see the <a href="https://aws.amazon.com/lex/faqs#data-security">Amazon Lex FAQ.</a> </p>"""
    detect_sentiment: NotRequired[
        "capo_lex_model_building_service.types.boolean.Boolean"
    ]
    """<p>When set to <code>true</code> user utterances are sent to Amazon Comprehend for sentiment analysis. If you don't specify <code>detectSentiment</code>, the default is <code>false</code>.</p>"""
    create_version: NotRequired["capo_lex_model_building_service.types.boolean.Boolean"]
    """<p>When set to <code>true</code> a new numbered version of the bot is created. This is the same as calling the <code>CreateBotVersion</code> operation. If you don't specify <code>createVersion</code>, the default is <code>false</code>.</p>"""
    tags: NotRequired["capo_lex_model_building_service.types.tag_list.TagList"]
    """<p>A list of tags to add to the bot. You can only add tags when you create a bot, you can't use the <code>PutBot</code> operation to update the tags on a bot. To update tags, use the <code>TagResource</code> operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutBotRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "intents" in value:
        import capo_lex_model_building_service.types.intent_list

        out["intents"] = (
            capo_lex_model_building_service.types.intent_list.serialize_json(
                value["intents"]
            )
        )
    if "enable_model_improvements" in value:
        out["enableModelImprovements"] = value["enable_model_improvements"]
    if "nlu_intent_confidence_threshold" in value:
        out["nluIntentConfidenceThreshold"] = (
            "NaN"
            if value["nlu_intent_confidence_threshold"]
            != value["nlu_intent_confidence_threshold"]
            else "Infinity"
            if value["nlu_intent_confidence_threshold"] == float("inf")
            else "-Infinity"
            if value["nlu_intent_confidence_threshold"] == float("-inf")
            else value["nlu_intent_confidence_threshold"]
        )
    if "clarification_prompt" in value:
        import capo_lex_model_building_service.types.prompt

        out["clarificationPrompt"] = (
            capo_lex_model_building_service.types.prompt.serialize_json(
                value["clarification_prompt"]
            )
        )
    if "abort_statement" in value:
        import capo_lex_model_building_service.types.statement

        out["abortStatement"] = (
            capo_lex_model_building_service.types.statement.serialize_json(
                value["abort_statement"]
            )
        )
    if "idle_session_ttl_in_seconds" in value:
        out["idleSessionTTLInSeconds"] = value["idle_session_ttl_in_seconds"]
    if "voice_id" in value:
        out["voiceId"] = value["voice_id"]
    if "checksum" in value:
        out["checksum"] = value["checksum"]
    if "process_behavior" in value:
        import capo_lex_model_building_service.types.process_behavior

        out["processBehavior"] = (
            capo_lex_model_building_service.types.process_behavior.serialize_json(
                value["process_behavior"]
            )
        )
    import capo_lex_model_building_service.types.locale

    out["locale"] = capo_lex_model_building_service.types.locale.serialize_json(
        value["locale"]
    )
    out["childDirected"] = value["child_directed"]
    if "detect_sentiment" in value:
        out["detectSentiment"] = value["detect_sentiment"]
    if "create_version" in value:
        out["createVersion"] = value["create_version"]
    if "tags" in value:
        import capo_lex_model_building_service.types.tag_list

        out["tags"] = capo_lex_model_building_service.types.tag_list.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> PutBotRequest:
    out: PutBotRequest = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("intents") is not None:
        import capo_lex_model_building_service.types.intent_list

        out["intents"] = (
            capo_lex_model_building_service.types.intent_list.deserialize_json(
                data["intents"]
            )
        )
    if data.get("enableModelImprovements") is not None:
        out["enable_model_improvements"] = data["enableModelImprovements"]
    if data.get("nluIntentConfidenceThreshold") is not None:
        out["nlu_intent_confidence_threshold"] = float(
            data["nluIntentConfidenceThreshold"]
        )
    if data.get("clarificationPrompt") is not None:
        import capo_lex_model_building_service.types.prompt

        out["clarification_prompt"] = (
            capo_lex_model_building_service.types.prompt.deserialize_json(
                data["clarificationPrompt"]
            )
        )
    if data.get("abortStatement") is not None:
        import capo_lex_model_building_service.types.statement

        out["abort_statement"] = (
            capo_lex_model_building_service.types.statement.deserialize_json(
                data["abortStatement"]
            )
        )
    if data.get("idleSessionTTLInSeconds") is not None:
        out["idle_session_ttl_in_seconds"] = data["idleSessionTTLInSeconds"]
    if data.get("voiceId") is not None:
        out["voice_id"] = data["voiceId"]
    if data.get("checksum") is not None:
        out["checksum"] = data["checksum"]
    if data.get("processBehavior") is not None:
        import capo_lex_model_building_service.types.process_behavior

        out["process_behavior"] = (
            capo_lex_model_building_service.types.process_behavior.deserialize_json(
                data["processBehavior"]
            )
        )
    if data.get("locale") is not None:
        import capo_lex_model_building_service.types.locale

        out["locale"] = capo_lex_model_building_service.types.locale.deserialize_json(
            data["locale"]
        )
    else:
        raise DeserializationError("PutBotRequest.locale required")
    if data.get("childDirected") is not None:
        out["child_directed"] = data["childDirected"]
    else:
        raise DeserializationError("PutBotRequest.child_directed required")
    if data.get("detectSentiment") is not None:
        out["detect_sentiment"] = data["detectSentiment"]
    if data.get("createVersion") is not None:
        out["create_version"] = data["createVersion"]
    if data.get("tags") is not None:
        import capo_lex_model_building_service.types.tag_list

        out["tags"] = capo_lex_model_building_service.types.tag_list.deserialize_json(
            data["tags"]
        )
    return out
