"""Generated from Smithy shape ``com.amazonaws.forecast#TimeSeriesCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.attribute_value
    import capo_forecast.types.condition
    import capo_forecast.types.name


class TimeSeriesCondition(TypedDict, closed=True):
    attribute_name: "capo_forecast.types.name.Name"
    """<p>The item_id, dimension name, IM name, or timestamp that you are modifying.</p>"""
    attribute_value: "capo_forecast.types.attribute_value.AttributeValue"
    """<p>The value that is applied for the chosen <code>Condition</code>.</p>"""
    condition: "capo_forecast.types.condition.Condition"
    """<p>The condition to apply. Valid values are <code>EQUALS</code>, <code>NOT_EQUALS</code>, <code>LESS_THAN</code> and <code>GREATER_THAN</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimeSeriesCondition) -> dict:
    out: dict = {}
    out["AttributeName"] = value["attribute_name"]
    out["AttributeValue"] = value["attribute_value"]
    import capo_forecast.types.condition

    out["Condition"] = capo_forecast.types.condition.serialize_aws_json_1_1(
        value["condition"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TimeSeriesCondition:
    out: TimeSeriesCondition = {}  # type: ignore[typeddict-item]
    if data.get("AttributeName") is not None:
        out["attribute_name"] = data["AttributeName"]
    else:
        out["attribute_name"] = ""
    if data.get("AttributeValue") is not None:
        out["attribute_value"] = data["AttributeValue"]
    else:
        out["attribute_value"] = ""
    if data.get("Condition") is not None:
        import capo_forecast.types.condition

        out["condition"] = capo_forecast.types.condition.deserialize_aws_json_1_1(
            data["Condition"]
        )
    else:
        import typing

        out["condition"] = typing.cast("capo_forecast.types.condition.Condition", "")
    return out
