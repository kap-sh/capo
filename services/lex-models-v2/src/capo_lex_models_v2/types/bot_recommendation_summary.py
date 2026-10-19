"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotRecommendationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_recommendation_status
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.timestamp


class BotRecommendationSummary(TypedDict, closed=True):
    bot_recommendation_status: (
        "capo_lex_models_v2.types.bot_recommendation_status.BotRecommendationStatus"
    )
    """<p>The status of the bot recommendation.</p> <p>If the status is Failed, then the reasons for the failure are listed in the failureReasons field. </p>"""
    bot_recommendation_id: "capo_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the bot recommendation to be updated.</p>"""
    creation_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>A timestamp of the date and time that the bot recommendation was created.</p>"""
    last_updated_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>A timestamp of the date and time that the bot recommendation was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BotRecommendationSummary) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.bot_recommendation_status

    out["botRecommendationStatus"] = (
        capo_lex_models_v2.types.bot_recommendation_status.serialize_json(
            value["bot_recommendation_status"]
        )
    )
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
    return out


def deserialize_json(data: dict) -> BotRecommendationSummary:
    out: BotRecommendationSummary = {}  # type: ignore[typeddict-item]
    if data.get("botRecommendationStatus") is not None:
        import capo_lex_models_v2.types.bot_recommendation_status

        out["bot_recommendation_status"] = (
            capo_lex_models_v2.types.bot_recommendation_status.deserialize_json(
                data["botRecommendationStatus"]
            )
        )
    else:
        import typing

        out["bot_recommendation_status"] = typing.cast(
            "capo_lex_models_v2.types.bot_recommendation_status.BotRecommendationStatus",
            "",
        )
    if data.get("botRecommendationId") is not None:
        out["bot_recommendation_id"] = data["botRecommendationId"]
    else:
        out["bot_recommendation_id"] = ""
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
