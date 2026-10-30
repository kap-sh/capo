"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#LoadWeightsForSamplingConfig``."""

from typing_extensions import TypedDict


class LoadWeightsForSamplingConfig(TypedDict, closed=True):
    model_package_arn: "str"
    """<p>The ARN of the model package containing the weights to load for sampling. Must be a valid SageMaker model package ARN in the format <code>arn:aws:sagemaker:REGION:ACCOUNT:model-package/PACKAGE_NAME/VERSION</code>. The model package must belong to the same AWS account as the training session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoadWeightsForSamplingConfig) -> dict:
    out: dict = {}
    out["modelPackageArn"] = value["model_package_arn"]
    return out


def deserialize_json(data: dict) -> LoadWeightsForSamplingConfig:
    out: LoadWeightsForSamplingConfig = {}  # type: ignore[typeddict-item]
    if data.get("modelPackageArn") is not None:
        out["model_package_arn"] = data["modelPackageArn"]
    else:
        out["model_package_arn"] = ""
    return out
