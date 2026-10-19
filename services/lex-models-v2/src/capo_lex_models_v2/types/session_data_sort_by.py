"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SessionDataSortBy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.analytics_session_sort_by_name
    import capo_lex_models_v2.types.analytics_sort_order


class SessionDataSortBy(TypedDict, closed=True):
    name: "capo_lex_models_v2.types.analytics_session_sort_by_name.AnalyticsSessionSortByName"
    """<p>The measure by which to sort the session analytics data.</p> <ul> <li> <p> <code>conversationStartTime</code> – The date and time when the conversation began. A conversation is defined as a unique combination of a <code>sessionId</code> and an <code>originatingRequestId</code>.</p> </li> <li> <p> <code>numberOfTurns</code> – The number of turns that the session took.</p> </li> <li> <p> <code>conversationDurationSeconds</code> – The duration of the conversation in seconds.</p> </li> </ul>"""
    order: "capo_lex_models_v2.types.analytics_sort_order.AnalyticsSortOrder"
    """<p>Specifies whether to sort the results in ascending or descending order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionDataSortBy) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.analytics_session_sort_by_name

    out["name"] = (
        capo_lex_models_v2.types.analytics_session_sort_by_name.serialize_json(
            value["name"]
        )
    )
    import capo_lex_models_v2.types.analytics_sort_order

    out["order"] = capo_lex_models_v2.types.analytics_sort_order.serialize_json(
        value["order"]
    )
    return out


def deserialize_json(data: dict) -> SessionDataSortBy:
    out: SessionDataSortBy = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_lex_models_v2.types.analytics_session_sort_by_name

        out["name"] = (
            capo_lex_models_v2.types.analytics_session_sort_by_name.deserialize_json(
                data["name"]
            )
        )
    else:
        import typing

        out["name"] = typing.cast(
            "capo_lex_models_v2.types.analytics_session_sort_by_name.AnalyticsSessionSortByName",
            "",
        )
    if data.get("order") is not None:
        import capo_lex_models_v2.types.analytics_sort_order

        out["order"] = capo_lex_models_v2.types.analytics_sort_order.deserialize_json(
            data["order"]
        )
    else:
        import typing

        out["order"] = typing.cast(
            "capo_lex_models_v2.types.analytics_sort_order.AnalyticsSortOrder", ""
        )
    return out
