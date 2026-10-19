"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotImportSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.data_privacy
    import capo_lex_models_v2.types.error_log_settings
    import capo_lex_models_v2.types.name
    import capo_lex_models_v2.types.role_arn
    import capo_lex_models_v2.types.session_ttl
    import capo_lex_models_v2.types.tag_map


class BotImportSpecification(TypedDict, closed=True):
    bot_name: "capo_lex_models_v2.types.name.Name"
    """<p>The name that Amazon Lex should use for the bot.</p>"""
    role_arn: "capo_lex_models_v2.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role used to build and run the bot.</p>"""
    data_privacy: "capo_lex_models_v2.types.data_privacy.DataPrivacy"
    error_log_settings: NotRequired[
        "capo_lex_models_v2.types.error_log_settings.ErrorLogSettings"
    ]
    """<p>Allows you to configure destinations where error logs will be published during the bot import process.</p>"""
    idle_session_ttl_in_seconds: NotRequired[
        "capo_lex_models_v2.types.session_ttl.SessionTTL"
    ]
    """<p>The time, in seconds, that Amazon Lex should keep information about a user's conversation with the bot. </p> <p>A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Lex deletes any data provided before the timeout.</p> <p>You can specify between 60 (1 minute) and 86,400 (24 hours) seconds.</p>"""
    bot_tags: NotRequired["capo_lex_models_v2.types.tag_map.TagMap"]
    """<p>A list of tags to add to the bot. You can only add tags when you import a bot. You can't use the <code>UpdateBot</code> operation to update tags. To update tags, use the <code>TagResource</code> operation.</p>"""
    test_bot_alias_tags: NotRequired["capo_lex_models_v2.types.tag_map.TagMap"]
    """<p>A list of tags to add to the test alias for a bot. You can only add tags when you import a bot. You can't use the <code>UpdateAlias</code> operation to update tags. To update tags on the test alias, use the <code>TagResource</code> operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BotImportSpecification) -> dict:
    out: dict = {}
    out["botName"] = value["bot_name"]
    out["roleArn"] = value["role_arn"]
    import capo_lex_models_v2.types.data_privacy

    out["dataPrivacy"] = capo_lex_models_v2.types.data_privacy.serialize_json(
        value["data_privacy"]
    )
    if "error_log_settings" in value:
        import capo_lex_models_v2.types.error_log_settings

        out["errorLogSettings"] = (
            capo_lex_models_v2.types.error_log_settings.serialize_json(
                value["error_log_settings"]
            )
        )
    if "idle_session_ttl_in_seconds" in value:
        out["idleSessionTTLInSeconds"] = value["idle_session_ttl_in_seconds"]
    if "bot_tags" in value:
        import capo_lex_models_v2.types.tag_map

        out["botTags"] = capo_lex_models_v2.types.tag_map.serialize_json(
            value["bot_tags"]
        )
    if "test_bot_alias_tags" in value:
        import capo_lex_models_v2.types.tag_map

        out["testBotAliasTags"] = capo_lex_models_v2.types.tag_map.serialize_json(
            value["test_bot_alias_tags"]
        )
    return out


def deserialize_json(data: dict) -> BotImportSpecification:
    out: BotImportSpecification = {}  # type: ignore[typeddict-item]
    if data.get("botName") is not None:
        out["bot_name"] = data["botName"]
    else:
        out["bot_name"] = ""
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("dataPrivacy") is not None:
        import capo_lex_models_v2.types.data_privacy

        out["data_privacy"] = capo_lex_models_v2.types.data_privacy.deserialize_json(
            data["dataPrivacy"]
        )
    else:
        raise DeserializationError("BotImportSpecification.data_privacy required")
    if data.get("errorLogSettings") is not None:
        import capo_lex_models_v2.types.error_log_settings

        out["error_log_settings"] = (
            capo_lex_models_v2.types.error_log_settings.deserialize_json(
                data["errorLogSettings"]
            )
        )
    if data.get("idleSessionTTLInSeconds") is not None:
        out["idle_session_ttl_in_seconds"] = data["idleSessionTTLInSeconds"]
    if data.get("botTags") is not None:
        import capo_lex_models_v2.types.tag_map

        out["bot_tags"] = capo_lex_models_v2.types.tag_map.deserialize_json(
            data["botTags"]
        )
    if data.get("testBotAliasTags") is not None:
        import capo_lex_models_v2.types.tag_map

        out["test_bot_alias_tags"] = capo_lex_models_v2.types.tag_map.deserialize_json(
            data["testBotAliasTags"]
        )
    return out
