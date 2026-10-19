"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotAnalyzerHistorySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_analyzer_status
    import capo_lex_models_v2.types.timestamp
    import capo_lex_models_v2.types.uuid


class BotAnalyzerHistorySummary(TypedDict, closed=True):
    bot_analyzer_status: (
        "capo_lex_models_v2.types.bot_analyzer_status.BotAnalyzerStatus"
    )
    """<p>The status of the historical analysis execution.</p> <p>Valid Values: <code>Processing | Available | Failed | Stopping | Stopped</code> </p>"""
    creation_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The date and time when the analysis was initiated.</p>"""
    bot_analyzer_request_id: "capo_lex_models_v2.types.uuid.UUID"
    """<p>The unique identifier for the analysis request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BotAnalyzerHistorySummary) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.bot_analyzer_status

    out["botAnalyzerStatus"] = (
        capo_lex_models_v2.types.bot_analyzer_status.serialize_json(
            value["bot_analyzer_status"]
        )
    )
    if "creation_date_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["creationDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    out["botAnalyzerRequestId"] = value["bot_analyzer_request_id"]
    return out


def deserialize_json(data: dict) -> BotAnalyzerHistorySummary:
    out: BotAnalyzerHistorySummary = {}  # type: ignore[typeddict-item]
    if data.get("botAnalyzerStatus") is not None:
        import capo_lex_models_v2.types.bot_analyzer_status

        out["bot_analyzer_status"] = (
            capo_lex_models_v2.types.bot_analyzer_status.deserialize_json(
                data["botAnalyzerStatus"]
            )
        )
    else:
        import typing

        out["bot_analyzer_status"] = typing.cast(
            "capo_lex_models_v2.types.bot_analyzer_status.BotAnalyzerStatus", ""
        )
    if data.get("creationDateTime") is not None:
        import capo_lex_models_v2.types.timestamp

        out["creation_date_time"] = capo_lex_models_v2.types.timestamp.deserialize_json(
            data["creationDateTime"]
        )
    if data.get("botAnalyzerRequestId") is not None:
        out["bot_analyzer_request_id"] = data["botAnalyzerRequestId"]
    else:
        out["bot_analyzer_request_id"] = ""
    return out
