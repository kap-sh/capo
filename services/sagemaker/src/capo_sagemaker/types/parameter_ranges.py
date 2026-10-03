"""Generated from Smithy shape ``com.amazonaws.sagemaker#ParameterRanges``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.auto_parameters
    import capo_sagemaker.types.categorical_parameter_ranges
    import capo_sagemaker.types.continuous_parameter_ranges
    import capo_sagemaker.types.integer_parameter_ranges


class ParameterRanges(TypedDict, closed=True):
    integer_parameter_ranges: NotRequired[
        "capo_sagemaker.types.integer_parameter_ranges.IntegerParameterRanges"
    ]
    """<p>The array of <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_IntegerParameterRange.html">IntegerParameterRange</a> objects that specify ranges of integer hyperparameters that a hyperparameter tuning job searches.</p>"""
    continuous_parameter_ranges: NotRequired[
        "capo_sagemaker.types.continuous_parameter_ranges.ContinuousParameterRanges"
    ]
    """<p>The array of <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ContinuousParameterRange.html">ContinuousParameterRange</a> objects that specify ranges of continuous hyperparameters that a hyperparameter tuning job searches.</p>"""
    categorical_parameter_ranges: NotRequired[
        "capo_sagemaker.types.categorical_parameter_ranges.CategoricalParameterRanges"
    ]
    """<p>The array of <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CategoricalParameterRange.html">CategoricalParameterRange</a> objects that specify ranges of categorical hyperparameters that a hyperparameter tuning job searches.</p>"""
    auto_parameters: NotRequired["capo_sagemaker.types.auto_parameters.AutoParameters"]
    """<p>A list containing hyperparameter names and example values to be used by Autotune to determine optimal ranges for your tuning job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterRanges) -> dict:
    out: dict = {}
    if "integer_parameter_ranges" in value:
        import capo_sagemaker.types.integer_parameter_ranges

        out["IntegerParameterRanges"] = (
            capo_sagemaker.types.integer_parameter_ranges.serialize_aws_json_1_1(
                value["integer_parameter_ranges"]
            )
        )
    if "continuous_parameter_ranges" in value:
        import capo_sagemaker.types.continuous_parameter_ranges

        out["ContinuousParameterRanges"] = (
            capo_sagemaker.types.continuous_parameter_ranges.serialize_aws_json_1_1(
                value["continuous_parameter_ranges"]
            )
        )
    if "categorical_parameter_ranges" in value:
        import capo_sagemaker.types.categorical_parameter_ranges

        out["CategoricalParameterRanges"] = (
            capo_sagemaker.types.categorical_parameter_ranges.serialize_aws_json_1_1(
                value["categorical_parameter_ranges"]
            )
        )
    if "auto_parameters" in value:
        import capo_sagemaker.types.auto_parameters

        out["AutoParameters"] = (
            capo_sagemaker.types.auto_parameters.serialize_aws_json_1_1(
                value["auto_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ParameterRanges:
    out: ParameterRanges = {}  # type: ignore[typeddict-item]
    if data.get("IntegerParameterRanges") is not None:
        import capo_sagemaker.types.integer_parameter_ranges

        out["integer_parameter_ranges"] = (
            capo_sagemaker.types.integer_parameter_ranges.deserialize_aws_json_1_1(
                data["IntegerParameterRanges"]
            )
        )
    if data.get("ContinuousParameterRanges") is not None:
        import capo_sagemaker.types.continuous_parameter_ranges

        out["continuous_parameter_ranges"] = (
            capo_sagemaker.types.continuous_parameter_ranges.deserialize_aws_json_1_1(
                data["ContinuousParameterRanges"]
            )
        )
    if data.get("CategoricalParameterRanges") is not None:
        import capo_sagemaker.types.categorical_parameter_ranges

        out["categorical_parameter_ranges"] = (
            capo_sagemaker.types.categorical_parameter_ranges.deserialize_aws_json_1_1(
                data["CategoricalParameterRanges"]
            )
        )
    if data.get("AutoParameters") is not None:
        import capo_sagemaker.types.auto_parameters

        out["auto_parameters"] = (
            capo_sagemaker.types.auto_parameters.deserialize_aws_json_1_1(
                data["AutoParameters"]
            )
        )
    return out
