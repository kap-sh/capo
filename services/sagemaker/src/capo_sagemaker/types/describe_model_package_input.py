"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeModelPackageInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.included_data
    import capo_sagemaker.types.versioned_arn_or_name


class DescribeModelPackageInput(TypedDict, closed=True):
    model_package_name: NotRequired[
        "capo_sagemaker.types.versioned_arn_or_name.VersionedArnOrName"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the model package to describe.</p> <p>When you specify a name, the name must have 1 to 63 characters. Valid characters are a-z, A-Z, 0-9, and - (hyphen).</p>"""
    included_data: NotRequired["capo_sagemaker.types.included_data.IncludedData"]
    """<p>Specifies the level of model package data to include in the response. Use this parameter to call <code>DescribeModelPackage</code> on a model package that has an associated model card without requiring <code>kms:Decrypt</code> permission on the customer-managed KMS key associated with the embedded model card.</p> <ul> <li> <p> <code>AllData</code>: Returns the full model package response, including the unredacted <code>ModelCard.ModelCardContent</code>. This option requires <code>kms:Decrypt</code> permission on the customer-managed key, if one is associated with the embedded model card. This is the default.</p> </li> <li> <p> <code>MetadataOnly</code>: Returns the full model package response, but with the embedded <code>ModelCard.ModelCardContent</code> sanitized to include only a small set of unencrypted metadata fields. This option does not require <code>kms:Decrypt</code> permission. All other top-level response fields, including <code>InferenceSpecification</code>, <code>ModelMetrics</code>, <code>DriftCheckBaselines</code>, and <code>SecurityConfig</code>, are returned unchanged. For the list of fields preserved within <code>ModelCardContent</code>, see <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeModelPackage.html#sagemaker-DescribeModelPackage-response-ModelCard">ModelCard</a>.</p> </li> </ul> <p>If you don't specify a value, SageMaker returns <code>AllData</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeModelPackageInput) -> dict:
    out: dict = {}
    if "model_package_name" in value:
        out["ModelPackageName"] = value["model_package_name"]
    if "included_data" in value:
        import capo_sagemaker.types.included_data

        out["IncludedData"] = capo_sagemaker.types.included_data.serialize_aws_json_1_1(
            value["included_data"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeModelPackageInput:
    out: DescribeModelPackageInput = {}  # type: ignore[typeddict-item]
    if data.get("ModelPackageName") is not None:
        out["model_package_name"] = data["ModelPackageName"]
    if data.get("IncludedData") is not None:
        import capo_sagemaker.types.included_data

        out["included_data"] = (
            capo_sagemaker.types.included_data.deserialize_aws_json_1_1(
                data["IncludedData"]
            )
        )
    return out
