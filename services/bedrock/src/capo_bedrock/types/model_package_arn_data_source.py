"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelPackageArnDataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.model_package_arn


class ModelPackageArnDataSource(TypedDict, closed=True):
    model_package_arn: "capo_bedrock.types.model_package_arn.ModelPackageArn"
    """<p>The Amazon Resource Name (ARN) of the SageMaker AI model package. The ARN must be for a model package of <code>restricted</code> type.</p> <p>To use a model package ARN, you must have the <code>sagemaker:DescribeModelPackage</code> and <code>sagemaker:AccessModelPackageData</code> permissions on the model package resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelPackageArnDataSource) -> dict:
    out: dict = {}
    out["modelPackageArn"] = value["model_package_arn"]
    return out


def deserialize_json(data: dict) -> ModelPackageArnDataSource:
    out: ModelPackageArnDataSource = {}  # type: ignore[typeddict-item]
    if data.get("modelPackageArn") is not None:
        out["model_package_arn"] = data["modelPackageArn"]
    else:
        out["model_package_arn"] = ""
    return out
