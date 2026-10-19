"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CreateBotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_members
    import capo_lex_models_v2.types.bot_type
    import capo_lex_models_v2.types.data_privacy
    import capo_lex_models_v2.types.description
    import capo_lex_models_v2.types.error_log_settings
    import capo_lex_models_v2.types.name
    import capo_lex_models_v2.types.role_arn
    import capo_lex_models_v2.types.session_ttl
    import capo_lex_models_v2.types.tag_map


class CreateBotRequest(TypedDict, closed=True):
    bot_name: "capo_lex_models_v2.types.name.Name"
    """<p>The name of the bot. The bot name must be unique in the account that creates the bot.</p>"""
    description: NotRequired["capo_lex_models_v2.types.description.Description"]
    """<p>A description of the bot. It appears in lists to help you identify a particular bot.</p>"""
    role_arn: "capo_lex_models_v2.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of an IAM role that has permission to access the bot.</p>"""
    data_privacy: "capo_lex_models_v2.types.data_privacy.DataPrivacy"
    """<p>Provides information on additional privacy protections Amazon Lex should use with the bot's data.</p>"""
    idle_session_ttl_in_seconds: "capo_lex_models_v2.types.session_ttl.SessionTTL"
    """<p>The time, in seconds, that Amazon Lex should keep information about a user's conversation with the bot. </p> <p>A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Lex deletes any data provided before the timeout.</p> <p>You can specify between 60 (1 minute) and 86,400 (24 hours) seconds.</p>"""
    bot_tags: NotRequired["capo_lex_models_v2.types.tag_map.TagMap"]
    """<p>A list of tags to add to the bot. You can only add tags when you create a bot. You can't use the <code>UpdateBot</code> operation to update tags. To update tags, use the <code>TagResource</code> operation.</p>"""
    test_bot_alias_tags: NotRequired["capo_lex_models_v2.types.tag_map.TagMap"]
    """<p>A list of tags to add to the test alias for a bot. You can only add tags when you create a bot. You can't use the <code>UpdateAlias</code> operation to update tags. To update tags on the test alias, use the <code>TagResource</code> operation.</p>"""
    bot_type: NotRequired["capo_lex_models_v2.types.bot_type.BotType"]
    """<p>The type of a bot to create.</p>"""
    bot_members: NotRequired["capo_lex_models_v2.types.bot_members.BotMembers"]
    """<p>The list of bot members in a network to be created.</p>"""
    error_log_settings: NotRequired[
        "capo_lex_models_v2.types.error_log_settings.ErrorLogSettings"
    ]
    """<p>Specifies the configuration for error logging during bot creation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBotRequest) -> dict:
    out: dict = {}
    out["botName"] = value["bot_name"]
    if "description" in value:
        out["description"] = value["description"]
    out["roleArn"] = value["role_arn"]
    import capo_lex_models_v2.types.data_privacy

    out["dataPrivacy"] = capo_lex_models_v2.types.data_privacy.serialize_json(
        value["data_privacy"]
    )
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
    if "bot_type" in value:
        import capo_lex_models_v2.types.bot_type

        out["botType"] = capo_lex_models_v2.types.bot_type.serialize_json(
            value["bot_type"]
        )
    if "bot_members" in value:
        import capo_lex_models_v2.types.bot_members

        out["botMembers"] = capo_lex_models_v2.types.bot_members.serialize_json(
            value["bot_members"]
        )
    if "error_log_settings" in value:
        import capo_lex_models_v2.types.error_log_settings

        out["errorLogSettings"] = (
            capo_lex_models_v2.types.error_log_settings.serialize_json(
                value["error_log_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateBotRequest:
    out: CreateBotRequest = {}  # type: ignore[typeddict-item]
    if data.get("botName") is not None:
        out["bot_name"] = data["botName"]
    else:
        out["bot_name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
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
        raise DeserializationError("CreateBotRequest.data_privacy required")
    if data.get("idleSessionTTLInSeconds") is not None:
        out["idle_session_ttl_in_seconds"] = data["idleSessionTTLInSeconds"]
    else:
        out["idle_session_ttl_in_seconds"] = 0
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
    if data.get("botType") is not None:
        import capo_lex_models_v2.types.bot_type

        out["bot_type"] = capo_lex_models_v2.types.bot_type.deserialize_json(
            data["botType"]
        )
    if data.get("botMembers") is not None:
        import capo_lex_models_v2.types.bot_members

        out["bot_members"] = capo_lex_models_v2.types.bot_members.deserialize_json(
            data["botMembers"]
        )
    if data.get("errorLogSettings") is not None:
        import capo_lex_models_v2.types.error_log_settings

        out["error_log_settings"] = (
            capo_lex_models_v2.types.error_log_settings.deserialize_json(
                data["errorLogSettings"]
            )
        )
    return out
