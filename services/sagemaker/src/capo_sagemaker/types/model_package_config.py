"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelPackageConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.model_package_arn
    import capo_sagemaker.types.model_package_group_arn


class ModelPackageConfig(TypedDict, closed=True):
    model_package_group_arn: (
        "capo_sagemaker.types.model_package_group_arn.ModelPackageGroupArn"
    )
    """<p> The Amazon Resource Name (ARN) of the model package group of output model package. </p>"""
    source_model_package_arn: NotRequired[
        "capo_sagemaker.types.model_package_arn.ModelPackageArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the source model package used for continued fine-tuning and custom model evaluation. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelPackageConfig) -> dict:
    out: dict = {}
    out["ModelPackageGroupArn"] = value["model_package_group_arn"]
    if "source_model_package_arn" in value:
        out["SourceModelPackageArn"] = value["source_model_package_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelPackageConfig:
    out: ModelPackageConfig = {}  # type: ignore[typeddict-item]
    if data.get("ModelPackageGroupArn") is not None:
        out["model_package_group_arn"] = data["ModelPackageGroupArn"]
    else:
        out["model_package_group_arn"] = ""
    if data.get("SourceModelPackageArn") is not None:
        out["source_model_package_arn"] = data["SourceModelPackageArn"]
    return out
