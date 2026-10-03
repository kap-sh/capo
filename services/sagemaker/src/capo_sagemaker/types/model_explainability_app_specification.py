"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelExplainabilityAppSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.image_uri
    import capo_sagemaker.types.monitoring_environment_map
    import capo_sagemaker.types.s3_uri


class ModelExplainabilityAppSpecification(TypedDict, closed=True):
    image_uri: NotRequired["capo_sagemaker.types.image_uri.ImageUri"]
    """<p>The container image to be run by the model explainability job.</p>"""
    config_uri: NotRequired["capo_sagemaker.types.s3_uri.S3Uri"]
    """<p>JSON formatted Amazon S3 file that defines explainability parameters. For more information on this JSON configuration file, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-config-json-monitor-model-explainability-parameters.html">Configure model explainability parameters</a>.</p>"""
    environment: NotRequired[
        "capo_sagemaker.types.monitoring_environment_map.MonitoringEnvironmentMap"
    ]
    """<p>Sets the environment variables in the Docker container.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelExplainabilityAppSpecification) -> dict:
    out: dict = {}
    if "image_uri" in value:
        out["ImageUri"] = value["image_uri"]
    if "config_uri" in value:
        out["ConfigUri"] = value["config_uri"]
    if "environment" in value:
        import capo_sagemaker.types.monitoring_environment_map

        out["Environment"] = (
            capo_sagemaker.types.monitoring_environment_map.serialize_aws_json_1_1(
                value["environment"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelExplainabilityAppSpecification:
    out: ModelExplainabilityAppSpecification = {}  # type: ignore[typeddict-item]
    if data.get("ImageUri") is not None:
        out["image_uri"] = data["ImageUri"]
    if data.get("ConfigUri") is not None:
        out["config_uri"] = data["ConfigUri"]
    if data.get("Environment") is not None:
        import capo_sagemaker.types.monitoring_environment_map

        out["environment"] = (
            capo_sagemaker.types.monitoring_environment_map.deserialize_aws_json_1_1(
                data["Environment"]
            )
        )
    return out
