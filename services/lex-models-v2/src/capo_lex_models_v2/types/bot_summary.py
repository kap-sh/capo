"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_status
    import capo_lex_models_v2.types.bot_type
    import capo_lex_models_v2.types.description
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.name
    import capo_lex_models_v2.types.numerical_bot_version
    import capo_lex_models_v2.types.timestamp


class BotSummary(TypedDict, closed=True):
    bot_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The unique identifier assigned to the bot. Use this ID to get detailed information about the bot with the <a href="https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeBot.html">DescribeBot</a> operation.</p>"""
    bot_name: NotRequired["capo_lex_models_v2.types.name.Name"]
    """<p>The name of the bot.</p>"""
    description: NotRequired["capo_lex_models_v2.types.description.Description"]
    """<p>The description of the bot.</p>"""
    bot_status: NotRequired["capo_lex_models_v2.types.bot_status.BotStatus"]
    """<p>The current status of the bot. When the status is <code>Available</code> the bot is ready for use.</p>"""
    latest_bot_version: NotRequired[
        "capo_lex_models_v2.types.numerical_bot_version.NumericalBotVersion"
    ]
    """<p>The latest numerical version in use for the bot.</p>"""
    last_updated_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The date and time that the bot was last updated.</p>"""
    bot_type: NotRequired["capo_lex_models_v2.types.bot_type.BotType"]
    """<p>The type of the bot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BotSummary) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_name" in value:
        out["botName"] = value["bot_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "bot_status" in value:
        import capo_lex_models_v2.types.bot_status

        out["botStatus"] = capo_lex_models_v2.types.bot_status.serialize_json(
            value["bot_status"]
        )
    if "latest_bot_version" in value:
        out["latestBotVersion"] = value["latest_bot_version"]
    if "last_updated_date_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["lastUpdatedDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
            value["last_updated_date_time"]
        )
    if "bot_type" in value:
        import capo_lex_models_v2.types.bot_type

        out["botType"] = capo_lex_models_v2.types.bot_type.serialize_json(
            value["bot_type"]
        )
    return out


def deserialize_json(data: dict) -> BotSummary:
    out: BotSummary = {}  # type: ignore[typeddict-item]
    if data.get("botId") is not None:
        out["bot_id"] = data["botId"]
    if data.get("botName") is not None:
        out["bot_name"] = data["botName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("botStatus") is not None:
        import capo_lex_models_v2.types.bot_status

        out["bot_status"] = capo_lex_models_v2.types.bot_status.deserialize_json(
            data["botStatus"]
        )
    if data.get("latestBotVersion") is not None:
        out["latest_bot_version"] = data["latestBotVersion"]
    if data.get("lastUpdatedDateTime") is not None:
        import capo_lex_models_v2.types.timestamp

        out["last_updated_date_time"] = (
            capo_lex_models_v2.types.timestamp.deserialize_json(
                data["lastUpdatedDateTime"]
            )
        )
    if data.get("botType") is not None:
        import capo_lex_models_v2.types.bot_type

        out["bot_type"] = capo_lex_models_v2.types.bot_type.deserialize_json(
            data["botType"]
        )
    return out
