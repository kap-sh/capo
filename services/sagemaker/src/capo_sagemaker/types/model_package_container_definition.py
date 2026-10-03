"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelPackageContainerDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.additional_model_data_sources
    import capo_sagemaker.types.additional_s3_data_source
    import capo_sagemaker.types.base_model
    import capo_sagemaker.types.boolean
    import capo_sagemaker.types.container_hostname
    import capo_sagemaker.types.container_image
    import capo_sagemaker.types.environment_map
    import capo_sagemaker.types.image_digest
    import capo_sagemaker.types.model_data_source
    import capo_sagemaker.types.model_input
    import capo_sagemaker.types.model_package_framework_version
    import capo_sagemaker.types.product_id
    import capo_sagemaker.types.string
    import capo_sagemaker.types.url


class ModelPackageContainerDefinition(TypedDict, closed=True):
    container_hostname: NotRequired[
        "capo_sagemaker.types.container_hostname.ContainerHostname"
    ]
    """<p>The DNS host name for the Docker container.</p>"""
    image: NotRequired["capo_sagemaker.types.container_image.ContainerImage"]
    """<p>The Amazon Elastic Container Registry (Amazon ECR) path where inference code is stored.</p> <p>If you are using your own custom algorithm instead of an algorithm provided by SageMaker, the inference code must meet SageMaker requirements. SageMaker supports both <code>registry/repository[:tag]</code> and <code>registry/repository[@digest]</code> image path formats. For more information, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html">Using Your Own Algorithms with Amazon SageMaker</a>.</p>"""
    image_digest: NotRequired["capo_sagemaker.types.image_digest.ImageDigest"]
    """<p>An MD5 hash of the training algorithm that identifies the Docker image used for training.</p>"""
    model_data_url: NotRequired["capo_sagemaker.types.url.Url"]
    """<p>The Amazon S3 path where the model artifacts, which result from model training, are stored. This path must point to a single <code>gzip</code> compressed tar archive (<code>.tar.gz</code> suffix).</p> <note> <p>The model artifacts must be in an S3 bucket that is in the same region as the model package.</p> </note>"""
    model_data_source: NotRequired[
        "capo_sagemaker.types.model_data_source.ModelDataSource"
    ]
    """<p>Specifies the location of ML model data to deploy during endpoint creation.</p>"""
    product_id: NotRequired["capo_sagemaker.types.product_id.ProductId"]
    """<p>The Amazon Web Services Marketplace product ID of the model package.</p>"""
    environment: NotRequired["capo_sagemaker.types.environment_map.EnvironmentMap"]
    """<p>The environment variables to set in the Docker container. Each key and value in the <code>Environment</code> string to string map can have length of up to 1024. We support up to 16 entries in the map.</p>"""
    model_input: NotRequired["capo_sagemaker.types.model_input.ModelInput"]
    """<p>A structure with Model Input details.</p>"""
    framework: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The machine learning framework of the model package container image.</p>"""
    framework_version: NotRequired[
        "capo_sagemaker.types.model_package_framework_version.ModelPackageFrameworkVersion"
    ]
    """<p>The framework version of the Model Package Container Image.</p>"""
    nearest_model_name: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The name of a pre-trained machine learning benchmarked by Amazon SageMaker Inference Recommender model that matches your model. You can find a list of benchmarked models by calling <code>ListModelMetadata</code>.</p>"""
    additional_model_data_sources: NotRequired[
        "capo_sagemaker.types.additional_model_data_sources.AdditionalModelDataSources"
    ]
    """<p>Data sources that are available to your model in addition to the one that you specify for <code>ModelDataSource</code> when you use the <code>CreateModelPackage</code> action.</p>"""
    additional_s3_data_source: NotRequired[
        "capo_sagemaker.types.additional_s3_data_source.AdditionalS3DataSource"
    ]
    """<p>The additional data source that is used during inference in the Docker container for your model package.</p>"""
    model_data_e_tag: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The ETag associated with Model Data URL.</p>"""
    is_checkpoint: NotRequired["capo_sagemaker.types.boolean.Boolean"]
    """<p> Specifies whether the model data is a training checkpoint. </p>"""
    base_model: NotRequired["capo_sagemaker.types.base_model.BaseModel"]
    """<p> Identifies the foundation model that was used as the starting point for model customization. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelPackageContainerDefinition) -> dict:
    out: dict = {}
    if "container_hostname" in value:
        out["ContainerHostname"] = value["container_hostname"]
    if "image" in value:
        out["Image"] = value["image"]
    if "image_digest" in value:
        out["ImageDigest"] = value["image_digest"]
    if "model_data_url" in value:
        out["ModelDataUrl"] = value["model_data_url"]
    if "model_data_source" in value:
        import capo_sagemaker.types.model_data_source

        out["ModelDataSource"] = (
            capo_sagemaker.types.model_data_source.serialize_aws_json_1_1(
                value["model_data_source"]
            )
        )
    if "product_id" in value:
        out["ProductId"] = value["product_id"]
    if "environment" in value:
        import capo_sagemaker.types.environment_map

        out["Environment"] = (
            capo_sagemaker.types.environment_map.serialize_aws_json_1_1(
                value["environment"]
            )
        )
    if "model_input" in value:
        import capo_sagemaker.types.model_input

        out["ModelInput"] = capo_sagemaker.types.model_input.serialize_aws_json_1_1(
            value["model_input"]
        )
    if "framework" in value:
        out["Framework"] = value["framework"]
    if "framework_version" in value:
        out["FrameworkVersion"] = value["framework_version"]
    if "nearest_model_name" in value:
        out["NearestModelName"] = value["nearest_model_name"]
    if "additional_model_data_sources" in value:
        import capo_sagemaker.types.additional_model_data_sources

        out["AdditionalModelDataSources"] = (
            capo_sagemaker.types.additional_model_data_sources.serialize_aws_json_1_1(
                value["additional_model_data_sources"]
            )
        )
    if "additional_s3_data_source" in value:
        import capo_sagemaker.types.additional_s3_data_source

        out["AdditionalS3DataSource"] = (
            capo_sagemaker.types.additional_s3_data_source.serialize_aws_json_1_1(
                value["additional_s3_data_source"]
            )
        )
    if "model_data_e_tag" in value:
        out["ModelDataETag"] = value["model_data_e_tag"]
    if "is_checkpoint" in value:
        out["IsCheckpoint"] = value["is_checkpoint"]
    if "base_model" in value:
        import capo_sagemaker.types.base_model

        out["BaseModel"] = capo_sagemaker.types.base_model.serialize_aws_json_1_1(
            value["base_model"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelPackageContainerDefinition:
    out: ModelPackageContainerDefinition = {}  # type: ignore[typeddict-item]
    if data.get("ContainerHostname") is not None:
        out["container_hostname"] = data["ContainerHostname"]
    if data.get("Image") is not None:
        out["image"] = data["Image"]
    if data.get("ImageDigest") is not None:
        out["image_digest"] = data["ImageDigest"]
    if data.get("ModelDataUrl") is not None:
        out["model_data_url"] = data["ModelDataUrl"]
    if data.get("ModelDataSource") is not None:
        import capo_sagemaker.types.model_data_source

        out["model_data_source"] = (
            capo_sagemaker.types.model_data_source.deserialize_aws_json_1_1(
                data["ModelDataSource"]
            )
        )
    if data.get("ProductId") is not None:
        out["product_id"] = data["ProductId"]
    if data.get("Environment") is not None:
        import capo_sagemaker.types.environment_map

        out["environment"] = (
            capo_sagemaker.types.environment_map.deserialize_aws_json_1_1(
                data["Environment"]
            )
        )
    if data.get("ModelInput") is not None:
        import capo_sagemaker.types.model_input

        out["model_input"] = capo_sagemaker.types.model_input.deserialize_aws_json_1_1(
            data["ModelInput"]
        )
    if data.get("Framework") is not None:
        out["framework"] = data["Framework"]
    if data.get("FrameworkVersion") is not None:
        out["framework_version"] = data["FrameworkVersion"]
    if data.get("NearestModelName") is not None:
        out["nearest_model_name"] = data["NearestModelName"]
    if data.get("AdditionalModelDataSources") is not None:
        import capo_sagemaker.types.additional_model_data_sources

        out["additional_model_data_sources"] = (
            capo_sagemaker.types.additional_model_data_sources.deserialize_aws_json_1_1(
                data["AdditionalModelDataSources"]
            )
        )
    if data.get("AdditionalS3DataSource") is not None:
        import capo_sagemaker.types.additional_s3_data_source

        out["additional_s3_data_source"] = (
            capo_sagemaker.types.additional_s3_data_source.deserialize_aws_json_1_1(
                data["AdditionalS3DataSource"]
            )
        )
    if data.get("ModelDataETag") is not None:
        out["model_data_e_tag"] = data["ModelDataETag"]
    if data.get("IsCheckpoint") is not None:
        out["is_checkpoint"] = data["IsCheckpoint"]
    if data.get("BaseModel") is not None:
        import capo_sagemaker.types.base_model

        out["base_model"] = capo_sagemaker.types.base_model.deserialize_aws_json_1_1(
            data["BaseModel"]
        )
    return out
