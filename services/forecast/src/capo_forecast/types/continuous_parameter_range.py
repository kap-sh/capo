"""Generated from Smithy shape ``com.amazonaws.forecast#ContinuousParameterRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import capo_forecast.types.double
    import capo_forecast.types.name
    import capo_forecast.types.scaling_type


class ContinuousParameterRange(TypedDict, closed=True):
    name: "capo_forecast.types.name.Name"
    """<p>The name of the hyperparameter to tune.</p>"""
    max_value: "capo_forecast.types.double.Double"
    """<p>The maximum tunable value of the hyperparameter.</p>"""
    min_value: "capo_forecast.types.double.Double"
    """<p>The minimum tunable value of the hyperparameter.</p>"""
    scaling_type: NotRequired["capo_forecast.types.scaling_type.ScalingType"]
    """<p>The scale that hyperparameter tuning uses to search the hyperparameter range. Valid values:</p> <dl> <dt>Auto</dt> <dd> <p>Amazon Forecast hyperparameter tuning chooses the best scale for the hyperparameter.</p> </dd> <dt>Linear</dt> <dd> <p>Hyperparameter tuning searches the values in the hyperparameter range by using a linear scale.</p> </dd> <dt>Logarithmic</dt> <dd> <p>Hyperparameter tuning searches the values in the hyperparameter range by using a logarithmic scale.</p> <p>Logarithmic scaling works only for ranges that have values greater than 0.</p> </dd> <dt>ReverseLogarithmic</dt> <dd> <p>hyperparameter tuning searches the values in the hyperparameter range by using a reverse logarithmic scale.</p> <p>Reverse logarithmic scaling works only for ranges that are entirely within the range 0 <= x < 1.0.</p> </dd> </dl> <p>For information about choosing a hyperparameter scale, see <a href="http://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-ranges.html#scaling-type">Hyperparameter Scaling</a>. One of the following values:</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContinuousParameterRange) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["MaxValue"] = (
        "NaN"
        if value["max_value"] != value["max_value"]
        else "Infinity"
        if value["max_value"] == float("inf")
        else "-Infinity"
        if value["max_value"] == float("-inf")
        else value["max_value"]
    )
    out["MinValue"] = (
        "NaN"
        if value["min_value"] != value["min_value"]
        else "Infinity"
        if value["min_value"] == float("inf")
        else "-Infinity"
        if value["min_value"] == float("-inf")
        else value["min_value"]
    )
    if "scaling_type" in value:
        import capo_forecast.types.scaling_type

        out["ScalingType"] = capo_forecast.types.scaling_type.serialize_aws_json_1_1(
            value["scaling_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContinuousParameterRange:
    out: ContinuousParameterRange = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ContinuousParameterRange.name required")
    if data.get("MaxValue") is not None:
        out["max_value"] = float(data["MaxValue"])
    else:
        raise DeserializationError("ContinuousParameterRange.max_value required")
    if data.get("MinValue") is not None:
        out["min_value"] = float(data["MinValue"])
    else:
        raise DeserializationError("ContinuousParameterRange.min_value required")
    if data.get("ScalingType") is not None:
        import capo_forecast.types.scaling_type

        out["scaling_type"] = capo_forecast.types.scaling_type.deserialize_aws_json_1_1(
            data["ScalingType"]
        )
    return out
