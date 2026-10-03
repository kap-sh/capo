"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ContainerConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanroomsml.types.algorithm_image
    import capo_cleanroomsml.types.container_arguments
    import capo_cleanroomsml.types.container_entrypoint
    import capo_cleanroomsml.types.metric_definition_list


class ContainerConfig(TypedDict, closed=True):
    image_uri: "capo_cleanroomsml.types.algorithm_image.AlgorithmImage"
    """<p>The registry path of the docker image that contains the algorithm. Clean Rooms ML currently only supports the <code>registry/repository[:tag]</code> image path format. For more information about using images in Clean Rooms ML, see the <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AlgorithmSpecification.html#sagemaker-Type-AlgorithmSpecification-TrainingImage">Sagemaker API reference</a>.</p>"""
    entrypoint: NotRequired[
        "capo_cleanroomsml.types.container_entrypoint.ContainerEntrypoint"
    ]
    """<p>The entrypoint script for a Docker container used to run a training job. This script takes precedence over the default train processing instructions. See How Amazon SageMaker Runs Your Training Image for additional information. For more information, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-training-algo-dockerfile.html">How Sagemaker runs your training image</a>.</p>"""
    arguments: NotRequired[
        "capo_cleanroomsml.types.container_arguments.ContainerArguments"
    ]
    """<p>The arguments for a container used to run a training job. See How Amazon SageMaker Runs Your Training Image for additional information. For more information, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-training-algo-dockerfile.html">How Sagemaker runs your training image</a>.</p>"""
    metric_definitions: NotRequired[
        "capo_cleanroomsml.types.metric_definition_list.MetricDefinitionList"
    ]
    """<p>A list of metric definition objects. Each object specifies the metric name and regular expressions used to parse algorithm logs. Amazon Web Services Clean Rooms ML publishes each metric to all members' Amazon CloudWatch using IAM role configured in <a>PutMLConfiguration</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContainerConfig) -> dict:
    out: dict = {}
    out["imageUri"] = value["image_uri"]
    if "entrypoint" in value:
        import capo_cleanroomsml.types.container_entrypoint

        out["entrypoint"] = capo_cleanroomsml.types.container_entrypoint.serialize_json(
            value["entrypoint"]
        )
    if "arguments" in value:
        import capo_cleanroomsml.types.container_arguments

        out["arguments"] = capo_cleanroomsml.types.container_arguments.serialize_json(
            value["arguments"]
        )
    if "metric_definitions" in value:
        import capo_cleanroomsml.types.metric_definition_list

        out["metricDefinitions"] = (
            capo_cleanroomsml.types.metric_definition_list.serialize_json(
                value["metric_definitions"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContainerConfig:
    out: ContainerConfig = {}  # type: ignore[typeddict-item]
    if data.get("imageUri") is not None:
        out["image_uri"] = data["imageUri"]
    else:
        raise DeserializationError("ContainerConfig.image_uri required")
    if data.get("entrypoint") is not None:
        import capo_cleanroomsml.types.container_entrypoint

        out["entrypoint"] = (
            capo_cleanroomsml.types.container_entrypoint.deserialize_json(
                data["entrypoint"]
            )
        )
    if data.get("arguments") is not None:
        import capo_cleanroomsml.types.container_arguments

        out["arguments"] = capo_cleanroomsml.types.container_arguments.deserialize_json(
            data["arguments"]
        )
    if data.get("metricDefinitions") is not None:
        import capo_cleanroomsml.types.metric_definition_list

        out["metric_definitions"] = (
            capo_cleanroomsml.types.metric_definition_list.deserialize_json(
                data["metricDefinitions"]
            )
        )
    return out
