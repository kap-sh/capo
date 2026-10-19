"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsBinBySpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.analytics_bin_by_name
    import capo_lex_models_v2.types.analytics_interval
    import capo_lex_models_v2.types.analytics_sort_order


class AnalyticsBinBySpecification(TypedDict, closed=True):
    name: "capo_lex_models_v2.types.analytics_bin_by_name.AnalyticsBinByName"
    """<p>Specifies the time metric by which to bin the analytics data.</p>"""
    interval: "capo_lex_models_v2.types.analytics_interval.AnalyticsInterval"
    """<p>Specifies the interval of time by which to bin the analytics data.</p>"""
    order: NotRequired[
        "capo_lex_models_v2.types.analytics_sort_order.AnalyticsSortOrder"
    ]
    """<p>Specifies whether to bin the analytics data in ascending or descending order. If this field is left blank, the default order is by the key of the bin in descending order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsBinBySpecification) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.analytics_bin_by_name

    out["name"] = capo_lex_models_v2.types.analytics_bin_by_name.serialize_json(
        value["name"]
    )
    import capo_lex_models_v2.types.analytics_interval

    out["interval"] = capo_lex_models_v2.types.analytics_interval.serialize_json(
        value["interval"]
    )
    if "order" in value:
        import capo_lex_models_v2.types.analytics_sort_order

        out["order"] = capo_lex_models_v2.types.analytics_sort_order.serialize_json(
            value["order"]
        )
    return out


def deserialize_json(data: dict) -> AnalyticsBinBySpecification:
    out: AnalyticsBinBySpecification = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_lex_models_v2.types.analytics_bin_by_name

        out["name"] = capo_lex_models_v2.types.analytics_bin_by_name.deserialize_json(
            data["name"]
        )
    else:
        import typing

        out["name"] = typing.cast(
            "capo_lex_models_v2.types.analytics_bin_by_name.AnalyticsBinByName", ""
        )
    if data.get("interval") is not None:
        import capo_lex_models_v2.types.analytics_interval

        out["interval"] = capo_lex_models_v2.types.analytics_interval.deserialize_json(
            data["interval"]
        )
    else:
        import typing

        out["interval"] = typing.cast(
            "capo_lex_models_v2.types.analytics_interval.AnalyticsInterval", ""
        )
    if data.get("order") is not None:
        import capo_lex_models_v2.types.analytics_sort_order

        out["order"] = capo_lex_models_v2.types.analytics_sort_order.deserialize_json(
            data["order"]
        )
    return out
