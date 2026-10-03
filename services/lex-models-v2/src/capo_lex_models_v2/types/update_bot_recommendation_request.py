"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UpdateBotRecommendationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.draft_bot_version
    import capo_lex_models_v2.types.encryption_setting
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id


class UpdateBotRecommendationRequest(TypedDict, closed=True):
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the bot containing the bot recommendation to be updated.</p>"""
    bot_version: "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    """<p>The version of the bot containing the bot recommendation to be updated.</p>"""
    locale_id: "capo_lex_models_v2.types.locale_id.LocaleId"
    """<p>The identifier of the language and locale of the bot recommendation to update. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a> </p>"""
    bot_recommendation_id: "capo_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the bot recommendation to be updated.</p>"""
    encryption_setting: "capo_lex_models_v2.types.encryption_setting.EncryptionSetting"
    """<p>The object representing the passwords that will be used to encrypt the data related to the bot recommendation results, as well as the KMS key ARN used to encrypt the associated metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBotRecommendationRequest) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.encryption_setting

    out["encryptionSetting"] = (
        capo_lex_models_v2.types.encryption_setting.serialize_json(
            value["encryption_setting"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateBotRecommendationRequest:
    out: UpdateBotRecommendationRequest = {}  # type: ignore[typeddict-item]
    if data.get("encryptionSetting") is not None:
        import capo_lex_models_v2.types.encryption_setting

        out["encryption_setting"] = (
            capo_lex_models_v2.types.encryption_setting.deserialize_json(
                data["encryptionSetting"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateBotRecommendationRequest.encryption_setting required"
        )
    return out
