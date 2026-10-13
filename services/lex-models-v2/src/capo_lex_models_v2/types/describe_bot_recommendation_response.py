"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DescribeBotRecommendationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_recommendation_results
    import capo_lex_models_v2.types.bot_recommendation_status
    import capo_lex_models_v2.types.draft_bot_version
    import capo_lex_models_v2.types.encryption_setting
    import capo_lex_models_v2.types.failure_reasons
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id
    import capo_lex_models_v2.types.timestamp
    import capo_lex_models_v2.types.transcript_source_setting


class DescribeBotRecommendationResponse(TypedDict, closed=True):
    bot_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The identifier of the bot associated with the bot recommendation.</p>"""
    bot_version: NotRequired[
        "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    ]
    """<p>The version of the bot associated with the bot recommendation.</p>"""
    locale_id: NotRequired["capo_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The identifier of the language and locale of the bot recommendation to describe.</p>"""
    bot_recommendation_status: NotRequired[
        "capo_lex_models_v2.types.bot_recommendation_status.BotRecommendationStatus"
    ]
    """<p>The status of the bot recommendation. If the status is Failed, then the reasons for the failure are listed in the failureReasons field. </p>"""
    bot_recommendation_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The identifier of the bot recommendation being described.</p>"""
    failure_reasons: NotRequired[
        "capo_lex_models_v2.types.failure_reasons.FailureReasons"
    ]
    """<p>If botRecommendationStatus is Failed, Amazon Lex explains why.</p>"""
    creation_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The date and time that the bot recommendation was created.</p>"""
    last_updated_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The date and time that the bot recommendation was last updated.</p>"""
    transcript_source_setting: NotRequired[
        "capo_lex_models_v2.types.transcript_source_setting.TranscriptSourceSetting"
    ]
    """<p>The object representing the Amazon S3 bucket containing the transcript, as well as the associated metadata.</p>"""
    encryption_setting: NotRequired[
        "capo_lex_models_v2.types.encryption_setting.EncryptionSetting"
    ]
    """<p>The object representing the passwords that were used to encrypt the data related to the bot recommendation results, as well as the KMS key ARN used to encrypt the associated metadata.</p>"""
    bot_recommendation_results: NotRequired[
        "capo_lex_models_v2.types.bot_recommendation_results.BotRecommendationResults"
    ]
    """<p>The object representing the URL of the bot definition, the URL of the associated transcript and a statistical summary of the bot recommendation results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBotRecommendationResponse) -> dict:
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
    if "failure_reasons" in value:
        import capo_lex_models_v2.types.failure_reasons

        out["failureReasons"] = capo_lex_models_v2.types.failure_reasons.serialize_json(
            value["failure_reasons"]
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
    if "bot_recommendation_results" in value:
        import capo_lex_models_v2.types.bot_recommendation_results

        out["botRecommendationResults"] = (
            capo_lex_models_v2.types.bot_recommendation_results.serialize_json(
                value["bot_recommendation_results"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeBotRecommendationResponse:
    out: DescribeBotRecommendationResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("failureReasons") is not None:
        import capo_lex_models_v2.types.failure_reasons

        out["failure_reasons"] = (
            capo_lex_models_v2.types.failure_reasons.deserialize_json(
                data["failureReasons"]
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
    if data.get("botRecommendationResults") is not None:
        import capo_lex_models_v2.types.bot_recommendation_results

        out["bot_recommendation_results"] = (
            capo_lex_models_v2.types.bot_recommendation_results.deserialize_json(
                data["botRecommendationResults"]
            )
        )
    return out


def redact_sensitive(value: DescribeBotRecommendationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "encryption_setting" in value:
        import capo_lex_models_v2.types.encryption_setting

        out["encryption_setting"] = (
            capo_lex_models_v2.types.encryption_setting.redact_sensitive(
                value["encryption_setting"]
            )
        )
    return out
