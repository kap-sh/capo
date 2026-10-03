"""Generated from Smithy shape ``com.amazonaws.forecast#FeaturizationMethod``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import capo_forecast.types.featurization_method_name
    import capo_forecast.types.featurization_method_parameters


class FeaturizationMethod(TypedDict, closed=True):
    featurization_method_name: (
        "capo_forecast.types.featurization_method_name.FeaturizationMethodName"
    )
    """<p>The name of the method. The "filling" method is the only supported method.</p>"""
    featurization_method_parameters: NotRequired[
        "capo_forecast.types.featurization_method_parameters.FeaturizationMethodParameters"
    ]
    """<p>The method parameters (key-value pairs), which are a map of override parameters. Specify these parameters to override the default values. Related Time Series attributes do not accept aggregation parameters.</p> <p>The following list shows the parameters and their valid values for the "filling" featurization method for a <b>Target Time Series</b> dataset. Bold signifies the default value.</p> <ul> <li> <p> <code>aggregation</code>: <b>sum</b>, <code>avg</code>, <code>first</code>, <code>min</code>, <code>max</code> </p> </li> <li> <p> <code>frontfill</code>: <b>none</b> </p> </li> <li> <p> <code>middlefill</code>: <b>zero</b>, <code>nan</code> (not a number), <code>value</code>, <code>median</code>, <code>mean</code>, <code>min</code>, <code>max</code> </p> </li> <li> <p> <code>backfill</code>: <b>zero</b>, <code>nan</code>, <code>value</code>, <code>median</code>, <code>mean</code>, <code>min</code>, <code>max</code> </p> </li> </ul> <p>The following list shows the parameters and their valid values for a <b>Related Time Series</b> featurization method (there are no defaults):</p> <ul> <li> <p> <code>middlefill</code>: <code>zero</code>, <code>value</code>, <code>median</code>, <code>mean</code>, <code>min</code>, <code>max</code> </p> </li> <li> <p> <code>backfill</code>: <code>zero</code>, <code>value</code>, <code>median</code>, <code>mean</code>, <code>min</code>, <code>max</code> </p> </li> <li> <p> <code>futurefill</code>: <code>zero</code>, <code>value</code>, <code>median</code>, <code>mean</code>, <code>min</code>, <code>max</code> </p> </li> </ul> <p>To set a filling method to a specific value, set the fill parameter to <code>value</code> and define the value in a corresponding <code>_value</code> parameter. For example, to set backfilling to a value of 2, include the following: <code>"backfill": "value"</code> and <code>"backfill_value":"2"</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeaturizationMethod) -> dict:
    out: dict = {}
    import capo_forecast.types.featurization_method_name

    out["FeaturizationMethodName"] = (
        capo_forecast.types.featurization_method_name.serialize_aws_json_1_1(
            value["featurization_method_name"]
        )
    )
    if "featurization_method_parameters" in value:
        import capo_forecast.types.featurization_method_parameters

        out["FeaturizationMethodParameters"] = (
            capo_forecast.types.featurization_method_parameters.serialize_aws_json_1_1(
                value["featurization_method_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FeaturizationMethod:
    out: FeaturizationMethod = {}  # type: ignore[typeddict-item]
    if data.get("FeaturizationMethodName") is not None:
        import capo_forecast.types.featurization_method_name

        out["featurization_method_name"] = (
            capo_forecast.types.featurization_method_name.deserialize_aws_json_1_1(
                data["FeaturizationMethodName"]
            )
        )
    else:
        raise DeserializationError(
            "FeaturizationMethod.featurization_method_name required"
        )
    if data.get("FeaturizationMethodParameters") is not None:
        import capo_forecast.types.featurization_method_parameters

        out["featurization_method_parameters"] = (
            capo_forecast.types.featurization_method_parameters.deserialize_aws_json_1_1(
                data["FeaturizationMethodParameters"]
            )
        )
    return out
