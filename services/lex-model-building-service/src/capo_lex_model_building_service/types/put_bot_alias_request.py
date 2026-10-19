"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#PutBotAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.alias_name
    import capo_lex_model_building_service.types.bot_name
    import capo_lex_model_building_service.types.conversation_logs_request
    import capo_lex_model_building_service.types.description
    import capo_lex_model_building_service.types.string
    import capo_lex_model_building_service.types.tag_list
    import capo_lex_model_building_service.types.version


class PutBotAliasRequest(TypedDict, closed=True):
    name: "capo_lex_model_building_service.types.alias_name.AliasName"
    """<p>The name of the alias. The name is <i>not</i> case sensitive.</p>"""
    description: NotRequired[
        "capo_lex_model_building_service.types.description.Description"
    ]
    """<p>A description of the alias.</p>"""
    bot_version: "capo_lex_model_building_service.types.version.Version"
    """<p>The version of the bot.</p>"""
    bot_name: "capo_lex_model_building_service.types.bot_name.BotName"
    """<p>The name of the bot.</p>"""
    checksum: NotRequired["capo_lex_model_building_service.types.string.String"]
    """<p>Identifies a specific revision of the <code>$LATEST</code> version.</p> <p>When you create a new bot alias, leave the <code>checksum</code> field blank. If you specify a checksum you get a <code>BadRequestException</code> exception.</p> <p>When you want to update a bot alias, set the <code>checksum</code> field to the checksum of the most recent revision of the <code>$LATEST</code> version. If you don't specify the <code> checksum</code> field, or if the checksum does not match the <code>$LATEST</code> version, you get a <code>PreconditionFailedException</code> exception.</p>"""
    conversation_logs: NotRequired[
        "capo_lex_model_building_service.types.conversation_logs_request.ConversationLogsRequest"
    ]
    """<p>Settings for conversation logs for the alias.</p>"""
    tags: NotRequired["capo_lex_model_building_service.types.tag_list.TagList"]
    """<p>A list of tags to add to the bot alias. You can only add tags when you create an alias, you can't use the <code>PutBotAlias</code> operation to update the tags on a bot alias. To update tags, use the <code>TagResource</code> operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutBotAliasRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    out["botVersion"] = value["bot_version"]
    if "checksum" in value:
        out["checksum"] = value["checksum"]
    if "conversation_logs" in value:
        import capo_lex_model_building_service.types.conversation_logs_request

        out["conversationLogs"] = (
            capo_lex_model_building_service.types.conversation_logs_request.serialize_json(
                value["conversation_logs"]
            )
        )
    if "tags" in value:
        import capo_lex_model_building_service.types.tag_list

        out["tags"] = capo_lex_model_building_service.types.tag_list.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> PutBotAliasRequest:
    out: PutBotAliasRequest = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("botVersion") is not None:
        out["bot_version"] = data["botVersion"]
    else:
        out["bot_version"] = ""
    if data.get("checksum") is not None:
        out["checksum"] = data["checksum"]
    if data.get("conversationLogs") is not None:
        import capo_lex_model_building_service.types.conversation_logs_request

        out["conversation_logs"] = (
            capo_lex_model_building_service.types.conversation_logs_request.deserialize_json(
                data["conversationLogs"]
            )
        )
    if data.get("tags") is not None:
        import capo_lex_model_building_service.types.tag_list

        out["tags"] = capo_lex_model_building_service.types.tag_list.deserialize_json(
            data["tags"]
        )
    return out
