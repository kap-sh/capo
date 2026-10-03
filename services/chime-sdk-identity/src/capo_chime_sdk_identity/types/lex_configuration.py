"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#LexConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_identity.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.invoked_by
    import capo_chime_sdk_identity.types.lex_bot_alias_arn
    import capo_chime_sdk_identity.types.lex_intent_name
    import capo_chime_sdk_identity.types.responds_to
    import capo_chime_sdk_identity.types.string


class LexConfiguration(TypedDict, closed=True):
    responds_to: NotRequired["capo_chime_sdk_identity.types.responds_to.RespondsTo"]
    """<important> <p> <b>Deprecated</b>. Use <code>InvokedBy</code> instead.</p> </important> <p>Determines whether the Amazon Lex V2 bot responds to all standard messages. Control messages are not supported.</p>"""
    invoked_by: NotRequired["capo_chime_sdk_identity.types.invoked_by.InvokedBy"]
    """<p>Specifies the type of message that triggers a bot.</p>"""
    lex_bot_alias_arn: "capo_chime_sdk_identity.types.lex_bot_alias_arn.LexBotAliasArn"
    """<p>The ARN of the Amazon Lex V2 bot's alias. The ARN uses this format: <code>arn:aws:lex:REGION:ACCOUNT:bot-alias/MYBOTID/MYBOTALIAS</code> </p>"""
    locale_id: "capo_chime_sdk_identity.types.string.String"
    """<p>Identifies the Amazon Lex V2 bot's language and locale. The string must match one of the supported locales in Amazon Lex V2. All of the intents, slot types, and slots used in the bot must have the same locale. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a> in the <i>Amazon Lex V2 Developer Guide</i>.</p>"""
    welcome_intent: NotRequired[
        "capo_chime_sdk_identity.types.lex_intent_name.LexIntentName"
    ]
    """<p>The name of the welcome intent configured in the Amazon Lex V2 bot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LexConfiguration) -> dict:
    out: dict = {}
    if "responds_to" in value:
        import capo_chime_sdk_identity.types.responds_to

        out["RespondsTo"] = capo_chime_sdk_identity.types.responds_to.serialize_json(
            value["responds_to"]
        )
    if "invoked_by" in value:
        import capo_chime_sdk_identity.types.invoked_by

        out["InvokedBy"] = capo_chime_sdk_identity.types.invoked_by.serialize_json(
            value["invoked_by"]
        )
    out["LexBotAliasArn"] = value["lex_bot_alias_arn"]
    out["LocaleId"] = value["locale_id"]
    if "welcome_intent" in value:
        out["WelcomeIntent"] = value["welcome_intent"]
    return out


def deserialize_json(data: dict) -> LexConfiguration:
    out: LexConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("RespondsTo") is not None:
        import capo_chime_sdk_identity.types.responds_to

        out["responds_to"] = capo_chime_sdk_identity.types.responds_to.deserialize_json(
            data["RespondsTo"]
        )
    if data.get("InvokedBy") is not None:
        import capo_chime_sdk_identity.types.invoked_by

        out["invoked_by"] = capo_chime_sdk_identity.types.invoked_by.deserialize_json(
            data["InvokedBy"]
        )
    if data.get("LexBotAliasArn") is not None:
        out["lex_bot_alias_arn"] = data["LexBotAliasArn"]
    else:
        raise DeserializationError("LexConfiguration.lex_bot_alias_arn required")
    if data.get("LocaleId") is not None:
        out["locale_id"] = data["LocaleId"]
    else:
        raise DeserializationError("LexConfiguration.locale_id required")
    if data.get("WelcomeIntent") is not None:
        out["welcome_intent"] = data["WelcomeIntent"]
    return out
