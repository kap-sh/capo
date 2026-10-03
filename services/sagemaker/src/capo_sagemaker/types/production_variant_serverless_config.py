"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProductionVariantServerlessConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.serverless_max_concurrency
    import capo_sagemaker.types.serverless_memory_size_in_mb
    import capo_sagemaker.types.serverless_provisioned_concurrency


class ProductionVariantServerlessConfig(TypedDict, closed=True):
    memory_size_in_mb: NotRequired[
        "capo_sagemaker.types.serverless_memory_size_in_mb.ServerlessMemorySizeInMB"
    ]
    """<p>The memory size of your serverless endpoint. Valid values are in 1 GB increments: 1024 MB, 2048 MB, 3072 MB, 4096 MB, 5120 MB, or 6144 MB.</p>"""
    max_concurrency: NotRequired[
        "capo_sagemaker.types.serverless_max_concurrency.ServerlessMaxConcurrency"
    ]
    """<p>The maximum number of concurrent invocations your serverless endpoint can process.</p>"""
    provisioned_concurrency: NotRequired[
        "capo_sagemaker.types.serverless_provisioned_concurrency.ServerlessProvisionedConcurrency"
    ]
    """<p>The amount of provisioned concurrency to allocate for the serverless endpoint. Should be less than or equal to <code>MaxConcurrency</code>.</p> <note> <p>This field is not supported for serverless endpoint recommendations for Inference Recommender jobs. For more information about creating an Inference Recommender job, see <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceRecommendationsJob.html">CreateInferenceRecommendationsJobs</a>.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductionVariantServerlessConfig) -> dict:
    out: dict = {}
    if "memory_size_in_mb" in value:
        out["MemorySizeInMB"] = value["memory_size_in_mb"]
    if "max_concurrency" in value:
        out["MaxConcurrency"] = value["max_concurrency"]
    if "provisioned_concurrency" in value:
        out["ProvisionedConcurrency"] = value["provisioned_concurrency"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProductionVariantServerlessConfig:
    out: ProductionVariantServerlessConfig = {}  # type: ignore[typeddict-item]
    if data.get("MemorySizeInMB") is not None:
        out["memory_size_in_mb"] = data["MemorySizeInMB"]
    if data.get("MaxConcurrency") is not None:
        out["max_concurrency"] = data["MaxConcurrency"]
    if data.get("ProvisionedConcurrency") is not None:
        out["provisioned_concurrency"] = data["ProvisionedConcurrency"]
    return out
