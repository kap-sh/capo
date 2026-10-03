"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceComponentStartupParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.production_variant_container_startup_health_check_timeout_in_seconds
    import capo_sagemaker.types.production_variant_model_data_download_timeout_in_seconds


class InferenceComponentStartupParameters(TypedDict, closed=True):
    model_data_download_timeout_in_seconds: NotRequired[
        "capo_sagemaker.types.production_variant_model_data_download_timeout_in_seconds.ProductionVariantModelDataDownloadTimeoutInSeconds"
    ]
    """<p>The timeout value, in seconds, to download and extract the model that you want to host from Amazon S3 to the individual inference instance associated with this inference component.</p>"""
    container_startup_health_check_timeout_in_seconds: NotRequired[
        "capo_sagemaker.types.production_variant_container_startup_health_check_timeout_in_seconds.ProductionVariantContainerStartupHealthCheckTimeoutInSeconds"
    ]
    """<p>The timeout value, in seconds, for your inference container to pass health check by Amazon S3 Hosting. For more information about health check, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-inference-code.html#your-algorithms-inference-algo-ping-requests">How Your Container Should Respond to Health Check (Ping) Requests</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceComponentStartupParameters) -> dict:
    out: dict = {}
    if "model_data_download_timeout_in_seconds" in value:
        out["ModelDataDownloadTimeoutInSeconds"] = value[
            "model_data_download_timeout_in_seconds"
        ]
    if "container_startup_health_check_timeout_in_seconds" in value:
        out["ContainerStartupHealthCheckTimeoutInSeconds"] = value[
            "container_startup_health_check_timeout_in_seconds"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> InferenceComponentStartupParameters:
    out: InferenceComponentStartupParameters = {}  # type: ignore[typeddict-item]
    if data.get("ModelDataDownloadTimeoutInSeconds") is not None:
        out["model_data_download_timeout_in_seconds"] = data[
            "ModelDataDownloadTimeoutInSeconds"
        ]
    if data.get("ContainerStartupHealthCheckTimeoutInSeconds") is not None:
        out["container_startup_health_check_timeout_in_seconds"] = data[
            "ContainerStartupHealthCheckTimeoutInSeconds"
        ]
    return out
