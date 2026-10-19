"""Generated from Smithy shape ``com.amazonaws.budgets#AutoAdjustData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_budgets.types.auto_adjust_type
    import capo_budgets.types.generic_timestamp
    import capo_budgets.types.historical_options


class AutoAdjustData(TypedDict, closed=True):
    auto_adjust_type: "capo_budgets.types.auto_adjust_type.AutoAdjustType"
    """<p>The string that defines whether your budget auto-adjusts based on historical or forecasted data.</p>"""
    historical_options: NotRequired[
        "capo_budgets.types.historical_options.HistoricalOptions"
    ]
    """<p>The parameters that define or describe the historical data that your auto-adjusting budget is based on.</p>"""
    last_auto_adjust_time: NotRequired[
        "capo_budgets.types.generic_timestamp.GenericTimestamp"
    ]
    """<p>The last time that your budget was auto-adjusted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoAdjustData) -> dict:
    out: dict = {}
    import capo_budgets.types.auto_adjust_type

    out["AutoAdjustType"] = capo_budgets.types.auto_adjust_type.serialize_aws_json_1_1(
        value["auto_adjust_type"]
    )
    if "historical_options" in value:
        import capo_budgets.types.historical_options

        out["HistoricalOptions"] = (
            capo_budgets.types.historical_options.serialize_aws_json_1_1(
                value["historical_options"]
            )
        )
    if "last_auto_adjust_time" in value:
        import capo_budgets.types.generic_timestamp

        out["LastAutoAdjustTime"] = (
            capo_budgets.types.generic_timestamp.serialize_aws_json_1_1(
                value["last_auto_adjust_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoAdjustData:
    out: AutoAdjustData = {}  # type: ignore[typeddict-item]
    if data.get("AutoAdjustType") is not None:
        import capo_budgets.types.auto_adjust_type

        out["auto_adjust_type"] = (
            capo_budgets.types.auto_adjust_type.deserialize_aws_json_1_1(
                data["AutoAdjustType"]
            )
        )
    else:
        import typing

        out["auto_adjust_type"] = typing.cast(
            "capo_budgets.types.auto_adjust_type.AutoAdjustType", ""
        )
    if data.get("HistoricalOptions") is not None:
        import capo_budgets.types.historical_options

        out["historical_options"] = (
            capo_budgets.types.historical_options.deserialize_aws_json_1_1(
                data["HistoricalOptions"]
            )
        )
    if data.get("LastAutoAdjustTime") is not None:
        import capo_budgets.types.generic_timestamp

        out["last_auto_adjust_time"] = (
            capo_budgets.types.generic_timestamp.deserialize_aws_json_1_1(
                data["LastAutoAdjustTime"]
            )
        )
    return out
