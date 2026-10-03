"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UpdateBotRecommendationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_recommendation_status
    import capo_lex_models_v2.types.draft_bot_version
    import capo_lex_models_v2.types.encryption_setting
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id
    import capo_lex_models_v2.types.timestamp
    import capo_lex_models_v2.types.transcript_source_setting


class UpdateBotRecommendationResponse(TypedDict, closed=True):
    bot_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the bot containing the bot recommendation that has been updated.</p>"""
    bot_version: NotRequired[
        "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    ]
    """<p>The version of the bot containing the bot recommendation that has been updated.</p>"""
    locale_id: NotRequired["capo_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The identifier of the language and locale of the bot recommendation to update. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a> </p>"""
    bot_recommendation_status: NotRequired[
        "capo_lex_models_v2.types.bot_recommendation_status.BotRecommendationStatus"
    ]
    """<p>The status of the bot recommendation.</p> <p>If the status is Failed, then the reasons for the failure are listed in the failureReasons field. </p>"""
    bot_recommendation_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the bot recommendation to be updated.</p>"""
    creation_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>A timestamp of the date and time that the bot recommendation was created.</p>"""
    last_updated_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>A timestamp of the date and time that the bot recommendation was last updated.</p>"""
    transcript_source_setting: NotRequired[
        "capo_lex_models_v2.types.transcript_source_setting.TranscriptSourceSetting"
    ]
    """<p>The object representing the Amazon S3 bucket containing the transcript, as well as the associated metadata.</p>"""
    encryption_setting: NotRequired[
        "capo_lex_models_v2.types.encryption_setting.EncryptionSetting"
    ]
    """<p>The object representing the passwords that were used to encrypt the data related to the bot recommendation results, as well as the KMS key ARN used to encrypt the associated metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBotRecommendationResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    if "bot_recommendation_status" in value:
        import capo_lex_models_v2.types.bot_recommendation_status

        out["botRecommendationStatus"] = (
            capo_lex_models_v2.types.bot_recommendation_status.serialize_json(
                value["bot_recommendation_status"]
            )
        )
    if "bot_recommendation_id" in value:
        out["botRecommendationId"] = value["bot_recommendation_id"]
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
    if "transcript_source_setting" in value:
        import capo_lex_models_v2.types.transcript_source_setting

        out["transcriptSourceSetting"] = (
            capo_lex_models_v2.types.transcript_source_setting.serialize_json(
                value["transcript_source_setting"]
            )
        )
    if "encryption_setting" in value:
        import capo_lex_models_v2.types.encryption_setting

        out["encryptionSetting"] = (
            capo_lex_models_v2.types.encryption_setting.serialize_json(
                value["encryption_setting"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateBotRecommendationResponse:
    out: UpdateBotRecommendationResponse = {}  # type: ignore[typeddict-item]
    if data.get("botId") is not None:
        out["bot_id"] = data["botId"]
    if data.get("botVersion") is not None:
        out["bot_version"] = data["botVersion"]
    if data.get("localeId") is not None:
        out["locale_id"] = data["localeId"]
    if data.get("botRecommendationStatus") is not None:
        import capo_lex_models_v2.types.bot_recommendation_status

        out["bot_recommendation_status"] = (
            capo_lex_models_v2.types.bot_recommendation_status.deserialize_json(
                data["botRecommendationStatus"]
            )
        )
    if data.get("botRecommendationId") is not None:
        out["bot_recommendation_id"] = data["botRecommendationId"]
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
    if data.get("transcriptSourceSetting") is not None:
        import capo_lex_models_v2.types.transcript_source_setting

        out["transcript_source_setting"] = (
            capo_lex_models_v2.types.transcript_source_setting.deserialize_json(
                data["transcriptSourceSetting"]
            )
        )
    if data.get("encryptionSetting") is not None:
        import capo_lex_models_v2.types.encryption_setting

        out["encryption_setting"] = (
            capo_lex_models_v2.types.encryption_setting.deserialize_json(
                data["encryptionSetting"]
            )
        )
    return out
