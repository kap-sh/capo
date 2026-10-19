"""Generated from Smithy shape ``com.amazonaws.personalize#CreateMetricAttributionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.metric_attributes
    import capo_personalize.types.metric_attribution_output
    import capo_personalize.types.name


class CreateMetricAttributionRequest(TypedDict, closed=True):
    name: "capo_personalize.types.name.Name"
    """<p>A name for the metric attribution.</p>"""
    dataset_group_arn: "capo_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the destination dataset group for the metric attribution.</p>"""
    metrics: "capo_personalize.types.metric_attributes.MetricAttributes"
    """<p>A list of metric attributes for the metric attribution. Each metric attribute specifies an event type to track and a function. Available functions are <code>SUM()</code> or <code>SAMPLECOUNT()</code>. For SUM() functions, provide the dataset type (either Interactions or Items) and column to sum as a parameter. For example SUM(Items.PRICE).</p>"""
    metrics_output_config: (
        "capo_personalize.types.metric_attribution_output.MetricAttributionOutput"
    )
    """<p>The output configuration details for the metric attribution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateMetricAttributionRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["datasetGroupArn"] = value["dataset_group_arn"]
    import capo_personalize.types.metric_attributes

    out["metrics"] = capo_personalize.types.metric_attributes.serialize_aws_json_1_1(
        value["metrics"]
    )
    import capo_personalize.types.metric_attribution_output

    out["metricsOutputConfig"] = (
        capo_personalize.types.metric_attribution_output.serialize_aws_json_1_1(
            value["metrics_output_config"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateMetricAttributionRequest:
    out: CreateMetricAttributionRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("datasetGroupArn") is not None:
        out["dataset_group_arn"] = data["datasetGroupArn"]
    else:
        out["dataset_group_arn"] = ""
    if data.get("metrics") is not None:
        import capo_personalize.types.metric_attributes

        out["metrics"] = (
            capo_personalize.types.metric_attributes.deserialize_aws_json_1_1(
                data["metrics"]
            )
        )
    else:
        out["metrics"] = []
    if data.get("metricsOutputConfig") is not None:
        import capo_personalize.types.metric_attribution_output

        out["metrics_output_config"] = (
            capo_personalize.types.metric_attribution_output.deserialize_aws_json_1_1(
                data["metricsOutputConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreateMetricAttributionRequest.metrics_output_config required"
        )
    return out
