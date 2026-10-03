"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotAliasSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_alias_id
    import capo_lex_models_v2.types.bot_alias_status
    import capo_lex_models_v2.types.bot_version
    import capo_lex_models_v2.types.description
    import capo_lex_models_v2.types.name
    import capo_lex_models_v2.types.timestamp


class BotAliasSummary(TypedDict, closed=True):
    bot_alias_id: NotRequired["capo_lex_models_v2.types.bot_alias_id.BotAliasId"]
    """<p>The unique identifier assigned to the bot alias. You can use this ID to get detailed information about the alias using the <a href="https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeBotAlias.html">DescribeBotAlias</a> operation.</p>"""
    bot_alias_name: NotRequired["capo_lex_models_v2.types.name.Name"]
    """<p>The name of the bot alias.</p>"""
    description: NotRequired["capo_lex_models_v2.types.description.Description"]
    """<p>The description of the bot alias.</p>"""
    bot_version: NotRequired["capo_lex_models_v2.types.bot_version.BotVersion"]
    """<p>The version of the bot that the bot alias references.</p>"""
    bot_alias_status: NotRequired[
        "capo_lex_models_v2.types.bot_alias_status.BotAliasStatus"
    ]
    """<p>The current state of the bot alias. If the status is <code>Available</code>, the alias is ready for use.</p>"""
    creation_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>A timestamp of the date and time that the bot alias was created.</p>"""
    last_updated_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>A timestamp of the date and time that the bot alias was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BotAliasSummary) -> dict:
    out: dict = {}
    if "bot_alias_id" in value:
        out["botAliasId"] = value["bot_alias_id"]
    if "bot_alias_name" in value:
        out["botAliasName"] = value["bot_alias_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "bot_alias_status" in value:
        import capo_lex_models_v2.types.bot_alias_status

        out["botAliasStatus"] = (
            capo_lex_models_v2.types.bot_alias_status.serialize_json(
                value["bot_alias_status"]
            )
        )
    if "creation_date_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["creationDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    if "last_updated_date_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["lastUpdatedDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
            value["last_updated_date_time"]
        )
    return out


def deserialize_json(data: dict) -> BotAliasSummary:
    out: BotAliasSummary = {}  # type: ignore[typeddict-item]
    if data.get("botAliasId") is not None:
        out["bot_alias_id"] = data["botAliasId"]
    if data.get("botAliasName") is not None:
        out["bot_alias_name"] = data["botAliasName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("botVersion") is not None:
        out["bot_version"] = data["botVersion"]
    if data.get("botAliasStatus") is not None:
        import capo_lex_models_v2.types.bot_alias_status

        out["bot_alias_status"] = (
            capo_lex_models_v2.types.bot_alias_status.deserialize_json(
                data["botAliasStatus"]
            )
        )
    if data.get("creationDateTime") is not None:
        import capo_lex_models_v2.types.timestamp

        out["creation_date_time"] = capo_lex_models_v2.types.timestamp.deserialize_json(
            data["creationDateTime"]
        )
    if data.get("lastUpdatedDateTime") is not None:
        import capo_lex_models_v2.types.timestamp

        out["last_updated_date_time"] = (
            capo_lex_models_v2.types.timestamp.deserialize_json(
                data["lastUpdatedDateTime"]
            )
        )
    return out
