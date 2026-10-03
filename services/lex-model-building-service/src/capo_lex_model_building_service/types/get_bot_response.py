"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetBotResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.boolean
    import capo_lex_model_building_service.types.bot_name
    import capo_lex_model_building_service.types.confidence_threshold
    import capo_lex_model_building_service.types.description
    import capo_lex_model_building_service.types.intent_list
    import capo_lex_model_building_service.types.locale
    import capo_lex_model_building_service.types.prompt
    import capo_lex_model_building_service.types.session_ttl
    import capo_lex_model_building_service.types.statement
    import capo_lex_model_building_service.types.status
    import capo_lex_model_building_service.types.string
    import capo_lex_model_building_service.types.timestamp
    import capo_lex_model_building_service.types.version


class GetBotResponse(TypedDict, closed=True):
    name: NotRequired["capo_lex_model_building_service.types.bot_name.BotName"]
    """<p>The name of the bot.</p>"""
    description: NotRequired[
        "capo_lex_model_building_service.types.description.Description"
    ]
    """<p>A description of the bot.</p>"""
    intents: NotRequired["capo_lex_model_building_service.types.intent_list.IntentList"]
    """<p>An array of <code>intent</code> objects. For more information, see <a>PutBot</a>.</p>"""
    enable_model_improvements: NotRequired[
        "capo_lex_model_building_service.types.boolean.Boolean"
    ]
    """<p>Indicates whether the bot uses accuracy improvements. <code>true</code> indicates that the bot is using the improvements, otherwise, <code>false</code>.</p>"""
    nlu_intent_confidence_threshold: NotRequired[
        "capo_lex_model_building_service.types.confidence_threshold.ConfidenceThreshold"
    ]
    """<p>The score that determines where Amazon Lex inserts the <code>AMAZON.FallbackIntent</code>, <code>AMAZON.KendraSearchIntent</code>, or both when returning alternative intents in a <a href="https://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostContent.html">PostContent</a> or <a href="https://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html">PostText</a> response. <code>AMAZON.FallbackIntent</code> is inserted if the confidence score for all intents is below this value. <code>AMAZON.KendraSearchIntent</code> is only inserted if it is configured for the bot.</p>"""
    clarification_prompt: NotRequired[
        "capo_lex_model_building_service.types.prompt.Prompt"
    ]
    """<p>The message Amazon Lex uses when it doesn't understand the user's request. For more information, see <a>PutBot</a>. </p>"""
    abort_statement: NotRequired[
        "capo_lex_model_building_service.types.statement.Statement"
    ]
    """<p>The message that Amazon Lex returns when the user elects to end the conversation without completing it. For more information, see <a>PutBot</a>.</p>"""
    status: NotRequired["capo_lex_model_building_service.types.status.Status"]
    """<p>The status of the bot. </p> <p>When the status is <code>BUILDING</code> Amazon Lex is building the bot for testing and use.</p> <p>If the status of the bot is <code>READY_BASIC_TESTING</code>, you can test the bot using the exact utterances specified in the bot's intents. When the bot is ready for full testing or to run, the status is <code>READY</code>.</p> <p>If there was a problem with building the bot, the status is <code>FAILED</code> and the <code>failureReason</code> field explains why the bot did not build.</p> <p>If the bot was saved but not built, the status is <code>NOT_BUILT</code>.</p>"""
    failure_reason: NotRequired["capo_lex_model_building_service.types.string.String"]
    """<p>If <code>status</code> is <code>FAILED</code>, Amazon Lex explains why it failed to build the bot.</p>"""
    last_updated_date: NotRequired[
        "capo_lex_model_building_service.types.timestamp.Timestamp"
    ]
    """<p>The date that the bot was updated. When you create a resource, the creation date and last updated date are the same. </p>"""
    created_date: NotRequired[
        "capo_lex_model_building_service.types.timestamp.Timestamp"
    ]
    """<p>The date that the bot was created.</p>"""
    idle_session_ttl_in_seconds: NotRequired[
        "capo_lex_model_building_service.types.session_ttl.SessionTTL"
    ]
    """<p>The maximum time in seconds that Amazon Lex retains the data gathered in a conversation. For more information, see <a>PutBot</a>.</p>"""
    voice_id: NotRequired["capo_lex_model_building_service.types.string.String"]
    """<p>The Amazon Polly voice ID that Amazon Lex uses for voice interaction with the user. For more information, see <a>PutBot</a>.</p>"""
    checksum: NotRequired["capo_lex_model_building_service.types.string.String"]
    """<p>Checksum of the bot used to identify a specific revision of the bot's <code>$LATEST</code> version.</p>"""
    version: NotRequired["capo_lex_model_building_service.types.version.Version"]
    """<p>The version of the bot. For a new bot, the version is always <code>$LATEST</code>.</p>"""
    locale: NotRequired["capo_lex_model_building_service.types.locale.Locale"]
    """<p> The target locale for the bot. </p>"""
    child_directed: NotRequired["capo_lex_model_building_service.types.boolean.Boolean"]
    """<p>For each Amazon Lex bot created with the Amazon Lex Model Building Service, you must specify whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to the Children's Online Privacy Protection Act (COPPA) by specifying <code>true</code> or <code>false</code> in the <code>childDirected</code> field. By specifying <code>true</code> in the <code>childDirected</code> field, you confirm that your use of Amazon Lex <b>is</b> related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. By specifying <code>false</code> in the <code>childDirected</code> field, you confirm that your use of Amazon Lex <b>is not</b> related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. You may not specify a default value for the <code>childDirected</code> field that does not accurately reflect whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA.</p> <p>If your use of Amazon Lex relates to a website, program, or other application that is directed in whole or in part, to children under age 13, you must obtain any required verifiable parental consent under COPPA. For information regarding the use of Amazon Lex in connection with websites, programs, or other applications that are directed or targeted, in whole or in part, to children under age 13, see the <a href="https://aws.amazon.com/lex/faqs#data-security">Amazon Lex FAQ.</a> </p>"""
    detect_sentiment: NotRequired[
        "capo_lex_model_building_service.types.boolean.Boolean"
    ]
    """<p>Indicates whether user utterances should be sent to Amazon Comprehend for sentiment analysis.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBotResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
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
    if "status" in value:
        import capo_lex_model_building_service.types.status

        out["status"] = capo_lex_model_building_service.types.status.serialize_json(
            value["status"]
        )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    if "last_updated_date" in value:
        import capo_lex_model_building_service.types.timestamp

        out["lastUpdatedDate"] = (
            capo_lex_model_building_service.types.timestamp.serialize_json(
                value["last_updated_date"]
            )
        )
    if "created_date" in value:
        import capo_lex_model_building_service.types.timestamp

        out["createdDate"] = (
            capo_lex_model_building_service.types.timestamp.serialize_json(
                value["created_date"]
            )
        )
    if "idle_session_ttl_in_seconds" in value:
        out["idleSessionTTLInSeconds"] = value["idle_session_ttl_in_seconds"]
    if "voice_id" in value:
        out["voiceId"] = value["voice_id"]
    if "checksum" in value:
        out["checksum"] = value["checksum"]
    if "version" in value:
        out["version"] = value["version"]
    if "locale" in value:
        import capo_lex_model_building_service.types.locale

        out["locale"] = capo_lex_model_building_service.types.locale.serialize_json(
            value["locale"]
        )
    if "child_directed" in value:
        out["childDirected"] = value["child_directed"]
    if "detect_sentiment" in value:
        out["detectSentiment"] = value["detect_sentiment"]
    return out


def deserialize_json(data: dict) -> GetBotResponse:
    out: GetBotResponse = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
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
    if data.get("status") is not None:
        import capo_lex_model_building_service.types.status

        out["status"] = capo_lex_model_building_service.types.status.deserialize_json(
            data["status"]
        )
    if data.get("failureReason") is not None:
        out["failure_reason"] = data["failureReason"]
    if data.get("lastUpdatedDate") is not None:
        import capo_lex_model_building_service.types.timestamp

        out["last_updated_date"] = (
            capo_lex_model_building_service.types.timestamp.deserialize_json(
                data["lastUpdatedDate"]
            )
        )
    if data.get("createdDate") is not None:
        import capo_lex_model_building_service.types.timestamp

        out["created_date"] = (
            capo_lex_model_building_service.types.timestamp.deserialize_json(
                data["createdDate"]
            )
        )
    if data.get("idleSessionTTLInSeconds") is not None:
        out["idle_session_ttl_in_seconds"] = data["idleSessionTTLInSeconds"]
    if data.get("voiceId") is not None:
        out["voice_id"] = data["voiceId"]
    if data.get("checksum") is not None:
        out["checksum"] = data["checksum"]
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("locale") is not None:
        import capo_lex_model_building_service.types.locale

        out["locale"] = capo_lex_model_building_service.types.locale.deserialize_json(
            data["locale"]
        )
    if data.get("childDirected") is not None:
        out["child_directed"] = data["childDirected"]
    if data.get("detectSentiment") is not None:
        out["detect_sentiment"] = data["detectSentiment"]
    return out
