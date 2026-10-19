"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListIntentPathsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.analytics_path
    import capo_lex_models_v2.types.analytics_path_filters
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.timestamp


class ListIntentPathsRequest(TypedDict, closed=True):
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The identifier for the bot for which you want to retrieve intent path metrics.</p>"""
    start_date_time: "capo_lex_models_v2.types.timestamp.Timestamp"
    """<p>The date and time that marks the beginning of the range of time for which you want to see intent path metrics.</p>"""
    end_date_time: "capo_lex_models_v2.types.timestamp.Timestamp"
    """<p>The date and time that marks the end of the range of time for which you want to see intent path metrics.</p>"""
    intent_path: "capo_lex_models_v2.types.analytics_path.AnalyticsPath"
    """<p>The intent path for which you want to retrieve metrics. Use a forward slash to separate intents in the path. For example:</p> <ul> <li> <p>/BookCar</p> </li> <li> <p>/BookCar/BookHotel</p> </li> <li> <p>/BookHotel/BookCar</p> </li> </ul>"""
    filters: NotRequired[
        "capo_lex_models_v2.types.analytics_path_filters.AnalyticsPathFilters"
    ]
    """<p>A list of objects, each describes a condition by which you want to filter the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIntentPathsRequest) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.timestamp

    out["startDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
        value["start_date_time"]
    )
    import capo_lex_models_v2.types.timestamp

    out["endDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
        value["end_date_time"]
    )
    out["intentPath"] = value["intent_path"]
    if "filters" in value:
        import capo_lex_models_v2.types.analytics_path_filters

        out["filters"] = capo_lex_models_v2.types.analytics_path_filters.serialize_json(
            value["filters"]
        )
    return out


def deserialize_json(data: dict) -> ListIntentPathsRequest:
    out: ListIntentPathsRequest = {}  # type: ignore[typeddict-item]
    if data.get("startDateTime") is not None:
        import capo_lex_models_v2.types.timestamp

        out["start_date_time"] = capo_lex_models_v2.types.timestamp.deserialize_json(
            data["startDateTime"]
        )
    else:
        import datetime

        out["start_date_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("endDateTime") is not None:
        import capo_lex_models_v2.types.timestamp

        out["end_date_time"] = capo_lex_models_v2.types.timestamp.deserialize_json(
            data["endDateTime"]
        )
    else:
        import datetime

        out["end_date_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("intentPath") is not None:
        out["intent_path"] = data["intentPath"]
    else:
        out["intent_path"] = ""
    if data.get("filters") is not None:
        import capo_lex_models_v2.types.analytics_path_filters

        out["filters"] = (
            capo_lex_models_v2.types.analytics_path_filters.deserialize_json(
                data["filters"]
            )
        )
    return out
