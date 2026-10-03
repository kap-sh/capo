"""Generated from Smithy shape ``com.amazonaws.forecast#AttributeConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import capo_forecast.types.name
    import capo_forecast.types.transformations


class AttributeConfig(TypedDict, closed=True):
    attribute_name: "capo_forecast.types.name.Name"
    """<p>The name of the attribute as specified in the schema. Amazon Forecast supports the target field of the target time series and the related time series datasets. For example, for the RETAIL domain, the target is <code>demand</code>.</p>"""
    transformations: "capo_forecast.types.transformations.Transformations"
    """<p>The method parameters (key-value pairs), which are a map of override parameters. Specify these parameters to override the default values. Related Time Series attributes do not accept aggregation parameters.</p> <p>The following list shows the parameters and their valid values for the "filling" featurization method for a <b>Target Time Series</b> dataset. Default values are bolded.</p> <ul> <li> <p> <code>aggregation</code>: <b>sum</b>, <code>avg</code>, <code>first</code>, <code>min</code>, <code>max</code> </p> </li> <li> <p> <code>frontfill</code>: <b>none</b> </p> </li> <li> <p> <code>middlefill</code>: <b>zero</b>, <code>nan</code> (not a number), <code>value</code>, <code>median</code>, <code>mean</code>, <code>min</code>, <code>max</code> </p> </li> <li> <p> <code>backfill</code>: <b>zero</b>, <code>nan</code>, <code>value</code>, <code>median</code>, <code>mean</code>, <code>min</code>, <code>max</code> </p> </li> </ul> <p>The following list shows the parameters and their valid values for a <b>Related Time Series</b> featurization method (there are no defaults):</p> <ul> <li> <p> <code>middlefill</code>: <code>zero</code>, <code>value</code>, <code>median</code>, <code>mean</code>, <code>min</code>, <code>max</code> </p> </li> <li> <p> <code>backfill</code>: <code>zero</code>, <code>value</code>, <code>median</code>, <code>mean</code>, <code>min</code>, <code>max</code> </p> </li> <li> <p> <code>futurefill</code>: <code>zero</code>, <code>value</code>, <code>median</code>, <code>mean</code>, <code>min</code>, <code>max</code> </p> </li> </ul> <p>To set a filling method to a specific value, set the fill parameter to <code>value</code> and define the value in a corresponding <code>_value</code> parameter. For example, to set backfilling to a value of 2, include the following: <code>"backfill": "value"</code> and <code>"backfill_value":"2"</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttributeConfig) -> dict:
    out: dict = {}
    out["AttributeName"] = value["attribute_name"]
    import capo_forecast.types.transformations

    out["Transformations"] = capo_forecast.types.transformations.serialize_aws_json_1_1(
        value["transformations"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AttributeConfig:
    out: AttributeConfig = {}  # type: ignore[typeddict-item]
    if data.get("AttributeName") is not None:
        out["attribute_name"] = data["AttributeName"]
    else:
        raise DeserializationError("AttributeConfig.attribute_name required")
    if data.get("Transformations") is not None:
        import capo_forecast.types.transformations

        out["transformations"] = (
            capo_forecast.types.transformations.deserialize_aws_json_1_1(
                data["Transformations"]
            )
        )
    else:
        raise DeserializationError("AttributeConfig.transformations required")
    return out
