"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#MetricDimension``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.metric_dimension_name
    import capo_application_auto_scaling.types.metric_dimension_value


class MetricDimension(TypedDict, closed=True):
    name: (
        "capo_application_auto_scaling.types.metric_dimension_name.MetricDimensionName"
    )
    """<p>The name of the dimension.</p>"""
    value: "capo_application_auto_scaling.types.metric_dimension_value.MetricDimensionValue"
    """<p>The value of the dimension.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricDimension) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricDimension:
    out: MetricDimension = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
