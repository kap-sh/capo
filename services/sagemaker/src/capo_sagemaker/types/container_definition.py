"""Generated from Smithy shape ``com.amazonaws.sagemaker#ContainerDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.additional_model_data_sources
    import capo_sagemaker.types.container_hostname
    import capo_sagemaker.types.container_image
    import capo_sagemaker.types.container_metrics_config
    import capo_sagemaker.types.container_mode
    import capo_sagemaker.types.environment_map
    import capo_sagemaker.types.image_config
    import capo_sagemaker.types.inference_specification_name
    import capo_sagemaker.types.model_data_source
    import capo_sagemaker.types.multi_model_config
    import capo_sagemaker.types.url
    import capo_sagemaker.types.versioned_arn_or_name


class ContainerDefinition(TypedDict, closed=True):
    container_hostname: NotRequired[
        "capo_sagemaker.types.container_hostname.ContainerHostname"
    ]
    """<p>This parameter is ignored for models that contain only a <code>PrimaryContainer</code>.</p> <p>When a <code>ContainerDefinition</code> is part of an inference pipeline, the value of the parameter uniquely identifies the container for the purposes of logging and metrics. For information, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/inference-pipeline-logs-metrics.html">Use Logs and Metrics to Monitor an Inference Pipeline</a>. If you don't specify a value for this parameter for a <code>ContainerDefinition</code> that is part of an inference pipeline, a unique name is automatically assigned based on the position of the <code>ContainerDefinition</code> in the pipeline. If you specify a value for the <code>ContainerHostName</code> for any <code>ContainerDefinition</code> that is part of an inference pipeline, you must specify a value for the <code>ContainerHostName</code> parameter of every <code>ContainerDefinition</code> in that pipeline.</p>"""
    image: NotRequired["capo_sagemaker.types.container_image.ContainerImage"]
    """<p>The path where inference code is stored. This can be either in Amazon EC2 Container Registry or in a Docker registry that is accessible from the same VPC that you configure for your endpoint. If you are using your own custom algorithm instead of an algorithm provided by SageMaker, the inference code must meet SageMaker requirements. SageMaker supports both <code>registry/repository[:tag]</code> and <code>registry/repository[@digest]</code> image path formats. For more information, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html">Using Your Own Algorithms with Amazon SageMaker</a>. </p> <note> <p>The model artifacts in an Amazon S3 bucket and the Docker image for inference container in Amazon EC2 Container Registry must be in the same region as the model or endpoint you are creating.</p> </note>"""
    image_config: NotRequired["capo_sagemaker.types.image_config.ImageConfig"]
    """<p>Specifies whether the model container is in Amazon ECR or a private Docker registry accessible from your Amazon Virtual Private Cloud (VPC). For information about storing containers in a private Docker registry, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-containers-inference-private.html">Use a Private Docker Registry for Real-Time Inference Containers</a>. </p> <note> <p>The model artifacts in an Amazon S3 bucket and the Docker image for inference container in Amazon EC2 Container Registry must be in the same region as the model or endpoint you are creating.</p> </note>"""
    mode: NotRequired["capo_sagemaker.types.container_mode.ContainerMode"]
    """<p>Whether the container hosts a single model or multiple models.</p>"""
    model_data_url: NotRequired["capo_sagemaker.types.url.Url"]
    """<p>The S3 path where the model artifacts, which result from model training, are stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix). The S3 path is required for SageMaker built-in algorithms, but not if you use your own algorithms. For more information on built-in algorithms, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-algo-docker-registry-paths.html">Common Parameters</a>. </p> <note> <p>The model artifacts must be in an S3 bucket that is in the same region as the model or endpoint you are creating.</p> </note> <p>If you provide a value for this parameter, SageMaker uses Amazon Web Services Security Token Service to download model artifacts from the S3 path you provide. Amazon Web Services STS is activated in your Amazon Web Services account by default. If you previously deactivated Amazon Web Services STS for a region, you need to reactivate Amazon Web Services STS for that region. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html">Activating and Deactivating Amazon Web Services STS in an Amazon Web Services Region</a> in the <i>Amazon Web Services Identity and Access Management User Guide</i>.</p> <important> <p>If you use a built-in algorithm to create a model, SageMaker requires that you provide a S3 path to the model artifacts in <code>ModelDataUrl</code>.</p> </important>"""
    model_data_source: NotRequired[
        "capo_sagemaker.types.model_data_source.ModelDataSource"
    ]
    """<p>Specifies the location of ML model data to deploy.</p> <note> <p>Currently you cannot use <code>ModelDataSource</code> in conjunction with SageMaker batch transform, SageMaker serverless endpoints, SageMaker multi-model endpoints, and SageMaker Marketplace.</p> </note>"""
    additional_model_data_sources: NotRequired[
        "capo_sagemaker.types.additional_model_data_sources.AdditionalModelDataSources"
    ]
    """<p>Data sources that are available to your model in addition to the one that you specify for <code>ModelDataSource</code> when you use the <code>CreateModel</code> action.</p>"""
    environment: NotRequired["capo_sagemaker.types.environment_map.EnvironmentMap"]
    """<p>The environment variables to set in the Docker container. Don't include any sensitive data in your environment variables.</p> <p>The maximum length of each key and value in the <code>Environment</code> map is 1024 bytes. The maximum length of all keys and values in the map, combined, is 32 KB. If you pass multiple containers to a <code>CreateModel</code> request, then the maximum length of all of their maps, combined, is also 32 KB.</p>"""
    model_package_name: NotRequired[
        "capo_sagemaker.types.versioned_arn_or_name.VersionedArnOrName"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the model package to use to create the model.</p>"""
    inference_specification_name: NotRequired[
        "capo_sagemaker.types.inference_specification_name.InferenceSpecificationName"
    ]
    """<p>The inference specification name in the model package version.</p>"""
    multi_model_config: NotRequired[
        "capo_sagemaker.types.multi_model_config.MultiModelConfig"
    ]
    """<p>Specifies additional configuration for multi-model endpoints.</p>"""
    container_metrics_config: NotRequired[
        "capo_sagemaker.types.container_metrics_config.ContainerMetricsConfig"
    ]
    """<p>The configuration for container metrics scraping. Specifies the metrics endpoint path and publishing frequency. If not specified when <code>EnableDetailedObservability</code> is <code>True</code>, the default path <code>/metrics</code> on port <code>8080</code> is used. For first-party and Deep Learning Containers (DLC), the endpoint path is determined automatically and this configuration is optional.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerDefinition) -> dict:
    out: dict = {}
    if "container_hostname" in value:
        out["ContainerHostname"] = value["container_hostname"]
    if "image" in value:
        out["Image"] = value["image"]
    if "image_config" in value:
        import capo_sagemaker.types.image_config

        out["ImageConfig"] = capo_sagemaker.types.image_config.serialize_aws_json_1_1(
            value["image_config"]
        )
    if "mode" in value:
        import capo_sagemaker.types.container_mode

        out["Mode"] = capo_sagemaker.types.container_mode.serialize_aws_json_1_1(
            value["mode"]
        )
    if "model_data_url" in value:
        out["ModelDataUrl"] = value["model_data_url"]
    if "model_data_source" in value:
        import capo_sagemaker.types.model_data_source

        out["ModelDataSource"] = (
            capo_sagemaker.types.model_data_source.serialize_aws_json_1_1(
                value["model_data_source"]
            )
        )
    if "additional_model_data_sources" in value:
        import capo_sagemaker.types.additional_model_data_sources

        out["AdditionalModelDataSources"] = (
            capo_sagemaker.types.additional_model_data_sources.serialize_aws_json_1_1(
                value["additional_model_data_sources"]
            )
        )
    if "environment" in value:
        import capo_sagemaker.types.environment_map

        out["Environment"] = (
            capo_sagemaker.types.environment_map.serialize_aws_json_1_1(
                value["environment"]
            )
        )
    if "model_package_name" in value:
        out["ModelPackageName"] = value["model_package_name"]
    if "inference_specification_name" in value:
        out["InferenceSpecificationName"] = value["inference_specification_name"]
    if "multi_model_config" in value:
        import capo_sagemaker.types.multi_model_config

        out["MultiModelConfig"] = (
            capo_sagemaker.types.multi_model_config.serialize_aws_json_1_1(
                value["multi_model_config"]
            )
        )
    if "container_metrics_config" in value:
        import capo_sagemaker.types.container_metrics_config

        out["ContainerMetricsConfig"] = (
            capo_sagemaker.types.container_metrics_config.serialize_aws_json_1_1(
                value["container_metrics_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerDefinition:
    out: ContainerDefinition = {}  # type: ignore[typeddict-item]
    if data.get("ContainerHostname") is not None:
        out["container_hostname"] = data["ContainerHostname"]
    if data.get("Image") is not None:
        out["image"] = data["Image"]
    if data.get("ImageConfig") is not None:
        import capo_sagemaker.types.image_config

        out["image_config"] = (
            capo_sagemaker.types.image_config.deserialize_aws_json_1_1(
                data["ImageConfig"]
            )
        )
    if data.get("Mode") is not None:
        import capo_sagemaker.types.container_mode

        out["mode"] = capo_sagemaker.types.container_mode.deserialize_aws_json_1_1(
            data["Mode"]
        )
    if data.get("ModelDataUrl") is not None:
        out["model_data_url"] = data["ModelDataUrl"]
    if data.get("ModelDataSource") is not None:
        import capo_sagemaker.types.model_data_source

        out["model_data_source"] = (
            capo_sagemaker.types.model_data_source.deserialize_aws_json_1_1(
                data["ModelDataSource"]
            )
        )
    if data.get("AdditionalModelDataSources") is not None:
        import capo_sagemaker.types.additional_model_data_sources

        out["additional_model_data_sources"] = (
            capo_sagemaker.types.additional_model_data_sources.deserialize_aws_json_1_1(
                data["AdditionalModelDataSources"]
            )
        )
    if data.get("Environment") is not None:
        import capo_sagemaker.types.environment_map

        out["environment"] = (
            capo_sagemaker.types.environment_map.deserialize_aws_json_1_1(
                data["Environment"]
            )
        )
    if data.get("ModelPackageName") is not None:
        out["model_package_name"] = data["ModelPackageName"]
    if data.get("InferenceSpecificationName") is not None:
        out["inference_specification_name"] = data["InferenceSpecificationName"]
    if data.get("MultiModelConfig") is not None:
        import capo_sagemaker.types.multi_model_config

        out["multi_model_config"] = (
            capo_sagemaker.types.multi_model_config.deserialize_aws_json_1_1(
                data["MultiModelConfig"]
            )
        )
    if data.get("ContainerMetricsConfig") is not None:
        import capo_sagemaker.types.container_metrics_config

        out["container_metrics_config"] = (
            capo_sagemaker.types.container_metrics_config.deserialize_aws_json_1_1(
                data["ContainerMetricsConfig"]
            )
        )
    return out
