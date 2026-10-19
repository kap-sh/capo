"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ConversationLogsDataSourceFilterBy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.conversation_logs_input_mode_filter
    import capo_lex_models_v2.types.timestamp


class ConversationLogsDataSourceFilterBy(TypedDict, closed=True):
    start_time: "capo_lex_models_v2.types.timestamp.Timestamp"
    """<p>The start time for the conversation log.</p>"""
    end_time: "capo_lex_models_v2.types.timestamp.Timestamp"
    """<p>The end time for the conversation log.</p>"""
    input_mode: "capo_lex_models_v2.types.conversation_logs_input_mode_filter.ConversationLogsInputModeFilter"
    """<p>The selection to filter by input mode for the conversation logs. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConversationLogsDataSourceFilterBy) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.timestamp

    out["startTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
        value["start_time"]
    )
    import capo_lex_models_v2.types.timestamp

    out["endTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
        value["end_time"]
    )
    import capo_lex_models_v2.types.conversation_logs_input_mode_filter

    out["inputMode"] = (
        capo_lex_models_v2.types.conversation_logs_input_mode_filter.serialize_json(
            value["input_mode"]
        )
    )
    return out


def deserialize_json(data: dict) -> ConversationLogsDataSourceFilterBy:
    out: ConversationLogsDataSourceFilterBy = {}  # type: ignore[typeddict-item]
    if data.get("startTime") is not None:
        import capo_lex_models_v2.types.timestamp

        out["start_time"] = capo_lex_models_v2.types.timestamp.deserialize_json(
            data["startTime"]
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("endTime") is not None:
        import capo_lex_models_v2.types.timestamp

        out["end_time"] = capo_lex_models_v2.types.timestamp.deserialize_json(
            data["endTime"]
        )
    else:
        import datetime

        out["end_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("inputMode") is not None:
        import capo_lex_models_v2.types.conversation_logs_input_mode_filter

        out["input_mode"] = (
            capo_lex_models_v2.types.conversation_logs_input_mode_filter.deserialize_json(
                data["inputMode"]
            )
        )
    else:
        import typing

        out["input_mode"] = typing.cast(
            "capo_lex_models_v2.types.conversation_logs_input_mode_filter.ConversationLogsInputModeFilter",
            "",
        )
    return out
