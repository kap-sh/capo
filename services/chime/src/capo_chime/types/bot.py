"""Generated from Smithy shape ``com.amazonaws.chime#Bot``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.bot_type
    import capo_chime.types.iso8601_timestamp
    import capo_chime.types.nullable_boolean
    import capo_chime.types.sensitive_string
    import capo_chime.types.string


class Bot(TypedDict, closed=True):
    bot_id: NotRequired["capo_chime.types.string.String"]
    """<p>The bot ID.</p>"""
    user_id: NotRequired["capo_chime.types.string.String"]
    """<p>The unique ID for the bot user.</p>"""
    display_name: NotRequired["capo_chime.types.sensitive_string.SensitiveString"]
    """<p>The bot display name.</p>"""
    bot_type: NotRequired["capo_chime.types.bot_type.BotType"]
    """<p>The bot type.</p>"""
    disabled: NotRequired["capo_chime.types.nullable_boolean.NullableBoolean"]
    """<p>When true, the bot is stopped from running in your account.</p>"""
    created_timestamp: NotRequired[
        "capo_chime.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The bot creation timestamp, in ISO 8601 format.</p>"""
    updated_timestamp: NotRequired[
        "capo_chime.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The updated bot timestamp, in ISO 8601 format.</p>"""
    bot_email: NotRequired["capo_chime.types.sensitive_string.SensitiveString"]
    """<p>The bot email address.</p>"""
    security_token: NotRequired["capo_chime.types.sensitive_string.SensitiveString"]
    """<p>The security token used to authenticate Amazon Chime with the outgoing event endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Bot) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["BotId"] = value["bot_id"]
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "bot_type" in value:
        import capo_chime.types.bot_type

        out["BotType"] = capo_chime.types.bot_type.serialize_json(value["bot_type"])
    if "disabled" in value:
        out["Disabled"] = value["disabled"]
    if "created_timestamp" in value:
        import capo_chime.types.iso8601_timestamp

        out["CreatedTimestamp"] = capo_chime.types.iso8601_timestamp.serialize_json(
            value["created_timestamp"]
        )
    if "updated_timestamp" in value:
        import capo_chime.types.iso8601_timestamp

        out["UpdatedTimestamp"] = capo_chime.types.iso8601_timestamp.serialize_json(
            value["updated_timestamp"]
        )
    if "bot_email" in value:
        out["BotEmail"] = value["bot_email"]
    if "security_token" in value:
        out["SecurityToken"] = value["security_token"]
    return out


def deserialize_json(data: dict) -> Bot:
    out: Bot = {}  # type: ignore[typeddict-item]
    if data.get("BotId") is not None:
        out["bot_id"] = data["BotId"]
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("BotType") is not None:
        import capo_chime.types.bot_type

        out["bot_type"] = capo_chime.types.bot_type.deserialize_json(data["BotType"])
    if data.get("Disabled") is not None:
        out["disabled"] = data["Disabled"]
    if data.get("CreatedTimestamp") is not None:
        import capo_chime.types.iso8601_timestamp

        out["created_timestamp"] = capo_chime.types.iso8601_timestamp.deserialize_json(
            data["CreatedTimestamp"]
        )
    if data.get("UpdatedTimestamp") is not None:
        import capo_chime.types.iso8601_timestamp

        out["updated_timestamp"] = capo_chime.types.iso8601_timestamp.deserialize_json(
            data["UpdatedTimestamp"]
        )
    if data.get("BotEmail") is not None:
        out["bot_email"] = data["BotEmail"]
    if data.get("SecurityToken") is not None:
        out["security_token"] = data["SecurityToken"]
    return out


def redact_sensitive(value: Bot) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "display_name" in value:
        out["display_name"] = "*** Sensitive Data Redacted ***"
    if "bot_email" in value:
        out["bot_email"] = "*** Sensitive Data Redacted ***"
    if "security_token" in value:
        out["security_token"] = "*** Sensitive Data Redacted ***"
    return out
