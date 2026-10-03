"""Generated from Smithy shape ``com.amazonaws.sagemaker#AlgorithmSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.algorithm_image
    import capo_sagemaker.types.arn_or_name
    import capo_sagemaker.types.boolean
    import capo_sagemaker.types.metric_definition_list
    import capo_sagemaker.types.training_container_arguments
    import capo_sagemaker.types.training_container_entrypoint
    import capo_sagemaker.types.training_image_config
    import capo_sagemaker.types.training_input_mode


class AlgorithmSpecification(TypedDict, closed=True):
    training_image: NotRequired["capo_sagemaker.types.algorithm_image.AlgorithmImage"]
    """<p>The registry path of the Docker image that contains the training algorithm. For information about docker registry paths for SageMaker built-in algorithms, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-algo-docker-registry-paths.html">Docker Registry Paths and Example Code</a> in the <i>Amazon SageMaker developer guide</i>. SageMaker supports both <code>registry/repository[:tag]</code> and <code>registry/repository[@digest]</code> image path formats. For more information about using your custom training container, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html">Using Your Own Algorithms with Amazon SageMaker</a>.</p> <note> <p>You must specify either the algorithm name to the <code>AlgorithmName</code> parameter or the image URI of the algorithm container to the <code>TrainingImage</code> parameter.</p> <p>For more information, see the note in the <code>AlgorithmName</code> parameter description.</p> </note>"""
    algorithm_name: NotRequired["capo_sagemaker.types.arn_or_name.ArnOrName"]
    """<p>The name of the algorithm resource to use for the training job. This must be an algorithm resource that you created or subscribe to on Amazon Web Services Marketplace.</p> <note> <p>You must specify either the algorithm name to the <code>AlgorithmName</code> parameter or the image URI of the algorithm container to the <code>TrainingImage</code> parameter.</p> <p>Note that the <code>AlgorithmName</code> parameter is mutually exclusive with the <code>TrainingImage</code> parameter. If you specify a value for the <code>AlgorithmName</code> parameter, you can't specify a value for <code>TrainingImage</code>, and vice versa.</p> <p>If you specify values for both parameters, the training job might break; if you don't specify any value for both parameters, the training job might raise a <code>null</code> error.</p> </note>"""
    training_input_mode: NotRequired[
        "capo_sagemaker.types.training_input_mode.TrainingInputMode"
    ]
    metric_definitions: NotRequired[
        "capo_sagemaker.types.metric_definition_list.MetricDefinitionList"
    ]
    """<p>A list of metric definition objects. Each object specifies the metric name and regular expressions used to parse algorithm logs. SageMaker publishes each metric to Amazon CloudWatch.</p>"""
    enable_sage_maker_metrics_time_series: NotRequired[
        "capo_sagemaker.types.boolean.Boolean"
    ]
    """<p>To generate and save time-series metrics during training, set to <code>true</code>. The default is <code>false</code> and time-series metrics aren't generated except in the following cases:</p> <ul> <li> <p>You use one of the SageMaker built-in algorithms</p> </li> <li> <p>You use one of the following <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/pre-built-containers-frameworks-deep-learning.html">Prebuilt SageMaker Docker Images</a>:</p> <ul> <li> <p>Tensorflow (version &gt;= 1.15)</p> </li> <li> <p>MXNet (version &gt;= 1.6)</p> </li> <li> <p>PyTorch (version &gt;= 1.3)</p> </li> </ul> </li> <li> <p>You specify at least one <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MetricDefinition.html">MetricDefinition</a> </p> </li> </ul>"""
    container_entrypoint: NotRequired[
        "capo_sagemaker.types.training_container_entrypoint.TrainingContainerEntrypoint"
    ]
    """<p>The <a href="https://docs.docker.com/engine/reference/builder/">entrypoint script for a Docker container</a> used to run a training job. This script takes precedence over the default train processing instructions. See <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-training-algo-dockerfile.html">How Amazon SageMaker Runs Your Training Image</a> for more information.</p>"""
    container_arguments: NotRequired[
        "capo_sagemaker.types.training_container_arguments.TrainingContainerArguments"
    ]
    """<p>The arguments for a container used to run a training job. See <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-training-algo-dockerfile.html">How Amazon SageMaker Runs Your Training Image</a> for additional information.</p>"""
    training_image_config: NotRequired[
        "capo_sagemaker.types.training_image_config.TrainingImageConfig"
    ]
    """<p>The configuration to use an image from a private Docker registry for a training job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AlgorithmSpecification) -> dict:
    out: dict = {}
    if "training_image" in value:
        out["TrainingImage"] = value["training_image"]
    if "algorithm_name" in value:
        out["AlgorithmName"] = value["algorithm_name"]
    if "training_input_mode" in value:
        import capo_sagemaker.types.training_input_mode

        out["TrainingInputMode"] = (
            capo_sagemaker.types.training_input_mode.serialize_aws_json_1_1(
                value["training_input_mode"]
            )
        )
    if "metric_definitions" in value:
        import capo_sagemaker.types.metric_definition_list

        out["MetricDefinitions"] = (
            capo_sagemaker.types.metric_definition_list.serialize_aws_json_1_1(
                value["metric_definitions"]
            )
        )
    if "enable_sage_maker_metrics_time_series" in value:
        out["EnableSageMakerMetricsTimeSeries"] = value[
            "enable_sage_maker_metrics_time_series"
        ]
    if "container_entrypoint" in value:
        import capo_sagemaker.types.training_container_entrypoint

        out["ContainerEntrypoint"] = (
            capo_sagemaker.types.training_container_entrypoint.serialize_aws_json_1_1(
                value["container_entrypoint"]
            )
        )
    if "container_arguments" in value:
        import capo_sagemaker.types.training_container_arguments

        out["ContainerArguments"] = (
            capo_sagemaker.types.training_container_arguments.serialize_aws_json_1_1(
                value["container_arguments"]
            )
        )
    if "training_image_config" in value:
        import capo_sagemaker.types.training_image_config

        out["TrainingImageConfig"] = (
            capo_sagemaker.types.training_image_config.serialize_aws_json_1_1(
                value["training_image_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AlgorithmSpecification:
    out: AlgorithmSpecification = {}  # type: ignore[typeddict-item]
    if data.get("TrainingImage") is not None:
        out["training_image"] = data["TrainingImage"]
    if data.get("AlgorithmName") is not None:
        out["algorithm_name"] = data["AlgorithmName"]
    if data.get("TrainingInputMode") is not None:
        import capo_sagemaker.types.training_input_mode

        out["training_input_mode"] = (
            capo_sagemaker.types.training_input_mode.deserialize_aws_json_1_1(
                data["TrainingInputMode"]
            )
        )
    if data.get("MetricDefinitions") is not None:
        import capo_sagemaker.types.metric_definition_list

        out["metric_definitions"] = (
            capo_sagemaker.types.metric_definition_list.deserialize_aws_json_1_1(
                data["MetricDefinitions"]
            )
        )
    if data.get("EnableSageMakerMetricsTimeSeries") is not None:
        out["enable_sage_maker_metrics_time_series"] = data[
            "EnableSageMakerMetricsTimeSeries"
        ]
    if data.get("ContainerEntrypoint") is not None:
        import capo_sagemaker.types.training_container_entrypoint

        out["container_entrypoint"] = (
            capo_sagemaker.types.training_container_entrypoint.deserialize_aws_json_1_1(
                data["ContainerEntrypoint"]
            )
        )
    if data.get("ContainerArguments") is not None:
        import capo_sagemaker.types.training_container_arguments

        out["container_arguments"] = (
            capo_sagemaker.types.training_container_arguments.deserialize_aws_json_1_1(
                data["ContainerArguments"]
            )
        )
    if data.get("TrainingImageConfig") is not None:
        import capo_sagemaker.types.training_image_config

        out["training_image_config"] = (
            capo_sagemaker.types.training_image_config.deserialize_aws_json_1_1(
                data["TrainingImageConfig"]
            )
        )
    return out
