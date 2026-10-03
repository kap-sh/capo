"""Generated from Smithy shape ``com.amazonaws.kendra#HookConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.document_attribute_condition
    import capo_kendra.types.lambda_arn
    import capo_kendra.types.s3_bucket_name


class HookConfiguration(TypedDict, closed=True):
    invocation_condition: NotRequired[
        "capo_kendra.types.document_attribute_condition.DocumentAttributeCondition"
    ]
    """<p>The condition used for when a Lambda function should be invoked.</p> <p>For example, you can specify a condition that if there are empty date-time values, then Amazon Kendra should invoke a function that inserts the current date-time.</p>"""
    lambda_arn: "capo_kendra.types.lambda_arn.LambdaArn"
    """<p>The Amazon Resource Name (ARN) of an IAM role with permission to run a Lambda function during ingestion. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html">an IAM roles for Amazon Kendra</a>.</p>"""
    s3_bucket: "capo_kendra.types.s3_bucket_name.S3BucketName"
    """<p>Stores the original, raw documents or the structured, parsed documents before and after altering them. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html#cde-data-contracts-lambda">Data contracts for Lambda functions</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HookConfiguration) -> dict:
    out: dict = {}
    if "invocation_condition" in value:
        import capo_kendra.types.document_attribute_condition

        out["InvocationCondition"] = (
            capo_kendra.types.document_attribute_condition.serialize_aws_json_1_1(
                value["invocation_condition"]
            )
        )
    out["LambdaArn"] = value["lambda_arn"]
    out["S3Bucket"] = value["s3_bucket"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HookConfiguration:
    out: HookConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("InvocationCondition") is not None:
        import capo_kendra.types.document_attribute_condition

        out["invocation_condition"] = (
            capo_kendra.types.document_attribute_condition.deserialize_aws_json_1_1(
                data["InvocationCondition"]
            )
        )
    if data.get("LambdaArn") is not None:
        out["lambda_arn"] = data["LambdaArn"]
    else:
        raise DeserializationError("HookConfiguration.lambda_arn required")
    if data.get("S3Bucket") is not None:
        out["s3_bucket"] = data["S3Bucket"]
    else:
        raise DeserializationError("HookConfiguration.s3_bucket required")
    return out
