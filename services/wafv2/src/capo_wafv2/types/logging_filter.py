"""Generated from Smithy shape ``com.amazonaws.wafv2#LoggingFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.filter_behavior
    import capo_wafv2.types.filters


class LoggingFilter(TypedDict, closed=True):
    filters: "capo_wafv2.types.filters.Filters"
    """<p>The filters that you want to apply to the logs. </p>"""
    default_behavior: "capo_wafv2.types.filter_behavior.FilterBehavior"
    """<p>Default handling for logs that don't match any of the specified filtering conditions. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoggingFilter) -> dict:
    out: dict = {}
    import capo_wafv2.types.filters

    out["Filters"] = capo_wafv2.types.filters.serialize_aws_json_1_1(value["filters"])
    import capo_wafv2.types.filter_behavior

    out["DefaultBehavior"] = capo_wafv2.types.filter_behavior.serialize_aws_json_1_1(
        value["default_behavior"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> LoggingFilter:
    out: LoggingFilter = {}  # type: ignore[typeddict-item]
    if data.get("Filters") is not None:
        import capo_wafv2.types.filters

        out["filters"] = capo_wafv2.types.filters.deserialize_aws_json_1_1(
            data["Filters"]
        )
    else:
        out["filters"] = []
    if data.get("DefaultBehavior") is not None:
        import capo_wafv2.types.filter_behavior

        out["default_behavior"] = (
            capo_wafv2.types.filter_behavior.deserialize_aws_json_1_1(
                data["DefaultBehavior"]
            )
        )
    else:
        import typing

        out["default_behavior"] = typing.cast(
            "capo_wafv2.types.filter_behavior.FilterBehavior", ""
        )
    return out
