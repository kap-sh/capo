"""Generated from Smithy shape ``com.amazonaws.sagemaker#ContinuousParameterRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.hyper_parameter_scaling_type
    import capo_sagemaker.types.parameter_key
    import capo_sagemaker.types.parameter_value


class ContinuousParameterRange(TypedDict, closed=True):
    name: NotRequired["capo_sagemaker.types.parameter_key.ParameterKey"]
    """<p>The name of the continuous hyperparameter to tune.</p>"""
    min_value: NotRequired["capo_sagemaker.types.parameter_value.ParameterValue"]
    """<p>The minimum value for the hyperparameter. The tuning job uses floating-point values between this value and <code>MaxValue</code>for tuning.</p>"""
    max_value: NotRequired["capo_sagemaker.types.parameter_value.ParameterValue"]
    """<p>The maximum value for the hyperparameter. The tuning job uses floating-point values between <code>MinValue</code> value and this value for tuning.</p>"""
    scaling_type: NotRequired[
        "capo_sagemaker.types.hyper_parameter_scaling_type.HyperParameterScalingType"
    ]
    """<p>The scale that hyperparameter tuning uses to search the hyperparameter range. For information about choosing a hyperparameter scale, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-ranges.html#scaling-type">Hyperparameter Scaling</a>. One of the following values:</p> <dl> <dt>Auto</dt> <dd> <p>SageMaker hyperparameter tuning chooses the best scale for the hyperparameter.</p> </dd> <dt>Linear</dt> <dd> <p>Hyperparameter tuning searches the values in the hyperparameter range by using a linear scale.</p> </dd> <dt>Logarithmic</dt> <dd> <p>Hyperparameter tuning searches the values in the hyperparameter range by using a logarithmic scale.</p> <p>Logarithmic scaling works only for ranges that have only values greater than 0.</p> </dd> <dt>ReverseLogarithmic</dt> <dd> <p>Hyperparameter tuning searches the values in the hyperparameter range by using a reverse logarithmic scale.</p> <p>Reverse logarithmic scaling works only for ranges that are entirely within the range 0&lt;=x&lt;1.0.</p> </dd> </dl>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContinuousParameterRange) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "min_value" in value:
        out["MinValue"] = value["min_value"]
    if "max_value" in value:
        out["MaxValue"] = value["max_value"]
    if "scaling_type" in value:
        import capo_sagemaker.types.hyper_parameter_scaling_type

        out["ScalingType"] = (
            capo_sagemaker.types.hyper_parameter_scaling_type.serialize_aws_json_1_1(
                value["scaling_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContinuousParameterRange:
    out: ContinuousParameterRange = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("MinValue") is not None:
        out["min_value"] = data["MinValue"]
    if data.get("MaxValue") is not None:
        out["max_value"] = data["MaxValue"]
    if data.get("ScalingType") is not None:
        import capo_sagemaker.types.hyper_parameter_scaling_type

        out["scaling_type"] = (
            capo_sagemaker.types.hyper_parameter_scaling_type.deserialize_aws_json_1_1(
                data["ScalingType"]
            )
        )
    return out
