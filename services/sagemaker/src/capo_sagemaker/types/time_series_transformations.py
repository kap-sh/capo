"""Generated from Smithy shape ``com.amazonaws.sagemaker#TimeSeriesTransformations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.aggregation_transformations
    import capo_sagemaker.types.filling_transformations


class TimeSeriesTransformations(TypedDict, closed=True):
    filling: NotRequired[
        "capo_sagemaker.types.filling_transformations.FillingTransformations"
    ]
    """<p>A key value pair defining the filling method for a column, where the key is the column name and the value is an object which defines the filling logic. You can specify multiple filling methods for a single column.</p> <p>The supported filling methods and their corresponding options are:</p> <ul> <li> <p> <code>frontfill</code>: <code>none</code> (Supported only for target column)</p> </li> <li> <p> <code>middlefill</code>: <code>zero</code>, <code>value</code>, <code>median</code>, <code>mean</code>, <code>min</code>, <code>max</code> </p> </li> <li> <p> <code>backfill</code>: <code>zero</code>, <code>value</code>, <code>median</code>, <code>mean</code>, <code>min</code>, <code>max</code> </p> </li> <li> <p> <code>futurefill</code>: <code>zero</code>, <code>value</code>, <code>median</code>, <code>mean</code>, <code>min</code>, <code>max</code> </p> </li> </ul> <p>To set a filling method to a specific value, set the fill parameter to the chosen filling method value (for example <code>"backfill" : "value"</code>), and define the filling value in an additional parameter prefixed with "_value". For example, to set <code>backfill</code> to a value of <code>2</code>, you must include two parameters: <code>"backfill": "value"</code> and <code>"backfill_value":"2"</code>.</p>"""
    aggregation: NotRequired[
        "capo_sagemaker.types.aggregation_transformations.AggregationTransformations"
    ]
    """<p>A key value pair defining the aggregation method for a column, where the key is the column name and the value is the aggregation method.</p> <p>The supported aggregation methods are <code>sum</code> (default), <code>avg</code>, <code>first</code>, <code>min</code>, <code>max</code>.</p> <note> <p>Aggregation is only supported for the target column.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimeSeriesTransformations) -> dict:
    out: dict = {}
    if "filling" in value:
        import capo_sagemaker.types.filling_transformations

        out["Filling"] = (
            capo_sagemaker.types.filling_transformations.serialize_aws_json_1_1(
                value["filling"]
            )
        )
    if "aggregation" in value:
        import capo_sagemaker.types.aggregation_transformations

        out["Aggregation"] = (
            capo_sagemaker.types.aggregation_transformations.serialize_aws_json_1_1(
                value["aggregation"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TimeSeriesTransformations:
    out: TimeSeriesTransformations = {}  # type: ignore[typeddict-item]
    if data.get("Filling") is not None:
        import capo_sagemaker.types.filling_transformations

        out["filling"] = (
            capo_sagemaker.types.filling_transformations.deserialize_aws_json_1_1(
                data["Filling"]
            )
        )
    if data.get("Aggregation") is not None:
        import capo_sagemaker.types.aggregation_transformations

        out["aggregation"] = (
            capo_sagemaker.types.aggregation_transformations.deserialize_aws_json_1_1(
                data["Aggregation"]
            )
        )
    return out
