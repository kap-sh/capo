"""Generated from Smithy shape ``com.amazonaws.forecast#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.arn
    import capo_forecast.types.filter_condition_string
    import capo_forecast.types.string


class Filter(TypedDict, closed=True):
    key: "capo_forecast.types.string.String"
    """<p>The name of the parameter to filter on.</p>"""
    value: "capo_forecast.types.arn.Arn"
    """<p>The value to match.</p>"""
    condition: "capo_forecast.types.filter_condition_string.FilterConditionString"
    """<p>The condition to apply. To include the objects that match the statement, specify <code>IS</code>. To exclude matching objects, specify <code>IS_NOT</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Filter) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    import capo_forecast.types.filter_condition_string

    out["Condition"] = (
        capo_forecast.types.filter_condition_string.serialize_aws_json_1_1(
            value["condition"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        out["key"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    if data.get("Condition") is not None:
        import capo_forecast.types.filter_condition_string

        out["condition"] = (
            capo_forecast.types.filter_condition_string.deserialize_aws_json_1_1(
                data["Condition"]
            )
        )
    else:
        import typing

        out["condition"] = typing.cast(
            "capo_forecast.types.filter_condition_string.FilterConditionString", ""
        )
    return out
