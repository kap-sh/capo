"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLContainerDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.container_image
    import capo_sagemaker.types.environment_map
    import capo_sagemaker.types.url


class AutoMLContainerDefinition(TypedDict, closed=True):
    image: NotRequired["capo_sagemaker.types.container_image.ContainerImage"]
    """<p>The Amazon Elastic Container Registry (Amazon ECR) path of the container. For more information, see <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ContainerDefinition.html"> ContainerDefinition</a>.</p>"""
    model_data_url: NotRequired["capo_sagemaker.types.url.Url"]
    """<p>The location of the model artifacts. For more information, see <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ContainerDefinition.html"> ContainerDefinition</a>.</p>"""
    environment: NotRequired["capo_sagemaker.types.environment_map.EnvironmentMap"]
    """<p>The environment variables to set in the container. For more information, see <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ContainerDefinition.html"> ContainerDefinition</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLContainerDefinition) -> dict:
    out: dict = {}
    if "image" in value:
        out["Image"] = value["image"]
    if "model_data_url" in value:
        out["ModelDataUrl"] = value["model_data_url"]
    if "environment" in value:
        import capo_sagemaker.types.environment_map

        out["Environment"] = (
            capo_sagemaker.types.environment_map.serialize_aws_json_1_1(
                value["environment"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoMLContainerDefinition:
    out: AutoMLContainerDefinition = {}  # type: ignore[typeddict-item]
    if data.get("Image") is not None:
        out["image"] = data["Image"]
    if data.get("ModelDataUrl") is not None:
        out["model_data_url"] = data["ModelDataUrl"]
    if data.get("Environment") is not None:
        import capo_sagemaker.types.environment_map

        out["environment"] = (
            capo_sagemaker.types.environment_map.deserialize_aws_json_1_1(
                data["Environment"]
            )
        )
    return out
