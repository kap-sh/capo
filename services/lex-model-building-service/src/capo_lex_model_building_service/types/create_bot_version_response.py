"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#CreateBotVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.boolean
    import capo_lex_model_building_service.types.bot_name
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


class CreateBotVersionResponse(TypedDict, closed=True):
    name: NotRequired["capo_lex_model_building_service.types.bot_name.BotName"]
    """<p>The name of the bot.</p>"""
    description: NotRequired[
        "capo_lex_model_building_service.types.description.Description"
    ]
    """<p>A description of the bot.</p>"""
    intents: NotRequired["capo_lex_model_building_service.types.intent_list.IntentList"]
    """<p>An array of <code>Intent</code> objects. For more information, see <a>PutBot</a>.</p>"""
    clarification_prompt: NotRequired[
        "capo_lex_model_building_service.types.prompt.Prompt"
    ]
    """<p>The message that Amazon Lex uses when it doesn't understand the user's request. For more information, see <a>PutBot</a>. </p>"""
    abort_statement: NotRequired[
        "capo_lex_model_building_service.types.statement.Statement"
    ]
    """<p>The message that Amazon Lex uses to cancel a conversation. For more information, see <a>PutBot</a>.</p>"""
    status: NotRequired["capo_lex_model_building_service.types.status.Status"]
    """<p> When you send a request to create or update a bot, Amazon Lex sets the <code>status</code> response element to <code>BUILDING</code>. After Amazon Lex builds the bot, it sets <code>status</code> to <code>READY</code>. If Amazon Lex can't build the bot, it sets <code>status</code> to <code>FAILED</code>. Amazon Lex returns the reason for the failure in the <code>failureReason</code> response element. </p>"""
    failure_reason: NotRequired["capo_lex_model_building_service.types.string.String"]
    """<p>If <code>status</code> is <code>FAILED</code>, Amazon Lex provides the reason that it failed to build the bot.</p>"""
    last_updated_date: NotRequired[
        "capo_lex_model_building_service.types.timestamp.Timestamp"
    ]
    """<p>The date when the <code>$LATEST</code> version of this bot was updated. </p>"""
    created_date: NotRequired[
        "capo_lex_model_building_service.types.timestamp.Timestamp"
    ]
    """<p>The date when the bot version was created.</p>"""
    idle_session_ttl_in_seconds: NotRequired[
        "capo_lex_model_building_service.types.session_ttl.SessionTTL"
    ]
    """<p>The maximum time in seconds that Amazon Lex retains the data gathered in a conversation. For more information, see <a>PutBot</a>.</p>"""
    voice_id: NotRequired["capo_lex_model_building_service.types.string.String"]
    """<p>The Amazon Polly voice ID that Amazon Lex uses for voice interactions with the user.</p>"""
    checksum: NotRequired["capo_lex_model_building_service.types.string.String"]
    """<p>Checksum identifying the version of the bot that was created.</p>"""
    version: NotRequired["capo_lex_model_building_service.types.version.Version"]
    """<p>The version of the bot. </p>"""
    locale: NotRequired["capo_lex_model_building_service.types.locale.Locale"]
    """<p> Specifies the target locale for the bot. </p>"""
    child_directed: NotRequired["capo_lex_model_building_service.types.boolean.Boolean"]
    """<p>For each Amazon Lex bot created with the Amazon Lex Model Building Service, you must specify whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to the Children's Online Privacy Protection Act (COPPA) by specifying <code>true</code> or <code>false</code> in the <code>childDirected</code> field. By specifying <code>true</code> in the <code>childDirected</code> field, you confirm that your use of Amazon Lex <b>is</b> related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. By specifying <code>false</code> in the <code>childDirected</code> field, you confirm that your use of Amazon Lex <b>is not</b> related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. You may not specify a default value for the <code>childDirected</code> field that does not accurately reflect whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA.</p> <p>If your use of Amazon Lex relates to a website, program, or other application that is directed in whole or in part, to children under age 13, you must obtain any required verifiable parental consent under COPPA. For information regarding the use of Amazon Lex in connection with websites, programs, or other applications that are directed or targeted, in whole or in part, to children under age 13, see the <a href="https://aws.amazon.com/lex/faqs#data-security">Amazon Lex FAQ.</a> </p>"""
    enable_model_improvements: NotRequired[
        "capo_lex_model_building_service.types.boolean.Boolean"
    ]
    """<p>Indicates whether the bot uses accuracy improvements. <code>true</code> indicates that the bot is using the improvements, otherwise, <code>false</code>.</p>"""
    detect_sentiment: NotRequired[
        "capo_lex_model_building_service.types.boolean.Boolean"
    ]
    """<p>Indicates whether utterances entered by the user should be sent to Amazon Comprehend for sentiment analysis.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBotVersionResponse) -> dict:
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
    if "enable_model_improvements" in value:
        out["enableModelImprovements"] = value["enable_model_improvements"]
    if "detect_sentiment" in value:
        out["detectSentiment"] = value["detect_sentiment"]
    return out


def deserialize_json(data: dict) -> CreateBotVersionResponse:
    out: CreateBotVersionResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("enableModelImprovements") is not None:
        out["enable_model_improvements"] = data["enableModelImprovements"]
    if data.get("detectSentiment") is not None:
        out["detect_sentiment"] = data["detectSentiment"]
    return out
