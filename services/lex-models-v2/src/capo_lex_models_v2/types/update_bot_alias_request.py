"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UpdateBotAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_alias_id
    import capo_lex_models_v2.types.bot_alias_locale_settings_map
    import capo_lex_models_v2.types.bot_version
    import capo_lex_models_v2.types.conversation_log_settings
    import capo_lex_models_v2.types.description
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.name
    import capo_lex_models_v2.types.sentiment_analysis_settings


class UpdateBotAliasRequest(TypedDict, closed=True):
    bot_alias_id: "capo_lex_models_v2.types.bot_alias_id.BotAliasId"
    """<p>The unique identifier of the bot alias.</p>"""
    bot_alias_name: "capo_lex_models_v2.types.name.Name"
    """<p>The new name to assign to the bot alias.</p>"""
    description: NotRequired["capo_lex_models_v2.types.description.Description"]
    """<p>The new description to assign to the bot alias.</p>"""
    bot_version: NotRequired["capo_lex_models_v2.types.bot_version.BotVersion"]
    """<p>The new bot version to assign to the bot alias.</p>"""
    bot_alias_locale_settings: NotRequired[
        "capo_lex_models_v2.types.bot_alias_locale_settings_map.BotAliasLocaleSettingsMap"
    ]
    """<p>The new Lambda functions to use in each locale for the bot alias.</p>"""
    conversation_log_settings: NotRequired[
        "capo_lex_models_v2.types.conversation_log_settings.ConversationLogSettings"
    ]
    """<p>The new settings for storing conversation logs in Amazon CloudWatch Logs and Amazon S3 buckets.</p>"""
    sentiment_analysis_settings: NotRequired[
        "capo_lex_models_v2.types.sentiment_analysis_settings.SentimentAnalysisSettings"
    ]
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The identifier of the bot with the updated alias.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBotAliasRequest) -> dict:
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
    return out


def deserialize_json(data: dict) -> UpdateBotAliasRequest:
    out: UpdateBotAliasRequest = {}  # type: ignore[typeddict-item]
    if data.get("botAliasName") is not None:
        out["bot_alias_name"] = data["botAliasName"]
    else:
        out["bot_alias_name"] = ""
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
    return out
