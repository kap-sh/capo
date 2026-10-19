"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UtteranceDataSortBy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.analytics_sort_order
    import capo_lex_models_v2.types.analytics_utterance_sort_by_name


class UtteranceDataSortBy(TypedDict, closed=True):
    name: "capo_lex_models_v2.types.analytics_utterance_sort_by_name.AnalyticsUtteranceSortByName"
    """<p>The measure by which to sort the utterance analytics data.</p> <ul> <li> <p> <code>Count</code> – The number of utterances.</p> </li> <li> <p> <code>UtteranceTimestamp</code> – The date and time of the utterance.</p> </li> </ul>"""
    order: "capo_lex_models_v2.types.analytics_sort_order.AnalyticsSortOrder"
    """<p>Specifies whether to sort the results in ascending or descending order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UtteranceDataSortBy) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.analytics_utterance_sort_by_name

    out["name"] = (
        capo_lex_models_v2.types.analytics_utterance_sort_by_name.serialize_json(
            value["name"]
        )
    )
    import capo_lex_models_v2.types.analytics_sort_order

    out["order"] = capo_lex_models_v2.types.analytics_sort_order.serialize_json(
        value["order"]
    )
    return out


def deserialize_json(data: dict) -> UtteranceDataSortBy:
    out: UtteranceDataSortBy = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_lex_models_v2.types.analytics_utterance_sort_by_name

        out["name"] = (
            capo_lex_models_v2.types.analytics_utterance_sort_by_name.deserialize_json(
                data["name"]
            )
        )
    else:
        import typing

        out["name"] = typing.cast(
            "capo_lex_models_v2.types.analytics_utterance_sort_by_name.AnalyticsUtteranceSortByName",
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
