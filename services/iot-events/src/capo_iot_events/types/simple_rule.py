"""Generated from Smithy shape ``com.amazonaws.iotevents#SimpleRule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.comparison_operator
    import capo_iot_events.types.input_property
    import capo_iot_events.types.threshold


class SimpleRule(TypedDict, closed=True):
    input_property: "capo_iot_events.types.input_property.InputProperty"
    """<p>The value on the left side of the comparison operator. You can specify an AWS IoT Events input attribute as an input property.</p>"""
    comparison_operator: "capo_iot_events.types.comparison_operator.ComparisonOperator"
    """<p>The comparison operator.</p>"""
    threshold: "capo_iot_events.types.threshold.Threshold"
    """<p>The value on the right side of the comparison operator. You can enter a number or specify an AWS IoT Events input attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SimpleRule) -> dict:
    out: dict = {}
    out["inputProperty"] = value["input_property"]
    import capo_iot_events.types.comparison_operator

    out["comparisonOperator"] = (
        capo_iot_events.types.comparison_operator.serialize_json(
            value["comparison_operator"]
        )
    )
    out["threshold"] = value["threshold"]
    return out


def deserialize_json(data: dict) -> SimpleRule:
    out: SimpleRule = {}  # type: ignore[typeddict-item]
    if data.get("inputProperty") is not None:
        out["input_property"] = data["inputProperty"]
    else:
        out["input_property"] = ""
    if data.get("comparisonOperator") is not None:
        import capo_iot_events.types.comparison_operator

        out["comparison_operator"] = (
            capo_iot_events.types.comparison_operator.deserialize_json(
                data["comparisonOperator"]
            )
        )
    else:
        import typing

        out["comparison_operator"] = typing.cast(
            "capo_iot_events.types.comparison_operator.ComparisonOperator", ""
        )
    if data.get("threshold") is not None:
        out["threshold"] = data["threshold"]
    else:
        out["threshold"] = ""
    return out
