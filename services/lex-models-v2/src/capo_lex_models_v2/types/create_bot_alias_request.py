"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CreateBotAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_alias_locale_settings_map
    import capo_lex_models_v2.types.conversation_log_settings
    import capo_lex_models_v2.types.description
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.name
    import capo_lex_models_v2.types.numerical_bot_version
    import capo_lex_models_v2.types.sentiment_analysis_settings
    import capo_lex_models_v2.types.tag_map


class CreateBotAliasRequest(TypedDict, closed=True):
    bot_alias_name: "capo_lex_models_v2.types.name.Name"
    """<p>The alias to create. The name must be unique for the bot.</p>"""
    description: NotRequired["capo_lex_models_v2.types.description.Description"]
    """<p>A description of the alias. Use this description to help identify the alias.</p>"""
    bot_version: NotRequired[
        "capo_lex_models_v2.types.numerical_bot_version.NumericalBotVersion"
    ]
    """<p>The version of the bot that this alias points to. You can use the <a href="https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateBotAlias.html">UpdateBotAlias</a> operation to change the bot version associated with the alias.</p>"""
    bot_alias_locale_settings: NotRequired[
        "capo_lex_models_v2.types.bot_alias_locale_settings_map.BotAliasLocaleSettingsMap"
    ]
    """<p>Maps configuration information to a specific locale. You can use this parameter to specify a specific Lambda function to run different functions in different locales.</p>"""
    conversation_log_settings: NotRequired[
        "capo_lex_models_v2.types.conversation_log_settings.ConversationLogSettings"
    ]
    """<p>Specifies whether Amazon Lex logs text and audio for a conversation with the bot. When you enable conversation logs, text logs store text input, transcripts of audio input, and associated metadata in Amazon CloudWatch Logs. Audio logs store audio input in Amazon S3.</p>"""
    sentiment_analysis_settings: NotRequired[
        "capo_lex_models_v2.types.sentiment_analysis_settings.SentimentAnalysisSettings"
    ]
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the bot that the alias applies to.</p>"""
    tags: NotRequired["capo_lex_models_v2.types.tag_map.TagMap"]
    """<p>A list of tags to add to the bot alias. You can only add tags when you create an alias, you can't use the <code>UpdateBotAlias</code> operation to update the tags on a bot alias. To update tags, use the <code>TagResource</code> operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBotAliasRequest) -> dict:
    out: dict = {}
    out["botAliasName"] = value["bot_alias_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "bot_alias_locale_settings" in value:
        import capo_lex_models_v2.types.bot_alias_locale_settings_map

        out["botAliasLocaleSettings"] = (
            capo_lex_models_v2.types.bot_alias_locale_settings_map.serialize_json(
                value["bot_alias_locale_settings"]
            )
        )
    if "conversation_log_settings" in value:
        import capo_lex_models_v2.types.conversation_log_settings

        out["conversationLogSettings"] = (
            capo_lex_models_v2.types.conversation_log_settings.serialize_json(
                value["conversation_log_settings"]
            )
        )
    if "sentiment_analysis_settings" in value:
        import capo_lex_models_v2.types.sentiment_analysis_settings

        out["sentimentAnalysisSettings"] = (
            capo_lex_models_v2.types.sentiment_analysis_settings.serialize_json(
                value["sentiment_analysis_settings"]
            )
        )
    if "tags" in value:
        import capo_lex_models_v2.types.tag_map

        out["tags"] = capo_lex_models_v2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateBotAliasRequest:
    out: CreateBotAliasRequest = {}  # type: ignore[typeddict-item]
    if data.get("botAliasName") is not None:
        out["bot_alias_name"] = data["botAliasName"]
    else:
        raise DeserializationError("CreateBotAliasRequest.bot_alias_name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("botVersion") is not None:
        out["bot_version"] = data["botVersion"]
    if data.get("botAliasLocaleSettings") is not None:
        import capo_lex_models_v2.types.bot_alias_locale_settings_map

        out["bot_alias_locale_settings"] = (
            capo_lex_models_v2.types.bot_alias_locale_settings_map.deserialize_json(
                data["botAliasLocaleSettings"]
            )
        )
    if data.get("conversationLogSettings") is not None:
        import capo_lex_models_v2.types.conversation_log_settings

        out["conversation_log_settings"] = (
            capo_lex_models_v2.types.conversation_log_settings.deserialize_json(
                data["conversationLogSettings"]
            )
        )
    if data.get("sentimentAnalysisSettings") is not None:
        import capo_lex_models_v2.types.sentiment_analysis_settings

        out["sentiment_analysis_settings"] = (
            capo_lex_models_v2.types.sentiment_analysis_settings.deserialize_json(
                data["sentimentAnalysisSettings"]
            )
        )
    if data.get("tags") is not None:
        import capo_lex_models_v2.types.tag_map

        out["tags"] = capo_lex_models_v2.types.tag_map.deserialize_json(data["tags"])
    return out
