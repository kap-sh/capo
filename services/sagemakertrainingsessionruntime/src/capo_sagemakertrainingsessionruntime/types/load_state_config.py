"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#LoadStateConfig``."""

from typing_extensions import TypedDict


class LoadStateConfig(TypedDict, closed=True):
    model_package_arn: "str"
    """<p>The ARN of the model package containing the checkpoint to load. Must be a valid SageMaker model package ARN in the format <code>arn:aws:sagemaker:REGION:ACCOUNT:model-package/PACKAGE_NAME/VERSION</code>. Model package group ARNs are not accepted.</p>"""
    load_optimizer: "bool"
    """<p>Specifies whether to also restore the optimizer state alongside model weights. When true, optimizer state is restored to resume training from where it left off.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoadStateConfig) -> dict:
    out: dict = {}
    out["modelPackageArn"] = value["model_package_arn"]
    out["loadOptimizer"] = value["load_optimizer"]
    return out


def deserialize_json(data: dict) -> LoadStateConfig:
    out: LoadStateConfig = {}  # type: ignore[typeddict-item]
    if data.get("modelPackageArn") is not None:
        out["model_package_arn"] = data["modelPackageArn"]
    else:
        out["model_package_arn"] = ""
    if data.get("loadOptimizer") is not None:
        out["load_optimizer"] = data["loadOptimizer"]
    else:
        out["load_optimizer"] = False
    return out
